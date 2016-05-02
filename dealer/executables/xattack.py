#!/usr/bin/env python
# a test harness for the attackable method in Dealer for a game of Evolution
import sys, os, json
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))

import species
from processing import parse_json
from processing import make_json
import trait


class TestHarness:
	def __init__(self):
		## uncomment this when running harness
		# self.main()
		pass

	def main(self):
		"""
		For a given Situation (a JSON of [attacking:Species, defending:Species, (neighbor:Species), (neighbor:Species)],
			return a Boolean to stdout whether or not the attack is successful.
		"""
		situation = json.load(sys.stdin)
		m_json = make_json.MakeJSON()

		species_list = parse_json.parse_situation(situation)

		defender, attacker, neighborLeft, neighborRight = species_list

		result = defender.attackable(attacker, neighborLeft, neighborRight)

		m_json.make_attack(result)

	def testMethod(self, given):
		"""
		For a given Situation (a JSON of [attacking:Species, defending:Species, (neighbor:Species), (neighbor:Species)],
			return a Boolean to stdout whether or not the attack is successful. (TESTS)
		"""
		m_json = make_json.MakeJSON()

		species_list = parse_json.parse_situation(given)

		defender, attacker, neighborLeft, neighborRight = species_list

		result = defender.attackable(attacker, neighborLeft, neighborRight)

		return m_json.make_attack(result)

if __name__ == "__main__":
	TestHarness()
