# Create JSON representations of Evolution python objects
import sys, os, json
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))

import trait
import species
import inPlayer
import dealer
from process_output import make_lop_json, make_loc_json, make_player_json, make_lolos_json


## lolos_json : [[Species_j+, ...], ...]
## 

class MakeJSON:

	def __init__(self):
		pass

	def make_meal(self, feeding_out):
		"""
		Construct a JSON message to describe a player's feeding decision.
		The output is one of:
			false : no species is to be fed
			Nat : index of a Herbivore
			[Nat, Nat] : index of a Herbivore and the amount of Fat Food to consume
			[Nat, Nat, Nat] : index of a Carnivore, the Player index of the owner of
				the victim species, and the index of the victim
		"""
		return json.dumps(feeding_out)

	def make_attack(self, attack):
		"""
		Construct a JSON message to describe the result of an species' attack scenario (Boolean)
		:param attack: boolean
		:return: String
		"""
		return json.dumps(attack)


	def make_configuration(self, configuration):
		"""
		constructs a configuration
		:param configuration: Configuration
		:return: String
		"""
		[lop, watering_hole, loc] = configuration
		configuration_j = [make_lop_json(lop), watering_hole, make_loc_json(loc)]
		return json.dumps(configuration_j)

	def make_choice(self, player, lolos1, lolos2):
		"""
		constucts a make_choice
		:param player: Player
		:param lolos1: [[Species, ...], ...]
		:param lolos2: [[Species, ...], ...]
		:return: [player+_json, lolos_json, lolos_json]
		"""
		choice =  [make_player_json(player), make_lolos_json(lolos1), make_lolos_json(lolos2)]
		return choice
