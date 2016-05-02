# a test harness for the feed method in Player for a game of Evolution
import sys, os, json
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))

import inPlayer
from processing import parse_json
from processing import make_json

class TestHarness:
	def __init__(self):
		## uncomment this when running harness
		#self.main()
		pass

	def main(self):
		"""
		Get input from stdin, parse, and get Player's response, parse, and return to stdout
		"""
		feeding = json.load(sys.stdin)

		m_json = make_json.MakeJSON()

		feeding_py = parse_json.parse_feeding(feeding)

		[test_player, free_food, players_list] = feeding_py
		result = test_player.feed(players_list, free_food)

		print m_json.make_meal(result)

	def testMethod(self, given):
		"""
		Method to unit test xfeed, feeding in a JSON from the method rather than stdin and
		returning the result rather than printing tp stdout
		"""
		m_json = make_json.MakeJSON()

		feeding_py = parse_json.parse_feeding(given)

		test_player, free_food, players_list = feeding_py

		result = test_player.feed(players_list, free_food)

		return m_json.make_meal(result)

if __name__ == "__main__":
	TestHarness()
