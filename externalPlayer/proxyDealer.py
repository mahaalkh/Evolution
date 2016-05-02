#Representation of the external player object for the Evolution game
import os, sys, json, socket
from  sillyPlayer import SillyPlayer

this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../dealer/processing/'))
import parse_json

this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))
import xstream


HOST = 'localhost'
PORT = 45678
SIZE = 1024
### calls to proxy player should be done by tcp

class ProxyDealer:
  def __init__(self):
    self.sock = None
    #self.streamer = xstream.EchoStream()
    self.proxyPlayer = None
    self.externalPlayer = None
    # SillyPlayer(9, [], 0)
    self.gotOK = False

  def receiveData(self):
    data = None
    try:
        data = self.sock.recv(SIZE)
        return data
    except socket.error:
        return data

  def disconnect(self):
    self.sock.close()

  def getExternalPlayer(self):
    return self.externalPlayer

  def signUp(self, s):
    """
    send a massage to the server in order to join the game
    :param s: String
    """
    self.sock.sendall(json.dumps(s))


  def new(self, pid):
    """
    add a player to this proxyDealer
    :param pid: int
    """
    self.externalPlayer = SillyPlayer(pid, [], 0)


  def start(self, s):
    """
    intializes the externalPlayer
    :param s: [int, int, [Species_j+, ...], [SpeciesCard, ...]]
    :effect: calls the start method of the external player
    """
    t = parse_json.parse_s(s)
    self.externalPlayer.start(t)
    # self.sock.sendall(json.dumps("ok"))

  def choose(self, cdj):
    """
    asks the external player how it chooses the cards
    :param cdj: [[[Species_j+, ...], ...], [[Species_j+, ...], ...]]
    :effect: calls the choose method of the external player
    :return: Action4
    """
    c, d = parse_json.parse_cdj(cdj)
    action4 = self.externalPlayer.choose(c, d)
    self.sock.sendall(json.dumps(action4))

  def feedNext(self, zs):
    """
    asks the external player what species to feed next
    :param zs: [int, [Species_j+, ...], [SpeciesCard, ...], int, [[Species_j, ...], ...]]
    :effect: calls the feedNext method in the external player
    :return: FeedingChoice
    """
    ys = parse_json.parse_state(zs)
    feeding = self.externalPlayer.feedNext(ys[0], ys[1], ys[2])
    self.sock.sendall(json.dumps(feeding))

  def callMethod(self, data):
    """
    calls the correct method based on the received data
    :param data: List
    """
    if ((data == "ok") and (not self.gotOK)):
        self.gotOk = True

    elif self.gotOk:
        if (not isinstance(data, list) and (data != "ok")):
            self.new(data)
        elif len(data) == 2:
            self.choose(data)
        elif len(data) == 4:
            self.start(data)
        elif len(data) == 5:
            self.feedNext(data)
        else:
            self.disconnect()
    else:
        self.disconnect()


  def main(self):
    """
    Setup and manage TCP connection to game server; deliver messages as Python
    objects to the appropriate player proxy method, return their responses (as JSON)
    to the game server.
    """
    try:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        raise Exception('Socket error {} : {}'.format(msg[0], msg[1]))
    try:
        self.sock.connect((HOST, PORT))
    except socket.error as msg:
        raise Exception('Socket error {} : {}'.format(msg[0], msg[1]))

    self.signUp("Pikachu")

    while True:
        data = self.receiveData()
        if data:
            try:
                d = json.loads(data)
                self.callMethod(d)
            except ValueError:
                self.disconnect()

    self.disconnect()

ProxyDealer().main()








