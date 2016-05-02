import os, sys
import json
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))
from dealer import *
from processing import parse_json
from processing import make_json


def main():
	"""
	takes a configuration from stdin and outputs the new_situation after the first step in the feeding
	"""

	configuration = json.load(sys.stdin)
	process_configuration = parse_json.parse_configuration(configuration)
	[lop, watering_hole, loc] = process_configuration
	dealer = Dealer(watering_hole, lop, loc)
	new_cofiguration = dealer.executeFeed1AndReturn()
	m_json = make_json.MakeJSON()
	output = m_json.make_configuration(new_cofiguration)
	print output


def test_xstep(configuration):
	"""
	takes a configuration and outputs the new_situation after the first step in the feeding
	:param cofiguration: Configuration
	:return: Configuration
	"""

	process_configuration = parse_json.parse_configuration(configuration)
	[lop, watering_hole, loc] = process_configuration
	dealer = Dealer(watering_hole, lop, loc)
	new_cofiguration = dealer.executeFeed1AndReturn()
	m_json = make_json.MakeJSON()
	output = m_json.make_configuration(new_cofiguration)
	return output

# main()
