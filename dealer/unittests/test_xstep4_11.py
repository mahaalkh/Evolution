# Automated unit tests for the step test harness for Evolution game
import unittest
import os, sys
import json
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../executables/'))
import xstep4_testing

class TestXStep4Tests11(unittest.TestCase):
  def setUp(self):
    self.case1_in = [
                      [
                        [
                          [["id", 1],
                            ["species", []],
                            ["bag", 0],
                            ["cards",[[3, "carnivore"]]]],
                          [["id", 1],
                            ["species", []],
                            ["bag", 0],
                            ["cards", [[1, "herding"]]]],
                          [["id", 1],
                            ["species", []],
                            ["bag", 0],
                            ["cards", [[2, "long-neck"]]]]
                        ],
                        9,
                        []
                      ],
                      [
                        [0, [],[],[],[]],
                        [0, [],[],[],[]],
                        [0, [],[],[],[]]
                      ]
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
                                  15,
                                  []
                                ])
    self.case2_in = [
                      [
                        [
                          [["id", 1],
                            ["species", []],
                            ["bag", 0],
                            ["cards",[[3, "carnivore"], [3, "herding"], [-1, "ambush"], [1, "long-neck"]]]],
                          [["id", 1],
                            ["species", []],
                            ["bag", 0],
                            ["cards", [[1, "herding"]]]],
                          [["id", 1],
                            ["species", []],
                            ["bag", 0],
                            ["cards", [[2, "long-neck"]]]]
                        ],
                        0,
                        []
                      ],
                      [
                        [3, [],[],[[1,0,2]],[]],
                        [0, [],[],[],[]],
                        [0, [],[],[],[]]
                      ]
                    ]
    self.case2_out = json.dumps([
                                  [
                                    [["id", 1],
                                      ["species", [
                                        [["food", 0],
                                         ["body", 0],
                                         ["population", 1],
                                         ["traits", ["carnivore", "ambush"]]]
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
                                ]
                                )
    self.case3_in = [
                      [
                        [
                          [["id", 1],
                            ["species", [
                              [["food", 0],
                                ["body", 1],
                                ["population",3 ],
                                ["traits", ["long-neck", "climbing"]]]
                            ]],
                            ["bag", 0],
                            ["cards",[[3, "carnivore"], [4, "carnivore"], [-1, "herding"], [3, "symbiosis"]]]],
                          [["id", 1],
                            ["species", [
                              [["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits", ["cooperation"]]]
                            ]],
                            ["bag", 0],
                            ["cards", [[1, "herding"], [-2, "hard-shell"], [0, "scavenger"], [1, "foraging"], [2, "burrowing"]]]],
                          [["id", 1],
                            ["species", [
                              [["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits", ["symbiosis", "herding", "burrowing"]]
                              ]]],
                            ["bag", 0],
                            ["cards", [[2, "long-neck"], [1, "climbing"], [1, "burrowing"], [0, "carnivore"], [6, "carnivore"]]]]
                        ],
                        0,
                        [[2, "herding"], [0, "herding"], [3, "herding"], [-6, "carnivore"], [-2, "symbiosis"]]
                      ],
                      [
                        [0, [],[],[[3,1,2]],[]],
                        [0, [],[],[[1,2,3,4]],[]],
                        [0, [],[],[[3,2,4]],[[0,0,1]]]
                      ]
                    ]
    self.case3_out = json.dumps([
                                  [
                                    [["id", 1],
                                      ["species", [
                                        [["food", 3],
                                          ["body", 1],
                                          ["population",3 ],
                                          ["traits", ["long-neck", "climbing"]]],
                                        [["food", 0],
                                          ["body", 0],
                                          ["population", 1],
                                          ["traits", ["carnivore", "herding"]]]
                                      ]],
                                      ["bag", 0]],
                                    [["id", 1],
                                      ["species", [
                                        [["food", 1],
                                          ["body", 0],
                                          ["population", 1],
                                          ["traits", ["cooperation"]]],
                                        [["food", 1],
                                          ["body", 0],
                                          ["population", 1],
                                          ["traits", ["scavenger", "foraging", "burrowing"]]]
                                      ]],
                                      ["bag", 0]],
                                    [["id", 1],
                                      ["species", [
                                        [["food", 1],
                                          ["body", 0],
                                          ["population", 1],
                                          ["traits", ["climbing", "herding", "burrowing"]]],
                                        [["food", 0],
                                          ["body", 0],
                                          ["population", 1],
                                          ["traits", ["burrowing", "carnivore"]]]
                                      ]],
                                      ["bag", 0]]
                                  ],
                                  0,
                                  [[2, "herding"], [0, "herding"], [3, "herding"], [-6, "carnivore"], [-2, "symbiosis"]]
                                ])
    self.case4_in = [
                      [
                        [
                          [["id", 1],
                            ["species", [
                              [["food", 0],
                                ["body", 1],
                                ["population",3 ],
                                ["traits", ["long-neck", "climbing"]]]
                            ]],
                            ["bag", 0],
                            ["cards",[[3, "carnivore"], [4, "carnivore"], [-1, "herding"], [3, "symbiosis"], [1, "cooperation"]]]],
                          [["id", 1],
                            ["species", [
                              [["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits", ["cooperation"]]]
                            ]],
                            ["bag", 0],
                            ["cards", [[1, "herding"], [-2, "hard-shell"], [0, "scavenger"], [1, "foraging"], [2, "burrowing"]]]],
                          [["id", 1],
                            ["species", [
                              [["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits", ["symbiosis", "herding", "burrowing"]]
                              ]]],
                            ["bag", 0],
                            ["cards", [[2, "long-neck"], [1, "climbing"], [1, "burrowing"], [0, "carnivore"], [6, "carnivore"]]]]
                        ],
                        0,
                        [[2, "herding"], [0, "herding"], [3, "herding"], [-6, "carnivore"], [-2, "symbiosis"]]
                      ],
                      [
                        [0, [["population",1,4]],[],[[3,1,2]],[]],
                        [0, [],[],[[1,2,3,4]],[]],
                        [0, [],[],[[3,2,4]],[[0,0,1]]]
                      ]
                    ]
    self.case4_out = json.dumps([
                                  [
                                    [["id", 1],
                                      ["species", [
                                        [["food", 3],
                                          ["body", 1],
                                          ["population",3 ],
                                          ["traits", ["long-neck", "climbing"]]],
                                        [["food", 0],
                                          ["body", 0],
                                          ["population", 2],
                                          ["traits", ["carnivore", "herding"]]]
                                      ]],
                                      ["bag", 0]],
                                    [["id", 1],
                                      ["species", [
                                        [["food", 1],
                                          ["body", 0],
                                          ["population", 1],
                                          ["traits", ["cooperation"]]],
                                        [["food", 1],
                                          ["body", 0],
                                          ["population", 1],
                                          ["traits", ["scavenger", "foraging", "burrowing"]]]
                                      ]],
                                      ["bag", 0]],
                                    [["id", 1],
                                      ["species", [
                                        [["food", 1],
                                          ["body", 0],
                                          ["population", 1],
                                          ["traits", ["climbing", "herding", "burrowing"]]],
                                        [["food", 0],
                                          ["body", 0],
                                          ["population", 1],
                                          ["traits", ["burrowing", "carnivore"]]]
                                      ]],
                                      ["bag", 0]]
                                  ],
                                  0,
                                  [[2, "herding"], [0, "herding"], [3, "herding"], [-6, "carnivore"], [-2, "symbiosis"]]
                                ]
                                )
    self.case5_in = [
                      [
                        [
                          [["id", 1],
                            ["species", [
                              [["food", 0],
                                ["body", 1],
                                ["population",3 ],
                                ["traits", ["long-neck", "climbing"]]]
                            ]],
                            ["bag", 0],
                            ["cards",[[3, "carnivore"], [4, "carnivore"], [-1, "herding"], [3, "symbiosis"], [1, "cooperation"]]]],
                          [["id", 1],
                            ["species", [
                              [["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits", ["cooperation"]]]
                            ]],
                            ["bag", 0],
                            ["cards", [[1, "herding"], [-2, "hard-shell"], [0, "scavenger"], [1, "foraging"], [2, "burrowing"]]]],
                          [["id", 1],
                            ["species", [
                              [["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits", ["symbiosis", "herding", "burrowing"]]
                              ]]],
                            ["bag", 0],
                            ["cards", [[2, "long-neck"], [1, "climbing"], [1, "burrowing"], [0, "carnivore"], [6, "carnivore"]]]]
                        ],
                        0,
                        [[2, "herding"], [0, "herding"], [3, "herding"], [-6, "carnivore"], [-2, "symbiosis"]]
                      ],
                      [
                        [4, [],[],[[0, 1]],[[1, 0, 2], [1, 0, 3]]],
                        [0, [],[],[[1,2,3,4]],[]],
                        [0, [],[],[[3,2,4]],[[0,0,1]]]
                      ]
                    ]
    self.case5_out = json.dumps([
                                  [
                                    [
                                      [
                                        "id",
                                        1
                                      ],
                                      [
                                        "species",
                                        [
                                          [
                                            [
                                              "food",
                                              2
                                            ],
                                            [
                                              "body",
                                              1
                                            ],
                                            [
                                              "population",
                                              3
                                            ],
                                            [
                                              "traits",
                                              [
                                                "long-neck",
                                                "climbing"
                                              ]
                                            ]
                                          ],
                                          [
                                            [
                                              "food",
                                              0
                                            ],
                                            [
                                              "body",
                                              0
                                            ],
                                            [
                                              "population",
                                              1
                                            ],
                                            [
                                              "traits",
                                              [
                                                "symbiosis"
                                              ]
                                            ]
                                          ]
                                        ]
                                      ],
                                      [
                                        "bag",
                                        0
                                      ]
                                    ],
                                    [
                                      [
                                        "id",
                                        1
                                      ],
                                      [
                                        "species",
                                        [
                                          [
                                            [
                                              "food",
                                              1
                                            ],
                                            [
                                              "body",
                                              0
                                            ],
                                            [
                                              "population",
                                              1
                                            ],
                                            [
                                              "traits",
                                              [
                                                "cooperation"
                                              ]
                                            ]
                                          ],
                                          [
                                            [
                                              "food",
                                              1
                                            ],
                                            [
                                              "body",
                                              0
                                            ],
                                            [
                                              "population",
                                              1
                                            ],
                                            [
                                              "traits",
                                              [
                                                "scavenger",
                                                "foraging",
                                                "burrowing"
                                              ]
                                            ]
                                          ]
                                        ]
                                      ],
                                      [
                                        "bag",
                                        0
                                      ]
                                    ],
                                    [
                                      [
                                        "id",
                                        1
                                      ],
                                      [
                                        "species",
                                        [
                                          [
                                            [
                                              "food",
                                              0
                                            ],
                                            [
                                              "body",
                                              0
                                            ],
                                            [
                                              "population",
                                              1
                                            ],
                                            [
                                              "traits",
                                              [
                                                "climbing",
                                                "herding",
                                                "burrowing"
                                              ]
                                            ]
                                          ],
                                          [
                                            [
                                              "food",
                                              0
                                            ],
                                            [
                                              "body",
                                              0
                                            ],
                                            [
                                              "population",
                                              1
                                            ],
                                            [
                                              "traits",
                                              [
                                                "burrowing",
                                                "carnivore"
                                              ]
                                            ]
                                          ]
                                        ]
                                      ],
                                      [
                                        "bag",
                                        0
                                      ]
                                    ]
                                  ],
                                  0,
                                  [
                                    [
                                      2,
                                      "herding"
                                    ],
                                    [
                                      0,
                                      "herding"
                                    ],
                                    [
                                      3,
                                      "herding"
                                    ],
                                    [
                                      -6,
                                      "carnivore"
                                    ],
                                    [
                                      -2,
                                      "symbiosis"
                                    ]
                                  ]
                                ])
    self.case6_in = [
                        [
                            [
                                [["id", 1], ["species", [[["food", 1], ["body", 1], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 3], ["cards", [[2, "horns"]]]],
                                [["id", 2], ["species", [[["food", 1], ["body", 1], ["population", 2], ["traits", ["horns"]]]]], ["bag", 5], ["cards", [[1, "horns"]]]],
                                [["id", 3], ["species", []], ["bag", 8], ["cards", [[-1, "horns"]]]]
                            ],
                            10,
                            [[3, "carnivore"]]
                        ],
                        [
                            [0, [], [], [], []],
                            [0, [], [], [], []],
                            [0, [], [], [], []]
                        ]
                    ]
    self.case6_out = json.dumps([
                                    [
                                        [["id", 1], ["species", [[["food", 2], ["body", 1], ["population", 2], ["traits", ["carnivore"]]]]], ["bag", 3]],
                                        [["id", 2], ["species", [[["food", 1], ["body", 1], ["population", 1], ["traits", ["horns"]]]]], ["bag", 5]],
                                        [["id", 3], ["species", []], ["bag", 8]]
                                    ],
                                    11,
                                    [[3, "carnivore"]]
                                ])
    self.case7_in = [
                        [
                            [
                                [["id", 1], ["species", [[["food", 1], ["body", 1], ["population", 3], ["traits", ["foraging"]]]]], ["bag", 3], ["cards", [[-2, "carnivore"]]]],
                                [["id", 2], ["species", [[["food", 1], ["body", 1], ["population", 3], ["traits", ["foraging", "long-neck"]]]]], ["bag", 5], ["cards", [[3, "carnivore"]]]],
                                [["id", 3], ["species", []], ["bag", 8], ["cards", [[5, "carnivore"]]]]
                            ],
                            10,
                            [[3, "carnivore"]]
                        ],
                        [
                            [0, [], [], [], []],
                            [0, [], [], [], []],
                            [0, [], [], [], []]
                        ]
                    ]
    self.case7_out = json.dumps([
                                    [
                                        [["id", 1], ["species", [[["food", 3], ["body", 1], ["population", 3], ["traits", ["foraging"]]]]], ["bag", 3]],
                                        [["id", 2], ["species", [[["food", 3], ["body", 1], ["population", 3], ["traits", ["foraging", "long-neck"]]]]], ["bag", 5]],
                                        [["id", 3], ["species", []], ["bag", 8]]
                                    ],
                                    12,
                                    [[3, "carnivore"]]
                                ])
    self.case8_in = [
                        [
                            [
                                [["id", 1], ["species", [[["food", 1], ["body", 1], ["population", 3], ["traits", ["foraging"]]]]], ["bag", 3], ["cards", [[-2, "carnivore"], [4, "carnivore"]]]],
                                [["id", 2], ["species", [[["food", 1], ["body", 1], ["population", 3], ["traits", ["foraging", "long-neck"]]]]], ["bag", 5], ["cards", [[3, "carnivore"]]]],
                                [["id", 3], ["species", []], ["bag", 8], ["cards", [[5, "carnivore"]]]]
                            ],
                            10,
                            [[3, "carnivore"]]
                        ],
                        [
                            [1, [["population", 0, 0]], [], [], []],
                            [0, [], [], [], []],
                            [0, [], [], [], []]
                        ]
                    ]
    self.case8_out = json.dumps([
                                    [
                                        [["id", 1], ["species", [[["food", 4], ["body", 1], ["population", 4], ["traits", ["foraging"]]]]], ["bag", 3]],
                                        [["id", 2], ["species", [[["food", 3], ["body", 1], ["population", 3], ["traits", ["foraging", "long-neck"]]]]], ["bag", 5]],
                                        [["id", 3], ["species", []], ["bag", 8]]
                                    ],
                                    17,
                                    [[3, "carnivore"]]
                                ])
    self.case9_in = [
                        [
                            [
                                [["id", 1], ["species", [[["food", 1], ["body", 1], ["population", 3], ["traits", ["foraging"]]]]], ["bag", 3], ["cards", [[-2, "carnivore"], [1, "carnivore"]]]],
                                [["id", 2], ["species", [[["food", 1], ["body", 1], ["population", 3], ["traits", []]]]], ["bag", 5], ["cards", [[3, "carnivore"], [-2, "carnivore"]]]],
                                [["id", 3], ["species", []], ["bag", 8], ["cards", [[5, "carnivore"]]]]
                            ],
                            10,
                            [[3, "carnivore"]]
                        ],
                        [
                            [1, [], [["body", 0, 0]], [], []],
                            [1, [], [["body", 0, 0]], [], []],
                            [0, [], [], [], []]
                        ]
                    ]
    self.case9_out = json.dumps([
                                    [
                                        [["id", 1], ["species", [[["food", 3], ["body", 2], ["population", 3], ["traits", ["foraging"]]]]], ["bag", 3]],
                                        [["id", 2], ["species", [[["food", 3], ["body", 2], ["population", 3], ["traits", []]]]], ["bag", 5]],
                                        [["id", 3], ["species", []], ["bag", 8]]
                                    ],
                                    10,
                                    [[3, "carnivore"]]
                                ])
    self.case10_in = [
                        [
                            [
                                [["id", 1], ["species", [[["food", 1], ["body", 1], ["population", 3], ["traits", ["foraging"]]]]], ["bag", 3], ["cards", [[-2, "carnivore"], [1, "carnivore"], [4, "carnivore"]]]],
                                [["id", 2], ["species", [[["food", 1], ["body", 1], ["population", 3], ["traits", []]]]], ["bag", 5], ["cards", [[3, "carnivore"], [-2, "carnivore"]]]],
                                [["id", 3], ["species", []], ["bag", 8], ["cards", [[5, "carnivore"]]]]
                            ],
                            10,
                            [[3, "carnivore"]]
                        ],
                        [
                            [1, [], [["body", 0, 0]], [], [[0, 0, 2]]],
                            [1, [], [["body", 0, 0]], [], []],
                            [0, [], [], [], []]
                        ]
                    ]
    self.case10_out = json.dumps([
                                    [
                                        [["id", 1], ["species", [[["food", 3], ["body", 2], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 3]],
                                        [["id", 2], ["species", [[["food", 1], ["body", 2], ["population", 1], ["traits", []]]]], ["bag", 5]],
                                        [["id", 3], ["species", []], ["bag", 8]]
                                    ],
                                    11,
                                    [[3, "carnivore"]]
                                ])
    self.case11_in =[[[[["id",2],
                       ["species",[[["food",0],
                                    ["body",4],
                                    ["population",4],
                                    ["traits",["fat-tissue"]]]]],
                       ["bag",42],
                       ["cards",[[3, "climbing"]]]],
                      [["id",3],
                       ["species",[[["food",0],
                                    ["body",4],
                                    ["population",4],
                                    ["traits",[]]]]],
                       ["bag",2],
                       ["cards",[[3, "burrowing"]]]],
                      [["id",4],
                       ["species",[[["food",0],
                                    ["body",7],
                                    ["population",1],
                                    ["traits",["fat-tissue"]]]]],
                       ["bag",100],
                       ["cards", [[3, "burrowing"]]]]],
                     10,
                     []],
                     [[0, [], [], [], []],
                      [0, [], [], [], []],
                      [0, [], [], [], []]]]

    self.case11_out = json.dumps([[[["id",2],
                                   ["species",[[["food",3],
                                                ["body",4],
                                                ["population",4],
                                                ["traits",["fat-tissue"]],
                                                ["fat-food",4]]]],
                                   ["bag",42]],
                                  [["id",3],
                                   ["species",[[["food",4],
                                                ["body",4],
                                                ["population",4],
                                                ["traits",[]]]]],
                                   ["bag",2]],
                                  [["id",4],
                                   ["species",[[["food",1],
                                                ["body",7],
                                                ["population",1],
                                                ["traits",["fat-tissue"]],
                                                ["fat-food",7]]]],
                                   ["bag",100]]],
                                 0,
                                 []]
                                )
    self.case12_in = [[[[["id",2],
                       ["species",[[["food",0],
                                    ["body",4],
                                    ["population",4],
                                    ["traits",["long-neck"]]]]],
                       ["bag",42],
                       ["cards",[[3, "climbing"]]]],
                      [["id",3],
                       ["species",[[["food",0],
                                    ["body",4],
                                    ["population",4],
                                    ["traits",["fertile"]]]]],
                       ["bag",2],
                       ["cards",[[3, "burrowing"]]]],
                      [["id",4],
                       ["species",[[["food",0],
                                    ["body",7],
                                    ["population",1],
                                    ["traits",["fat-tissue"]],
                                    ["fat-food", 1]]]],
                       ["bag",100],
                       ["cards", [[3, "burrowing"]]]]],
                     0,
                     []],
                     [[0, [], [], [], []],
                      [0, [], [], [], []],
                      [0, [], [], [], []]]]

    self.case12_out = json.dumps([[[["id",2],
                                   ["species",[[["food",2],
                                                ["body",4],
                                                ["population",4],
                                                ["traits",["long-neck"]]]]],
                                   ["bag",42]],
                                  [["id",3],
                                   ["species",[[["food",1],
                                                ["body",4],
                                                ["population",5],
                                                ["traits",["fertile"]]]]],
                                   ["bag",2]],
                                  [["id",4],
                                   ["species",[[["food",1],
                                                ["body",7],
                                                ["population",1],
                                                ["traits",["fat-tissue"]],
                                                ["fat-food", 6]]]],
                                   ["bag",100]]],
                                 0,
                                 []]
                                )
    self.case13_in = [[[[["id",2],
                           ["species",[[["food",0],
                                        ["body",4],
                                        ["population",4],
                                        ["traits",["carnivore"]]]]],
                           ["bag",42],
                           ["cards",[[0, "fertile"], [3, "long-neck"]]]],
                          [["id",3],
                           ["species",[[["food",0],
                                        ["body",4],
                                        ["population",4],
                                        ["traits",["fertile"]]]]],
                           ["bag",2],
                           ["cards",[[0, "burrowing"]]]],
                          [["id",4],
                           ["species",[[["food",0],
                                        ["body",4],
                                        ["population",1],
                                        ["traits",["fat-tissue"]],
                                        ["fat-food", 1]]]],
                           ["bag",100],
                           ["cards", [[0, "burrowing"]]]]],
                         0,
                         [[3, "burrowing"],
                          [3, "long-neck"],
                          [2, "burrowing"],
                          [-1, "burrowing"]]],
                         [[0, [], [], [], [[0, 0, 1]]],
                          [0, [], [], [], []],
                          [0, [], [], [], []]]]

    self.case13_out = json.dumps([[[["id",2],
                                   ["species",[[["food",0],
                                                ["body",4],
                                                ["population",4],
                                                ["traits",["long-neck"]]]]],
                                   ["bag",42]],
                                  [["id",3],
                                   ["species",[[["food",0],
                                                ["body",4],
                                                ["population",5],
                                                ["traits",["fertile"]]]]],
                                   ["bag",2]],
                                  [["id",4],
                                   ["species",[[["food",1],
                                                ["body",4],
                                                ["population",1],
                                                ["traits",["fat-tissue"]]]]],
                                   ["bag",100]]],
                                 0,
                                 [[3, "burrowing"],
                                  [3, "long-neck"],
                                  [2, "burrowing"],
                                  [-1, "burrowing"]]])
    self.case14_in = [[[[["id",1],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[3, "cooperation"], [1, "climbing"]]]],

                        [["id",2],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[2, "carnivore"]]]],

                        [["id",3],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[2, "long-neck"]]]]],
                         0,
                         []],

                     [[1, [], [], [], []],
                      [0, [], [], [], []],
                      [0, [], [], [], []]]]
    self.case14_out = json.dumps([[[["id", 1],
                                    ["species", []],
                                    ["bag", 0],
                                    ["cards", [[3, "cooperation"]]]],
                                  [["id", 2],
                                    ["species", []],
                                    ["bag", 0]],
                                  [["id", 3],
                                    ["species", []],
                                    ["bag", 0]]],
                                  5,
                                  []])
    self.case15_in = [[[[["id",1],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[3, "cooperation"], [1, "climbing"]]]],

                        [["id",2],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[2, "carnivore"]]]],

                        [["id",3],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[2, "long-neck"]]]]],
                         0,
                         []],

                     [[1, [], [], [[0]], []],
                      [0, [], [], [], []],
                      [0, [], [], [], []]]]
    self.case15_out = json.dumps([[[["id", 1],
                                  ["species",
                                    [[["food", 1],
                                      ["body", 0],
                                      ["population", 1],
                                      ["traits", []]]]],
                                  ["bag", 0]],
                                  [["id", 2],
                                  ["species", []],
                                  ["bag", 0]],
                                  [["id", 3],
                                  ["species", []],
                                   ["bag", 0]]],
                                4,
                                []]
                                )
    self.case16_in = [[[[["id",1],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[3, "cooperation"], [1, "climbing"], [2, "fertile"]]]],

                        [["id",2],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[2, "carnivore"]]]],

                        [["id",3],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[2, "long-neck"], [-8, "carnivore"]]]]],
                         0,
                         []],

                     [[1, [], [], [[0, 2]], []],
                      [0, [], [], [], []],
                      [1, [], [], [], []]]]

    self.case16_out = json.dumps([[[["id", 1],
                                  ["species",
                                   [[["food", 0],
                                    ["body", 0],
                                    ["population", 2],
                                     ["traits", ["fertile"]]]]],
                                  ["bag", 0]],
                                  [["id", 2],
                                    ["species", []],
                                    ["bag", 0]],
                                  [["id", 3],
                                    ["species", []],
                                    ["bag", 0],
                                    ["cards", [[2, "long-neck"]]]]],
                                    0,
                                  []])
    self.case17_in = [[[[["id",1],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[3, "cooperation"], [1, "climbing"], [-3, "fertile"], [3, "ambush"]]]],

                        [["id",2],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[2, "carnivore"], [3, "burrowing"], [0, "cooperation"]]]],

                        [["id",3],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[2, "long-neck"]]]]],
                         0,
                         []],

                     [[1, [["population", 0, 3]], [], [[0, 2]], []],
                      [0, [], [["body", 0, 2]], [[1]], []],
                      [0, [], [], [], []]]]

    self.case17_out = json.dumps([[[["id", 1],
                                  ["species",
                                      [[["food", 3],
                                       ["body", 0],
                                       ["population", 3],
                                       ["traits", ["fertile"]]]]],
                                   ["bag", 0]],
                                [["id", 2],
                                 ["species",
                                     [[["food", 1],
                                     ["body", 1],
                                     ["population", 1],
                                      ["traits", []]]]],
                                  ["bag", 0]],
                                [["id", 3],
                                 ["species", []],
                                 ["bag", 0]]],
                                1,
                                []])
    self.case18_in = [[[[["id",1],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[3, "cooperation"], [1, "climbing"], [-3, "fertile"], [3, "ambush"], [-2, "long-neck"]]]],

                        [["id",2],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[2, "carnivore"], [3, "burrowing"], [0, "cooperation"]]]],

                        [["id",3],
                         ["species",[]],
                         ["bag", 0],
                         ["cards", [[2, "long-neck"]]]]],
                         0,
                         []],

                     [[1, [["population", 0, 3]], [], [[0, 2]], [[0, 0, 4]]],
                      [0, [], [["body", 0, 2]], [[1]], []],
                      [0, [], [], [], []]]]

    self.case18_out = json.dumps([[[["id", 1],
                                    ["species",
                                      [[["food", 2],
                                        ["body", 0],
                                        ["population", 2],
                                        ["traits", ["long-neck"]]]]],
                                    ["bag", 0]],
                                [["id", 2],
                                    ["species",
                                       [[["food", 1],
                                         ["body", 1],
                                         ["population", 1],
                                      ["traits", []]]]],
                                  ["bag", 0]],
                                [["id", 3],
                                 ["species", []],
                                  ["bag", 0]]],
                                2,
                                []])
    self.case19_in = [
                        [
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
                              ["bag", 3],
                              ["cards", [[2, "foraging"]]]
                            ],
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
                              ["bag", 4],
                              ["cards", [[-1, "burrowing"]]]
                            ],
                            [
                              ["id", 3],
                              ["species",
                                []
                              ],
                              ["bag", 5],
                              ["cards", [[1, "fat-tissue"]]]
                            ]
                          ],
                          0,
                          []
                        ],
                         [
                          [0, [], [], [], []],
                          [0, [], [], [], []],
                          [0, [], [], [], []]
                         ]
                        ]
    self.case19_out = json.dumps([
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
                                      ["bag", 3]
                                    ],
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
    self.case20_in =  [
                        [
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
                              ["bag", 3],
                              ["cards", [[3, "foraging"]]]
                            ],
                            [
                              ["id", 2],
                              ["species",
                                [
                                  [
                                    ["food", 2],
                                    ["body", 3],
                                    ["population", 2],
                                    ["traits", ["burrowing", "long-neck", "fertile"]]
                                  ]
                                ]
                              ],
                              ["bag", 4],
                              ["cards", [[-1, "burrowing"]]]
                            ],
                            [
                              ["id", 3],
                              ["species",
                                []
                              ],
                              ["bag", 5],
                              ["cards", [[1, "fat-tissue"]]]
                            ]
                          ],
                          0,
                          []
                        ],
                         [
                          [0, [], [], [], []],
                          [0, [], [], [], []],
                          [0, [], [], [], []]
                         ]
                        ]

    self.case20_out = json.dumps([
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
                                      ["bag", 3]
                                    ],
                                    [
                                      ["id", 2],
                                      ["species",
                                        [
                                          [
                                            ["food", 3],
                                            ["body", 3],
                                            ["population", 3],
                                            ["traits", ["burrowing", "long-neck", "fertile"]]
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
                                ]
                                )
    self.case21_in =[
                    [
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
                          ["bag", 3],
                          ["cards", [[3, "foraging"]]]
                        ],
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 2],
                                ["body", 3],
                                ["population", 3],
                                ["traits", ["foraging", "long-neck", "fertile"]]
                              ]
                            ]
                          ],
                          ["bag", 4],
                          ["cards", [[-1, "burrowing"]]]
                        ],
                        [
                          ["id", 3],
                          ["species",
                            []
                          ],
                          ["bag", 5],
                          ["cards", [[1, "fat-tissue"]]]
                        ]
                      ],
                      0,
                      []
                    ],
                     [
                      [0, [], [], [], []],
                      [0, [], [], [], []],
                      [0, [], [], [], []]
                     ]
                    ]

    self.case21_out = json.dumps([
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
                                            ["fat-food", 1]
                                          ]
                                        ]
                                      ],
                                      ["bag", 3]
                                    ],
                                    [
                                      ["id", 2],
                                      ["species",
                                        [
                                          [
                                            ["food", 4],
                                            ["body", 3],
                                            ["population", 4],
                                            ["traits", ["foraging", "long-neck", "fertile"]]
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
    self.case22_in = [
    [
        [
            [
                ["id", 1],
                ["species", [
                    [
                        ["food", 0],
                        ["body", 3],
                        ["population", 1],
                        ["traits", []]
                    ],
                    [
                        ["food", 1],
                        ["body", 3],
                        ["population", 1],
                        ["traits", []]
                    ],
                    [
                        ["food", 0],
                        ["body", 3],
                        ["population", 1],
                        ["traits", ["carnivore"]]
                    ]
                ]],
                ["bag", 0],
                ["cards", [
                    [3, "carnivore"],
                    [2, "climbing"]
                ]]
            ],
            [
                ["id", 2],
                ["species", [
                    [
                        ["food", 0],
                        ["body", 3],
                        ["population", 1],
                        ["traits", []]
                    ],
                    [
                        ["food", 0],
                        ["body", 3],
                        ["population", 1],
                        ["traits", ["climbing"]]
                    ]
                ]],
                ["bag", 0],
                ["cards", [
                    [-3, "carnivore"],
                    [-2, "climbing"]
                ]]


            ],
            [
                ["id", 3],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 3],
                        ["population", 1],
                        ["traits", []]
                    ]
                ]],
                ["bag", 0],
                ["cards", [
                    [0, "carnivore"],
                    [0, "climbing"]
                ]]

            ]
        ], 9, []
    ],
    [
        [0, [],
            [],
            [],
            []
        ],
        [0, [],
            [],
            [],
            []
        ],
        [0, [],
            [],
            [],
            []
        ]
    ]
]
    self.case22_out = json.dumps(   [
        [
            [
                ["id", 1],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 3],
                        ["population", 1],
                        ["traits", []]
                    ],
                    [
                        ["food", 1],
                        ["body", 3],
                        ["population", 1],
                        ["traits", []]
                    ],
                    [
                        ["food", 1],
                        ["body", 3],
                        ["population", 1],
                        ["traits", ["carnivore"]]
                    ]
                ]],
                ["bag", 0],
                ["cards", [
                    [2, "climbing"]
                ]]
            ],
            [
                ["id", 2],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 3],
                        ["population", 1],
                        ["traits", ["climbing"]]
                    ]
                ]],
                ["bag", 0],
                ["cards", [
                    [-2, "climbing"]
                ]]


            ],
            [
                ["id", 3],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 3],
                        ["population", 1],
                        ["traits", []]
                    ]
                ]],
                ["bag", 0],
                ["cards", [
                    [0, "climbing"]
                ]]

            ]
        ], 5, []
    ])
    self.case23_in = [
    [
        [
            [
                ["id", 4],
                ["species", [
                    [
                        ["food", 0],
                        ["body", 0],
                        ["population", 1],
                        ["traits", ["cooperation"]]
                    ]
                ]],
                ["bag", 0],
                ["cards", [
                    [1, "carnivore"],
                    [2, "carnivore"],
                    [1, "fertile"],
                    [-1, "long-neck"],
                    [-3, "carnivore"]
                ]]
            ],
            [
                ["id", 13],
                ["species", [
                    [
                        ["food", 0],
                        ["body", 0],
                        ["population", 1],
                        ["traits", ["foraging"]]
                    ]
                ]],
                ["bag", 0],
                ["cards", [
                    [-1, "foraging"]
                ]]


            ]
        ], 10, []
    ],
    [
        [0, [["population", 1, 3]],
            [["body", 1, 4]],
            [[1, 2]],
            []
        ],
        [0, [],
            [],
            [],
            []
        ]
    ]
]
    self.case23_out = json.dumps([
        [
            [
                ["id", 4],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 0],
                        ["population", 1],
                        ["traits", ["cooperation"]]
                    ],
                  [
                        ["food", 3],
                        ["body", 1],
                        ["population", 3],
                        ["traits", ["fertile"]]
                    ]
                ]],
                ["bag", 0]
            ],
            [
                ["id", 13],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 0],
                        ["population", 1],
                        ["traits", ["foraging"]]
                    ]
                ]],
                ["bag", 0]
            ]
        ], 5, []
    ])
    self.case24_in = [
    [
        [
            [
                ["id", 1],
                ["species", [
                    [
                        ["food", 0],
                        ["body", 3],
                        ["population", 1],
                        ["traits", []]
                    ]
                ]],
                ["bag", 0],
                ["cards", [
                    [0, "carnivore"]]]
            ],
            [
                ["id", 2],
                ["species", [
                    [
                        ["food", 0],
                        ["body", 1],
                        ["population", 1],
                        ["traits", ["foraging", "fertile", "long-neck"]]
                    ]
                ]],
                ["bag", 0],
                ["cards", [
                    [0, "climbing"]
                ]]


            ]
        ], 2, []
    ],
    [
        [0, [],
            [],
            [],
            []
        ],
        [0, [],
            [],
            [],
            []
        ]
    ]
]
    self.case24_out = json.dumps([
        [
            [
                ["id", 1],
                ["species", [
                    [
                        ["food", 0],
                        ["body", 3],
                        ["population", 1],
                        ["traits", []]
                    ]
                ]],
                ["bag", 0]
            ],
            [
                ["id", 2],
                ["species", [
                    [
                        ["food", 2],
                        ["body", 1],
                        ["population", 2],
                        ["traits", ["foraging", "fertile", "long-neck"]]
                    ]
                ]],
                ["bag", 0]

            ]
        ], 0, []
    ])
    self.case25_in = [
    [
        [
            [
                ["id", 4],
                ["species", [
                    [
                        ["food", 0],
                        ["body", 0],
                        ["population", 2],
                        ["traits", ["hard-shell"]]
                    ]
                ]],
                ["bag", 0],
                ["cards", [
                    [0, "foraging"],
                    [1, "carnivore"]
                ]]
            ],
            [
                ["id", 13],
                ["species", [
                    [
                        ["food", 0],
                        ["body", 0],
                        ["population", 1],
                        ["traits", ["foraging"]]
                    ]
                ]],
                ["bag", 0],
                ["cards", [
                    [-1, "foraging"]
                ]]


            ]
        ], 2, []
    ],
    [
        [1, [],
            [],
            [],
            [[0, 0, 0]]
        ],
        [0, [],
            [],
            [],
            []
        ]
    ]
]
    self.case25_out = json.dumps([
  [
            [
                ["id", 4],
                ["species", [
                    [
                        ["food", 2],
                        ["body", 0],
                        ["population", 2],
                        ["traits", ["foraging"]]
                    ]
                ]],
                ["bag", 0]
            ],
            [
                ["id", 13],
                ["species", [
                    [
                        ["food", 0],
                        ["body", 0],
                        ["population", 1],
                        ["traits", ["foraging"]]
                    ]
                ]],
                ["bag", 0]

            ]
        ], 0, []
    ]
)
    self.case26_in = [
    [
        [
            [
                ["id", 1],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 1],
                        ["population", 1],
                        ["traits", ["carnivore"]]
                    ],
                    [
                        ["food", 1],
                        ["body", 2],
                        ["population", 6],
                        ["traits", ["carnivore", "cooperation"]]
                    ],
                    [
                        ["food", 2],
                        ["body", 4],
                        ["population", 5],
                        ["traits", ["carnivore", "cooperation"]]
                    ],
                    [
                        ["food", 2],
                        ["body", 4],
                        ["population", 5],
                        ["traits", ["carnivore", "cooperation"]]
                    ]
                ]],
                ["bag", 2],
                ["cards", [
                    [1, "scavenger"],
                    [-2, "long-neck"],
                    [-1, "carnivore"]
                ]]
            ],
            [
                ["id", 2],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 2],
                        ["population", 1],
                        ["traits", []]
                    ],
                    [
                        ["food", 1],
                        ["body", 2],
                        ["population", 1],
                        ["traits", []]
                    ],
                    [
                        ["food", 1],
                        ["body", 2],
                        ["population", 1],
                        ["traits", []]
                    ]
                ]],
                ["bag", 3],
                ["cards", [
                    [1, "fertile"],
                    [-2, "carnivore"],
                    [-1, "cooperation"]
                ]]
            ],
            [
                ["id", 3],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 2],
                        ["population", 1],
                        ["traits", ["carnivore"]]
                    ],
                    [
                        ["food", 1],
                        ["body", 2],
                        ["population", 1],
                        ["traits", ["carnivore"]]
                    ]
                ]],
                ["bag", 1],
                ["cards", [
                    [1, "pack-hunting"],
                    [-2, "hard-shell"],
                    [-1, "burrowing"]
                ]]
            ]
        ], 10, [
            [1, "foraging"],
            [-2, "fertile"],
            [-1, "long-neck"],
            [5, "carnivore"],
            [3, "herding"],
            [2, "fat-tissue"],
            [0, "ambush"]
        ]

], [
    [1, [],
        [],
        [],
        [[2,0,0]]
    ],
    [0, [["population",2,2]],
        [],
        [],
        []
    ],
    [2, [],
        [],
        [[0,1]],
        []
    ]
]]

    self.case26_out = json.dumps([[[["id",1],["species",[[["food",1],["body",1],["population",1],["traits",["carnivore"]]],[["food",1],["body",2],["population",6],["traits",["carnivore","cooperation"]]],[["food",5],["body",4],["population",5],["traits",["scavenger","cooperation"]]],[["food",5],["body",4],["population",5],["traits",["carnivore","cooperation"]]]]],["bag",2],["cards",[[-1,"carnivore"]]]],[["id",2],["species",[[["food",1],["body",2],["population",1],["traits",[]]],[["food",1],["body",2],["population",1],["traits",[]]],[["food",2],["body",2],["population",2],["traits",[]]]]],["bag",3],["cards",[[-2,"carnivore"]]]],[["id",3],["species",[[["food",1],["body",2],["population",1],["traits",["carnivore"]]],[["food",1],["body",2],["population",1],["traits",["carnivore"]]],[["food",1],["body",0],["population",1],["traits",["hard-shell"]]]]],["bag",1]]],0,[[1,"foraging"],[-2,"fertile"],[-1,"long-neck"],[5,"carnivore"],[3,"herding"],[2,"fat-tissue"],[0,"ambush"]]]
)
    self.case27_in =   [
    [
        [
            [
                ["id", 1],
                ["species", [
                    [
                        ["food", 0],
                        ["body", 3],
                        ["population", 1],
                        ["traits", ["fat-tissue"]],
                        ["fat-food", 3]
                    ]
                ]],
                ["bag", 2],
                ["cards", [
                    [1, "scavenger"],
                    [-2, "long-neck"],
                    [-1, "carnivore"]
                ]]
            ],
            [
                ["id", 2],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 2],
                        ["population", 2],
                        ["traits", ["long-neck"]]
                    ]
                ]],
                ["bag", 3],
                ["cards", [
                    [1, "fertile"],
                    [-2, "carnivore"],
                    [-1, "cooperation"]
                ]]
            ],
            [
                ["id", 3],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 2],
                        ["population", 1],
                        ["traits", ["fertile"]]
                    ]
                ]],
                ["bag", 1],
                ["cards", [
                    [1, "pack-hunting"],
                    [-2, "hard-shell"],
                    [-1, "burrowing"]
                ]]
            ]
        ], 10, [
            [1, "foraging"],
            [-2, "fertile"],
            [-1, "long-neck"],
            [5, "carnivore"],
            [3, "herding"],
            [2, "fat-tissue"],
            [0, "ambush"]
        ]

    ],
    [
        [1, [],
            [],
            [],
            []
        ],
        [0, [],
            [],
            [],
            []
        ],
        [2, [],
            [],
            [],
            []
        ]
    ]
]

    self.case27_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",["fat-tissue"]],["fat-food",3]]]],["bag",2],["cards",[[1,"scavenger"],[-1,"carnivore"]]]],[["id",2],["species",[[["food",2],["body",2],["population",2],["traits",["long-neck"]]]]],["bag",3],["cards",[[-2,"carnivore"],[-1,"cooperation"]]]],[["id",3],["species",[[["food",2],["body",2],["population",2],["traits",["fertile"]]]]],["bag",1],["cards",[[1,"pack-hunting"],[-2,"hard-shell"]]]]],5,[[1,"foraging"],[-2,"fertile"],[-1,"long-neck"],[5,"carnivore"],[3,"herding"],[2,"fat-tissue"],[0,"ambush"]]]
)
    self.case28_in = [
    [
        [
            [
                ["id", 1],
                ["species", [
                    [
                        ["food", 0],
                        ["body", 1],
                        ["population", 1],
                        ["traits", ["carnivore"]]
                    ]
                ]],
                ["bag", 2],
                ["cards", [
                    [5, "carnivore"]
                ]]
            ],
            [
                ["id", 2],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 2],
                        ["population", 1],
                        ["traits", ["climbing"]]
                    ]
                ]],
                ["bag", 3],
                ["cards", [
                    [1, "fertile"]
                ]]
            ],
            [
                ["id", 3],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 2],
                        ["population", 1],
                        ["traits", ["carnivore", "climbing"]]
                    ]
                ]],
                ["bag", 1],
                ["cards", [
                    [0, "fat-tissue"]
                ]]
            ]
        ], 10, [
            [1, "foraging"],
            [-2, "fertile"],
            [-1, "long-neck"],
            [5, "carnivore"],
            [3, "herding"],
            [2, "fat-tissue"],
            [0, "ambush"]
        ]

    ],
    [
        [0, [],
            [],
            [],
            []
        ],
        [0, [],
            [],
            [],
            []
        ],
        [0, [],
            [],
            [],
            []
        ]
    ]
]

    self.case28_out = json.dumps([[[["id",1],["species",[[["food",0],["body",1],["population",1],["traits",["carnivore"]]]]],["bag",2]],[["id",2],["species",[[["food",1],["body",2],["population",1],["traits",["climbing"]]]]],["bag",3]],[["id",3],["species",[[["food",1],["body",2],["population",1],["traits",["carnivore","climbing"]]]]],["bag",1]]],16,[[1,"foraging"],[-2,"fertile"],[-1,"long-neck"],[5,"carnivore"],[3,"herding"],[2,"fat-tissue"],[0,"ambush"]]]
)
    self.case29_in =    [
    [
        [
            [
                ["id", 1],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 1],
                        ["population", 1],
                        ["traits", ["fat-tissue"]]
                    ]
                ]],
                ["bag", 2],
                ["cards", [
                    [5, "carnivore"]
                ]]
            ],
            [
                ["id", 2],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 2],
                        ["population", 1],
                        ["traits", ["climbing"]]
                    ]
                ]],
                ["bag", 3],
                ["cards", [
                    [1, "fertile"]
                ]]
            ],
            [
                ["id", 3],
                ["species", [
                    [
                        ["food", 1],
                        ["body", 2],
                        ["population", 1],
                        ["traits", ["carnivore", "climbing"]]
                    ]
                ]],
                ["bag", 1],
                ["cards", [
                    [0, "fat-tissue"]
                ]]
            ]
        ], 10, [
            [1, "foraging"],
            [-2, "fertile"],
            [-1, "long-neck"],
            [5, "carnivore"],
            [3, "herding"],
            [2, "fat-tissue"],
            [0, "ambush"]
        ]

    ],
    [
        [0, [],
            [],
            [],
            []
        ],
        [0, [],
            [],
            [],
            []
        ],
        [0, [],
            [],
            [],
            []
        ]
    ]
]

    self.case29_out = json.dumps([[[["id",1],["species",[[["food",1],["body",1],["population",1],["traits",["fat-tissue"]],["fat-food",1]]]],["bag",2]],[["id",2],["species",[[["food",1],["body",2],["population",1],["traits",["climbing"]]]]],["bag",3]],[["id",3],["species",[[["food",1],["body",2],["population",1],["traits",["carnivore","climbing"]]]]],["bag",1]]],15,[[1,"foraging"],[-2,"fertile"],[-1,"long-neck"],[5,"carnivore"],[3,"herding"],[2,"fat-tissue"],[0,"ambush"]]]
)
    self.case30_in = [
  [
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
        ["bag", 0],
        ["cards", [[0, "carnivore"], [-1, "horns"], [0, "fertile"], [0, "horns"], [0, "scavenger"], [0, "foraging"]]]
      ],
      [["id", 2],
        ["species", [[["food", 2],
                      ["body", 5],
                      ["population", 4],
                      ["traits", ["scavenger"]]]]],
        ["bag", 0],
        ["cards", [[0, "carnivore"], [0, "horns"], [0, "fertile"], [1, "horns"], [3, "scavenger"], [0, "foraging"]]]
      ],
      [["id", 3], ["species",
                    [[["food", 2],
                      ["body", 1],
                      ["population", 6],
                      ["traits", ["foraging", "horns"]]]]],
        ["bag", 0],
        ["cards", [[0, "carnivore"], [0, "horns"], [0, "fertile"], [0, "horns"], [3, "scavenger"], [1, "foraging"]]]
      ]
    ],
    0,
    [
      [4, "carnivore"],
      [3, "scavenger"],
      [0, "fertile"],
      [3, "long-neck"],
      [4, "carnivore"],
      [3, "scavenger"],
      [-1, "horns"],
      [3, "fat-tissue"]
    ]
  ],
  [
    [1, [["population", 1, 2]], [["body", 2, 3]], [[4, 0]], [[2, 0, 5]]],

    [0, [], [], [], []],

    [0, [["population", 0, 1]], [], [], []]

  ]
]
    self.case30_out = json.dumps([[[["id", 1], ["species", [[["food", 2], ["body", 5], ["population", 6], ["traits", ["carnivore", "cooperation"]]], [["food", 2], ["body", 5], ["population", 4], ["traits", ["carnivore", "cooperation"]]], [["food", 2], ["body", 6], ["population", 3], ["traits", ["foraging"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]]]], ["bag", 0]], [["id", 2], ["species", [[["food", 2], ["body", 5], ["population", 4], ["traits", ["scavenger"]]]]], ["bag", 0], ["cards", [[0, "horns"], [0, "fertile"], [1, "horns"], [3, "scavenger"], [0, "foraging"]]]], [["id", 3], ["species", [[["food", 2], ["body", 1], ["population", 7], ["traits", ["foraging", "horns"]]]]], ["bag", 0], ["cards", [[0, "fertile"], [0, "horns"], [3, "scavenger"], [1, "foraging"]]]]], 0, [[4, "carnivore"], [3, "scavenger"], [0, "fertile"], [3, "long-neck"], [4, "carnivore"], [3, "scavenger"], [-1, "horns"], [3, "fat-tissue"]]])
    self.case31_in =  [
  [
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
        ["bag", 0],
        ["cards", [[0, "carnivore"], [3, "horns"], [0, "fertile"], [0, "horns"], [0, "scavenger"], [0, "foraging"]]]
      ],
      [["id", 2],
        ["species", [[["food", 2],
                      ["body", 5],
                      ["population", 4],
                      ["traits", ["scavenger"]]]]],
        ["bag", 0],
        ["cards", [[2, "carnivore"], [0, "horns"], [0, "fertile"], [1, "horns"], [3, "scavenger"], [0, "foraging"]]]
      ],
      [["id", 3], ["species",
                    [[["food", 2],
                      ["body", 1],
                      ["population", 6],
                      ["traits", ["foraging", "horns"]]]]],
        ["bag", 0],
        ["cards", [[2, "carnivore"], [0, "horns"], [0, "fertile"], [0, "horns"], [3, "scavenger"], [1, "foraging"]]]
      ]
    ],
    0,
    [
      [4, "carnivore"],
      [3, "scavenger"],
      [0, "fertile"],
      [3, "long-neck"],
      [4, "carnivore"],
      [3, "scavenger"],
      [-1, "horns"],
      [3, "fat-tissue"]
    ]
  ],
  [
    [1, [["population", 1, 2]], [["body", 2, 3]], [[4, 0]], [[2, 0, 5]]],

    [0, [], [], [], []],

    [0, [["population", 0, 1]], [], [], []]

  ]
]
    self.case31_out = json.dumps([[[["id", 1], ["species", [[["food", 3], ["body", 5], ["population", 5], ["traits", ["carnivore", "cooperation"]]], [["food", 3], ["body", 5], ["population", 4], ["traits", ["carnivore", "cooperation"]]], [["food", 3], ["body", 6], ["population", 3], ["traits", ["foraging"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]]]], ["bag", 0]], [["id", 2], ["species", [[["food", 4], ["body", 5], ["population", 4], ["traits", ["scavenger"]]]]], ["bag", 0], ["cards", [[0, "horns"], [0, "fertile"], [1, "horns"], [3, "scavenger"], [0, "foraging"]]]], [["id", 3], ["species", [[["food", 4], ["body", 1], ["population", 6], ["traits", ["foraging", "horns"]]]]], ["bag", 0], ["cards", [[0, "fertile"], [0, "horns"], [3, "scavenger"], [1, "foraging"]]]]], 0, [[4, "carnivore"], [3, "scavenger"], [0, "fertile"], [3, "long-neck"], [4, "carnivore"], [3, "scavenger"], [-1, "horns"], [3, "fat-tissue"]]])
    self.case32_in =  [
  [
    [
      [["id", 1],
        ["species", [[["food", 2],
                      ["body", 5],
                      ["population", 6],
                      ["traits", ["cooperation"]]],
                      [["food", 2],
                      ["body", 5],
                      ["population", 3],
                      ["traits", ["foraging", "cooperation"]]],
                      [["food", 2],
                      ["body", 5],
                      ["population", 3],
                      ["traits", ["cooperation"]]]]],
        ["bag", 0],
        ["cards", [[0, "burrowing"], [3, "horns"], [0, "climbing"], [0, "horns"], [0, "scavenger"], [0, "foraging"]]]
      ],
      [["id", 2],
        ["species", [[["food", 2],
                      ["body", 5],
                      ["population", 4],
                      ["traits", ["scavenger"]]]]],
        ["bag", 0],
        ["cards", [[2, "carnivore"], [0, "horns"], [0, "fertile"], [1, "horns"], [3, "scavenger"], [0, "foraging"]]]
      ],
      [["id", 3], ["species",
                    [[["food", 2],
                      ["body", 1],
                      ["population", 6],
                      ["traits", ["foraging", "horns"]]]]],
        ["bag", 0],
        ["cards", [[2, "carnivore"], [0, "horns"], [0, "warning-call"], [0, "horns"], [3, "scavenger"], [1, "foraging"]]]
      ]
    ],
    92,
    [
      [4, "carnivore"],
      [3, "scavenger"],
      [0, "fertile"],
      [3, "long-neck"],
      [4, "carnivore"],
      [3, "scavenger"],
      [-1, "horns"],
      [3, "fat-tissue"]
    ]
  ],
  [
    [1, [], [], [[4, 0, 2, 3]], [[2, 0, 5]]],

    [4, [], [["body", 0, 1], ["body", 0, 0]], [], []],

    [0, [], [], [[1, 2], [3, 4, 5]], []]

  ]
]
    self.case32_out = json.dumps([[[["id", 1], ["species", [[["food", 6], ["body", 5], ["population", 6], ["traits", ["cooperation"]]], [["food", 3], ["body", 5], ["population", 3], ["traits", ["foraging", "cooperation"]]], [["food", 3], ["body", 5], ["population", 3], ["traits", ["foraging"]]], [["food", 1], ["body", 0], ["population", 1], ["traits", ["burrowing", "climbing", "horns"]]]]], ["bag", 0]], [["id", 2], ["species", [[["food", 4], ["body", 7], ["population", 4], ["traits", ["scavenger"]]]]], ["bag", 0], ["cards", [[0, "fertile"], [1, "horns"], [0, "foraging"]]]], [["id", 3], ["species", [[["food", 6], ["body", 1], ["population", 6], ["traits", ["foraging", "horns"]]], [["food", 1], ["body", 0], ["population", 1], ["traits", ["warning-call"]]], [["food", 1], ["body", 0], ["population", 1], ["traits", ["scavenger", "foraging"]]]]], ["bag", 0]]], 85, [[4, "carnivore"], [3, "scavenger"], [0, "fertile"], [3, "long-neck"], [4, "carnivore"], [3, "scavenger"], [-1, "horns"], [3, "fat-tissue"]]])
    self.case33_in =  [
  [
    [
      [["id", 1],
        ["species", [[["food", 2],
                      ["body", 5],
                      ["population", 6],
                      ["traits", ["cooperation"]]],
                      [["food", 2],
                      ["body", 5],
                      ["population", 3],
                      ["traits", ["foraging", "cooperation"]]],
                      [["food", 2],
                      ["body", 5],
                      ["population", 3],
                      ["traits", ["cooperation"]]]]],
        ["bag", 0],
        ["cards", [[0, "long-neck"], [0, "horns"], [0, "fertile"], [0, "fat-tissue"], [0, "scavenger"], [0, "foraging"]]]
      ],
      [["id", 2],
        ["species", [[["food", 2],
                      ["body", 5],
                      ["population", 4],
                      ["traits", ["fat-tissue", "long-neck"]],
                      ["fat-food", 4]]]],
        ["bag", 0],
        ["cards", [[2, "carnivore"], [0, "horns"], [0, "fertile"], [1, "horns"], [-1, "scavenger"], [0, "foraging"]]]
      ],
      [["id", 3], ["species",
                    [[["food", 2],
                      ["body", 1],
                      ["population", 6],
                      ["traits", ["fertile", "long-neck"]]]]],
        ["bag", 0],
        ["cards", [[0, "carnivore"], [0, "horns"], [0, "warning-call"], [0, "horns"], [3, "scavenger"], [1, "foraging"]]]
      ]
    ],
    3,
    [
      [4, "carnivore"],
      [3, "scavenger"],
      [0, "fertile"],
      [3, "long-neck"],
      [4, "carnivore"],
      [3, "scavenger"],
      [-1, "horns"],
      [3, "fat-tissue"]
    ]
  ],
  [
    [1, [], [], [[4, 0, 2, 3]], [[2, 0, 5]]],

    [4, [["population", 0, 1]], [["body", 0, 0]], [], []],

    [0, [], [], [[1, 2], [3, 4, 5]], []]

  ]
]
    self.case33_out = json.dumps([[[["id", 1], ["species", [[["food", 2], ["body", 5], ["population", 6], ["traits", ["cooperation"]]], [["food", 2], ["body", 5], ["population", 3], ["traits", ["foraging", "cooperation"]]], [["food", 2], ["body", 5], ["population", 3], ["traits", ["foraging"]]], [["food", 1], ["body", 0], ["population", 2], ["traits", ["long-neck", "fertile", "fat-tissue"]]]]], ["bag", 0]], [["id", 2], ["species", [[["food", 5], ["body", 6], ["population", 5], ["traits", ["fat-tissue", "long-neck"]], ["fat-food", 2]]]], ["bag", 0], ["cards", [[0, "fertile"], [1, "horns"], [0, "foraging"]]]], [["id", 3], ["species", [[["food", 2], ["body", 1], ["population", 7], ["traits", ["fertile", "long-neck"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["warning-call"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["scavenger", "foraging"]]]]], ["bag", 0]]], 0, [[4, "carnivore"], [3, "scavenger"], [0, "fertile"], [3, "long-neck"], [4, "carnivore"], [3, "scavenger"], [-1, "horns"], [3, "fat-tissue"]]])
    self.case34_in =   [
  [
    [
      [["id", 1],
        ["species", [[["food", 2],
                      ["body", 5],
                      ["population", 6],
                      ["traits", ["cooperation"]]],
                      [["food", 2],
                      ["body", 5],
                      ["population", 3],
                      ["traits", ["foraging", "cooperation"]]],
                      [["food", 2],
                      ["body", 5],
                      ["population", 3],
                      ["traits", ["cooperation"]]]]],
        ["bag", 10],
        ["cards", [[-1, "long-neck"], [3, "horns"], [-2, "fertile"], [2, "fat-tissue"], [1, "scavenger"], [0, "foraging"]]]
      ],
      [["id", 2],
        ["species", [[["food", 2],
                      ["body", 5],
                      ["population", 4],
                      ["traits", ["fat-tissue", "long-neck"]],
                      ["fat-food", 4]]]],
        ["bag", 1],
        ["cards", [[2, "carnivore"], [2, "horns"], [0, "fertile"], [1, "horns"], [-1, "scavenger"], [0, "foraging"]]]
      ],
      [["id", 3], ["species",
                    [[["food", 2],
                      ["body", 1],
                      ["population", 6],
                      ["traits", ["carnivore", "long-neck"]]],
                     [["food", 2],
                      ["body", 1],
                      ["population", 6],
                      ["traits", ["foraging", "long-neck", "fat-tissue"]],
                      ["fat-food", 1]]]],
        ["bag", 5],
        ["cards", [[5, "carnivore"], [0, "horns"], [-1, "warning-call"], [0, "horns"], [3, "scavenger"], [1, "foraging"]]]
      ]
    ],
    5,
    [
      [4, "carnivore"],
      [3, "scavenger"],
      [0, "fertile"],
      [3, "long-neck"],
      [4, "carnivore"],
      [3, "scavenger"],
      [-1, "horns"],
      [3, "fat-tissue"]
    ]
  ],
  [
    [0, [], [], [], []],

    [0, [], [], [], []],

    [0, [], [["body", 1, 1], ["body", 1, 2], ["body", 1, 3]], [], []]

  ]
]
    self.case34_out = json.dumps([[[["id", 1], ["species", [[["food", 3], ["body", 5], ["population", 6], ["traits", ["cooperation"]]], [["food", 3], ["body", 5], ["population", 3], ["traits", ["foraging", "cooperation"]]], [["food", 3], ["body", 5], ["population", 3], ["traits", ["cooperation"]]]]], ["bag", 10], ["cards", [[3, "horns"], [-2, "fertile"], [2, "fat-tissue"], [1, "scavenger"], [0, "foraging"]]]], [["id", 2], ["species", [[["food", 4], ["body", 5], ["population", 4], ["traits", ["fat-tissue", "long-neck"]], ["fat-food", 5]]]], ["bag", 1], ["cards", [[2, "horns"], [0, "fertile"], [1, "horns"], [-1, "scavenger"], [0, "foraging"]]]], [["id", 3], ["species", [[["food", 3], ["body", 1], ["population", 6], ["traits", ["carnivore", "long-neck"]]], [["food", 5], ["body", 4], ["population", 6], ["traits", ["foraging", "long-neck", "fat-tissue"]], ["fat-food", 2]]]], ["bag", 5], ["cards", [[3, "scavenger"], [1, "foraging"]]]]], 0, [[4, "carnivore"], [3, "scavenger"], [0, "fertile"], [3, "long-neck"], [4, "carnivore"], [3, "scavenger"], [-1, "horns"], [3, "fat-tissue"]]])
    self.case35_in = [[[[["id", 1], ["species", [[["food", 3], ["body", 3], ["population", 3], ["traits", []]], [["food", 2], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 10], ["cards", [[-3, "long-neck"], [0, "long-neck"]]]], [["id", 2], ["species", []], ["bag", 40], ["cards", [[8, "carnivore"]]]], [["id", 3], ["species", []], ["bag", 1], ["cards", [[-8, "carnivore"]]]]], 10, []], [[0, [["population", 0, 1]], [], [], []], [0, [], [], [], []], [0, [], [], [], []]]]
    self.case35_out = json.dumps([[[["id", 1], ["species", [[["food", 4], ["body", 3], ["population", 4], ["traits", []]], [["food", 2], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 10]], [["id", 2], ["species", []], ["bag", 40]], [["id", 3], ["species", []], ["bag", 1]]], 6, []])

    self.case36_in =  [[[[["id", 1], ["species", [[["food", 3], ["body", 3], ["population", 3], ["traits", ["carnivore"]]], [["food", 2], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 10], ["cards", [[-3, "long-neck"], [0, "long-neck"]]]], [["id", 2], ["species", []], ["bag", 40], ["cards", [[8, "carnivore"]]]], [["id", 3], ["species", []], ["bag", 1], ["cards", [[-8, "carnivore"]]]]], 10, []], [[1, [], [], [], [[0, 0, 0]]], [0, [], [], [], []], [0, [], [], [], []]]]
    self.case36_out = json.dumps([[[["id", 1], ["species", [[["food", 3], ["body", 3], ["population", 3], ["traits", ["long-neck"]]], [["food", 2], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 10]], [["id", 2], ["species", []], ["bag", 40]], [["id", 3], ["species", []], ["bag", 1]]], 10, []])

    self.case37_in =  [[[[["id", 1], ["species", [[["food", 0], ["body", 4], ["population", 2], ["traits", ["fat-tissue"]], ["fat-food", 3]]]], ["bag", 10], ["cards", [[-3, "long-neck"]]]], [["id", 2], ["species", []], ["bag", 40], ["cards", [[8, "carnivore"]]]], [["id", 3], ["species", []], ["bag", 1], ["cards", [[-8, "carnivore"]]]]], 4, []], [[0, [], [], [], []], [0, [], [], [], []], [0, [], [], [], []]]]
    self.case37_out = json.dumps([[[["id", 1], ["species", [[["food", 2], ["body", 4], ["population", 2], ["traits", ["fat-tissue"]], ["fat-food", 2]]]], ["bag", 10]], [["id", 2], ["species", []], ["bag", 40]], [["id", 3], ["species", []], ["bag", 1]]], 0, []])

    self.case38_in = [[[[["id", 1], ["species", [[["food", 1], ["body", 3], ["population", 3], ["traits", ["cooperation", "long-neck", "foraging"]]], [["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 10], ["cards", [[-3, "symbiosis"], [1, "scavenger"]]]], [["id", 2], ["species", []], ["bag", 1], ["cards", [[8, "carnivore"]]]], [["id", 3], ["species", []], ["bag", 1], ["cards", [[-8, "carnivore"]]]]], 10, []], [[1, [], [], [], [[0, 0, 0]]], [0, [], [], [], []], [0, [], [], [], []]]]
    self.case38_out = json.dumps([[[["id", 1], ["species", [[["food", 3], ["body", 3], ["population", 3], ["traits", ["symbiosis", "long-neck", "foraging"]]], [["food", 2], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 10]], [["id", 2], ["species", []], ["bag", 1]], [["id", 3], ["species", []], ["bag", 1]]], 8, []])

    self.case39_in =   [[[[["id", 1], ["species", [[["food", 3], ["body", 3], ["population", 3], ["traits", []]], [["food", 2], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 10], ["cards", [[-3, "long-neck"], [0, "long-neck"]]]], [["id", 2], ["species", []], ["bag", 40], ["cards", [[8, "carnivore"]]]], [["id", 3], ["species", []], ["bag", 1], ["cards", [[-8, "carnivore"]]]]], 10, []], [[0, [], [["body", 0, 1]], [], []], [0, [], [], [], []], [0, [], [], [], []]]]
    self.case39_out = json.dumps([[[["id", 1], ["species", [[["food", 3], ["body", 4], ["population", 3], ["traits", []]], [["food", 2], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 10]], [["id", 2], ["species", []], ["bag", 40]], [["id", 3], ["species", []], ["bag", 1]]], 7, []])

    self.case40_in = [[[[
["id", 1],
["species",
    [[["food", 0],["body", 0],["population", 5],["traits", ["foraging", "cooperation"]]],
    [["food", 0],["body", 0],["population", 5],["traits", ["foraging", "cooperation"]]],
    [["food", 0],["body", 0],["population", 3],["traits", ["long-neck"]]]]],
["bag", 0],
["cards", [[-8, "carnivore"],
           [2, "foraging"],
           [0, "warning-call"]]]],

[["id", 2],
["species",
    [[["food", 0],["body", 3],["population", 1],["traits", []]],
    [["food", 0],["body", 3],["population", 1],["traits", ["climbing"]]]]],
["bag", 0],
["cards", [[3, "scavenger"],
           [0, "herding"]]]],

[["id", 3],
["species",
    [[["food", 1],["body", 3],["population", 1],["traits", ["herding"]]]]],
["bag", 0],
["cards", [[1, "long-neck"],
           [0, "fat-tissue"]]]]],
10,
[]],

[[0, [["population", 3, 2]], [], [[1]], []],
 [0, [], [["body", 0, 1]], [], []],
 [0, [], [], [], [[0, 0, 1]]]]
]


    self.case40_out = json.dumps([[[
["id", 1],
["species",
    [[["food", 2], ["body", 0], ["population", 5], ["traits", ["foraging", "cooperation"]]],
    [["food", 2], ["body", 0], ["population", 5], ["traits", ["foraging", "cooperation"]]],
    [["food", 2], ["body", 0], ["population", 3], ["traits", ["long-neck"]]],
    [["food", 0], ["body", 0], ["population", 2], ["traits", []]]]],
["bag", 0]],

[["id", 2],
["species",
    [[["food", 0], ["body", 4], ["population", 1], ["traits", []]],
    [["food", 0], ["body", 3], ["population", 1], ["traits", ["climbing"]]]]],
["bag", 0]],

[["id", 3],
["species",
    [[["food", 1], ["body", 3], ["population", 1], ["traits", ["fat-tissue"]]]]],
["bag", 0]]],

0,
[]]
)

    self.case41_in =   [[[[
["id",1],
["species", []],
["bag",0],
["cards", [[3, "horns"],
           [1, "ambush"],
           [2, "carnivore"],
           [0, "fat-tissue"],
           [3, "foraging"],
           [0, "herding"]]]],

[["id",2],
["species",
    [[["food",0],["body",3],["population",1],["traits",[]]],
    [["food",0],["body",3],["population",1],["traits",["climbing"]]]]],
["bag",0],
["cards", [[-7, "carnivore"],
            [3, "scavenger"],
            [2, "horns"],
            [0, "herding"]]]],

[["id",3],
["species",
    [[["food",1],["body",3],["population",1],["traits",["herding"]]]]],
["bag",0],
["cards", [[-6, "carnivore"],
            [1, "long-neck"],
            [0, "fat-tissue"]]]]],
0,
[]],

[[0, [], [], [[1, 2, 3, 4]], []],
 [0, [], [["body", 0, 1]], [], []],
 [0, [], [], [], [[0, 0, 1]]]]
]


    self.case41_out = json.dumps([[[
["id", 1],
["species",
    [[["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore", "fat-tissue", "foraging"]]]]],
["bag", 0],
["cards", [[0, "herding"]]]],

[["id", 2],
["species",
    [[["food", 0], ["body", 4], ["population", 1], ["traits", []]],
    [["food", 0], ["body", 3], ["population", 1], ["traits", ["climbing"]]]]],
["bag", 0],
["cards", [[2, "horns"],
          [0, "herding"]]]],

[["id", 3],
["species",
    [[["food", 1], ["body", 3], ["population", 1], ["traits", ["long-neck"]]]]],
["bag", 0],
["cards", [[0, "fat-tissue"]]]]],

0,
[]]
)

    self.case42_in =     [[[[
["id",1],
["species", []],
["bag",0],
["cards", [[3, "horns"],
           [1, "ambush"],
           [2, "carnivore"],
           [0, "fat-tissue"],
           [3, "foraging"],
           [0, "herding"]]]],

[["id",2],
["species",
    [[["food",0],["body",3],["population",1],["traits",[]]],
    [["food",0],["body",3],["population",1],["traits",["climbing"]]]]],
["bag",0],
["cards", [[-7, "carnivore"],
            [3, "scavenger"],
            [2, "horns"],
            [0, "herding"]]]],

[["id",3],
["species",
    [[["food",1],["body",3],["population",1],["traits",["herding"]]]]],
["bag",0],
["cards", [[-6, "carnivore"],
            [1, "long-neck"],
            [0, "fat-tissue"]]]]],

0,
[]],

[[0, [["population", 0, 1]], [["body", 0, 2]], [[4, 5]], [[0, 0, 3]]],
 [0, [], [["body", 0, 1]], [], []],
 [0, [], [], [], [[0, 0, 1]]]]
]


    self.case42_out = json.dumps([[[
["id", 1],
["species",
    [[["food", 0], ["body", 1], ["population", 2], ["traits", ["fat-tissue"]]]]],
["bag", 0]],

[["id", 2],
["species",
    [[["food", 0], ["body", 4], ["population", 1], ["traits", []]],
    [["food", 0], ["body", 3], ["population", 1], ["traits", ["climbing"]]]]],
["bag", 0],
["cards", [[2, "horns"],
          [0, "herding"]]]],

[["id", 3],
["species",
    [[["food", 1], ["body", 3], ["population", 1], ["traits", ["long-neck"]]]]],
["bag", 0],
["cards", [[0, "fat-tissue"]]]]],

0,
[]]
)


    self.case43_in =  [[[[
                          ["id", 1],
                          ["species",
                              [[["food", 0], ["body", 2], ["population", 2], ["traits",["fat-tissue"]], ["fat-food", 2]]]],
                          ["bag", 0],
                          ["cards", [[3, "horns"],
                                     [1, "ambush"],
                                     [2, "carnivore"],
                                     [0, "fat-tissue"],
                                     [3, "foraging"],
                                     [0, "herding"]]]],

                          [["id",2],
                          ["species",
                              [[["food",0],["body",3],["population",1],["traits",[]]],
                              [["food",0],["body",3],["population",1],["traits",["climbing"]]]]],
                          ["bag",0],
                          ["cards", [[-7, "carnivore"],
                                      [3, "scavenger"],
                                      [2, "horns"],
                                      [0, "herding"]]]],

                          [["id",3],
                          ["species",
                              [[["food",1],["body",3],["population",1],["traits",["herding"]]]]],
                          ["bag",0],
                          ["cards", [[-6, "carnivore"],
                                      [1, "long-neck"],
                                      [0, "fat-tissue"]]]]],

                          0,
                          []],

                          [[0, [], [], [], [[0, 0, 4]]],
                           [0, [], [["body", 0, 1]], [], []],
                           [0, [], [], [], [[0, 0, 1]]]]
                          ]


    self.case43_out = json.dumps([[[
["id", 1],
["species",
    [[["food", 0], ["body", 2], ["population", 2], ["traits", ["foraging"]]]]],
["bag", 0],
["cards", [[1, "ambush"],
          [2, "carnivore"],
          [0, "fat-tissue"],
          [0, "herding"]]]],

[["id", 2],
["species",
    [[["food", 0], ["body", 4], ["population", 1], ["traits", []]],
    [["food", 0], ["body", 3], ["population", 1], ["traits", ["climbing"]]]]],
["bag", 0],
["cards", [[2, "horns"],
          [0, "herding"]]]],

[["id", 3],
["species",
    [[["food", 1], ["body", 3], ["population", 1], ["traits", ["long-neck"]]]]],
["bag", 0],
["cards", [[0, "fat-tissue"]]]]],

0,
[]]
)

    self.case44_in = [[[[
["id", 1],
["species",
    [[["food", 0], ["body", 0], ["population", 5], ["traits", ["fertile", "long-neck"]]],
    [["food", 0], ["body", 2], ["population", 5], ["traits", ["fat-tissue"]], ["fat-food", 2]],
    [["food", 0], ["body", 0], ["population", 3], ["traits", ["long-neck"]]]]],
["bag", 0],
["cards", [[-8, "carnivore"],
           [2, "foraging"],
           [0, "warning-call"]]]],

[["id", 2],
["species",
    [[["food", 0], ["body", 3], ["population", 1], ["traits", []]],
    [["food", 0], ["body", 3], ["population", 1], ["traits", ["long-neck"]]]]],
["bag", 0],
["cards", [[3, "scavenger"],
           [0, "herding"]]]],

[["id", 3],
["species",
    [[["food", 1], ["body", 3], ["population", 1], ["traits", ["fertile", "long-neck"]]]]],
["bag", 0],
["cards", [[1, "long-neck"],
           [0, "fat-tissue"]]]]],
10,
[]],

[[0, [], [], [], []],
 [0, [], [], [], []],
 [0, [], [], [], []]]
]


    self.case44_out = json.dumps([[[
["id", 1],
["species",
    [[["food", 1], ["body", 0], ["population", 6], ["traits", ["fertile", "long-neck"]]],
    [["food", 2], ["body", 2], ["population", 5], ["traits", ["fat-tissue"]], ["fat-food", 2]],
    [["food", 1], ["body", 0], ["population", 3], ["traits", ["long-neck"]]]]],
["bag", 0],
["cards", [[2, "foraging"],
           [0, "warning-call"]]]],

[["id", 2],
["species",
    [[["food", 0], ["body", 3], ["population", 1], ["traits", []]],
    [["food", 1], ["body", 3], ["population", 1], ["traits", ["long-neck"]]]]],
["bag", 0],
["cards", [[0, "herding"]]]],

[["id", 3],
["species",
    [[["food", 2], ["body", 3], ["population", 2], ["traits", ["fertile", "long-neck"]]]]],
["bag", 0],
["cards", [[0, "fat-tissue"]]]]],

0,
[]]
)

    self.case45_in =   [
  [
    [
      [
        ["id",1],
        ["species",[
          [
            ["food",0],
            ["body",3],
            ["population",1],
            ["traits",[]]],
          [
            ["food",1],
            ["body",3],
            ["population",1],
            ["traits",[]]],
          [
            ["food",0],
            ["body",3],
            ["population",1],
            ["traits",["carnivore"]]]]],
        ["bag",0],
        ["cards", [[-4, "carnivore"]]]
      ],
      [
        ["id",2],
        ["species",[
          [
            ["food",0],
            ["body",3],
            ["population",1],
            ["traits",[]]],
          [
            ["food",0],
            ["body",3],
            ["population",1],
            ["traits",["climbing"]]]]],
        ["bag",0],
        ["cards", [[3, "warning-call"]]]
      ],
      [
        ["id",3],
        ["species",[
          [
            ["food",1],
            ["body",3],
            ["population",1],["traits",[]]]]],
        ["bag",0],
        ["cards", [[-1, "burrowing"]]]
      ]
    ],
    0,
    []
  ],
  [
    [0, [], [], [], []],
    [0, [], [], [], []],
    [0, [], [], [], []]
  ]
]


    self.case45_out = json.dumps([
  [
    [
      ["id",1],
      ["species",[
        [
          ["food",1],
          ["body",3],
          ["population",1],
          ["traits",[]]],
        [
          ["food",1],
          ["body",3],
          ["population",1],
          ["traits",[]]],
        [
          ["food",0],
          ["body",3],
          ["population",1],
          ["traits",["carnivore"]]]]],
      ["bag",0]
    ],
    [
      ["id",2],
      ["species",[
        [
          ["food",1],
          ["body",3],
          ["population",1],
          ["traits",[]]],
        [
          ["food",0],
          ["body",3],
          ["population",1],
          ["traits",["climbing"]]]]],
      ["bag",0]
    ],
    [
      ["id",3],
      ["species",[
        [
          ["food",1],
          ["body",3],
          ["population",1],["traits",[]]]]],
      ["bag",0]
    ]
  ],
  0,
  []
])


    self.case46_in = [
  [
    [
      [
        ["id",1],
        ["species",[
          [
            ["food",0],
            ["body",3],
            ["population",1],
            ["traits",[]]],
          [
            ["food",1],
            ["body",3],
            ["population",1],
            ["traits",[]]],
          [
            ["food",0],
            ["body",3],
            ["population",1],
            ["traits",["carnivore"]]]]],
        ["bag",0],
        ["cards", [[3, "warning-call"]]]
      ],
      [
        ["id",2],
        ["species",[
          [
            ["food",0],
            ["body",3],
            ["population",1],
            ["traits",[]]],
          [
            ["food",0],
            ["body",3],
            ["population",1],
            ["traits",["climbing"]]]]],
        ["bag",0],
        ["cards", [[-1, "burrowing"]]]
      ],
      [
        ["id",3],
        ["species",[
          [
            ["food",1],
            ["body",3],
            ["population",1],["traits",[]]]]],
        ["bag",0],
        ["cards", [[-4, "carnivore"]]]
      ]
    ],
    0,
    []
  ],
  [
    [0, [], [], [], []],
    [0, [], [], [], []],
    [0, [], [], [], []]
  ]
]


    self.case46_out = json.dumps([
  [
    [
      ["id",1],
      ["species",[
        [
          ["food",0],
          ["body",3],
          ["population",1],
          ["traits",[]]],
        [
          ["food",1],
          ["body",3],
          ["population",1],
          ["traits",[]]],
        [
          ["food",0],
          ["body",3],
          ["population",1],
          ["traits",["carnivore"]]]]],
      ["bag",0]
    ],
    [
      ["id",2],
      ["species",[
        [
          ["food",0],
          ["body",3],
          ["population",1],
          ["traits",[]]],
        [
          ["food",0],
          ["body",3],
          ["population",1],
          ["traits",["climbing"]]]]],
      ["bag",0]
    ],
    [
      ["id",3],
      ["species",[
        [
          ["food",1],
          ["body",3],
          ["population",1],["traits",[]]]]],
      ["bag",0]
    ]
  ],
  0,
  []
])
    self.case47_in = [
  [
    [
      [
        ["id",1],
        ["species",[
          [
            ["food",0],
            ["body",3],
            ["population",1],
            ["traits",[]]],
          [
            ["food",1],
            ["body",3],
            ["population",1],
            ["traits",[]]],
          [
            ["food",0],
            ["body",3],
            ["population",1],
            ["traits",["carnivore"]]]]],
        ["bag",0],
        ["cards", [[4, "carnivore"]]]
      ],
      [
        ["id",2],
        ["species",[
          [
            ["food",0],
            ["body",3],
            ["population",1],
            ["traits",[]]],
          [
            ["food",0],
            ["body",3],
            ["population",1],
            ["traits",["climbing"]]]]],
        ["bag",0],
        ["cards", [[3, "warning-call"]]]
      ],
      [
        ["id",3],
        ["species",[
          [
            ["food",1],
            ["body",3],
            ["population",1],["traits",[]]]]],
        ["bag",0],
        ["cards", [[2, "burrowing"]]]
      ]
    ],
    0,
    [[-3, "symbiosis"], [0, "pack-hunting"]]
  ],
  [
    [0, [], [], [], []],
    [0, [], [], [], []],
    [0, [], [], [], []]
  ]
]
    self.case47_out = json.dumps([
    [
      [
        ["id",1],
        ["species",[
          [
            ["food",1],
            ["body",3],
            ["population",1],
            ["traits",[]]],
          [
            ["food",1],
            ["body",3],
            ["population",1],
            ["traits",[]]],
          [
            ["food",1],
            ["body",3],
            ["population",1],
            ["traits",["carnivore"]]]]],
        ["bag",0]
      ],
      [
        ["id",2],
        ["species",[
          [
            ["food",1],
            ["body",3],
            ["population",1],
            ["traits",["climbing"]]]]],
        ["bag",0],
        ["cards", [[-3, "symbiosis"], [0, "pack-hunting"]]]
      ],
      [
        ["id",3],
        ["species",[
          [
            ["food",1],
            ["body",3],
            ["population",1],["traits",[]]]]],
        ["bag",0]
      ]
    ],
    5,
    []
])
    self.case48_in =  [
                        [
                          [
                            [
                              ["id",1],
                              ["species",[
                                [
                                  ["food",0],
                                  ["body",3],
                                  ["population",1],
                                  ["traits",[]]],
                                [
                                  ["food",0],
                                  ["body",3],
                                  ["population",1],
                                  ["traits",[]]]]],
                              ["bag",0],
                              ["cards", [[-1, "foraging"], [2, "fat-tissue"], [3, "pack-hunting"], [-7, "carnivore"]]]
                            ],
                            [
                              ["id",2],
                              ["species",[
                                [
                                  ["food",0],
                                  ["body",2],
                                  ["population",1],
                                  ["traits",[]]],
                                [
                                  ["food",0],
                                  ["body",3],
                                  ["population",3],
                                  ["traits",["climbing", "carnivore"]]]]],
                              ["bag",0],
                              ["cards", [[3, "warning-call"], [0, "horns"]]]
                            ],
                            [
                              ["id",3],
                              ["species",[
                                [
                                  ["food",0],
                                  ["body",3],
                                  ["population",2],
                                  ["traits",["herding"]]]]],
                              ["bag",0],
                              ["cards", [[-1, "burrowing"], [5, "carnivore"], [-2, "carnivore"]]]
                            ]
                          ],
                          0,
                          [[-3, "ambush"], [0, "fertile"]]
                        ],
                        [
                          [3, [], [["body", 2, 2]], [[0, 1]], []],
                          [0, [], [], [], [[1, 0, 1]]],
                          [1, [["population", 0, 0]], [], [], [[0, 0, 2]]]
                        ]
                      ]
    self.case48_out = json.dumps([
  [
    [
      ["id",1],
      ["species",[
        [
          ["food",1],
          ["body",3],
          ["population",1],
          ["traits",[]]],
        [
          ["food",1],
          ["body",3],
          ["population",1],
          ["traits",[]]],
        [
          ["food",1],
          ["body",1],
          ["population",1],
          ["traits",["fat-tissue"]],
          ["fat-food", 1]]
      ]],
      ["bag",0]
    ],
    [
      ["id",2],
      ["species",[
        [
          ["food",1],
          ["body",2],
          ["population",1],
          ["traits",[]]],
        [
          ["food",2],
          ["body",3],
          ["population",2],
          ["traits",["horns", "carnivore"]]]]],
      ["bag",0]
    ],
    [
      ["id",3],
      ["species",[]],
      ["bag",0],
      ["cards", [[-3, "ambush"], [0, "fertile"]]]
    ]
  ],
  0,
  []
])
    self.case49_in =  [
  [
    [
      [
        ["id",1],
        ["species",[
          [
            ["food",0],
            ["body",3],
            ["population",2],
            ["traits",["long-neck"]]],
          [
            ["food",0],
            ["body",3],
            ["population",3],
            ["traits",[]]]]],
        ["bag",0],
        ["cards", [[-1, "foraging"], [3, "fat-tissue"], [3, "pack-hunting"], [-7, "carnivore"],
          [-2, "hard-shell"]]]
      ],
      [
        ["id",2],
        ["species",[
          [
            ["food",0],
            ["body",2],
            ["population",1],
            ["traits",["symbiosis"]]],
          [
            ["food",0],
            ["body",3],
            ["population",3],
            ["traits",["climbing", "carnivore", "fat-tissue"]],
            ["fat-food", 3]
          ]]],
        ["bag",0],
        ["cards", [[3, "warning-call"], [3, "horns"], [0, "cooperation"]]]
      ],
      [
        ["id",3],
        ["species",[
          [
            ["food",0],
            ["body",3],
            ["population",2],
            ["traits",["herding", "fertile"]]]]],
        ["bag",0],
        ["cards", [[-1, "burrowing"], [7, "carnivore"], [-2, "carnivore"], [3, "scavenger"]]]
      ]
    ],
    0,
    [[-3, "ambush"],
      [0, "fertile"],
      [-6, "carnivore"],
      [0, "cooperation"],
      [2, "hard-shell"],
      [-3, "scavenger"],
      [1, "scavenger"]
    ]
  ],
  [
    [1, [["population", 2, 4]], [], [[2, 0, 3]], []],
    [1, [["population", 1, 2]], [], [], []],
    [1, [], [], [[0, 2]], [[0, 0, 3]]]
  ]
]
    self.case49_out = json.dumps([
  [
    [
      ["id",1],
      ["species",[
        [
          ["food",1],
          ["body",3],
          ["population",2],
          ["traits",["long-neck"]]],
        [
          ["food",1],
          ["body",3],
          ["population",1],
          ["traits",[]]],
        [
          ["food",0],
          ["body",0],
          ["population",2],
          ["traits",["foraging", "carnivore"]]]
      ]],
      ["bag",0]
    ],
    [
      ["id",2],
      ["species",[
        [
          ["food",1],
          ["body",2],
          ["population",1],
          ["traits",["symbiosis"]]],
        [
          ["food",4],
          ["body",3],
          ["population",4],
          ["traits",["climbing", "carnivore", "fat-tissue"]],
          ["fat-food", 3]
        ]]],
      ["bag",0],
      ["cards", [[3, "warning-call"]]]
    ],
    [
      ["id",3],
      ["species",[
        [
          ["food",3],
          ["body",3],
          ["population",3],
          ["traits",["scavenger", "fertile"]]],
        [
          ["food",1],
          ["body",0],
          ["population",1],
          ["traits",["carnivore"]]]
      ]],
      ["bag",0]
    ]
  ],
  0,
  [[-3, "ambush"],
    [0, "fertile"],
    [-6, "carnivore"],
    [0, "cooperation"],
    [2, "hard-shell"],
    [-3, "scavenger"],
    [1, "scavenger"]
  ]
])

    self.case50_in = [
  [
    [
      [
        ["id",1],
        ["species",[
          [
            ["food",0],
            ["body",3],
            ["population",2],
            ["traits",["long-neck"]]],
          [
            ["food",0],
            ["body",3],
            ["population",3],
            ["traits",["fertile"]]]]],
        ["bag",0],
        ["cards", [[3, "foraging"]]]
      ],
      [
        ["id",2],
        ["species",[
          [
            ["food",0],
            ["body",2],
            ["population",1],
            ["traits",["symbiosis"]]],
          [
            ["food",0],
            ["body",3],
            ["population",3],
            ["traits",["long-neck", "carnivore", "fat-tissue"]],
            ["fat-food", 3]]]],
        ["bag",0],
        ["cards", [[2, "warning-call"]]]
      ],
      [
        ["id",3],
        ["species",[
          [
            ["food",0],
            ["body",5],
            ["population",2],
            ["traits",["herding", "fertile", "fat-tissue"]],
            ["fat-food", 5]]]],
        ["bag",0],
        ["cards", [[-7, "carnivore"]]]
      ]
    ],
    0,
    [[-3, "ambush"],
      [0, "fertile"],
      [-6, "carnivore"],
      [0, "cooperation"],
      [2, "hard-shell"],
      [-3, "scavenger"],
      [1, "scavenger"]
    ]
  ],
  [
    [0, [], [], [], []],
    [0, [], [], [], []],
    [0, [], [], [], []]
  ]
]
    self.case50_out = json.dumps([
  [
    [
      ["id",1],
      ["species",[
        [
          ["food",0],
          ["body",3],
          ["population",2],
          ["traits",["long-neck"]]],
        [
          ["food",0],
          ["body",3],
          ["population",4],
          ["traits",["fertile"]]]]],
      ["bag",0]
    ],
    [
      ["id",2],
      ["species",[
        [
          ["food",0],
          ["body",2],
          ["population",1],
          ["traits",["symbiosis"]]],
        [
          ["food",3],
          ["body",3],
          ["population",3],
          ["traits",["long-neck", "carnivore", "fat-tissue"]]]]],
      ["bag",0]
    ],
    [
      ["id",3],
      ["species",[
        [
          ["food",3],
          ["body",5],
          ["population",3],
          ["traits",["herding", "fertile", "fat-tissue"]],
          ["fat-food", 2]]]],
      ["bag",0]
    ]
  ],
  0,
  [[-3, "ambush"],
    [0, "fertile"],
    [-6, "carnivore"],
    [0, "cooperation"],
    [2, "hard-shell"],
    [-3, "scavenger"],
    [1, "scavenger"]
  ]
])

    self.case51_in =  [
  [
    [
      [
        ["id",1],
        ["species",[
          [
            ["food",0],
            ["body",3],
            ["population",2],
            ["traits",["long-neck", "foraging", "cooperation"]]],
          [
            ["food",0],
            ["body",3],
            ["population",3],
            ["traits",["cooperation", "carnivore"]]],
          [
            ["food",0],
            ["body",2],
            ["population",1],
            ["traits",[]]],
          [
            ["food",0],
            ["body",2],
            ["population",2],
            ["traits",["fat-tissue", "carnivore"]],
            ["fat-food", 2]]
        ]],
        ["bag",0],
        ["cards", [[5, "carnivore"]]]
      ],
      [
        ["id",2],
        ["species",[
          [
            ["food",0],
            ["body",7],
            ["population",7],
            ["traits",["long-neck", "fertile", "fat-tissue"]],
            ["fat-food", 7]],
          [
            ["food",0],
            ["body",2],
            ["population",3],
            ["traits",["fertile"]]]]],
        ["bag",0],
        ["cards", [[6, "carnivore"]]]
      ],
      [
        ["id",3],
        ["species",[
          [
            ["food",0],
            ["body",5],
            ["population",2],
            ["traits",["herding", "carnivore"]]]]],
        ["bag",0],
        ["cards", [[7, "carnivore"]]]
      ]
    ],
    0,
    [[-3, "ambush"],
      [0, "fertile"],
      [-6, "carnivore"],
      [0, "cooperation"],
      [2, "hard-shell"],
      [-3, "scavenger"],
      [1, "scavenger"]
    ]
  ],
  [
    [0, [], [], [], []],
    [0, [], [], [], []],
    [0, [], [], [], []]
  ]
]
    self.case51_out = json.dumps([
  [
    [
      ["id",1],
      ["species",[
        [
          ["food",2],
          ["body",3],
          ["population",2],
          ["traits",["long-neck", "foraging", "cooperation"]]],
        [
          ["food",3],
          ["body",3],
          ["population",3],
          ["traits",["cooperation", "carnivore"]]],
        [
          ["food",1],
          ["body",2],
          ["population",1],
          ["traits",[]]],
        [
          ["food",2],
          ["body",2],
          ["population",2],
          ["traits",["fat-tissue", "carnivore"]],
          ["fat-food", 2]
        ]
      ]],
      ["bag",0]
    ],
    [
      ["id",2],
      ["species",[
        [
          ["food",4],
          ["body",7],
          ["population",4],
          ["traits",["long-neck", "fertile", "fat-tissue"]],
          ["fat-food", 7]],
        [
          ["food",1],
          ["body",2],
          ["population",4],
          ["traits",["fertile"]]]]],
      ["bag",0]
    ],
    [
      ["id",3],
      ["species",[
        [
          ["food",2],
          ["body",5],
          ["population",2],
          ["traits",["herding", "carnivore"]]]]],
      ["bag",0]
    ]
  ],
  0,
  [[-3, "ambush"],
    [0, "fertile"],
    [-6, "carnivore"],
    [0, "cooperation"],
    [2, "hard-shell"],
    [-3, "scavenger"],
    [1, "scavenger"]
  ]
])
    self.case52_in =   [
  [
    [
      [
        ["id",1],
        ["species",[
          [
            ["food",0],
            ["body",3],
            ["population",2],
            ["traits",["long-neck", "foraging", "cooperation"]]],
          [
            ["food",0],
            ["body",3],
            ["population",6],
            ["traits",["cooperation"]]],
          [
            ["food",0],
            ["body",2],
            ["population",2],
            ["traits",[]]],
          [
            ["food",0],
            ["body",2],
            ["population",2],
            ["traits",["fat-tissue"]],
            ["fat-food", 2]]
        ]],
        ["bag",0],
        ["cards", [[3, "foraging"]]]
      ],
      [
        ["id",2],
        ["species",[
          [
            ["food",0],
            ["body",7],
            ["population",7],
            ["traits",["long-neck", "cooperation", "fat-tissue"]],
            ["fat-food", 7]],
          [
            ["food",0],
            ["body",2],
            ["population",7],
            ["traits",["fertile"]]]]],
        ["bag",0],
        ["cards", [[2, "warning-call"]]]
      ],
      [
        ["id",3],
        ["species",[
          [
            ["food",0],
            ["body",5],
            ["population",2],
            ["traits",["herding", "fertile"]]]]],
        ["bag",0],
        ["cards", [[0, "carnivore"]]]
      ]
    ],
    0,
    [[-3, "ambush"],
      [0, "fertile"],
      [-6, "carnivore"],
      [0, "cooperation"],
      [2, "hard-shell"],
      [-3, "scavenger"],
      [1, "scavenger"]
    ]
  ],
  [
    [0, [], [], [], []],
    [0, [], [], [], []],
    [0, [], [], [], []]
  ]
]
    self.case52_out = json.dumps([
  [
    [
      ["id",1],
      ["species",[
        [
          ["food",2],
          ["body",3],
          ["population",2],
          ["traits",["long-neck", "foraging", "cooperation"]]],
        [
          ["food",2],
          ["body",3],
          ["population",6],
          ["traits",["cooperation"]]],
        [
          ["food",1],
          ["body",2],
          ["population",2],
          ["traits",[]]],
        [
          ["food",2],
          ["body",2],
          ["population",2],
          ["traits",["fat-tissue"]]]
      ]],
      ["bag",0]
    ],
    [
      ["id",2],
      ["species",[
        [
          ["food",7],
          ["body",7],
          ["population",7],
          ["traits",["long-neck", "cooperation", "fat-tissue"]]],
        [
          ["food",0],
          ["body",2],
          ["population",7],
          ["traits",["fertile"]]]]],
      ["bag",0]
    ],
    [
      ["id",3],
      ["species",[
        [
          ["food",0],
          ["body",5],
          ["population",3],
          ["traits",["herding", "fertile"]]]]],
      ["bag",0]
    ]
  ],
  0,
  [[-3, "ambush"],
    [0, "fertile"],
    [-6, "carnivore"],
    [0, "cooperation"],
    [2, "hard-shell"],
    [-3, "scavenger"],
    [1, "scavenger"]
  ]
])
    self.case53_in = [
  [
    [
      [
        ["id",1],
        ["species",
          [
            [["food",0],["body",3],["population",1],["traits",["carnivore"]]],
            [["food",1],["body",3],["population",1],["traits",[]]]
          ]
        ],
        ["bag",0],
        ["cards", [[3, "carnivore"], [3, "ambush"]]]
      ],
      [
        ["id",2],
        ["species",
          [
            [["food",0],["body",3],["population",1],["traits",["climbing"]]]
          ]
        ],
        ["bag",0],
        ["cards", [[2, "carnivore"], [2, "ambush"]]]
      ],
      [
        ["id",3],
        ["species",[]],
        ["bag",0],
        ["cards", [[1, "carnivore"]]]
      ]
    ],
    1,
    []
  ],
  [
    [0, [["population", 0, 1]], [], [], []],
    [0, [], [["body", 0, 1]], [], []],
    [0, [], [], [], []]
  ]
]

    self.case53_out = json.dumps([
  [
    [
      ["id",1],
      ["species",
        [
          [["food",0],["body",3],["population",2],["traits",["carnivore"]]],
          [["food",1],["body",3],["population",1],["traits",[]]]
        ]
      ],
      ["bag",0]
    ],
    [
      ["id",2],
      ["species",
        [
          [["food",1],["body",4],["population",1],["traits",["climbing"]]]
        ]
      ],
      ["bag",0]
    ],
    [
      ["id",3],
      ["species",[]],
      ["bag",0]
    ]
  ],
  6,
  []
]
)
    self.case54_in =  [
  [
    [
      [
        ["id",1],
        ["species",
          [
            [["food",0],["body",3],["population",1],["traits",["carnivore"]]],
            [["food",1],["body",3],["population",1],["traits",[]]]
          ]
        ],
        ["bag",0],
        ["cards", [[3, "carnivore"], [3, "ambush"], [2, "burrowing"]]]
      ],
      [
        ["id",2],
        ["species",
          [
            [["food",0],["body",3],["population",1],["traits",["climbing"]]]
          ]
        ],
        ["bag",0],
        ["cards", [[2, "carnivore"], [2, "ambush"]]]
      ],
      [
        ["id",3],
        ["species",[]],
        ["bag",0],
        ["cards", [[1, "carnivore"]]]
      ]
    ],
    1,
    []
  ],
  [
    [0, [], [], [[1],[2]], []],
    [0, [], [], [], []],
    [0, [], [], [], []]
  ]
]

    self.case54_out = json.dumps([
  [
    [
      ["id",1],
      ["species",
        [
          [["food",0],["body",3],["population",1],["traits",["carnivore"]]],
          [["food",1],["body",3],["population",1],["traits",[]]],
          [["food",1],["body",0],["population",1],["traits",[]]],
          [["food",1],["body",0],["population",1],["traits",[]]]
        ]
      ],
      ["bag",0]
    ],
    [
      ["id",2],
      ["species",
        [
          [["food",1],["body",3],["population",1],["traits",["climbing"]]]
        ]
      ],
      ["bag",0],
      ["cards",[[2,"ambush"]]]
    ],
    [
      ["id",3],
      ["species",[]],
      ["bag",0]
    ]
  ],
  4,
  []
]
)
    self.case55_in =  [
  [
    [
      [
        ["id",1],
        ["species",
          [
            [["food",0],["body",3],["population",1],["traits",["ambush"]]],
            [["food",1],["body",3],["population",1],["traits",[]]]
          ]
        ],
        ["bag",0],
        ["cards", [[3, "carnivore"], [4, "carnivore"]]]
      ],
      [
        ["id",2],
        ["species",
          [
            [["food",0],["body",3],["population",2],["traits",[]]]
          ]
        ],
        ["bag",0],
        ["cards", [[2, "carnivore"], [2, "ambush"]]]
      ],
      [
        ["id",3],
        ["species",[]],
        ["bag",0],
        ["cards", [[1, "carnivore"]]]
      ]
    ],
    1,
    []
  ],
  [
    [0, [], [], [], [[0,0,1]]],
    [0, [], [], [], []],
    [0, [], [], [], []]
  ]
]

    self.case55_out = json.dumps([
  [
    [
      ["id",1],
      ["species",
        [
          [["food",1],["body",3],["population",1],["traits",["carnivore"]]],
          [["food",1],["body",3],["population",1],["traits",[]]]
        ]
      ],
      ["bag",0]
    ],
    [
      ["id",2],
      ["species",
        [
          [["food",1],["body",3],["population",1],["traits",[]]]
        ]
      ],
      ["bag",0],
      ["cards",[[2,"ambush"]]]
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
)
    self.case56_in =  [
  [
    [
      [
        ["id",1],
        ["species",
          [
            [["food",0],["body",3],["population",1],["traits",["ambush"]]],
            [["food",1],["body",3],["population",1],["traits",[]]]
          ]
        ],
        ["bag",0],
        ["cards", [[3, "carnivore"], [4, "carnivore"]]]
      ],
      [
        ["id",2],
        ["species",
          [
            [["food",0],["body",3],["population",2],["traits",[]]]
          ]
        ],
        ["bag",0],
        ["cards", [[2, "carnivore"], [2, "ambush"]]]
      ],
      [
        ["id",3],
        ["species",[]],
        ["bag",0],
        ["cards", [[1, "carnivore"], [5, "carnivore"], [8, "carnivore"]]]
      ]
    ],
    1,
    []
  ],
  [
    [0, [], [], [], []],
    [1, [], [], [], []],
    [2, [], [], [], []]
  ]
]

    self.case56_out = json.dumps([
  [
    [
      ["id",1],
      ["species",
        [
          [["food",1],["body",3],["population",1],["traits",["ambush"]]],
          [["food",1],["body",3],["population",1],["traits",[]]]
        ]
      ],
      ["bag",0],
      ["cards", [[4, "carnivore"]]]
    ],
    [
      ["id",2],
      ["species",
        [
          [["food",2],["body",3],["population",2],["traits",[]]]
        ]
      ],
      ["bag",0],
      ["cards", [[2, "carnivore"]]]
    ],
    [
      ["id",3],
      ["species",[]],
      ["bag",0],
      ["cards", [[1, "carnivore"], [5, "carnivore"]]]
    ]
  ],
  11,
  []
]
)
    self.case57_in =   [
  [
    [
      [
        ["id", 1],
        ["species",[] ],
        ["bag", 0],
        ["cards",[[-7, "carnivore"]]]
      ],
      [
        ["id", 2],
        ["species",[]],
        ["bag", 0],
        ["cards",[[3, "carnivore"]]]
      ],
      [
        ["id", 3],
        ["species",[]],
        ["bag", 0],
        ["cards",[[-2, "fertile"]]]
      ]
    ],
    6,
    []
  ],
  [
    [0, [], [], [], []],
    [0, [], [], [], []],
    [0, [], [], [], []]
  ]
]

    self.case57_out = json.dumps([
  [
    [
      ["id", 1],
      ["species",[] ],
      ["bag", 0]
    ],
    [
      ["id", 2],
      ["species",[]],
      ["bag", 0]
    ],
    [
      ["id", 3],
      ["species",[]],
      ["bag", 0]
    ]
  ],
  1,
  []
])

    self.m1_in =  [[[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[3,"ambush"],[3,"burrowing"],[3,"carnivore"],[3,"climbing"]]]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[-3,"ambush"],[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[0,"ambush"],[0,"burrowing"],[0,"carnivore"],[0,"climbing"]]]]],0,[]],[[0,[],[],[],[]],[0,[],[],[],[]],[0,[],[],[],[]]]]
    self.m1_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[3,"burrowing"],[3,"carnivore"],[3,"climbing"]]]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[0,"burrowing"],[0,"carnivore"],[0,"climbing"]]]]],0,[]])
    self.m2_in =  [[[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[3,"ambush"],[3,"burrowing"],[3,"carnivore"],[3,"climbing"]]]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[-3,"ambush"],[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[0,"ambush"],[0,"burrowing"],[0,"carnivore"],[0,"climbing"]]]]],1,[]],[[0,[],[],[],[]],[0,[],[],[],[]],[0,[],[],[],[]]]]
    self.m2_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[3,"burrowing"],[3,"carnivore"],[3,"climbing"]]]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[0,"burrowing"],[0,"carnivore"],[0,"climbing"]]]]],1,[]])
    self.m3_in = [[[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[3,"ambush"],[3,"burrowing"],[3,"carnivore"],[3,"climbing"]]]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[-3,"ambush"],[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[1,"ambush"],[1,"burrowing"],[1,"carnivore"]]]]],1,[]],[[0,[],[],[],[]],[0,[],[],[],[]],[0,[],[],[],[]]]]
    self.m3_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[3,"burrowing"],[3,"carnivore"],[3,"climbing"]]]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[1,"burrowing"],[1,"carnivore"]]]]],2,[]])
    self.m4_in =  [[[[["id",1],["species",[[["food",1],["body",0],["population",1],["traits",[]]]]],["bag",0],["cards",[[3,"ambush"],[3,"burrowing"],[3,"carnivore"],[3,"climbing"]]]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[-3,"ambush"],[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[1,"ambush"],[1,"burrowing"],[1,"carnivore"]]]]],1,[[-2,"ambush"],[-2,"burrowing"],[-2,"carnivore"],[-2,"climbing"],[-2,"cooperation"],[-2,"fat-tissue"],[-2,"fertile"],[-2,"foraging"],[-2,"hard-shell"],[-2,"herding"],[-2,"horns"],[-2,"long-neck"],[-2,"pack-hunting"],[-2,"scavenger"],[-2,"symbiosis"],[-2,"warning-call"]]],[[0,[["population",0,1],["population",0,2]],[],[],[]],[0,[],[],[],[]],[0,[],[],[],[]]]]
    self.m4_out = json.dumps([[[["id",1],["species",[[["food",3],["body",0],["population",3],["traits",[]]]]],["bag",0],["cards",[[3,"climbing"]]]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[1,"burrowing"],[1,"carnivore"]]]]],0,[[-2,"ambush"],[-2,"burrowing"],[-2,"carnivore"],[-2,"climbing"],[-2,"cooperation"],[-2,"fat-tissue"],[-2,"fertile"],[-2,"foraging"],[-2,"hard-shell"],[-2,"herding"],[-2,"horns"],[-2,"long-neck"],[-2,"pack-hunting"],[-2,"scavenger"],[-2,"symbiosis"],[-2,"warning-call"]]])
    self.m5_in =  [[[[["id",1],["species",[[["food",1],["body",1],["population",1],["traits",[]]]]],["bag",0],["cards",[[3,"ambush"],[3,"burrowing"],[3,"carnivore"],[3,"climbing"]]]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[-3,"ambush"],[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[1,"ambush"],[1,"burrowing"],[1,"carnivore"]]]]],1,[[-2,"ambush"],[-2,"burrowing"],[-2,"carnivore"],[-2,"climbing"],[-2,"cooperation"],[-2,"fat-tissue"],[-2,"fertile"],[-2,"foraging"],[-2,"hard-shell"],[-2,"herding"],[-2,"horns"],[-2,"long-neck"],[-2,"pack-hunting"],[-2,"scavenger"],[-2,"symbiosis"],[-2,"warning-call"]]],[[0,[],[["body",0,1],["body",0,2]],[],[]],[0,[],[],[],[]],[0,[],[],[],[]]]]
    self.m5_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[3,"climbing"]]]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[1,"burrowing"],[1,"carnivore"]]]]],2,[[-2,"ambush"],[-2,"burrowing"],[-2,"carnivore"],[-2,"climbing"],[-2,"cooperation"],[-2,"fat-tissue"],[-2,"fertile"],[-2,"foraging"],[-2,"hard-shell"],[-2,"herding"],[-2,"horns"],[-2,"long-neck"],[-2,"pack-hunting"],[-2,"scavenger"],[-2,"symbiosis"],[-2,"warning-call"]]])
    self.m6_in =  [[[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[3,"ambush"],[3,"burrowing"],[3,"carnivore"],[3,"climbing"]]]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[-3,"ambush"],[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[1,"ambush"],[1,"burrowing"],[1,"carnivore"]]]]],1,[[-2,"ambush"],[-2,"burrowing"],[-2,"carnivore"],[-2,"climbing"],[-2,"cooperation"],[-2,"fat-tissue"],[-2,"fertile"],[-2,"foraging"],[-2,"hard-shell"],[-2,"herding"],[-2,"horns"],[-2,"long-neck"],[-2,"pack-hunting"],[-2,"scavenger"],[-2,"symbiosis"],[-2,"warning-call"]]],[[0,[],[],[[1,2,3]],[]],[0,[],[],[],[]],[0,[],[],[],[]]]]
    self.m6_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",[]]],[["food",1],["body",0],["population",1],["traits",["carnivore","climbing"]]]]],["bag",0]],[["id",2],["species",[]],["bag",0],["cards",[[-2,"ambush"],[-2,"burrowing"],[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[1,"burrowing"],[1,"carnivore"]]]]],1,[[-2,"carnivore"],[-2,"climbing"],[-2,"cooperation"],[-2,"fat-tissue"],[-2,"fertile"],[-2,"foraging"],[-2,"hard-shell"],[-2,"herding"],[-2,"horns"],[-2,"long-neck"],[-2,"pack-hunting"],[-2,"scavenger"],[-2,"symbiosis"],[-2,"warning-call"]]])
    self.m7_in =  [[[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0],["cards",[[3,"ambush"],[3,"burrowing"],[3,"carnivore"],[3,"climbing"]]]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[-3,"ambush"],[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[1,"ambush"],[1,"burrowing"],[1,"carnivore"]]]]],1,[[-2,"ambush"],[-2,"burrowing"],[-2,"carnivore"],[-2,"climbing"],[-2,"cooperation"],[-2,"fat-tissue"],[-2,"fertile"],[-2,"foraging"],[-2,"hard-shell"],[-2,"herding"],[-2,"horns"],[-2,"long-neck"],[-2,"pack-hunting"],[-2,"scavenger"],[-2,"symbiosis"],[-2,"warning-call"]]],[[0,[],[],[],[[0,0,1]]],[0,[],[],[],[]],[0,[],[],[],[]]]]
    self.m7_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",["burrowing"]]]]],["bag",0],["cards",[[3,"carnivore"],[3,"climbing"]]]],[["id",2],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0],["cards",[[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[1,"burrowing"],[1,"carnivore"]]]]],2,[[-2,"ambush"],[-2,"burrowing"],[-2,"carnivore"],[-2,"climbing"],[-2,"cooperation"],[-2,"fat-tissue"],[-2,"fertile"],[-2,"foraging"],[-2,"hard-shell"],[-2,"herding"],[-2,"horns"],[-2,"long-neck"],[-2,"pack-hunting"],[-2,"scavenger"],[-2,"symbiosis"],[-2,"warning-call"]]])
    self.m8_in =  [[[[["id",1],
                        ["species",[[["food",0],["body",3],["population",1],["traits",["ambush","climbing"]]]]],
                        ["bag",0],
                        ["cards",[[3,"ambush"],[3,"burrowing"],[3,"carnivore"],[3,"climbing"]]]],
                      [["id",2],
                        ["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],
                        ["bag",0],
                        ["cards",[[-3,"ambush"],[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],
                      [["id",3],
                        ["species",[]],
                        ["bag",0],
                        ["cards",[[1,"ambush"],[1,"burrowing"],[1,"carnivore"]]]]],
                      1,
                      [[-2,"ambush"],[-2,"burrowing"],[-2,"carnivore"],[-2,"climbing"],[-2,"cooperation"],[-2,"fat-tissue"],[-2,"fertile"],[-2,"foraging"],[-2,"hard-shell"],[-2,"herding"],[-2,"horns"],[-2,"long-neck"],[-2,"pack-hunting"],[-2,"scavenger"],[-2,"symbiosis"],[-2,"warning-call"]]],
                  [[0,[],[],[],[[0,1,2]]],
                    [0,[],[],[],[]],
                    [0,[],[],[],[]]]]
    self.m8_out = json.dumps([[[["id",1],["species",[[["food",1],["body",3],["population",1],["traits",["carnivore","ambush"]]]]],["bag",0],["cards",[[3,"burrowing"],[3,"climbing"]]]],[["id",2],["species",[]],["bag",0],["cards",[[-2,"ambush"],[-2,"burrowing"],[-3,"burrowing"],[-3,"carnivore"],[-3,"climbing"]]]],[["id",3],["species",[]],["bag",0],["cards",[[1,"burrowing"],[1,"carnivore"]]]]],1,[[-2,"carnivore"],[-2,"climbing"],[-2,"cooperation"],[-2,"fat-tissue"],[-2,"fertile"],[-2,"foraging"],[-2,"hard-shell"],[-2,"herding"],[-2,"horns"],[-2,"long-neck"],[-2,"pack-hunting"],[-2,"scavenger"],[-2,"symbiosis"],[-2,"warning-call"]]])



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

  def test_case1(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case1_in), self.case1_out)

  def test_case2(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case2_in), self.case2_out)

  def test_case3(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case3_in), self.case3_out)

  def test_case4(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case4_in), self.case4_out)

  def test_case5(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case5_in), self.case5_out)

  def test_case6(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case6_in), self.case6_out)

  def test_case7(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case7_in), self.case7_out)

  def test_case8(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case8_in), self.case8_out)

  def test_case9(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case9_in), self.case9_out)

  def test_case10(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case10_in), self.case10_out)

  def test_case11(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case11_in), self.case11_out)

  def test_case12(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case12_in), self.case12_out)

  def test_case13(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case13_in), self.case13_out)

  def test_case14(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case14_in), self.case14_out)

  def test_case15(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case15_in), self.case15_out)

  def test_case16(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case16_in), self.case16_out)

  def test_case17(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case17_in), self.case17_out)

  def test_case18(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case18_in), self.case18_out)

  def test_case19(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case19_in), self.case19_out)

  def test_case20(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case20_in), self.case20_out)

  def test_case21(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case21_in), self.case21_out)

  def test_case22(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case22_in), self.case22_out)

  def test_case23(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case23_in), self.case23_out)

  def test_case24(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case24_in), self.case24_out)

  def test_case25(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case25_in), self.case25_out)

  def test_case26(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case26_in), self.case26_out)

  def test_case27(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case27_in), self.case27_out)

  def test_case28(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case28_in), self.case28_out)

  def test_case29(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case29_in), self.case29_out)

  def test_case30(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case30_in), self.case30_out)

  def test_case31(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case31_in), self.case31_out)

  def test_case32(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case32_in), self.case32_out)

  def test_case34(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case34_in), self.case34_out)

  def test_case35(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case35_in), self.case35_out)

  def test_case36(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case36_in), self.case36_out)

  def test_case37(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case37_in), self.case37_out)

  def test_case38(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case38_in), self.case38_out)

  def test_case39(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case39_in), self.case39_out)

  def test_case40(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case40_in), self.case40_out)

  def test_case41(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case41_in), self.case41_out)

  def test_case42(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case42_in), self.case42_out)

  def test_case43(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case43_in), self.case43_out)

  def test_case44(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case44_in), self.case44_out)

  def test_case45(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case45_in), self.case45_out)

  def test_case46(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case46_in), self.case46_out)

  def test_case47(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case47_in), self.case47_out)

  def test_case48(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case48_in), self.case48_out)

  def test_case49(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case49_in), self.case49_out)

  def test_case50(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case50_in), self.case50_out)

  def test_case51(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case51_in), self.case51_out)

  def test_case52(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case52_in), self.case52_out)

  def test_case53(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case53_in), self.case53_out)

  def test_case54(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case54_in), self.case54_out)

  def test_case55(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case55_in), self.case55_out)

  def test_case56(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case56_in), self.case56_out)

  def test_case57(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.case57_in), self.case57_out)

  def test_m1(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.m1_in), self.m1_out)

  def test_m2(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.m2_in), self.m2_out)

  def test_m3(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.m3_in), self.m3_out)

  def test_m4(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.m4_in), self.m4_out)

  def test_m5(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.m5_in), self.m5_out)

  def test_m6(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.m6_in), self.m6_out)

  def test_m7(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.m7_in), self.m7_out)

  def test_m8(self):
    self.assertEqual(xstep4_testing.executeXstep4(self.m8_in), self.m8_out)

if __name__ == '__main__':
  unittest.main()
