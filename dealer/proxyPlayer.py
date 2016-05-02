import os, sys, json, socket, signal

from inPlayer import Player
import validate
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, 'processing'))
import process_output


SIZE = 1024
TIMEOUT = 3

class ProxyPlayer:
  def __init__(self, conn, sock):
    """
    initializes this proxyPlayer
    :param conn: a connection 
    :param sock: Socket 
    """
    self.connection = conn
    self.sock = sock

  def returnDelete(self, signum, stack):
    print "ALARM RANG"
    return "delete"

  def getReply(self):
    """
    gets the reply from the connection
    :return: a response which is either
     the return from the proxyDealer or "delete"
    """
    signal.signal(signal.SIGALRM, self.returnDelete)
    response = False
    while True:
      signal.alarm(TIMEOUT)
      try:
        response = self.connection.recv(SIZE)
      except socket.error:
        return "delete"
      if response:
        signal.alarm(0)
        try:
          r = json.loads(response)
          return r
        except Exception as e:
          return "delete"
    return "delete"

  def disconnect(self):
    """
    disconnects from the socket
    (closes the connection)
    :return: "delete"
    """
    self.connection.close()
    return "delete"


  def new(self, pid):
    """
    sends the new call to the proxyDealer
    :pid: int
    """
    self.connection.send(json.dumps(pid))


  def start(self, t):
    """
    sends the start call to the proxyDealer
    :param t: [int, int, [Species, ...], [TraitCard, ...]]
    """
    s = process_output.make_t_json(t)
    self.connection.send(json.dumps(s))


  def choose(self, c, d):
    """
    sends the choose call to the proxyDealer
    :param c: [[Species, ...], ...]
    :param d: [[Species, ...], ...]
    :return: Action4 or "delete" where "delete" means the response was invalid
    """
    cdj = process_output.make_cd_json(c, d)
    self.connection.send(json.dumps(cdj))
    response = self.getReply()
    if response == "delete":
      self.disconnect()
    elif validate.formatAction4(response):
      return response
    self.disconnect()

  def feedNext(self, wateringHole, lolos, playerState):
    """
    sends the feedNext call to the proxyDealer
    :param wateringHole: int
    :param lolos:  [[Species ...], ...]]
    :param playerState: [int, [Species, ...], [TraitCard, ...]]

    :return: FeedChoice or "delete" where "delete" means the response was invalid
    """
    ys = [playerState[0], playerState[1], playerState[2], wateringHole, lolos]
    zs = process_output.make_state(ys)
    self.connection.send(json.dumps(zs))
    response = self.getReply()
    if response == "delete":
      self.disconnect()
    elif validate.formatFeedingChoice(response):
      return response
    self.disconnect()
