import os, sys
import json
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))
from dealer import *
from player import *
from processing import parse_json
from processing import make_json
from display import Display, spawnBoth


def main():
	"""
	takes a configuration from stdin and shows the
	contents of the first player in the dealer and the dealer
	"""

	configuration = json.load(sys.stdin)
	process_configuration = parse_json.parse_configuration(configuration)
	[lop, watering_hole, loc] = process_configuration
	dealer = Dealer(watering_hole, lop, loc)
	first_player = lop[0]
	dealerInfo = dealer.dealer_strings()
	playerInfo = first_player.player_strings()
	spawnBoth(dealerInfo, playerInfo)

main()
