PURPOSE:
Enable remote client support using the provided remote protocol for the Evolution Game

FILES:
Note: There are *'s in front of all files especially relevant for project 14
*14/main - executable for main.py
*14/main.py - evolution game main program
*14/client - executable for silly player client
*14/server - executable for dealer server
14/xstream.py - json stream reader from project 7

14/dealer/compareSpecies.py - comparators for species ordering
14/dealer/dealer.py - class representing a dealer object
14/dealer/deck.py - function for generating a deck and comparator for sorting cards
14/dealer/display.py - code to display basic gui interface
14/dealer/inPlayer.py - class representing the internal player object
*14/dealer/proxyPlayer - class representing the proxy player
14/dealer/species.py - class representing the species object
14/dealer/trait.py - enumeration for traits
14/dealer/trait_card.py - class representing a trait card object
14/dealer/utils.py - utility functions
*14/dealer/validate.py - data validation functions
14/dealer/wateringWhole.py - class representing a watering hole object

14/dealer/executables/xattack.py - test harness for the attackable method
14/dealer/executables/xfeed.py - test harness for the feed method
14/dealer/executables/xgui.py - test harness for the gui
14/dealer/executables/xstep.py - test harness for step method
14/dealer/executables/xstep4 - executable for xstep4.py
14/dealer/executables/xstep4.py - test harness for xstep4 method
14/dealer/executables/xstep4_testing.py - test harness for internal testing of xstep4 method
14/dealer/executables/xsilly - executable for xsilly.py
14/dealer/executables/xsilly.py - test harness for the silly external player
14/dealer/executables/xsilly_tester.py - test harness for internal testing the silly external player

14/dealer/processing/make_json.py - class for making different json objects
14/dealer/processing/parse_json.py - class for parsing different json objects
14/dealer/processing/process_output.py - functions for writing internal representations to json

14/dealer/unittests/test_attackable.py - unittests for attackable method
14/dealer/unittests/test_dealer.py - unittests for dealer.py
14/dealer/unittests/test_deck.py - unittests for deck.py
14/dealer/unittests/test_inPlayer.py - unittests for inPlayer.py
14/dealer/unittests/test_species.py - unittests for species.py
14/dealer/unittests/test_trait_card.py - unittests for trait_card.py
14/dealer/unittests/test_utils.py - unittests for utils.py
*14/dealer/unittests/test_validation.py - tests for validate.py
14/dealer/unittests/test_xattack.py - unittests for xattack.py
14/dealer/unittests/test_xfeed8.py - unittests from test fest for xfeed.py
14/dealer/unittests/test_xstep.py - unittests for xstep.py
14/dealer/unittests/test_xstep10.py - unittests from test fest for xstep.py


*14/externalPlayer/proxyDealer.py - class representing a proxy dealer for the external player
14/externalPlayer/sillyPlayer.py - code for a statically linked external player
14/externalPlayer/strategy.py - code for the game strategy used by the external "silly" player
*14/externalPlayer/validate.py - validation functions for the external player

*14/externalPlayer/unittests/test_proxyDealer.py - unittests for proxyDealer.py
14/externalPlayer/unittests/test_sillyPlayer.py - unittests for sillyPlayer.py
14/externalPlayer/unittests/test_strategy.py - unittests for strategy.py


14/test/1-in.json - xsilly json test case 1
14/test/1-out.json - xsilly expected output of json test case 1
14/test/2-in.json - xsilly json test case 2
14/test/2-out.json - xsilly expected output of json test case 2
14/test/3-in.json - xsilly json test case 3
14/test/3-out.json - xsilly expected output of json test case 3
14/test/4-in.json - xsilly json test case 4
14/test/4-out.json - xsilly expected output of json test case 4
14/test/5-in.json - xsilly json test case 5
14/test/5-out.json - xsilly expected output of json test case 5
14/test/test_jsonGenerator.py - unittests that print json output for testing purposes

READING/RUNNING THE CODE:
In order for any of the code to run you must run ./compile in the 14 directory

To run the game, run ./main portNumber  from the 14 directory followed by the number (between 3-8) of automated players desired
To run the client, run ./client from the 14 directory

All the unit test files (named test_) can be run in a virtualenv first running 'pip install enum34' and then 'python <filename>'

  To run the unit tests of xfeed, xattack, and xstep you must COMMENT OUT the
  calls to main() in the __init__ methods and UNCOMMENT "pass". To run the executables themselves, you must change this back.

To read the evolution game's code start from the top of the main.py's main method.
To read the remote client's game code start from the main method of proxyDealer.py
