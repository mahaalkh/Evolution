# Automated unit tests for the step test harness for Evolution game
import unittest
import os, sys
import json
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../executables'))
import xstep

class TestXStepTests(unittest.TestCase):
  def setUp(self):
    self.case1_in = [[[["id", 1],
                   ["species", [[["food", 1],
                         ["body", 2],
                         ["population", 1],
                         ["traits", ["fat-tissue"]],
                         ["fat-food", 1]],
                         [["food", 1],
                          ["body", 2],
                          ["population", 5],
                          ["traits", ["fat-tissue"]],
                          ["fat-food", 2]]]],
                   ["bag", 7]],
                   [["id", 0],
                   ["species", [[["food", 1],
                         ["body", 2],
                         ["population", 1],
                         ["traits", []]],
                        [["food", 3],
                         ["body", 7],
                         ["population", 3],
                         ["traits", ["carnivore"]]]]],
                   ["bag", 10]]],
                    11,
                    [[1, "carnivore"], [2, "pack-hunting"], [3, "scavenger"], [4, "long-neck"]]]
    self.case1_out = json.dumps([[[["id", 1],
                       ["species", [[["food", 1],
                             ["body", 2],
                             ["population", 1],
                             ["traits", ["fat-tissue"]],
                             ["fat-food", 2]],
                             [["food", 1],
                              ["body", 2],
                              ["population", 5],
                              ["traits", ["fat-tissue"]],
                              ["fat-food", 2]]]],
                       ["bag", 7]],
                       [["id", 0],
                       ["species", [[["food", 1],
                             ["body", 2],
                             ["population", 1],
                             ["traits", []]],
                            [["food", 3],
                             ["body", 7],
                             ["population", 3],
                             ["traits", ["carnivore"]]]]],
                       ["bag", 10]]],
                        10,
                        [[1, "carnivore"], [2, "pack-hunting"], [3, "scavenger"], [4, "long-neck"]]])

    self.case2_in = [[[["id", 0],
                       ["species", [[["food", 1],
                             ["body", 2],
                             ["population", 1],
                             ["traits", ["fat-tissue"]],
                             ["fat-food", 2]],
                            [["food", 3],
                             ["body", 7],
                             ["population", 6],
                             ["traits", ["carnivore"]]]]],
                       ["bag", 10]],
                       [["id", 1],
                       ["species", [[["food", 1],
                             ["body", 2],
                             ["population", 1],
                             ["traits", ["fat-tissue", "warning-call"]],
                             ["fat-food", 1]],
                             [["food", 1],
                              ["body", 2],
                              ["population", 5],
                              ["traits", ["fat-tissue"]],
                              ["fat-food", 2]],
                             [["food", 1],
                              ["body", 2],
                              ["population", 5],
                              ["traits", ["fat-tissue", "horns"]],
                              ["fat-food", 2]]]],
                       ["bag", 7]]],
                        11,
                        [[1, "carnivore"], [2, "pack-hunting"], [3, "scavenger"], [4, "long-neck"]]]
    self.case2_out = json.dumps([[[["id", 0],
                         ["species", [[["food", 1],
                               ["body", 2],
                               ["population", 1],
                               ["traits", ["fat-tissue"]],
                               ["fat-food", 2]],
                              [["food", 4],
                               ["body", 7],
                               ["population", 5],
                               ["traits", ["carnivore"]]]]],
                         ["bag", 10]],
                         [["id", 1],
                         ["species", [[["food", 1],
                               ["body", 2],
                               ["population", 1],
                               ["traits", ["fat-tissue", "warning-call"]],
                               ["fat-food", 1]],
                               [["food", 1],
                                ["body", 2],
                                ["population", 5],
                                ["traits", ["fat-tissue"]],
                                ["fat-food", 2]],
                               [["food", 1],
                                ["body", 2],
                                ["population", 4],
                                ["traits", ["fat-tissue", "horns"]],
                                ["fat-food", 2]]]],
                         ["bag", 7]]],
                          10,
                          [[1, "carnivore"], [2, "pack-hunting"], [3, "scavenger"], [4, "long-neck"]]])

    self.case3_in = [[ [["id", 2],
                     ["species", [[["food", 1],
                            ["body", 2],
                            ["population", 5],
                            ["traits", ["scavenger", "cooperation", "climbing"]]],
                           [["food", 1],
                             ["body", 2],
                             ["population", 5],
                             ["traits", ["climbing"]]]]],
                     ["bag", 7]],
                     [["id", 1],
                     ["species", [[["food", 1],
                           ["body", 2],
                           ["population", 1],
                           ["traits", ["fat-tissue", "warning-call", "climbing"]],
                           ["fat-food", 2]],
                           [["food", 5],
                            ["body", 2],
                            ["population", 5],
                            ["traits", ["fat-tissue"]],
                            ["fat-food", 2]],
                           [["food", 5],
                            ["body", 2],
                            ["population", 5],
                            ["traits", ["fat-tissue", "horns"]],
                            ["fat-food", 2]]]],
                     ["bag", 7]],
                  [["id", 0],
                     ["species", [[["food", 1],
                           ["body", 2],
                           ["population", 1],
                           ["traits", ["fat-tissue"]],
                           ["fat-food", 2]],
                          [["food", 0],
                           ["body", 7],
                           ["population", 1],
                           ["traits", ["carnivore"]]]]],
                     ["bag", 10]]],
                      11,
                      [[1, "carnivore"], [2, "pack-hunting"], [3, "scavenger"], [4, "long-neck"]]]
    self.case3_out = json.dumps([[ [["id", 2],
                     ["species", [[["food", 2],
                            ["body", 2],
                            ["population", 5],
                            ["traits", ["scavenger", "cooperation", "climbing"]]],
                           [["food", 2],
                             ["body", 2],
                             ["population", 5],
                             ["traits", ["climbing"]]]]],
                     ["bag", 7]],
                     [["id", 1],
                     ["species", [[["food", 1],
                           ["body", 2],
                           ["population", 1],
                           ["traits", ["fat-tissue", "warning-call", "climbing"]],
                           ["fat-food", 2]],
                           [["food", 5],
                            ["body", 2],
                            ["population", 5],
                            ["traits", ["fat-tissue"]],
                            ["fat-food", 2]],
                           [["food", 5],
                            ["body", 2],
                            ["population", 5],
                            ["traits", ["fat-tissue", "horns"]],
                            ["fat-food", 2]]]],
                     ["bag", 7]],
                  [["id", 0],
                     ["species", [[["food", 1],
                           ["body", 2],
                           ["population", 1],
                           ["traits", ["fat-tissue"]],
                           ["fat-food", 2]],
                          [["food", 0],
                           ["body", 7],
                           ["population", 1],
                           ["traits", ["carnivore"]]]]],
                     ["bag", 10]]],
                      9,
                      [[1, "carnivore"], [2, "pack-hunting"], [3, "scavenger"], [4, "long-neck"]]])

    self.case4_in = [[[["id", 0],
                       ["species", [[["food", 1],
                             ["body", 2],
                             ["population", 1],
                             ["traits", []]],
                            [["food", 1],
                             ["body", 7],
                             ["population", 3],
                             ["traits", ["foraging"]]]]],
                       ["bag", 10]],
                       [["id", 1],
                       ["species", [[["food", 1],
                             ["body", 2],
                             ["population", 1],
                             ["traits", ["fat-tissue"]],
                             ["fat-food", 1]],
                             [["food", 1],
                              ["body", 2],
                              ["population", 5],
                              ["traits", ["fat-tissue"]],
                              ["fat-food", 2]]]],
                       ["bag", 7]]],
                        11,
                        [[1, "carnivore"], [2, "pack-hunting"], [3, "scavenger"], [4, "long-neck"]]]
    self.case4_out = json.dumps([[[["id", 0],
                       ["species", [[["food", 1],
                             ["body", 2],
                             ["population", 1],
                             ["traits", []]],
                            [["food", 3],
                             ["body", 7],
                             ["population", 3],
                             ["traits", ["foraging"]]]]],
                       ["bag", 10]],
                        [["id", 1],
                       ["species", [[["food", 1],
                             ["body", 2],
                             ["population", 1],
                             ["traits", ["fat-tissue"]],
                             ["fat-food", 1]],
                             [["food", 1],
                              ["body", 2],
                              ["population", 5],
                              ["traits", ["fat-tissue"]],
                              ["fat-food", 2]]]],
                       ["bag", 7]]],
                        9,
                        [[1, "carnivore"], [2, "pack-hunting"], [3, "scavenger"], [4, "long-neck"]]])

    self.case5_in = [[[["id", 0],
                       ["species", [[["food", 1],
                             ["body", 2],
                             ["population", 1],
                             ["traits", []]],
                            [["food", 3],
                             ["body", 7],
                             ["population", 3],
                             ["traits", ["foraging"]]]]],
                       ["bag", 10]],
                        [["id", 1],
                       ["species", [[["food", 1],
                             ["body", 2],
                             ["population", 1],
                             ["traits", ["fat-tissue"]],
                             ["fat-food", 1]],
                             [["food", 5],
                              ["body", 2],
                              ["population", 5],
                              ["traits", ["fat-tissue"]],
                              ["fat-food", 2]]]],
                       ["bag", 7]]],
                        9,
                        [[1, "carnivore"], [2, "pack-hunting"], [3, "scavenger"], [4, "long-neck"]]]
    self.case5_out = json.dumps([[[["id", 0],
                       ["species", [[["food", 1],
                             ["body", 2],
                             ["population", 1],
                             ["traits", []]],
                            [["food", 3],
                             ["body", 7],
                             ["population", 3],
                             ["traits", ["foraging"]]]]],
                       ["bag", 10]],
                        [["id", 1],
                       ["species", [[["food", 1],
                             ["body", 2],
                             ["population", 1],
                             ["traits", ["fat-tissue"]],
                             ["fat-food", 1]],
                             [["food", 5],
                              ["body", 2],
                              ["population", 5],
                              ["traits", ["fat-tissue"]],
                              ["fat-food", 2]]]],
                       ["bag", 7]]],
                        9,
                        [[1, "carnivore"], [2, "pack-hunting"], [3, "scavenger"], [4, "long-neck"]]])

    self.caseFailed_in = [[[["id",111],
                             ["species",
                              [[["food",0],
                                ["body",0],
                                ["population",5],
                                ["traits",["foraging"]]]]],
                             ["bag",0],
                             ["cards",[]]],
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
                              ["bag",0],
                              ["cards",[]]],
                            [["id",66],
                              ["species",
                              [[["food",1],
                                ["body",3],
                                ["population",1],
                                ["traits",[]]]]],
                              ["bag",0],
                              ["cards",[]]]],
                            1,
                            []]
    self.caseFailed_out = json.dumps([[[["id",111],
                                       ["species",
                                        [[["food",1],
                                          ["body",0],
                                          ["population",5],
                                          ["traits",["foraging"]]]]],
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
                                      0,
                                      []])

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

  def test_caseFailed(self):
    self.assertEqual(xstep.test_xstep(self.caseFailed_in), self.caseFailed_out)
if __name__ == '__main__':
  unittest.main()
