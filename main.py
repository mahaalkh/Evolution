import os, sys, argparse, socket, select, json, time, signal
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, 'dealer/'))
import dealer
import deck
import inPlayer
import wateringWhole
import proxyPlayer
from processing import parse_json
from processing import make_json

parser = argparse.ArgumentParser()
parser.add_argument(dest = "port", default = 45678, type = int)
args = parser.parse_args()
args = vars(args)


HOST = 'localhost'
PORT = args['port']
SIZE = 1024
TIMEOUTFORJOINING = 5
TIMEOUT = 5
ACCEPTED = 8
MIN = 3
players = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
haveEnoughPlayers = False


def receive_alarm(signum, stack):
  haveEnoughPlayers = (len(players) <= ACCEPTED) and (len(players) >= MIN)
  if haveEnoughPlayers:
    print "started game"
    i = 1
    for player in players:
      player.getExternalPlayer().new(json.dumps(i))
      i += 1
    d = dealer.Dealer(wateringWhole.WateringHole(0), players, deck.generateDeck())
    results = d.runGame()
    for pr in results:
      print pr
    sock.close()

def main():
  """
  takes a int from standard in (between 3-8) and starts the game with that many players.
  """
  sock.bind((HOST,PORT))
  sock.listen(ACCEPTED)
  toread = [sock]
  i = 0

  signal.signal(signal.SIGALRM, receive_alarm)

  while (i <= ACCEPTED):
    if i >= MIN:
      signal.alarm(TIMEOUT)
      print "DONE"

    rready,wready,err = select.select(toread, [], [])

    for s in rready:
      if s == sock:
        client, address = sock.accept()
        toread.append(client)
        i = i + 1
      else:
        while True:
          data = s.recv(SIZE)
          if data:
            client.send(json.dumps("ok"))
            break
        player = proxyPlayer.ProxyPlayer(client, sock)
        players.append(inPlayer.Player(i, [], 0, player, data))

  receive_alarm("", "")
  sock.close()

main()

