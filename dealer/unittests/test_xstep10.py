# Automated unit tests for the step test harness for Evolution game
import unittest
import os, sys
import json
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../executables'))
import xstep

class TestXStepTests10(unittest.TestCase):
	def setUp(self):
		self.case1_in = [
											[
												[["id", 1],
												 ["species", []],
												 ["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]]
												],
											10,
											[]
										]
		self.case1_out = json.dumps([
											[
												[["id", 1],
													["species", []],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]]
											],
										10,
										[]
										])
		self.case2_in = [
											[
												[["id", 1],
													["species", [
														[["food", 0],
														 ["body", 1],
														 ["population", 1],
														 ["traits", []]
														]
													]],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]]
											],
											10,
											[]
										]
		self.case2_out = json.dumps([
											[
												[["id", 1],
													["species", [
														[["food", 1],
															["body", 1],
															["population", 1],
															["traits", []]
														]
													]],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]]
											],
											9,
											[]
										])
		self.case3_in = [
											[
												[["id", 1],
													["species", [
														[["food", 0],
														 ["body", 2],
														 ["population", 2],
														 ["traits", ["fat-tissue"]]]
													]],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]]
											],
											10,
											[]
										]
		self.case3_out = json.dumps([
											[
												[["id", 1],
													["species", [
														[["food", 0],
														 ["body", 2],
														 ["population", 2],
														 ["traits", ["fat-tissue"]],
														 ["fat-food", 2]]
													]],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]]
											],
											8,
											[]
										])
		self.case4_in = [
											[
												[["id", 1],
													["species", [
														[["food", 0],
															["body", 1],
															["population", 1],
															["traits", ["carnivore"]]
														],
														[["food", 0],
															["body", 1],
															["population", 1],
															["traits", ["horns"]]
														]
													]],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]]
											],
											10,
											[]
										]
		self.case4_out = json.dumps([
											[
												[["id", 1],
													["species", [
														[["food", 0],
															["body", 1],
															["population", 1],
															["traits", ["carnivore"]]
														],
														[["food", 1],
															["body", 1],
															["population", 1],
															["traits", ["horns"]]
														]
													]],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]]
											],
											9,
											[]
										])
		self.case5_in = [
											[
												[["id", 1],
													["species", [
														[["food", 0],
															["body", 1],
															["population", 1],
															["traits", ["cooperation"]]
														],
														[["food", 0],
															["body", 1],
															["population", 1],
															["traits", ["horns", "cooperation"]]
														],
														[["food", 0],
															["body", 1],
															["population", 1],
															["traits", []]
														]
													]],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]]
											],
											7,
											[]
										]
		self.case5_out = json.dumps([
											[
												[["id", 1],
													["species", [
														[["food", 1],
															["body", 1],
															["population", 1],
															["traits", ["cooperation"]]
														],
														[["food", 1],
															["body", 1],
															["population", 1],
															["traits", ["horns", "cooperation"]]
														],
														[["food", 1],
															["body", 1],
															["population", 1],
															["traits", []]
														]
													]],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]]
											],
											4,
											[]
										])
		self.case6_in = [
											[
												[["id", 1],
													["species", [
														[["food", 0],
															["body", 1],
															["population", 1],
															["traits", ["carnivore"]]
														],
														[["food", 1],
															["body", 1],
															["population", 1],
															["traits", ["horns", "cooperation"]]
														],
														[["food", 1],
															["body", 1],
															["population", 1],
															["traits", []]
														]
													]],
													["bag", 0]],
												[["id", 1],
													["species", [
														[["food", 0],
															["body", 1],
															["population", 1],
															["traits", []]
														]
													]],
													["bag", 0]],
												[["id", 1],
													["species", [
														[["food", 0],
															["body", 1],
															["population", 1],
															["traits", ["cooperation", "scavenger", "climbing"]]
														],
														[["food", 0],
															["body", 1],
															["population", 2],
															["traits", ["scavenger", "cooperation", "climbing"]]],

															[["food", 0],
																["body", 1],
																["population", 4],
																["traits", ["foraging", "climbing"]]
															]
														]],
														["bag", 0]]
													],
											10,
											[]
										]
		self.case6_out = json.dumps([
									[
										[["id", 1],
											["species", [
												[["food", 1],
													["body", 1],
													["population", 1],
													["traits", ["carnivore"]]
												],
												[["food", 1],
													["body", 1],
													["population", 1],
													["traits", ["horns", "cooperation"]]
												],
												[["food", 1],
													["body", 1],
													["population", 1],
													["traits", []]
												]
											]],
											["bag", 0]],
										[["id", 1],
											["species", []],
											["bag", 0]],
										[["id", 1],
											["species", [
												[["food", 1],
													["body", 1],
													["population", 1],
													["traits", ["cooperation", "scavenger", "climbing"]]
												],
												[["food", 2],
													["body", 1],
													["population", 2],
													["traits", ["scavenger", "cooperation", "climbing"]]
												],
													[["food", 4],
														["body", 1],
														["population", 4],
														["traits", ["foraging", "climbing"]]
													]
												]
											],
											["bag", 0]]
									],
									2,
									[]
								])
		self.case7_in = [
								[
									[["id", 1],
										["species", [
											[["food", 0],
												["body", 1],
												["population", 1],
												["traits", ["carnivore"]]
											],
											[["food", 1],
												["body", 1],
												["population", 1],
												["traits", ["horns", "cooperation"]]
											],
											[["food", 1],
												["body", 1],
												["population", 1],
												["traits", []]
											]
										]],
										["bag", 0]],
									[["id", 1],
										["species", [
											[["food", 0],
												["body", 1],
												["population", 1],
												["traits", ["hard-shell"]]
											]
										]],
										["bag", 0]],
									[["id", 1],
										["species", [
											[["food", 0],
												["body", 1],
												["population", 1],
												["traits", ["cooperation", "scavenger", "climbing"]]
											],
											[["food", 0],
												["body", 1],
												["population", 2],
												["traits", ["scavenger", "cooperation", "climbing"]]],

											[["food", 0],
												["body", 1],
												["population", 4],
												["traits", ["foraging", "hard-shell"]]
											]
										]],
										["bag", 0]]
								],
								10,
								[]
							]
		self.case7_out = json.dumps([
									[
										[["id", 1],
											["species", [
												[["food", 0],
													["body", 1],
													["population", 1],
													["traits", ["carnivore"]]
												],
												[["food", 1],
													["body", 1],
													["population", 1],
													["traits", ["horns", "cooperation"]]
												],
												[["food", 1],
													["body", 1],
													["population", 1],
													["traits", []]
												]
											]],
											["bag", 0]],
										[["id", 1],
											["species", [
												[["food", 0],
													["body", 1],
													["population", 1],
													["traits", ["hard-shell"]]
												]
											]],
											["bag", 0]],
										[["id", 1],
											["species", [
												[["food", 0],
													["body", 1],
													["population", 1],
													["traits", ["cooperation", "scavenger", "climbing"]]
												],
												[["food", 0],
													["body", 1],
													["population", 2],
													["traits", ["scavenger", "cooperation", "climbing"]]],

												[["food", 0],
													["body", 1],
													["population", 4],
													["traits", ["foraging", "hard-shell"]]
												]
											]],
											["bag", 0]]
									],
									10,
									[]
								])
		self.case8_in = [
								[
									[["id", 1],
										["species", [
											[["food", 0],
												["body", 1],
												["population", 1],
												["traits", ["carnivore"]]
											],
											[["food", 1],
												["body", 1],
												["population", 1],
												["traits", ["horns", "cooperation"]]
											],
											[["food", 1],
												["body", 1],
												["population", 1],
												["traits", []]
											]
										]],
										["bag", 0]],
									[["id", 1],
										["species", [
											[["food", 0],
												["body", 1],
												["population", 1],
												["traits", []]
											]
										]],
										["bag", 0]],
									[["id", 1],
										["species", [
											[["food", 0],
												["body", 1],
												["population", 1],
												["traits", ["cooperation", "scavenger", "climbing"]]
											],
											[["food", 0],
												["body", 1],
												["population", 2],
												["traits", ["scavenger", "cooperation", "climbing"]]],

											[["food", 0],
												["body", 1],
												["population", 4],
												["traits", ["foraging", "climbing"]]
											]
										]],
										["bag", 0]]
								],
								5,
								[]
							]
		self.case8_out = json.dumps([
											[
												[["id", 1],
													["species", [
														[["food", 1],
															["body", 1],
															["population", 1],
															["traits", ["carnivore"]]
														],
														[["food", 1],
															["body", 1],
															["population", 1],
															["traits", ["horns", "cooperation"]]
														],
														[["food", 1],
															["body", 1],
															["population", 1],
															["traits", []]
														]
													]],
													["bag", 0]],
												[["id", 1],
													["species", []],
													["bag", 0]],
												[["id", 1],
													["species", [
														[["food", 1],
															["body", 1],
															["population", 1],
															["traits", ["cooperation", "scavenger", "climbing"]]
														],
														[["food", 1],
															["body", 1],
															["population", 2],
															["traits", ["scavenger", "cooperation", "climbing"]]],

														[["food", 2],
															["body", 1],
															["population", 4],
															["traits", ["foraging", "climbing"]]
														]
													]],
													["bag", 0]]
											],
											0,
											[]
										])
		self.case9_in = [
											[
													[["id", 1], ["species", [[["food", 1], ["body", 1], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 3]],
													[["id", 2], ["species", [[["food", 1], ["body", 1], ["population", 2], ["traits", ["horns"]]]]], ["bag", 5]],
													[["id", 3], ["species", []], ["bag", 8]]
											],
											10,
											[[3, "carnivore"]]
									]
		self.case9_out = json.dumps([
											[
													[["id", 1], ["species", [[["food", 2], ["body", 1], ["population", 2], ["traits", ["carnivore"]]]]], ["bag", 3]],
													[["id", 2], ["species", [[["food", 1], ["body", 1], ["population", 1], ["traits", ["horns"]]]]], ["bag", 5]],
													[["id", 3], ["species", []], ["bag", 8]]
											],
											9,
											[[3, "carnivore"]]
									])
		self.case10_in =  [
												[
														[["id", 1], ["species", [[["food", 1], ["body", 1], ["population", 3], ["traits", ["foraging"]]]]], ["bag", 3]],
														[["id", 2], ["species", []], ["bag", 5]],
														[["id", 3], ["species", []], ["bag", 8]]
												],
												10,
												[[3, "carnivore"]]
											]
		self.case10_out = json.dumps([
												[
														[["id", 1], ["species", [[["food", 3], ["body", 1], ["population", 3], ["traits", ["foraging"]]]]], ["bag", 3]],
														[["id", 2], ["species", []], ["bag", 5]],
														[["id", 3], ["species", []], ["bag", 8]]
												],
												8,
												[[3, "carnivore"]]
										])
		self.case11_in = [
											[
													[["id", 1], ["species", [[["food", 1], ["body", 1], ["population", 3], ["traits", ["carnivore", "scavenger"]]]]], ["bag", 3]],
													[["id", 2], ["species", [[["food", 1], ["body", 1], ["population", 2], ["traits", []]]]], ["bag", 5]],
													[["id", 3], ["species", []], ["bag", 8]]
											],
											10,
											[[3, "carnivore"]]
									]
		self.case11_out = json.dumps([
												[
														[["id", 1], ["species", [[["food", 3], ["body", 1], ["population", 3], ["traits", ["carnivore", "scavenger"]]]]], ["bag", 3]],
														[["id", 2], ["species", [[["food", 1], ["body", 1], ["population", 1], ["traits", []]]]], ["bag", 5]],
														[["id", 3], ["species", []], ["bag", 8]]
												],
												8,
												[[3, "carnivore"]]
										])
		self.case12_in = [
											[
													[["id", 1], ["species", [[["food", 1], ["body", 1], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 3]],
													[["id", 2], ["species", [[["food", 1], ["body", 1], ["population", 5], ["traits", ["scavenger"]]]]], ["bag", 5]],
													[["id", 3], ["species", []], ["bag", 8]]
											],
											10,
											[[3, "carnivore"]]
									]
		self.case12_out = json.dumps([
												[
														[["id", 1], ["species", [[["food", 2], ["body", 1], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 3]],
														[["id", 2], ["species", [[["food", 2], ["body", 1], ["population", 4], ["traits", ["scavenger"]]]]], ["bag", 5]],
														[["id", 3], ["species", []], ["bag", 8]]
												],
												8,
												[[3, "carnivore"]]
	])
		self.case13_in = [
											[
													[["id", 1], ["species", [[["food", 1], ["body", 1], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 3]],
													[["id", 2], ["species", [[["food", 1], ["body", 1], ["population", 5], ["traits", ["scavenger", "foraging"]]]]], ["bag", 5]],
													[["id", 3], ["species", []], ["bag", 8]]
											],
											2,
											[[3, "carnivore"]]
									]
		self.case13_out = json.dumps([
												[
														[["id", 1], ["species", [[["food", 2], ["body", 1], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 3]],
														[["id", 2], ["species", [[["food", 2], ["body", 1], ["population", 4], ["traits", ["scavenger", "foraging"]]]]], ["bag", 5]],
														[["id", 3], ["species", []], ["bag", 8]]
												],
												0,
												[[3, "carnivore"]]
										])
		self.case14_in = [[[["id",2],
											 ["species",[[["food",4],
																		["body",4],
																		["population",4],
																		["traits",["fat-tissue"]],
																		["fat-food" ,4]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",3],
											 ["species",[[["food",1],
																		["body",4],
																		["population",4],
																		["traits",["carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",1],
																		["traits",["fat-tissue"]],
																		["fat-food" ,4]]]],
											 ["bag",100]]],
										 6,
										 []]
		self.case14_out = json.dumps([[[["id",2],
											 ["species",[[["food",4],
																		["body",4],
																		["population",4],
																		["traits",["fat-tissue"]],
																		["fat-food" ,4]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",3],
											 ["species",[[["food",1],
																		["body",4],
																		["population",4],
																		["traits",["carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",1],
																		["traits",["fat-tissue"]],
																		["fat-food" ,4]]]],
											 ["bag",100]]],
										 6,
										 []])
		self.case15_in = [[[["id",2],
											 ["species",[[["food",2],
																		["body",4],
																		["population",4],
																		["traits",[]]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",3],
											 ["species",[[["food",1],
																		["body",4],
																		["population",4],
																		["traits",["carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",1],
																		["traits",["fat-tissue"]],
																		["fat-food" ,4]]]],
											 ["bag",100]]],
										 6,
										 []]
		self.case15_out = json.dumps([[[["id",2],
											 ["species",[[["food",3],
																		["body",4],
																		["population",4],
																		["traits",[]]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",3],
											 ["species",[[["food",1],
																		["body",4],
																		["population",4],
																		["traits",["carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",1],
																		["traits",["fat-tissue"]],
																		["fat-food" ,4]]]],
											 ["bag",100]]],
										 5,
										 []])
		self.case16_in = [[[["id",2],
											 ["species",[[["food",2],
																		["body",4],
																		["population",4],
																		["traits",["fat-tissue"]],
																		["fat-food", 1]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",3],
											 ["species",[[["food",1],
																		["body",4],
																		["population",4],
																		["traits",["carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",1],
																		["traits",["fat-tissue"]],
																		["fat-food" ,4]]]],
											 ["bag",100]]],
										 6,
										 []]
		self.case16_out = json.dumps([[[["id",2],
											 ["species",[[["food",2],
																		["body",4],
																		["population",4],
																		["traits",["fat-tissue"]],
																		["fat-food", 4]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",3],
											 ["species",[[["food",1],
																		["body",4],
																		["population",4],
																		["traits",["carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",1],
																		["traits",["fat-tissue"]],
																		["fat-food" ,4]]]],
											 ["bag",100]]],
										 3,
										 []])
		self.case17_in = [[[["id",2],
											 ["species",[[["food",3],
																		["body",3],
																		["population",4],
																		["traits",["cooperation"]]],
																	 [["food",3],
																		["body",2],
																		["population",4],
																		["traits",["cooperation"]]],
																	 [["food",3],
																		["body",1],
																		["population",4],
																		["traits",["burrowing"]]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",3],
											 ["species",[[["food",1],
																		["body",4],
																		["population",4],
																		["traits",["carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",1],
																		["traits",["fat-tissue"]],
																		["fat-food" ,4]]]],
											 ["bag",100]]],
										 6,
										 []]
		self.case17_out = json.dumps([[[["id",2],
											 ["species",[[["food",4],
																		["body",3],
																		["population",4],
																		["traits",["cooperation"]]],
																	 [["food",4],
																		["body",2],
																		["population",4],
																		["traits",["cooperation"]]],
																	 [["food",4],
																		["body",1],
																		["population",4],
																		["traits",["burrowing"]]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",3],
											 ["species",[[["food",1],
																		["body",4],
																		["population",4],
																		["traits",["carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",1],
																		["traits",["fat-tissue"]],
																		["fat-food" ,4]]]],
											 ["bag",100]]],
										 3,
										 []])
		self.case18_in = [[[["id",3],
											 ["species",[[["food",1],
																		["body",4],
																		["population",4],
																		["traits",["carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",2],
											 ["species",[[["food",3],
																		["body",3],
																		["population",4],
																		["traits",["climbing", "cooperation", "scavenger"]]],
																	 [["food",3],
																		["body",2],
																		["population",4],
																		["traits",["climbing", "cooperation"]]],
																	 [["food",3],
																		["body",1],
																		["population",4],
																		["traits",["climbing", "burrowing"]]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",7],
																		["traits",["fat-tissue"]],
																		["fat-food" ,4]]]],
											 ["bag",100]]],
										 6,
										 []]
		self.case18_out = json.dumps([[[["id",3],
											 ["species",[[["food",2],
																		["body",4],
																		["population",4],
																		["traits",["carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",2],
											 ["species",[[["food",4],
																		["body",3],
																		["population",4],
																		["traits",["climbing", "cooperation", "scavenger"]]],
																	 [["food",4],
																		["body",2],
																		["population",4],
																		["traits",["climbing", "cooperation"]]],
																	 [["food",4],
																		["body",1],
																		["population",4],
																		["traits",["climbing", "burrowing"]]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",6],
																		["traits",["fat-tissue"]],
																		["fat-food" ,4]]]],
											 ["bag",100]]],
										 2,
										 []])
		self.case19_in = [[[["id",3],
											 ["species",[[["food",2],
																		["body",4],
																		["population",4],
																		["traits",["foraging", "carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",2],
											 ["species",[[["food",0],
																		["body",3],
																		["population",4],
																		["traits",["foraging", "scavenger"]]],
																	 [["food",4],
																		["body",2],
																		["population",4],
																		["traits",[]]],
																	 [["food",4],
																		["body",1],
																		["population",4],
																		["traits",[]]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",6],
																		["traits",["fat-tissue"]],
																		["fat-food" ,4]]]],
											 ["bag",100]]],
										 10,
										 []]
		self.case19_out = json.dumps([[[["id",3],
											 ["species",[[["food",4],
																		["body",4],
																		["population",4],
																		["traits",["foraging", "carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",2],
											 ["species",[[["food",2],
																		["body",3],
																		["population",4],
																		["traits",["foraging", "scavenger"]]],
																	 [["food",4],
																		["body",2],
																		["population",4],
																		["traits",[]]],
																	 [["food",4],
																		["body",1],
																		["population",4],
																		["traits",[]]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",5],
																		["traits",["fat-tissue"]],
																		["fat-food" ,4]]]],
											 ["bag",100]]],
										 6,
										 []])
		self.case20_in = [[[["id",3],
											 ["species",[[["food",2],
																		["body",4],
																		["population",4],
																		["traits",["carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",2],
											 ["species",[[["food",0],
																		["body",3],
																		["population",4],
																		["traits",[]]],
																	 [["food",4],
																		["body",2],
																		["population",4],
																		["traits",[]]],
																	 [["food",4],
																		["body",1],
																		["population",4],
																		["traits",[]]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",6],
																		["traits",["horns"]]]]],
											 ["bag",100]]],
										 10,
										 []]
		self.case20_out = json.dumps([[[["id",3],
											 ["species",[[["food",3],
																		["body",4],
																		["population",3],
																		["traits",["carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",2],
											 ["species",[[["food",0],
																		["body",3],
																		["population",4],
																		["traits",[]]],
																	 [["food",4],
																		["body",2],
																		["population",4],
																		["traits",[]]],
																	 [["food",4],
																		["body",1],
																		["population",4],
																		["traits",[]]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",5],
																		["traits",["horns"]]]]],
											 ["bag",100]]],
										 9,
										 []])
		self.case21_in = [[[["id",3],
											 ["species",[[["food",3],
																		["body",4],
																		["population",4],
																		["traits",["carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",2],
											 ["species",[[["food",0],
																		["body",3],
																		["population",4],
																		["traits",["climbing"]]],
																	 [["food",4],
																		["body",2],
																		["population",4],
																		["traits",["climbing"]]],
																	 [["food",4],
																		["body",1],
																		["population",4],
																		["traits",["climbing"]]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",4],
											 ["species",[[["food",0],
																		["body",7],
																		["population",1],
																		["traits",[]]]]],
											 ["bag",100]]],
										 9,
										 [[3, "burrowing"],
											[3, "horns"],
											[1, "climbing"]]]
		self.case21_out = json.dumps([[[["id",3],
											 ["species",[[["food",4],
																		["body",4],
																		["population",4],
																		["traits",["carnivore"]]]]],
											 ["bag",2],
											 ["cards",[[-3, "burrowing"]]]],
											[["id",2],
											 ["species",[[["food",0],
																		["body",3],
																		["population",4],
																		["traits",["climbing"]]],
																	 [["food",4],
																		["body",2],
																		["population",4],
																		["traits",["climbing"]]],
																	 [["food",4],
																		["body",1],
																		["population",4],
																		["traits",["climbing"]]]]],
											 ["bag",42],
											 ["cards",[[3, "climbing"]]]],
											[["id",4],
											 ["species",[]],
											 ["bag",100],
											 ["cards",[[3, "burrowing"],[3, "horns"]]]]],
										 8,
										 [[1, "climbing"]]])
		self.case22_in = [[[["id",1],["species",[[["food",1],["body",3],["population",2],["traits",["carnivore"]]]]],["bag",1]],
												[["id",2],["species",[[["food",1],["body",2],["population",2],["traits",["horns"]]]]],["bag",1]],
												[["id",3],["species",[[["food",1],["body",1],["population",1],["traits",[]]]]],["bag",1]]],20,[]]
		self.case22_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",1]],[["id",2],["species",[[["food",1],["body",2],["population",1],["traits",["horns"]]]]],["bag",1]],[["id",3],["species",[[["food",1],["body",1],["population",1],["traits",[]]]]],["bag",1]]],20,[]])
		self.case23_in = [[[["id",3],["species",[[["food",5],["body",5],["population",5],["traits",["fat-tissue","horns","foraging"]],["fat-food",5]]]],["bag",5]],[["id",1],["species",[]],["bag",3]],[["id",2],["species",[]],["bag",4]]],20,[[5,"carnivore"],[2,"long-neck"],[0,"symbiosis"]]]
		self.case23_out = json.dumps([[[["id",3],["species",[[["food",5],["body",5],["population",5],["traits",["fat-tissue","horns","foraging"]],["fat-food",5]]]],["bag",5]],[["id",1],["species",[]],["bag",3]],[["id",2],["species",[]],["bag",4]]],20,[[5,"carnivore"],[2,"long-neck"],[0,"symbiosis"]]])
		self.case24_in = [[[["id",1],["species",[[["food",3],["body",5],["population",5],["traits",["fat-tissue","horns"]],["fat-food",5]],
											[["food",3],["body",3],["population",3],["traits",["carnivore"]]],
											[["food",3],["body",3],["population",3],["traits",["carnivore"]]]]],["bag",0]],
											[["id",2],["species",[]],["bag",0]],
											[["id",3],["species",[]],["bag",0]]],20,[]]
		self.case24_out = json.dumps([[[["id",1],["species",[[["food",4],["body",5],["population",5],["traits",["fat-tissue","horns"]],["fat-food",5]],[["food",3],["body",3],["population",3],["traits",["carnivore"]]],[["food",3],["body",3],["population",3],["traits",["carnivore"]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],19,[]])
		self.case25_in = [
											[[["id",1],
												["species",[[["food",2],["body",3],["population",4],["traits",["carnivore"]]]]],["bag",2]],
											[["id",2],["species",[[["food",2],["body",2],["population",3],["traits",["scavenger","foraging"]]]]],["bag",2]],
											[["id",3],["species",[[["food",1],["body",1],["population",3],["traits",["scavenger","cooperation","climbing"]]],[["food",1],["body",2],["population",3],["traits",[]]]]],["bag",2]]],
											15,[]]
		self.case25_out = json.dumps([[[["id",1],["species",[[["food",3],["body",3],["population",4],["traits",["carnivore"]]]]],["bag",2]],[["id",2],["species",[[["food",2],["body",2],["population",2],["traits",["scavenger","foraging"]]]]],["bag",2]],[["id",3],["species",[[["food",2],["body",1],["population",3],["traits",["scavenger","cooperation","climbing"]]],[["food",2],["body",2],["population",3],["traits",[]]]]],["bag",2]]],12,[]])
		self.case26_in = [[[["id",1],["species",[
										[["food",1],["body",1],["population",1],["traits",["carnivore"]]],
										[["food",1],["body",2],["population",5],["traits",["carnivore","cooperation"]]],
										[["food",2],["body",4],["population",3],["traits",["carnivore","cooperation"]]],
										[["food",2],["body",4],["population",3],["traits",["carnivore","cooperation"]]]]],["bag",2]],

										[["id",2],["species",[
										[["food",1],["body",2],["population",1],["traits",[]]],
										[["food",1],["body",2],["population",1],["traits",[]]],
										[["food",1],["body",2],["population",1],["traits",[]]]]],["bag",3]],

										[["id",3],["species",[
										[["food",1],["body",2],["population",1],["traits",["carnivore"]]],
										[["food",1],["body",2],["population",1],["traits",["carnivore"]]]]],["bag",1]]],20,[[1,"foraging"],[2,"long-neck"]]]
		self.case26_out = json.dumps([[[["id",1],["species",[[["food",1],["body",1],["population",1],["traits",["carnivore"]]],[["food",2],["body",2],["population",5],["traits",["carnivore","cooperation"]]],[["food",3],["body",4],["population",3],["traits",["carnivore","cooperation"]]],[["food",3],["body",4],["population",3],["traits",["carnivore","cooperation"]]]]],["bag",2]],[["id",2],["species",[[["food",1],["body",2],["population",1],["traits",[]]],[["food",1],["body",2],["population",1],["traits",[]]]]],["bag",3],["cards",[[1,"foraging"],[2,"long-neck"]]]],[["id",3],["species",[[["food",1],["body",2],["population",1],["traits",["carnivore"]]],[["food",1],["body",2],["population",1],["traits",["carnivore"]]]]],["bag",1]]],17,[]])
		self.case27_in = [
											[
												[["id", 1],
													["species", [[["food", 1],
																				["body", 5],
																				["population", 6],
																				["traits", []]]]],
													["bag", 0]],
												[["id", 2], ["species", []], ["bag", 0]],
												[["id", 3], ["species", []], ["bag", 0]]
											],
											1,
											[
												[4, "carnivore"],
												[3, "scavenger"]
											]
										]
		self.case27_out = json.dumps([[[["id", 1], ["species", [[["food", 2], ["body", 5], ["population", 6], ["traits", []]]]], ["bag", 0]], [["id", 2], ["species", []], ["bag", 0]], [["id", 3], ["species", []], ["bag", 0]]], 0, [[4, "carnivore"], [3, "scavenger"]]])
		self.case28_in = [
											[
												[["id", 1],
													["species", [[["food", 2],
																				["body", 5],
																				["population", 6],
																				["traits", ["carnivore"]]]]],
													["bag", 0]],
												[["id", 2],
													["species", [[["food", 2],
																				["body", 5],
																				["population", 6],
																				["traits", []]]]],
													["bag", 0]],
												[["id", 3], ["species",
																			[[["food", 2],
																				["body", 1],
																				["population", 6],
																				["traits", ["scavenger"]]]]], ["bag", 0]]
											],
											3,
											[
												[4, "carnivore"],
												[3, "scavenger"]
											]
										]
		self.case28_out = json.dumps([[[["id", 1], ["species", [[["food", 3], ["body", 5], ["population", 6], ["traits", ["carnivore"]]]]], ["bag", 0]], [["id", 2], ["species", [[["food", 2], ["body", 5], ["population", 5], ["traits", []]]]], ["bag", 0]], [["id", 3], ["species", [[["food", 3], ["body", 1], ["population", 6], ["traits", ["scavenger"]]]]], ["bag", 0]]], 1, [[4, "carnivore"], [3, "scavenger"]]])
		self.case29_in = [
											[
												[["id", 1],
													["species", [[["food", 2],
																				["body", 5],
																				["population", 6],
																				["traits", ["foraging", "cooperation"]]],
																				[["food", 2],
																				["body", 5],
																				["population", 3],
																				["traits", ["cooperation"]]]]],
													["bag", 0]],
												[["id", 2],
													["species", [[["food", 2],
																				["body", 5],
																				["population", 6],
																				["traits", ["scavenger"]]]]],
													["bag", 0]],
												[["id", 3], ["species",
																			[[["food", 2],
																				["body", 1],
																				["population", 6],
																				["traits", ["foraging"]]]]], ["bag", 0]]
											],
											4,
											[
												[4, "carnivore"],
												[3, "scavenger"]
											]
										]
		self.case29_out = json.dumps([[[["id", 1], ["species", [[["food", 4], ["body", 5], ["population", 6], ["traits", ["foraging", "cooperation"]]], [["food", 3], ["body", 5], ["population", 3], ["traits", ["cooperation"]]]]], ["bag", 0]], [["id", 2], ["species", [[["food", 2], ["body", 5], ["population", 6], ["traits", ["scavenger"]]]]], ["bag", 0]], [["id", 3], ["species", [[["food", 2], ["body", 1], ["population", 6], ["traits", ["foraging"]]]]], ["bag", 0]]], 1, [[4, "carnivore"], [3, "scavenger"]]])
		self.case30_in = [
											[
												[["id", 1],
													["species", [[["food", 2],
																				["body", 5],
																				["population", 6],
																				["traits", ["carnivore", "cooperation"]]],
																				[["food", 2],
																				["body", 5],
																				["population", 3],
																				["traits", ["carnivore", "cooperation"]]],
																				[["food", 2],
																				["body", 5],
																				["population", 3],
																				["traits", ["carnivore"]]]]],
													["bag", 0]],
												[["id", 2],
													["species", [[["food", 2],
																				["body", 5],
																				["population", 4],
																				["traits", ["scavenger"]]]]],
													["bag", 0]],
												[["id", 3], ["species",
																			[[["food", 2],
																				["body", 1],
																				["population", 6],
																				["traits", ["foraging", "horns"]]]]], ["bag", 0]]
											],
											3,
											[
												[4, "carnivore"],
												[3, "scavenger"]
											]
										]
		self.case30_out = json.dumps([[[["id", 1], ["species", [[["food", 3], ["body", 5], ["population", 5], ["traits", ["carnivore", "cooperation"]]], [["food", 3], ["body", 5], ["population", 3], ["traits", ["carnivore", "cooperation"]]], [["food", 3], ["body", 5], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 0]], [["id", 2], ["species", [[["food", 2], ["body", 5], ["population", 4], ["traits", ["scavenger"]]]]], ["bag", 0]], [["id", 3], ["species", [[["food", 2], ["body", 1], ["population", 5], ["traits", ["foraging", "horns"]]]]], ["bag", 0]]], 0, [[4, "carnivore"], [3, "scavenger"]]])
		self.case31_in = [
											[
												[["id",1],
												 ["species",[]],
												 ["bag",0]],
												[["id",2],
												 ["species",[]],
												 ["bag",0]],
												[["id",3],
												 ["species",[]],
												 ["bag",0]]
											],
											1,
											[
												[8, "carnivore"],
												[-8, "carnivore"],
												[-3, "symbiosis"],
												[3, "horns"]
											]
										]
		self.case31_out = json.dumps([[[["id", 1], ["species", []], ["bag", 0]], [["id", 2], ["species", []], ["bag", 0]], [["id", 3], ["species", []], ["bag", 0]]], 1, [[8, "carnivore"], [-8, "carnivore"], [-3, "symbiosis"], [3, "horns"]]])
		self.case32_in = [
											[
												[["id",1],
												 ["species",[
													[
														["food",2],
														["body",2],
														["population",3],
														["traits",[]]
													]
												 ]],
												 ["bag",0]],
												[["id",2],
												 ["species",[]],
												 ["bag",0]],
												[["id",3],
												 ["species",[]],
												 ["bag",0]]
											],
											1,
											[
												[8, "carnivore"],
												[-8, "carnivore"],
												[-3, "symbiosis"],
												[3, "horns"]
											]
										]
		self.case32_out = json.dumps([[[["id", 1], ["species", [[["food", 3], ["body", 2], ["population", 3], ["traits", []]]]], ["bag", 0]], [["id", 2], ["species", []], ["bag", 0]], [["id", 3], ["species", []], ["bag", 0]]], 0, [[8, "carnivore"], [-8, "carnivore"], [-3, "symbiosis"], [3, "horns"]]])
		self.case33_in = [
											[
												[["id",1],
												 ["species",[
													[
														["food",3],
														["body",2],
														["population",3],
														["traits",["fat-tissue"]],
														["fat-food", 0]
													]
												 ]],
												 ["bag",0]],
												[["id",2],
												 ["species",[]],
												 ["bag",0]],
												[["id",3],
												 ["species",[]],
												 ["bag",0]]
											],
											1,
											[
												[8, "carnivore"],
												[-8, "carnivore"],
												[-3, "symbiosis"],
												[3, "horns"]
											]
										]
		self.case33_out = json.dumps([[[["id", 1], ["species", [[["food", 3], ["body", 2], ["population", 3], ["traits", ["fat-tissue"]], ["fat-food", 1]]]], ["bag", 0]], [["id", 2], ["species", []], ["bag", 0]], [["id", 3], ["species", []], ["bag", 0]]], 0, [[8, "carnivore"], [-8, "carnivore"], [-3, "symbiosis"], [3, "horns"]]])
		self.case34_in = [[[["id", 1], ["species",
											 [[["food",0],
													["body",5],
													["population",2],
													["traits",["foraging"]]]]],
								 ["bag", 4]],
								[["id", 2], ["species",
											 [[["food",0],
													["body",2],
													["population",1],
													["traits",["foraging"]]]]],
								 ["bag", 4]],
								[["id", 3], ["species",
											 [[["food",0],
													["body",1],
													["population",1],
													["traits",[]]]]],
								 ["bag", 4]]],
							 5,
							 [[-8, "carnivore"],
								[0, "herding"],
								[3, "fat-tissue"]
							 ]
							]
		self.case34_out = json.dumps([[[["id", 1], ["species",
														 [[["food",2],
																["body",5],
																["population",2],
																["traits",["foraging"]]]]],
											 ["bag", 4]],
											[["id", 2], ["species",
														 [[["food",0],
																["body",2],
																["population",1],
																["traits",["foraging"]]]]],
											 ["bag", 4]],
											[["id", 3], ["species",
														 [[["food",0],
																["body",1],
																["population",1],
																["traits",[]]]]],
											 ["bag", 4]]],
										 3,
										 [[-8, "carnivore"],
											[0, "herding"],
											[3, "fat-tissue"]
										 ]
										])
		self.case35_in = [[[["id", 1], ["species",
																		 [[["food",0],
																				["body",5],
																				["population",2],
																				["traits",["carnivore", "cooperation"]]],
																			[["food",0],
																				["body",5],
																				["population",1],
																				["traits",["carnivore"]]]]],
															 ["bag", 4]],
															[["id", 2], ["species",
																		 [[["food",0],
																				["body",2],
																				["population",2],
																				["traits",["scavenger", "foraging", "cooperation"]]],
																			[["food",0],
																				["body",5],
																				["population",2],
																				["traits",["carnivore", "cooperation"]]]]],
															 ["bag", 4]],
															[["id", 3], ["species",
																		 [[["food",0],
																				["body",4],
																				["population",1],
																				["traits",[]]]]],
															 ["bag", 4]]],
														 10,
														 [[-8, "carnivore"],
															[0, "herding"],
															[3, "fat-tissue"]
														 ]
														]
		self.case35_out = json.dumps([[[["id", 1], ["species",
																		 [[["food",1],
																				["body",5],
																				["population",2],
																				["traits",["carnivore", "cooperation"]]],
																			[["food",1],
																				["body",5],
																				["population",1],
																				["traits",["carnivore"]]]]],
															 ["bag", 4]],
															[["id", 2], ["species",
																		 [[["food",2],
																				["body",2],
																				["population",2],
																				["traits",["scavenger", "foraging", "cooperation"]]],
																			[["food",1],
																				["body",5],
																				["population",1],
																				["traits",["carnivore", "cooperation"]]]]],
															 ["bag", 4]],
															[["id", 3], ["species",
																		 [[["food",0],
																				["body",4],
																				["population",1],
																				["traits",[]]]]],
															 ["bag", 4]]],
														 5,
														 [[-8, "carnivore"],
															[0, "herding"],
															[3, "fat-tissue"]
														 ]
														])
		self.case36_in = [
											[
												[
													["id", 1],
													["species",
														[
															[
																["food", 1],
																["body", 2],
																["population", 3],
																["traits", ["carnivore"]]
															],
															[
																["food", 1],
																["body", 3],
																["population", 1],
																["traits", ["long-neck"]]
															]
														]
													],
													["bag", 3]],
												[
													["id", 2],
													["species",
														[
															[
																["food", 2],
																["body", 3],
																["population", 2],
																["traits", ["burrowing"]]
															]
														]
													],
													["bag", 4]
												],
												[
													["id", 3],
													["species",
														[]
													],
													["bag", 5]
												]
											],
											10,
											[]
										]
		self.case36_out = json.dumps([
												[
													[
														["id", 1],
														["species",
															[
																[
																	["food", 1],
																	["body", 2],
																	["population", 3],
																	["traits", ["carnivore"]]
																],
																[
																	["food", 1],
																	["body", 3],
																	["population", 1],
																	["traits", ["long-neck"]]
																]
															]
														],
														["bag", 3]],
													[
														["id", 2],
														["species",
															[
																[
																	["food", 2],
																	["body", 3],
																	["population", 2],
																	["traits", ["burrowing"]]
																]
															]
														],
														["bag", 4]
													],
													[
														["id", 3],
														["species",
															[]
														],
														["bag", 5]
													]
												],
												10,
												[]
											])
		self.case37_in = [
											[
												[
													["id", 1],
													["species",
														[
															[
																["food", 1],
																["body", 2],
																["population", 3],
																["traits", ["carnivore"]]
															],
															[
																["food", 1],
																["body", 3],
																["population", 4],
																["traits", ["foraging"]]
															]
														]
													],
													["bag", 3]],
												[
													["id", 2],
													["species",
														[
															[
																["food", 2],
																["body", 3],
																["population", 2],
																["traits", ["burrowing"]]
															]
														]
													],
													["bag", 4]
												],
												[
													["id", 3],
													["species",
														[]
													],
													["bag", 5]
												]
											],
											10,
											[]
										]
		self.case37_out = json.dumps([
												[
													[
														["id", 1],
														["species",
															[
																[
																	["food", 1],
																	["body", 2],
																	["population", 3],
																	["traits", ["carnivore"]]
																],
																[
																	["food", 3],
																	["body", 3],
																	["population", 4],
																	["traits", ["foraging"]]
																]
															]
														],
														["bag", 3]],
													[
														["id", 2],
														["species",
															[
																[
																	["food", 2],
																	["body", 3],
																	["population", 2],
																	["traits", ["burrowing"]]
																]
															]
														],
														["bag", 4]
													],
													[
														["id", 3],
														["species",
															[]
														],
														["bag", 5]
													]
												],
												8,
												[]
											])
		self.case38_in = [
											[
												[
													["id", 1],
													["species",
														[
															[
																["food", 1],
																["body", 2],
																["population", 3],
																["traits", ["carnivore"]]
															],
															[
																["food", 1],
																["body", 3],
																["population", 4],
																["traits", ["foraging", "fat-tissue"]]
															]
														]
													],
													["bag", 3]],
												[
													["id", 2],
													["species",
														[
															[
																["food", 2],
																["body", 3],
																["population", 2],
																["traits", ["burrowing"]]
															]
														]
													],
													["bag", 4]
												],
												[
													["id", 3],
													["species",
														[]
													],
													["bag", 5]
												]
											],
											2,
											[]
										]
		self.case38_out = json.dumps([
												[
													[
														["id", 1],
														["species",
															[
																[
																	["food", 1],
																	["body", 2],
																	["population", 3],
																	["traits", ["carnivore"]]
																],
																[
																	["food", 1],
																	["body", 3],
																	["population", 4],
																	["traits", ["foraging", "fat-tissue"]],
																	["fat-food", 2]
																]
															]
														],
														["bag", 3]],
													[
														["id", 2],
														["species",
															[
																[
																	["food", 2],
																	["body", 3],
																	["population", 2],
																	["traits", ["burrowing"]]
																]
															]
														],
														["bag", 4]
													],
													[
														["id", 3],
														["species",
															[]
														],
														["bag", 5]
													]
												],
												0,
												[]
											])
		self.case39_in = [
											[
												[
													["id", 1],
													["species",
														[
															[
																["food", 4],
																["body", 2],
																["population", 5],
																["traits", ["carnivore", "cooperation"]]
															],
															[
																["food", 1],
																["body", 3],
																["population", 4],
																["traits", ["foraging", "carnivore", "scavenger"]]
															]
														]
													],
													["bag", 3]],
												[
													["id", 2],
													["species",
														[
															[
																["food", 2],
																["body", 3],
																["population", 3],
																["traits", ["burrowing"]]
															]
														]
													],
													["bag", 4]
												],
												[
													["id", 3],
													["species",
														[]
													],
													["bag", 5]
												]
											],
											10,
											[]
										]
		self.case39_out = json.dumps([
													[
														[
															["id", 1],
															["species",
																[
																	[
																		["food", 5],
																		["body", 2],
																		["population", 5],
																		["traits", ["carnivore", "cooperation"]]
																	],
																	[
																		["food", 4],
																		["body", 3],
																		["population", 4],
																		["traits", ["foraging", "carnivore", "scavenger"]]
																	]
																]
															],
															["bag", 3]],
														[
															["id", 2],
															["species",
																[
																	[
																		["food", 2],
																		["body", 3],
																		["population", 2],
																		["traits", ["burrowing"]]
																	]
																]
															],
															["bag", 4]
														],
														[
															["id", 3],
															["species",
																[]
															],
															["bag", 5]
														]
													],
													6,
													[]
												])
		self.case40_in = [
											[
												[
													["id", 1],
													["species",
														[
															[
																["food", 0],
																["body", 2],
																["population", 1],
																["traits", ["carnivore", "cooperation"]]
															],
															[
																["food", 4],
																["body", 3],
																["population", 4],
																["traits", ["foraging", "carnivore", "scavenger"]]
															]
														]
													],
													["bag", 3]],
												[
													["id", 2],
													["species",
														[
															[
																["food", 0],
																["body", 3],
																["population", 1],
																["traits", ["burrowing", "horns"]]
															]
														]
													],
													["bag", 4]
												],
												[
													["id", 3],
													["species",
														[]
													],
													["bag", 5]
												]
											],
											10,
											[]
										]
		self.case40_out = json.dumps([
												[
												[
													["id", 1],
													["species",
														[
															[
																["food", 4],
																["body", 3],
																["population", 4],
																["traits", ["foraging", "carnivore", "scavenger"]]
															]
														]
													],
													["bag", 3]],
												[
													["id", 2],
													["species",
														[]
													],
													["bag", 4]
												],
												[
													["id", 3],
													["species",
														[]
													],
													["bag", 5]
												]
												],
												10,
												[]
												])
		self.case41_in = [
											[
												[
													["id",1],
													["species",
														[
															[["food",0],["body",3],["population",1],["traits",[]]],
															[["food",1],["body",3],["population",1],["traits",[]]]
														]
													],
													["bag",0]
												],
												[
													["id",2],
													["species",[]],
													["bag",0]
												],
												[
													["id",3],
													["species",[]],
													["bag",0]
												]
											],
											5,
											[]
										]
		self.case41_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],4,[]])
		self.case42_in = [[[["id",1],["species",[[["food",0],["body",3],["population",3],["traits",["foraging"]]],[["food",0],["body",3],["population",3],["traits",[]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],5,[]]
		self.case42_out = json.dumps([[[["id",1],["species",[[["food",2],["body",3],["population",3],["traits",["foraging"]]],[["food",0],["body",3],["population",3],["traits",[]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],3,[]])
		self.case43_in = [[[["id",1],["species",[[["food",2],["body",3],["population",3],["traits",["foraging"]]],[["food",1],["body",3],["population",3],["traits",[]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],5,[]]
		self.case43_out = json.dumps([[[["id",1],["species",[[["food",3],["body",3],["population",3],["traits",["foraging"]]],[["food",1],["body",3],["population",3],["traits",[]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],4,[]])
		self.case44_in = [[[["id",1],["species",[[["food",0],["body",3],["population",2],["traits",["carnivore"]]],[["food",0],["body",3],["population",1],["traits",["carnivore","scavenger"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",2],["traits",[]]]]],["bag",0]],[["id",3],["species",[]],["bag",0]]],5,[]]
		self.case44_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",2],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",["carnivore","scavenger"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",3],["species",[]],["bag",0]]],3,[]])
		self.case45_in = [[[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",0],["body",3],["population",1],["traits",["carnivore","scavenger"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",2],["traits",[]]]]],["bag",0]],[["id",3],["species",[]],["bag",0]]],1,[]]
		self.case45_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore"]]],[["food",0],["body",3],["population",1],["traits",["carnivore","scavenger"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",3],["species",[]],["bag",0]]],0,[]])
		self.case46_in = [[[["id",1],["species",[[["food",0],["body",3],["population",2],["traits",["carnivore","scavenger"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",2],["traits",[]]]]],["bag",0]],[["id",3],["species",[]],["bag",0]]],5,[]]
		self.case46_out = json.dumps([[[["id",1],["species",[[["food",2],["body",3],["population",2],["traits",["carnivore","scavenger"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",3],["species",[]],["bag",0]]],3,[]])
		self.case47_in = [[[["id",1],["species",[[["food",1],["body",3],["population",2],["traits",["carnivore"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",2],["traits",["scavenger"]]]]],["bag",0]],[["id",3],["species",[]],["bag",0]]],5,[]]
		self.case47_out = json.dumps([[[["id",1],["species",[[["food",2],["body",3],["population",2],["traits",["carnivore"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",["scavenger"]]]]],["bag",0]],[["id",3],["species",[]],["bag",0]]],4,[]])
		self.case48_in = [[[["id",1],["species",[[["food",1],["body",3],["population",2],["traits",["carnivore"]]],[["food",1],["body",3],["population",2],["traits",["carnivore","scavenger"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",2],["traits",[]]]]],["bag",0]],[["id",3],["species",[[["food",1],["body",3],["population",2],["traits",["scavenger"]]],[["food",1],["body",3],["population",2],["traits",["scavenger"]]]]],["bag",0]]],3,[]]
		self.case48_out = json.dumps([[[["id",1],["species",[[["food",2],["body",3],["population",2],["traits",["carnivore"]]],[["food",2],["body",3],["population",2],["traits",["carnivore","scavenger"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",3],["species",[[["food",2],["body",3],["population",2],["traits",["scavenger"]]],[["food",1],["body",3],["population",2],["traits",["scavenger"]]]]],["bag",0]]],0,[]])
		self.case49_in = [[[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",3],["traits",[]]]]],["bag",0],["cards",[]]],[["id",2],["species",[]],["bag",0],["cards",[]]],[["id",3],["species",[]],["bag",0],["cards",[]]]],5,[]]
		self.case49_out = json.dumps([[[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",2],["body",3],["population",3],["traits",[]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],4,[]])
		self.case50_in = [[[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",["cooperation"]]],[["food",0],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],5,[]]
		self.case50_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",["cooperation"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],3,[]])
		self.case51_in = [[[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",["cooperation"]]],[["food",0],["body",3],["population",1],["traits",["cooperation"]]],[["food",0],["body",3],["population",1],["traits",["cooperation"]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],5,[]]
		self.case51_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",["cooperation"]]],[["food",1],["body",3],["population",1],["traits",["cooperation"]]],[["food",1],["body",3],["population",1],["traits",["cooperation"]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],2,[]])
		self.case52_in = [[[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",["cooperation"]]],[["food",0],["body",3],["population",1],["traits",["cooperation"]]],[["food",0],["body",3],["population",1],["traits",["cooperation"]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],2,[]]
		self.case52_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",["cooperation"]]],[["food",1],["body",3],["population",1],["traits",["cooperation"]]],[["food",0],["body",3],["population",1],["traits",["cooperation"]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],0,[]])
		self.case53_in = [[[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore","scavenger","cooperation"]]],[["food",1],["body",3],["population",3],["traits",["carnivore"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",2],["traits",[]]]]],["bag",0]],[["id",3],["species",[]],["bag",0]]],3,[]]
		self.case53_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore","scavenger","cooperation"]]],[["food",3],["body",3],["population",3],["traits",["carnivore"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",3],["species",[]],["bag",0]]],0,[]])
		self.case54_in = [[[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore","scavenger","cooperation"]]],[["food",0],["body",3],["population",4],["traits",["carnivore","foraging"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",2],["traits",[]]]]],["bag",0]],[["id",3],["species",[]],["bag",0]]],5,[]]
		self.case54_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore","scavenger","cooperation"]]],[["food",4],["body",3],["population",4],["traits",["carnivore","foraging"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",3],["species",[]],["bag",0]]],0,[]])
		self.case55_in = [[[["id",1],["species",[[["food",0],["body",3],["population",2],["traits",["carnivore","scavenger","foraging"]]],[["food",0],["body",3],["population",4],["traits",["carnivore"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",2],["traits",[]]]]],["bag",0]],[["id",3],["species",[]],["bag",0]]],5,[]]
		self.case55_out = json.dumps([[[["id",1],["species",[[["food",2],["body",3],["population",2],["traits",["carnivore","scavenger","foraging"]]],[["food",1],["body",3],["population",4],["traits",["carnivore"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",3],["species",[]],["bag",0]]],2,[]])
		self.case56_in = [[[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",["fat-tissue"]],["fat-food",0]]]],["bag",0],["cards",[]]],[["id",2],["species",[]],["bag",0],["cards",[]]],[["id",2],["species",[]],["bag",0],["cards",[]]]],5,[]]
		self.case56_out = json.dumps([[[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",["fat-tissue"]],["fat-food",3]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",2],["species",[]],["bag",0]]],2,[]])
		self.case57_in = [[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],5,[]]
		self.case57_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]],5,[]])
		self.case58_in = [
											[
												[
													["id", 1],
													["species",
														[
															[
																["food", 2],
																["body", 3],
																["population", 3],
																["traits",["carnivore"]]
															]
														]
													],
													["bag", 0],
													["cards",
														[
															[1, "carnivore"],
															[2, "ambush"]
														]
													]
												],
												[
													["id", 2],
													["species",
														[
															[
																["food", 0],
																["body", 4],
																["population", 4],
																["traits",["horns"]]
															]
														]
													],
													["bag", 0],
													["cards",
														[
															[3, "carnivore"],
															[-2, "ambush"]
														]
													]
												],
												[
													["id", 3],
													["species",
														[
															[
																["food", 0],
																["body", 1],
																["population", 1],
																["traits", []]
															]
														]
													],
													["bag", 0],
													["cards",
														[
															[7, "carnivore"],
															[-3, "ambush"]
														]
													]
												]
											],
											5,
											[
												[-3, "burrowing"],
												[-2, "burrowing"],
												[-1, "burrowing"],
												[0, "burrowing"],
												[1, "burrowing"],
												[2, "burrowing"],
												[3, "burrowing"]
											]
										]
		self.case58_out = json.dumps([
												[
													[
														["id", 1],
														["species",
															[
																[
																	["food", 2],
																	["body", 3],
																	["population", 2],
																	["traits",["carnivore"]]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[1, "carnivore"],
																[2, "ambush"]
															]
														]
													],
													[
														["id", 2],
														["species",
															[
																[
																	["food", 0],
																	["body", 4],
																	["population", 3],
																	["traits",["horns"]]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[3, "carnivore"],
																[-2, "ambush"]
															]
														]
													],
													[
														["id", 3],
														["species",
															[
																[
																	["food", 0],
																	["body", 1],
																	["population", 1],
																	["traits", []]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[7, "carnivore"],
																[-3, "ambush"]
															]
														]
													]
												],
												5,
												[
													[-3, "burrowing"],
													[-2, "burrowing"],
													[-1, "burrowing"],
													[0, "burrowing"],
													[1, "burrowing"],
													[2, "burrowing"],
													[3, "burrowing"]
												]
											])
		self.case59_in = [
											[
												[
													["id", 1],
													["species",
														[
															[
																["food", 0],
																["body", 3],
																["population", 7],
																["traits", ["carnivore","cooperation"]]
															],
															[
																["food", 0],
																["body", 3],
																["population", 7],
																["traits", ["cooperation"]]
															],
															[
																["food", 7],
																["body", 3],
																["population", 7],
																["traits", ["cooperation"]]
															],
															[
																["food", 0],
																["body", 3],
																["population", 7],
																["traits", []]
															]

														]
													],
													["bag", 0],
													["cards",
														[
															[1, "carnivore"],
															[2, "ambush"]
														]
													]
												],
												[
													["id", 2],
													["species",
														[
															[
																["food", 1],
																["body", 3],
																["population", 3],
																["traits",[]]
															],
															[
																["food", 0],
																["body", 3],
																["population", 3],
																["traits", []]
															]
														]
													],
													["bag", 0],
													["cards",
														[
															[3, "carnivore"],
															[-2, "ambush"]
														]
													]
												],
												[
													["id", 3],
													["species",
														[
															[
																["food", 1],
																["body", 3],
																["population", 5],
																["traits",[]]
															],
															[
																["food", 0],
																["body", 3],
																["population", 5],
																["traits", []]
															]
														]
													],
													["bag", 0],
													["cards",[]]
												]
											],
											15,
											[
												[-3, "burrowing"],
												[-2, "burrowing"],
												[-1, "burrowing"],
												[0, "burrowing"],
												[1, "burrowing"],
												[2, "burrowing"],
												[3, "burrowing"]
											]
										]
		self.case59_out = json.dumps([
												[
													[
														["id", 1],
														["species",
															[
																[
																	["food", 0],
																	["body", 3],
																	["population", 7],
																	["traits", ["carnivore","cooperation"]]
																],
																[
																	["food", 1],
																	["body", 3],
																	["population", 7],
																	["traits", ["cooperation"]]
																],
																[
																	["food", 7],
																	["body", 3],
																	["population", 7],
																	["traits", ["cooperation"]]
																],
																[
																	["food", 0],
																	["body", 3],
																	["population", 7],
																	["traits", []]
																]

															]
														],
														["bag", 0],
														["cards",
															[
																[1, "carnivore"],
																[2, "ambush"]
															]
														]
													],
													[
														["id", 2],
														["species",
															[
																[
																	["food", 1],
																	["body", 3],
																	["population", 3],
																	["traits",[]]
																],
																[
																	["food", 0],
																	["body", 3],
																	["population", 3],
																	["traits", []]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[3, "carnivore"],
																[-2, "ambush"]
															]
														]
													],
													[
														["id", 3],
														["species",
															[
																[
																	["food", 1],
																	["body", 3],
																	["population", 5],
																	["traits",[]]
																],
																[
																	["food", 0],
																	["body", 3],
																	["population", 5],
																	["traits", []]
																]
															]
														],
														["bag", 0]
													]
												],
												14,
												[
													[-3, "burrowing"],
													[-2, "burrowing"],
													[-1, "burrowing"],
													[0, "burrowing"],
													[1, "burrowing"],
													[2, "burrowing"],
													[3, "burrowing"]
												]
											])
		self.case60_in = [
											[
												[
													["id", 1],
													["species",
														[
															[
																["food", 0],
																["body", 7],
																["population", 7],
																["traits", ["burrowing", "fat-tissue"]]
															]
														]
													],
													["bag", 0]
												],
												[
													["id", 2],
													["species", []],
													["bag", 0]
												],
												[
													["id", 3],
													["species", []],
													["bag", 0]
												]
											],
											100,
											[
												[-3, "burrowing"],
												[-2, "burrowing"],
												[-1, "burrowing"],
												[1, "burrowing"],
												[2, "burrowing"],
												[3, "burrowing"]
											]
										]
		self.case60_out = json.dumps([
												[
													[
														["id", 1],
														["species",
															[
																[
																	["food", 0],
																	["body", 7],
																	["population", 7],
																	["traits", ["burrowing", "fat-tissue"]],
																	["fat-food", 7]
																]
															]
														],
														["bag", 0]
													],
													[
														["id", 2],
														["species", []],
														["bag", 0]
													],
													[
														["id", 3],
														["species", []],
														["bag", 0]
													]
												],
												93,
												[
													[-3, "burrowing"],
													[-2, "burrowing"],
													[-1, "burrowing"],
													[1, "burrowing"],
													[2, "burrowing"],
													[3, "burrowing"]
												]
											])
		self.case61_in = [
											[
												[
													["id", 1],
													["species",
														[
															[
																["food", 0],
																["body", 7],
																["population", 7],
																["traits", ["carnivore", "fat-tissue"]]
															]
														]
													],
													["bag", 0]
												],
												[
													["id", 2],
													["species", []],
													["bag", 0]
												],
												[
													["id", 3],
													["species", []],
													["bag", 0]
												]
											],
											100,
											[
												[-8, "carnivore"],
												[-7, "carnivore"],
												[-6, "carnivore"],
												[-5, "carnivore"],
												[-4, "carnivore"],
												[-3, "carnivore"],
												[-2, "carnivore"],
												[-1, "carnivore"],
												[1, "carnivore"],
												[2, "carnivore"],
												[3, "carnivore"],
												[4, "carnivore"],
												[5, "carnivore"],
												[6, "carnivore"],
												[7, "carnivore"],
												[8, "carnivore"]
											]
										]
		self.case61_out = json.dumps([
												[
													[
														["id", 1],
														["species",
															[
																[
																	["food", 0],
																	["body", 7],
																	["population", 7],
																	["traits", ["carnivore", "fat-tissue"]],
																	["fat-food", 7]
																]
															]
														],
														["bag", 0]
													],
													[
														["id", 2],
														["species", []],
														["bag", 0]
													],
													[
														["id", 3],
														["species", []],
														["bag", 0]
													]
												],
												93,
												[
													[-8, "carnivore"],
													[-7, "carnivore"],
													[-6, "carnivore"],
													[-5, "carnivore"],
													[-4, "carnivore"],
													[-3, "carnivore"],
													[-2, "carnivore"],
													[-1, "carnivore"],
													[1, "carnivore"],
													[2, "carnivore"],
													[3, "carnivore"],
													[4, "carnivore"],
													[5, "carnivore"],
													[6, "carnivore"],
													[7, "carnivore"],
													[8, "carnivore"]
												]
											])
		self.case62_in = [
											[
												[
													["id", 1],
													["species",
														[
															[
																["food", 2],
																["body", 3],
																["population",3],
																["traits",[]]
															],
															[
																["food", 2],
																["body", 3],
																["population", 3],
																["traits", ["carnivore","pack-hunting", "ambush"]]
															]
														]
													],
													["bag", 0],
													["cards",
														[
															[1, "carnivore"],
															[2, "ambush"]
														]
													]
												],
												[
													["id", 2],
													["species",
														[
															[
																["food", 2],
																["body",3],
																["population",3],
																["traits",["carnivore"]]
															],
															[
																["food", 2],
																["body", 3],
																["population", 3],
																["traits", ["carnivore","pack-hunting", "ambush"]]
															]
														]
													],
													["bag", 0]
												],
												[
													["id", 3],
													["species",
														[
															[
																["food", 2],
																["body",3],
																["population",3],
																["traits",["carnivore"]]
															],
															[
																["food", 2],
																["body", 3],
																["population", 3],
																["traits", ["carnivore","pack-hunting", "ambush"]]
															]
														]
													],
													["bag", 0],
													["cards",
														[
															[7, "carnivore"],
															[-3, "ambush"]
														]
													]
												]
											],
											1,
											[
												[-3, "burrowing"],
												[-2, "burrowing"],
												[-1, "burrowing"],
												[0, "burrowing"],
												[1, "burrowing"],
												[2, "burrowing"],
												[3, "burrowing"]
											]
										]
		self.case62_out = json.dumps([
												[
													[
														["id", 1],
														["species",
															[
																[
																	["food", 3],
																	["body",3],
																	["population",3],
																	["traits",[]]
																],
																[
																	["food", 2],
																	["body", 3],
																	["population", 3],
																	["traits", ["carnivore","pack-hunting", "ambush"]]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[1, "carnivore"],
																[2, "ambush"]
															]
														]
													],
													[
														["id", 2],
														["species",
															[
																[
																	["food", 2],
																	["body", 3],
																	["population",3],
																	["traits",["carnivore"]]
																],
																[
																	["food", 2],
																	["body", 3],
																	["population", 3],
																	["traits", ["carnivore","pack-hunting", "ambush"]]
																]
															]
														],
														["bag", 0]
													],
													[
														["id", 3],
														["species",
															[
																[
																	["food", 2],
																	["body", 3],
																	["population",3],
																	["traits",["carnivore"]]
																],
																[
																	["food", 2],
																	["body", 3],
																	["population", 3],
																	["traits", ["carnivore","pack-hunting", "ambush"]]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[7, "carnivore"],
																[-3, "ambush"]
															]
														]
													]
												],
												0,
												[
													[-3, "burrowing"],
													[-2, "burrowing"],
													[-1, "burrowing"],
													[0, "burrowing"],
													[1, "burrowing"],
													[2, "burrowing"],
													[3, "burrowing"]
												]
											])
		self.case63_in = [
											[
												[
													["id", 1],
													["species",
														[
															[
																["food", 2],
																["body", 3],
																["population",3],
																["traits",["fat-tissue"]]
															],
															[
																["food", 2],
																["body", 3],
																["population", 3],
																["traits", ["carnivore","pack-hunting", "ambush"]]
															]
														]
													],
													["bag", 0],
													["cards",
														[
															[1, "carnivore"],
															[2, "ambush"]
														]
													]
												],
												[
													["id", 2],
													["species",
														[
															[
																["food", 2],
																["body",3],
																["population",3],
																["traits",["carnivore"]]
															],
															[
																["food", 2],
																["body", 3],
																["population", 3],
																["traits", ["carnivore","pack-hunting", "ambush"]]
															]
														]
													],
													["bag", 0],
													["cards",
														[
															[3, "carnivore"],
															[-2, "ambush"]
														]
													]
												],
												[
													["id", 3],
													["species",
														[
															[
																["food", 2],
																["body",3],
																["population",3],
																["traits",["carnivore"]]
															],
															[
																["food", 2],
																["body", 3],
																["population", 3],
																["traits", ["carnivore","pack-hunting", "ambush"]]
															]
														]
													],
													["bag", 0],
													["cards",
														[
															[7, "carnivore"],
															[-3, "ambush"]
														]
													]
												]
											],
											5,
											[
												[-3, "burrowing"],
												[-2, "burrowing"],
												[-1, "burrowing"],
												[0, "burrowing"],
												[1, "burrowing"],
												[2, "burrowing"],
												[3, "burrowing"]
											]
										]
		self.case63_out = json.dumps([
												[
													[
														["id", 1],
														["species",
															[
																[
																	["food", 2],
																	["body",3],
																	["population",3],
																	["traits",["fat-tissue"]],
																	["fat-food", 3]
																],
																[
																	["food", 2],
																	["body", 3],
																	["population", 3],
																	["traits", ["carnivore","pack-hunting", "ambush"]]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[1, "carnivore"],
																[2, "ambush"]
															]
														]
													],
													[
														["id", 2],
														["species",
															[
																[
																	["food", 2],
																	["body",3],
																	["population",3],
																	["traits",["carnivore"]]
																],
																[
																	["food", 2],
																	["body", 3],
																	["population", 3],
																	["traits", ["carnivore","pack-hunting", "ambush"]]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[3, "carnivore"],
																[-2, "ambush"]
															]
														]
													],
													[
														["id", 3],
														["species",
															[
																[
																	["food", 2],
																	["body", 3],
																	["population",3],
																	["traits",["carnivore"]]
																],
																[
																	["food", 2],
																	["body", 3],
																	["population", 3],
																	["traits", ["carnivore","pack-hunting", "ambush"]]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[7, "carnivore"],
																[-3, "ambush"]
															]
														]
													]
												],
												2,
												[
													[-3, "burrowing"],
													[-2, "burrowing"],
													[-1, "burrowing"],
													[0, "burrowing"],
													[1, "burrowing"],
													[2, "burrowing"],
													[3, "burrowing"]
												]
											])
		self.case64_in = [
											[
												[
													["id", 1],
													["species",
														[
															[
																["food", 3],
																["body",3],
																["population",3],
																["traits",[]]
															],
															[
																["food", 2],
																["body", 3],
																["population", 3],
																["traits", ["carnivore","pack-hunting", "ambush"]]
															]
														]
													],
													["bag", 0],
													["cards",
														[
															[1, "carnivore"],
															[2, "ambush"]
														]
													]
												],
												[
													["id", 2],
													["species",
														[
															[
																["food", 2],
																["body", 3],
																["population",3],
																["traits",["climbing"]]
															],
															[
																["food", 2],
																["body", 3],
																["population", 3],
																["traits", ["climbing","pack-hunting", "ambush"]]
															]
														]
													],
													["bag", 0],
													["cards",
														[
															[3, "carnivore"],
															[-2, "ambush"]
														]
													]
												],
												[
													["id", 3],
													["species",
														[
															[
																["food", 2],
																["body", 3],
																["population",3],
																["traits",["climbing"]]
															],
															[
																["food", 2],
																["body", 3],
																["population", 3],
																["traits", ["climbing","pack-hunting", "ambush"]]
															]
														]
													],
													["bag", 0],
													["cards",
														[
															[7, "carnivore"],
															[-3, "ambush"]
														]
													]
												]
											],
											5,
											[
												[-3, "burrowing"],
												[-2, "burrowing"],
												[-1, "burrowing"],
												[0, "burrowing"],
												[1, "burrowing"],
												[2, "burrowing"],
												[3, "burrowing"]
											]
										]
		self.case64_out = json.dumps([
												[
													[
														["id", 1],
														["species",
															[
																[
																	["food", 3],
																	["body", 3],
																	["population",3],
																	["traits",[]]
																],
																[
																	["food", 2],
																	["body", 3],
																	["population", 3],
																	["traits", ["carnivore","pack-hunting", "ambush"]]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[1, "carnivore"],
																[2, "ambush"]
															]
														]
													],
													[
														["id", 2],
														["species",
															[
																[
																	["food", 2],
																	["body", 3],
																	["population",3],
																	["traits",["climbing"]]
																],
																[
																	["food", 2],
																	["body", 3],
																	["population", 3],
																	["traits", ["climbing","pack-hunting", "ambush"]]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[3, "carnivore"],
																[-2, "ambush"]
															]
														]
													],
													[
														["id", 3],
														["species",
															[
																[
																	["food", 2],
																	["body",3],
																	["population",3],
																	["traits",["climbing"]]
																],
																[
																	["food", 2],
																	["body", 3],
																	["population", 3],
																	["traits", ["climbing","pack-hunting", "ambush"]]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[7, "carnivore"],
																[-3, "ambush"]
															]
														]
													]
												],
												5,
												[
													[-3, "burrowing"],
													[-2, "burrowing"],
													[-1, "burrowing"],
													[0, "burrowing"],
													[1, "burrowing"],
													[2, "burrowing"],
													[3, "burrowing"]
												]
											])
		self.case65_in = [
												[
													[
														["id", 1],
														["species",
															[
																[
																	["food", 0],
																	["body", 3],
																	["population", 5],
																	["traits", ["carnivore","cooperation"]]
																],
																[
																	["food", 0],
																	["body", 3],
																	["population", 3],
																	["traits", ["carnivore","cooperation"]]
																],
																[
																	["food", 0],
																	["body", 3],
																	["population", 3],
																	["traits", ["carnivore","cooperation"]]
																],
																[
																	["food", 0],
																	["body", 3],
																	["population", 2],
																	["traits", ["carnivore"]]
																],
																[
																	["food", 0],
																	["body", 3],
																	["population", 2],
																	["traits", ["carnivore"]]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[2, "ambush"]
															]
														]
													],
													[
														["id", 2],
														["species",
															[
																[
																	["food", 0],
																	["body",3],
																	["population",4],
																	["traits",["scavenger", "cooperation"]]
																],
																[
																	["food", 0],
																	["body", 3],
																	["population", 3],
																	["traits", []]
																],
																[
																	["food", 0],
																	["body", 3],
																	["population", 3],
																	["traits", []]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[3, "carnivore"],
																[-2, "ambush"]
															]
														]
													],
													[
														["id", 3],
														["species",
															[
																[
																	["food", 2],
																	["body",3],
																	["population",3],
																	["traits",[]]
																],
																[
																	["food", 2],
																	["body", 3],
																	["population", 3],
																	["traits", []]
																]
															]
														],
														["bag", 0],
														["cards",
															[
																[7, "carnivore"],
																[-3, "ambush"]
															]
														]
													]
												],
												15,
												[
													[-3, "burrowing"],
													[-2, "burrowing"],
													[-1, "burrowing"],
													[0, "burrowing"],
													[1, "burrowing"],
													[2, "burrowing"],
													[3, "burrowing"]
												]
											]
		self.case65_out = json.dumps([
																  [
																    [
																      ["id", 1],
																      ["species",
																        [
																          [
																            ["food", 1],
																            ["body", 3],
																            ["population", 5],
																            ["traits", ["carnivore","cooperation"]]
																          ],
																          [
																            ["food", 1],
																            ["body", 3],
																            ["population", 3],
																            ["traits", ["carnivore","cooperation"]]
																          ],
																          [
																            ["food", 1],
																            ["body", 3],
																            ["population", 3],
																            ["traits", ["carnivore","cooperation"]]
																          ],
																          [
																            ["food", 1],
																            ["body", 3],
																            ["population", 2],
																            ["traits", ["carnivore"]]
																          ],
																          [
																            ["food", 0],
																            ["body", 3],
																            ["population", 2],
																            ["traits", ["carnivore"]]
																          ]
																        ]
																      ],
																      ["bag", 0],
																      ["cards",
																        [
																          [2, "ambush"]
																        ]
																      ]
																    ],
																    [
																      ["id", 2],
																      ["species",
																        [
																          [
																            ["food", 1],
																            ["body",3],
																            ["population",3],
																            ["traits",["scavenger", "cooperation"]]
																          ],
																          [
																            ["food", 1],
																            ["body", 3],
																            ["population", 3],
																            ["traits", []]
																          ],
																          [
																            ["food", 0],
																            ["body", 3],
																            ["population", 3],
																            ["traits", []]
																          ]
																        ]
																      ],
																      ["bag", 0],
																      ["cards",
																        [
																          [3, "carnivore"],
																          [-2, "ambush"]
																        ]
																      ]
																    ],
																    [
																      ["id", 3],
																      ["species",
																        [
																          [
																            ["food", 2],
																            ["body",3],
																            ["population",3],
																            ["traits",[]]
																          ],
																          [
																            ["food", 2],
																            ["body", 3],
																            ["population", 3],
																            ["traits", []]
																          ]
																        ]
																      ],
																      ["bag", 0],
																      ["cards",
																        [
																          [7, "carnivore"],
																          [-3, "ambush"]
																        ]
																      ]
																    ]
																  ],
																  9,
																  [
																    [-3, "burrowing"],
																    [-2, "burrowing"],
																    [-1, "burrowing"],
																    [0, "burrowing"],
																    [1, "burrowing"],
																    [2, "burrowing"],
																    [3, "burrowing"]
																  ]
																])
		self.m1_in = [[[["id",2],
										["species",
											[[["food",0],
												["body",3],
												["population",1],
												["traits",["carnivore"]]],
											[["food",1],
												["body",3],
												["population",1],
												["traits",[]]]]],
										["bag",0]],
									[["id",99],
										["species",
										[[["food",0],
											["body",3],
											["population",1],
											["traits",["climbing"]]]]],
										["bag",0]],
									[["id",88],
										["species",[]],
										["bag",0]]],
									1,
									[]]
		self.m1_out = json.dumps([[[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",99],["species",[[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",88],["species",[]],["bag",0]]],1,[]])
		self.m10_in = [[[["id",111],["species",[[["food",0],["body",0],["population",5],["traits",["foraging"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],1,[]]
		self.m10_out = json.dumps([[[["id",111],["species",[[["food",1],["body",0],["population",5],["traits",["foraging"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],0,[]])
		self.m11_in = [[[["id",111],["species",[[["food",0],["body",0],["population",5],["traits",["foraging"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],2,[]]
		self.m11_out = json.dumps([[[["id",111],["species",[[["food",2],["body",0],["population",5],["traits",["foraging"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],0,[]])
		self.m12_in = [[[["id",112],
											["species",
												[[["food",0],
													["body",0],
													["population",5],
													["traits",["foraging","cooperation"]]],
												[["food",0],
													["body",0],
													["population",3],
													["traits",["long-neck"]]]]],
											["bag",0]],
										[["id",55],
											["species",
												[[["food",0],
													["body",3],
													["population",1],
													["traits",[]]],
												[["food",0],
													["body",3],
													["population",1],
													["traits",["climbing"]]]]],
											["bag",0]],
										[["id",66],
											["species",
												[[["food",1],
													["body",3],
													["population",1],
													["traits",[]]]]],
											["bag",0]]],
										5,
										[]]
		self.m12_out = json.dumps([[[["id",112],["species",[[["food",2],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",2],["body",0],["population",3],["traits",["long-neck"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],1,[]])
		self.m13_in = [[[["id",112],["species",[[["food",0],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",0],["body",0],["population",3],["traits",["long-neck"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],4,[]]
		self.m13_out = json.dumps([[[["id",112],["species",[[["food",2],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",2],["body",0],["population",3],["traits",["long-neck"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],0,[]])
		self.m14_in = [[[["id",112],["species",[[["food",0],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",0],["body",0],["population",3],["traits",["long-neck"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],3,[]]
		self.m14_out = json.dumps([[[["id",112],["species",[[["food",2],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",1],["body",0],["population",3],["traits",["long-neck"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],0,[]])
		self.m15_in = [[[["id",112],["species",[[["food",0],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",0],["body",0],["population",3],["traits",["long-neck"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],0,[]]
		self.m15_out = json.dumps([[[["id",112],["species",[[["food",0],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",0],["body",0],["population",3],["traits",["long-neck"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],0,[]])
		self.m16_in = [[[["id",113],
											["species",
											[[["food",0],
												["body",0],
												["population",5],
												["traits",["foraging","cooperation"]]],
											[["food",0],
												["body",0],
												["population",5],
												["traits",["foraging","cooperation"]]],
											[["food",0],
												["body",0],
												["population",3],
												["traits",["long-neck"]]]]],
											["bag",0]],
										[["id",55],
											["species",
												[[["food",0],
													["body",3],
													["population",1],
													["traits",[]]],
												[["food",0],
													["body",3],
													["population",1],
													["traits",["climbing"]]]]],
											["bag",0]],
										[["id",66],
											["species",
												[[["food",1],
													["body",3],
													["population",1],
													["traits",[]]]]],
											["bag",0]]],
									12,
									[]]
		self.m16_out = json.dumps([[[["id",113],["species",[[["food",2],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",4],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",3],["body",0],["population",3],["traits",["long-neck"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],3,[]])
		self.m17_in = [[[["id",113],["species",[[["food",0],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",0],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",0],["body",0],["population",3],["traits",["long-neck"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],10,[]]
		self.m17_out = json.dumps([[[["id",113],["species",[[["food",2],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",4],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",3],["body",0],["population",3],["traits",["long-neck"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],1,[]])
		self.m18_in = [[[["id",113],
											["species",
												[[["food",0],
													["body",0],
													["population",5],
													["traits",["foraging","cooperation"]]],
												[["food",0],
													["body",0],
													["population",5],
													["traits",["foraging","cooperation"]]],
												[["food",0],
													["body",0],
													["population",3],
													["traits",["long-neck"]]]]],
											["bag",0]],
										[["id",55],
											["species",
												[[["food",0],
													["body",3],
													["population",1],
													["traits",[]]],
												[["food",0],
													["body",3],
													["population",1],
													["traits",["climbing"]]]]],
											["bag",0]],
										[["id",66],
											["species",
												[[["food",1],
													["body",3],
													["population",1],
													["traits",[]]]]],
												["bag",0]]],
										8,
										[]]
		self.m18_out = json.dumps([[[["id",113],["species",[[["food",2],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",4],["body",0],["population",5],["traits",["foraging","cooperation"]]],[["food",2],["body",0],["population",3],["traits",["long-neck"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],0,[]])
		self.m19_in = [[[["id",2],
												["species",
													[[["food",0],
														["body",3],
														["population",1],
														["traits",["carnivore"]]],
													[["food",1],
														["body",3],
														["population",1],
														["traits",[]]]]],
												["bag",0]],
											[["id",66],
												["species",
													[[["food",1],
														["body",3],
														["population",1],
														["traits",[]]]]],
												["bag",0]],
											[["id",1],
												["species",
													[[["food",0],
														["body",3],
														["population",1],
														["traits",[]]],
													[["food",1],
														["body",3],
														["population",1],
														["traits",[]]],
													[["food",0],
														["body",3],
														["population",1],
														["traits",["carnivore"]]]]],
												["bag",0]]],
											1,
											[[-3,"ambush"],[-2,"ambush"]]]
		self.m19_out = json.dumps([[[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[]],["bag",0],["cards",[[-3,"ambush"],[-2,"ambush"]]]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],0,[]])
		self.m2_in = [[[["id",222],["species",[[["food",0],["body",2],["population",1],["traits",["fat-tissue"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],2,[]]
		self.m2_out = json.dumps([[[["id",222],["species",[[["food",0],["body",2],["population",1],["traits",["fat-tissue"]],["fat-food",2]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],0,[]])
		self.m20_in = [[[["id",2],
											["species",
											[[["food",0],
												["body",3],
												["population",1],
												["traits",["carnivore"]]],
											[["food",1],
											["body",3],
											["population",1],
											["traits",[]]]]],
										["bag",0]],
									[["id",3],
										["species",
										[[["food",0],
											["body",0],
											["population",1],
											["traits",["horns"]]]]],
										["bag",0]],
									[["id",32],
										["species",[]],
										["bag",0]]],1,
										[[-3,"ambush"],[-2,"ambush"],[-1,"ambush"],[0,"ambush"]]]
		self.m20_out = json.dumps([[[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[-1,"ambush"],[0,"ambush"]]]],[["id",3],["species",[]],["bag",0],["cards",[[-3,"ambush"],[-2,"ambush"]]]],[["id",32],["species",[]],["bag",0]]],1,[]])
		self.m21_in = [[[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",0],["body",0],["population",1],["traits",["scavenger"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],3,[[-3,"ambush"],[-2,"ambush"]]]
		self.m21_out = json.dumps([[[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[]],["bag",0],["cards",[[-3,"ambush"],[-2,"ambush"]]]],[["id",333],["species",[[["food",1],["body",0],["population",1],["traits",["scavenger"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],1,[]])
		self.m22_in = [[[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",0],["body",0],["population",1],["traits",["scavenger"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],2,[[-3,"ambush"],[-2,"ambush"]]]
		self.m22_out = json.dumps([[[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[]],["bag",0],["cards",[[-3,"ambush"],[-2,"ambush"]]]],[["id",333],["species",[[["food",1],["body",0],["population",1],["traits",["scavenger"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],0,[]])
		self.m23_in = [[[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",0],["body",0],["population",1],["traits",["scavenger"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],1,[[-3,"ambush"],[-2,"ambush"]]]
		self.m23_out = json.dumps([[[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[]],["bag",0],["cards",[[-3,"ambush"],[-2,"ambush"]]]],[["id",333],["species",[[["food",0],["body",0],["population",1],["traits",["scavenger"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],0,[]])
		self.m24_in = [[[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",0],["body",0],["population",3],["traits",["scavenger","foraging"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],4,[[-3,"ambush"],[-2,"ambush"]]]
		self.m24_out = json.dumps([[[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",2],["body",0],["population",2],["traits",["scavenger","foraging"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],1,[[-3,"ambush"],[-2,"ambush"]]])
		self.m25_in = [[[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",0],["body",0],["population",3],["traits",["scavenger","foraging"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],3,[[-3,"ambush"],[-2,"ambush"]]]
		self.m25_out = json.dumps([[[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",2],["body",0],["population",2],["traits",["scavenger","foraging"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],0,[[-3,"ambush"],[-2,"ambush"]]])
		self.m26_in = [[[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",0],["body",0],["population",1],["traits",["scavenger","foraging"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],2,[[-3,"ambush"],[-2,"ambush"]]]
		self.m26_out = json.dumps([[[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[]],["bag",0],["cards",[[-3,"ambush"],[-2,"ambush"]]]],[["id",333],["species",[[["food",1],["body",0],["population",1],["traits",["scavenger","foraging"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],0,[]])
		self.m27_in = [[[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",0],["body",0],["population",4],["traits",["scavenger","foraging","cooperation"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],6,[[-3,"ambush"],[-2,"ambush"]]]
		self.m27_out = json.dumps([[[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",2],["body",0],["population",3],["traits",["scavenger","foraging","cooperation"]]],[["food",1],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],2,[[-3,"ambush"],[-2,"ambush"]]])
		self.m28_in = [[[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",0],["body",0],["population",4],["traits",["scavenger","foraging","cooperation"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],5,[[-3,"ambush"],[-2,"ambush"]]]
		self.m28_out = json.dumps([[[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",2],["body",0],["population",3],["traits",["scavenger","foraging","cooperation"]]],[["food",1],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],1,[[-3,"ambush"],[-2,"ambush"]]])
		self.m29_in = [[[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",0],["body",0],["population",4],["traits",["scavenger","foraging","cooperation"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],4,[[-3,"ambush"],[-2,"ambush"]]]
		self.m29_out = json.dumps([[[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",2],["body",0],["population",3],["traits",["scavenger","foraging","cooperation"]]],[["food",1],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],0,[[-3,"ambush"],[-2,"ambush"]]])
		self.m3_in = [[[["id",222],["species",[[["food",0],["body",2],["population",1],["traits",["fat-tissue"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],1,[]]
		self.m3_out = json.dumps([[[["id",222],["species",[[["food",0],["body",2],["population",1],["traits",["fat-tissue"]],["fat-food",1]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],0,[]])
		self.m30_in = [[[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",0],["body",0],["population",4],["traits",["scavenger","foraging","cooperation"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],3,[[-3,"ambush"],[-2,"ambush"]]]
		self.m30_out = json.dumps([[[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",2],["body",0],["population",3],["traits",["scavenger","foraging","cooperation"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],0,[[-3,"ambush"],[-2,"ambush"]]])
		self.m31_in = [[[["id",333],["species",[[["food",0],["body",0],["population",4],["traits",["scavenger","foraging","carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",0],["body",0],["population",1],["traits",["scavenger"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],6,[[-3,"ambush"],[-2,"ambush"]]]
		self.m31_out = json.dumps([[[["id",333],["species",[[["food",4],["body",0],["population",4],["traits",["scavenger","foraging","carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[]],["bag",0],["cards",[[-3,"ambush"],[-2,"ambush"]]]],[["id",333],["species",[[["food",1],["body",0],["population",1],["traits",["scavenger"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],1,[]])
		self.m32_in = [[[["id",333],["species",[[["food",0],["body",0],["population",4],["traits",["scavenger","foraging","carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],6,[[-3,"ambush"],[-2,"ambush"]]]
		self.m32_out = json.dumps([[[["id",333],["species",[[["food",4],["body",0],["population",4],["traits",["scavenger","foraging","carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[]],["bag",0],["cards",[[-3,"ambush"],[-2,"ambush"]]]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],2,[]])
		self.m33_in = [[[["id",333],
											["species",
												[[["food",0],
													["body",0],
													["population",4],
													["traits",["scavenger","foraging","carnivore"]]],
												[["food",1],
													["body",3],
													["population",1],
													["traits",[]]]]],
											["bag",0]],
										[["id",66],
											["species",
												[[["food",1],
													["body",3],
													["population",1],
													["traits",[]]]]],
											["bag",0]],
										[["id",333],
											["species",
												[[["food",0],
													["body",0],
													["population",1],
													["traits",["scavenger"]]],
												[["food",0],
													["body",3],
													["population",1],
													["traits",["carnivore"]]]]],
											["bag",0]]],
										4,
										[[-3,"ambush"],[-2,"ambush"]]]
		self.m33_out = json.dumps([[[["id",333],["species",[[["food",4],["body",0],["population",4],["traits",["scavenger","foraging","carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",66],["species",[]],["bag",0],["cards",[[-3,"ambush"],[-2,"ambush"]]]],[["id",333],["species",[[["food",0],["body",0],["population",1],["traits",["scavenger"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],0,[]])
		self.m34_in = [[[["id",333],["species",[[["food",0],["body",0],["population",1],["traits",["scavenger","foraging","carnivore"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",333],["species",[[["food",0],["body",0],["population",1],["traits",["scavenger"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],3,[[-3,"ambush"],[-2,"ambush"]]]
		self.m34_out = json.dumps([[[["id",333],["species",[[["food",1],["body",0],["population",1],["traits",["scavenger","foraging","carnivore"]]],[["food",1],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",66],["species",[]],["bag",0],["cards",[[-3,"ambush"],[-2,"ambush"]]]],[["id",333],["species",[[["food",1],["body",0],["population",1],["traits",["scavenger"]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]],0,[]])
		self.m4_in = [[[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],0,[]]
		self.m4_out = json.dumps([[[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],0,[]])
		self.m5_in = [[[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],1,[]]
		self.m5_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],0,[]])
		self.m6_in = [[[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],1,[]]
		self.m6_out = json.dumps([[[["id",55],["species",[[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],0,[]])
		self.m7_in = [[[["id",55],["species",[[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],1,[]]
		self.m7_out = json.dumps([[[["id",55],["species",[[["food",1],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],0,[]])
		self.m8_in = [[[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]]],9,[]]
		self.m8_out = json.dumps([[[["id",66],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]]],9,[]])
		self.m9_in = [[[["id",110],["species",[[["food",0],["body",0],["population",1],["traits",["cooperation"]]],[["food",0],["body",0],["population",1],["traits",[]]]]],["bag",0]],[["id",110],["species",[[["food",0],["body",0],["population",1],["traits",["cooperation"]]],[["food",1],["body",0],["population",1],["traits",[]]]]],["bag",0]],[["id",110],["species",[[["food",0],["body",0],["population",1],["traits",["cooperation"]]],[["food",1],["body",0],["population",1],["traits",[]]]]],["bag",0]]],2,[]]
		self.m9_out = json.dumps([[[["id",110],["species",[[["food",1],["body",0],["population",1],["traits",["cooperation"]]],[["food",1],["body",0],["population",1],["traits",[]]]]],["bag",0]],[["id",110],["species",[[["food",0],["body",0],["population",1],["traits",["cooperation"]]],[["food",1],["body",0],["population",1],["traits",[]]]]],["bag",0]],[["id",110],["species",[[["food",0],["body",0],["population",1],["traits",["cooperation"]]],[["food",1],["body",0],["population",1],["traits",[]]]]],["bag",0]]],0,[]])
		self.m35_in = [[[["id",1],
											["species",
												[[["food",1],
													["body",0],
													["population",2],
													["traits",["cooperation","foraging"]]],
												[["food",0],
													["body",0],
													["population",2],
													["traits",[]]]]],
											["bag",0]],
										[["id",2],
											["species",
												[[["food",1],
													["body",3],
													["population",1],
													["traits",[]]]]],
											["bag",0]],
										[["id",3],
											["species",
												[[["food",1],
													["body",3],
													["population",1],
													["traits",[]]]]],
											["bag",0]]],
										3,
										[]]
		self.m35_out = json.dumps([[[["id",1],["species",[[["food",2],["body",0],["population",2],["traits",["cooperation","foraging"]]],[["food",1],["body",0],["population",2],["traits",[]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",3],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]],1,[]])
		self.m36_in = [[[["id",1],["species",[[["food",0],["body",3],["population",5],["traits",["carnivore","cooperation"]]],[["food",0],["body",3],["population",3],["traits",["carnivore","cooperation"]]],[["food",0],["body",3],["population",3],["traits",["carnivore","cooperation"]]],[["food",0],["body",3],["population",2],["traits",["carnivore"]]],[["food",0],["body",3],["population",2],["traits",["carnivore"]]]]],["bag",0]],[["id",2],["species",[[["food",0],["body",3],["population",4],["traits",["carnivore","scavenger","cooperation"]]],[["food",0],["body",3],["population",3],["traits",[]]],[["food",0],["body",3],["population",3],["traits",[]]]]],["bag",0]],[["id",3],["species",[[["food",2],["body",3],["population",3],["traits",[]]],[["food",2],["body",3],["population",3],["traits",[]]]]],["bag",0]]],15,[]]
		self.m36_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",5],["traits",["carnivore","cooperation"]]],[["food",1],["body",3],["population",3],["traits",["carnivore","cooperation"]]],[["food",1],["body",3],["population",3],["traits",["carnivore","cooperation"]]],[["food",1],["body",3],["population",2],["traits",["carnivore"]]],[["food",0],["body",3],["population",2],["traits",["carnivore"]]]]],["bag",0]],[["id",2],["species",[[["food",1],["body",3],["population",3],["traits",["carnivore","scavenger","cooperation"]]],[["food",1],["body",3],["population",3],["traits",[]]],[["food",0],["body",3],["population",3],["traits",[]]]]],["bag",0]],[["id",3],["species",[[["food",2],["body",3],["population",3],["traits",[]]],[["food",2],["body",3],["population",3],["traits",[]]]]],["bag",0]]],9,[]])

	def tearDown(self):
		del self.case1_in
		del self.case1_out
		del self.case2_in
		del self.case2_out
		del self.case3_in
		del self.case3_out
		del self.case4_in
		del self.case4_out
		del self.case5_in
		del self.case5_out
		del self.case6_in
		del self.case6_out
		del self.case7_in
		del self.case7_out
		del self.case8_in
		del self.case8_out
		del self.case9_in
		del self.case9_out
		del self.case10_in
		del self.case10_out
		del self.case11_in
		del self.case11_out
		del self.case12_in
		del self.case12_out
		del self.case13_in
		del self.case13_out
		del self.case14_in
		del self.case14_out
		del self.case15_in
		del self.case15_out
		del self.case16_in
		del self.case16_out
		del self.case17_in
		del self.case17_out
		del self.case18_in
		del self.case18_out
		del self.case19_in
		del self.case19_out
		del self.case20_in
		del self.case20_out
		del self.case21_in
		del self.case21_out
		del self.case22_in
		del self.case22_out
		del self.case23_in
		del self.case23_out
		del self.case24_in
		del self.case24_out
		del self.case25_in
		del self.case25_out
		del self.case26_in
		del self.case26_out
		del self.case27_in
		del self.case27_out
		del self.case28_in
		del self.case28_out
		del self.case29_in
		del self.case29_out
		del self.case30_in
		del self.case30_out
		del self.case31_in
		del self.case31_out
		del self.case32_in
		del self.case32_out
		del self.case33_in
		del self.case33_out
		del self.case34_in
		del self.case34_out
		del self.case35_in
		del self.case35_out
		del self.case36_in
		del self.case36_out
		del self.case37_in
		del self.case37_out
		del self.case38_in
		del self.case38_out
		del self.case39_in
		del self.case39_out
		del self.case40_in
		del self.case40_out
		del self.case41_in
		del self.case41_out
		del self.case42_in
		del self.case42_out
		del self.case43_in
		del self.case43_out
		del self.case44_in
		del self.case44_out
		del self.case45_in
		del self.case45_out
		del self.case46_in
		del self.case46_out
		del self.case47_in
		del self.case47_out
		del self.case48_in
		del self.case48_out
		del self.case49_in
		del self.case49_out
		del self.case50_in
		del self.case50_out
		del self.case51_in
		del self.case51_out
		del self.case52_in
		del self.case52_out
		del self.case53_in
		del self.case53_out
		del self.case54_in
		del self.case54_out
		del self.case55_in
		del self.case55_out
		del self.case56_in
		del self.case56_out
		del self.case57_in
		del self.case57_out
		del self.case58_in
		del self.case58_out
		del self.case59_in
		del self.case59_out
		del self.case60_in
		del self.case60_out
		del self.case61_in
		del self.case61_out
		del self.case62_in
		del self.case62_out
		del self.case63_in
		del self.case63_out
		del self.case64_in
		del self.case64_out
		del self.case65_in
		del self.case65_out
		del self.m1_in
		del self.m1_out
		del self.m2_in
		del self.m2_out
		del self.m3_in
		del self.m3_out
		del self.m4_in
		del self.m4_out
		del self.m5_in
		del self.m5_out
		del self.m6_in
		del self.m6_out
		del self.m7_in
		del self.m7_out
		del self.m8_in
		del self.m8_out
		del self.m9_in
		del self.m9_out
		del self.m10_in
		del self.m10_out
		del self.m11_in
		del self.m11_out
		del self.m12_in
		del self.m12_out
		del self.m13_in
		del self.m13_out
		del self.m14_in
		del self.m14_out
		del self.m15_in
		del self.m15_out
		del self.m16_in
		del self.m16_out
		del self.m17_in
		del self.m17_out
		del self.m18_in
		del self.m18_out
		del self.m19_in
		del self.m19_out
		del self.m20_in
		del self.m20_out
		del self.m21_in
		del self.m21_out
		del self.m22_in
		del self.m22_out
		del self.m23_in
		del self.m23_out
		del self.m24_in
		del self.m24_out
		del self.m25_in
		del self.m25_out
		del self.m26_in
		del self.m26_out
		del self.m27_in
		del self.m27_out
		del self.m28_in
		del self.m28_out
		del self.m29_in
		del self.m29_out
		del self.m30_in
		del self.m30_out
		del self.m31_in
		del self.m31_out
		del self.m32_in
		del self.m32_out
		del self.m33_in
		del self.m33_out
		del self.m34_in
		del self.m34_out
		del self.m35_in
		del self.m35_out
		del self.m36_in
		del self.m36_out
	def test_case1(self):
		self.assertEqual(xstep.test_xstep(self.case1_in), self.case1_out)

	def test_case2(self):
		self.assertEqual(xstep.test_xstep(self.case2_in), self.case2_out)

	def test_case3(self):
		self.assertEqual(xstep.test_xstep(self.case3_in), self.case3_out)

	def test_case4(self):
		self.assertEqual(xstep.test_xstep(self.case4_in), self.case4_out)

	def test_case5(self):
		self.assertEqual(xstep.test_xstep(self.case5_in), self.case5_out)

	def test_case6(self):
		self.assertEqual(xstep.test_xstep(self.case6_in), self.case6_out)

	def test_case7(self):
		self.assertEqual(xstep.test_xstep(self.case7_in), self.case7_out)

	def test_case8(self):
		self.assertEqual(xstep.test_xstep(self.case8_in), self.case8_out)

	def test_case9(self):
		self.assertEqual(xstep.test_xstep(self.case9_in), self.case9_out)

	def test_case10(self):
		self.assertEqual(xstep.test_xstep(self.case10_in), self.case10_out)

	def test_case11(self):
		self.assertEqual(xstep.test_xstep(self.case11_in), self.case11_out)

	def test_case12(self):
		self.assertEqual(xstep.test_xstep(self.case12_in), self.case12_out)

	def test_case13(self):
		self.assertEqual(xstep.test_xstep(self.case13_in), self.case13_out)

	def test_case14(self):
		self.assertEqual(xstep.test_xstep(self.case14_in), self.case14_out)

	def test_case15(self):
		self.assertEqual(xstep.test_xstep(self.case15_in), self.case15_out)

	def test_case16(self):
		self.assertEqual(xstep.test_xstep(self.case16_in), self.case16_out)

	def test_case17(self):
		self.assertEqual(xstep.test_xstep(self.case17_in), self.case17_out)

	def test_case18(self):
		self.assertEqual(xstep.test_xstep(self.case18_in), self.case18_out)

	def test_case19(self):
		self.assertEqual(xstep.test_xstep(self.case19_in), self.case19_out)

	def test_case20(self):
		self.assertEqual(xstep.test_xstep(self.case20_in), self.case20_out)

	def test_case21(self):
		self.assertEqual(xstep.test_xstep(self.case21_in), self.case21_out)

	def test_case22(self):
		self.assertEqual(xstep.test_xstep(self.case22_in), self.case22_out)

	def test_case23(self):
		self.assertEqual(xstep.test_xstep(self.case23_in), self.case23_out)

	def test_case24(self):
		self.assertEqual(xstep.test_xstep(self.case24_in), self.case24_out)

	def test_case25(self):
		self.assertEqual(xstep.test_xstep(self.case25_in), self.case25_out)

	def test_case26(self):
		self.assertEqual(xstep.test_xstep(self.case26_in), self.case26_out)

	def test_case27(self):
		self.assertEqual(xstep.test_xstep(self.case27_in), self.case27_out)

	def test_case28(self):
		self.assertEqual(xstep.test_xstep(self.case28_in), self.case28_out)

	def test_case29(self):
		self.assertEqual(xstep.test_xstep(self.case29_in), self.case29_out)

	def test_case30(self):
		self.assertEqual(xstep.test_xstep(self.case30_in), self.case30_out)

	def test_case31(self):
		self.assertEqual(xstep.test_xstep(self.case31_in), self.case31_out)

	def test_case32(self):
		self.assertEqual(xstep.test_xstep(self.case32_in), self.case32_out)

	def test_case34(self):
		self.assertEqual(xstep.test_xstep(self.case34_in), self.case34_out)

	def test_case35(self):
		self.assertEqual(xstep.test_xstep(self.case35_in), self.case35_out)

	def test_case36(self):
		self.assertEqual(xstep.test_xstep(self.case36_in), self.case36_out)

	def test_case37(self):
		self.assertEqual(xstep.test_xstep(self.case37_in), self.case37_out)

	def test_case38(self):
		self.assertEqual(xstep.test_xstep(self.case38_in), self.case38_out)

	def test_case39(self):
		self.assertEqual(xstep.test_xstep(self.case39_in), self.case39_out)

	def test_case40(self):
		self.assertEqual(xstep.test_xstep(self.case40_in), self.case40_out)

	def test_case41(self):
		self.assertEqual(xstep.test_xstep(self.case41_in), self.case41_out)

	def test_case42(self):
		self.assertEqual(xstep.test_xstep(self.case42_in), self.case42_out)

	def test_case43(self):
		self.assertEqual(xstep.test_xstep(self.case43_in), self.case43_out)

	def test_case44(self):
		self.assertEqual(xstep.test_xstep(self.case44_in), self.case44_out)

	def test_case45(self):
		self.assertEqual(xstep.test_xstep(self.case45_in), self.case45_out)

	def test_case46(self):
		self.assertEqual(xstep.test_xstep(self.case46_in), self.case46_out)

	def test_case47(self):
		self.assertEqual(xstep.test_xstep(self.case47_in), self.case47_out)

	def test_case48(self):
		self.assertEqual(xstep.test_xstep(self.case48_in), self.case48_out)

	def test_case49(self):
		self.assertEqual(xstep.test_xstep(self.case49_in), self.case49_out)

	def test_case50(self):
		self.assertEqual(xstep.test_xstep(self.case50_in), self.case50_out)

	def test_case51(self):
		self.assertEqual(xstep.test_xstep(self.case51_in), self.case51_out)

	def test_case52(self):
		self.assertEqual(xstep.test_xstep(self.case52_in), self.case52_out)

	def test_case53(self):
		self.assertEqual(xstep.test_xstep(self.case53_in), self.case53_out)

	def test_case54(self):
		self.assertEqual(xstep.test_xstep(self.case54_in), self.case54_out)

	def test_case55(self):
		self.assertEqual(xstep.test_xstep(self.case55_in), self.case55_out)

	def test_case56(self):
		self.assertEqual(xstep.test_xstep(self.case56_in), self.case56_out)

	def test_case57(self):
		self.assertEqual(xstep.test_xstep(self.case57_in), self.case57_out)

	def test_case58(self):
		self.assertEqual(xstep.test_xstep(self.case58_in), self.case58_out)

	def test_case59(self):
		self.assertEqual(xstep.test_xstep(self.case59_in), self.case59_out)

	def test_case60(self):
		self.assertEqual(xstep.test_xstep(self.case60_in), self.case60_out)

	def test_case61(self):
		self.assertEqual(xstep.test_xstep(self.case61_in), self.case61_out)

	def test_case62(self):
		self.assertEqual(xstep.test_xstep(self.case62_in), self.case62_out)

	def test_case63(self):
		self.assertEqual(xstep.test_xstep(self.case63_in), self.case63_out)

	def test_case64(self):
		self.assertEqual(xstep.test_xstep(self.case64_in), self.case64_out)

	def test_case65(self):
		self.assertEqual(xstep.test_xstep(self.case65_in), self.case65_out)

	def test_m1(self):
		self.assertEqual(xstep.test_xstep(self.m1_in), self.m1_out)

	def test_m2(self):
		self.assertEqual(xstep.test_xstep(self.m2_in), self.m2_out)

	def test_m3(self):
		self.assertEqual(xstep.test_xstep(self.m3_in), self.m3_out)

	def test_m4(self):
		self.assertEqual(xstep.test_xstep(self.m4_in), self.m4_out)

	def test_m5(self):
		self.assertEqual(xstep.test_xstep(self.m5_in), self.m5_out)

	def test_m6(self):
		self.assertEqual(xstep.test_xstep(self.m6_in), self.m6_out)

	def test_m7(self):
		self.assertEqual(xstep.test_xstep(self.m7_in), self.m7_out)

	def test_m8(self):
		self.assertEqual(xstep.test_xstep(self.m8_in), self.m8_out)

	def test_m9(self):
		self.assertEqual(xstep.test_xstep(self.m9_in), self.m9_out)

	def test_m10(self):
		self.assertEqual(xstep.test_xstep(self.m10_in), self.m10_out)

	def test_m11(self):
		self.assertEqual(xstep.test_xstep(self.m11_in), self.m11_out)

	def test_m12(self):
		self.assertEqual(xstep.test_xstep(self.m12_in), self.m12_out)

	def test_m13(self):
		self.assertEqual(xstep.test_xstep(self.m13_in), self.m13_out)

	def test_m14(self):
		self.assertEqual(xstep.test_xstep(self.m14_in), self.m14_out)

	def test_m15(self):
		self.assertEqual(xstep.test_xstep(self.m15_in), self.m15_out)

	def test_m16(self):
		self.assertEqual(xstep.test_xstep(self.m16_in), self.m16_out)

	def test_m17(self):
		self.assertEqual(xstep.test_xstep(self.m17_in), self.m17_out)

	def test_m18(self):
		self.assertEqual(xstep.test_xstep(self.m18_in), self.m18_out)

	def test_m19(self):
		self.assertEqual(xstep.test_xstep(self.m19_in), self.m19_out)

	def test_m20(self):
		self.assertEqual(xstep.test_xstep(self.m20_in), self.m20_out)

	def test_m21(self):
		self.assertEqual(xstep.test_xstep(self.m21_in), self.m21_out)

	def test_m22(self):
		self.assertEqual(xstep.test_xstep(self.m22_in), self.m22_out)

	def test_m23(self):
		self.assertEqual(xstep.test_xstep(self.m23_in), self.m23_out)

	def test_m24(self):
		self.assertEqual(xstep.test_xstep(self.m24_in), self.m24_out)

	def test_m25(self):
		self.assertEqual(xstep.test_xstep(self.m25_in), self.m25_out)

	def test_m26(self):
		self.assertEqual(xstep.test_xstep(self.m26_in), self.m26_out)

	def test_m27(self):
		self.assertEqual(xstep.test_xstep(self.m27_in), self.m27_out)

	def test_m28(self):
		self.assertEqual(xstep.test_xstep(self.m28_in), self.m28_out)

	def test_m29(self):
		self.assertEqual(xstep.test_xstep(self.m29_in), self.m29_out)

	def test_m30(self):
		self.assertEqual(xstep.test_xstep(self.m30_in), self.m30_out)

	def test_m31(self):
		self.assertEqual(xstep.test_xstep(self.m31_in), self.m31_out)

	def test_m32(self):
		self.assertEqual(xstep.test_xstep(self.m32_in), self.m32_out)

	def test_m33(self):
		self.assertEqual(xstep.test_xstep(self.m33_in), self.m33_out)

	def test_m34(self):
		self.assertEqual(xstep.test_xstep(self.m34_in), self.m34_out)

	def test_m35(self):
		self.assertEqual(xstep.test_xstep(self.m35_in), self.m35_out)

	def test_m36(self):
		self.assertEqual(xstep.test_xstep(self.m36_in), self.m36_out)



if __name__ == '__main__':
	unittest.main()
