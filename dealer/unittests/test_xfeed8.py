# Automated unit tests for the feed test harness for Evolution game
import unittest
import os, sys
import json
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../executables'))
import xfeed
import species
import trait

class TestXFeedClassTests(unittest.TestCase):
  def setUp(self):
    self.tester_xfeed = xfeed.TestHarness()
    self.case1_in =[
                      [["id",1],
                      ["species",[]],
                      ["bag",0]],
                      1,
                      []
                    ]
    self.case1_out = 'null'

    self.case2_in = [
                      [["id",1],
                      ["species",[
                        [["food",2],
                         ["body",2],
                         ["population",2],
                         ["traits",["carnivore"]]]
                      ]],
                      ["bag",0]],
                      1,
                      [
                        [["id",2],
                         ["species",[]],
                         ["bag",0]],
                        [["id",3],
                         ["species",[]],
                         ["bag",0]]
                      ]
                    ]
    self.case2_out = 'null'

    self.case3_in = [
                      [["id",1],
                      ["species",[
                        [["food",2],
                         ["body",2],
                         ["population",2],
                         ["traits",["carnivore"]]],
                        [["food",1],
                         ["body",2],
                         ["population",2],
                         ["traits",[]]],
                        [["food",2],
                         ["body",2],
                         ["population",2],
                         ["traits",["fat-tissue"]],
                          ["fat-food", 0]
                        ]
                      ]],
                      ["bag",3]],
                      2,
                      [
                        [["id",2],
                         ["species",[]],
                         ["bag",0]],
                        [["id",3],
                         ["species",[[["food",2],
                         ["body",2],
                         ["population",2],
                         ["traits",["fat-tissue"]],
                          ["fat-food", 0]
                        ]]],
                         ["bag",0]]
                      ]
                    ]
    self.case3_out = '[2, 2]'

    self.case4_in = [
                      [["id",1],
                      ["species",[
                        [["food",2],
                         ["body",5],
                         ["population",2],
                         ["traits",["carnivore"]]],
                        [["food",1],
                         ["body",4],
                         ["population",2],
                         ["traits",[]]],
                        [["food",1],
                         ["body",2],
                         ["population",3],
                         ["traits",["fat-tissue"]],
                          ["fat-food", 2]
                        ]
                      ]],
                      ["bag",3]],
                      1,
                      [
                        [["id",2],
                         ["species",[]],
                         ["bag",0]],
                        [["id",3],
                         ["species",[]],
                         ["bag",0]]
                      ]
                    ]
    self.case4_out = '2'

    self.case5_in = [
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
                                              2
                                         ],
                                         [
                                              "traits",
                                              []
                                         ]
                                    ],
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
                                              2
                                         ],
                                         [
                                              "traits",
                                              [
                                                   "fat-tissue"
                                              ]
                                         ],
                                         [
                                              "fat-food",
                                              1
                                         ]
                                    ],
                                    [
                                         [
                                              "food",
                                              2
                                         ],
                                         [
                                              "body",
                                              0
                                         ],
                                         [
                                              "population",
                                              2
                                         ],
                                         [
                                              "traits",
                                              [
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
                     ],
                     1,
                     [
                          [
                               [
                                    "id",
                                    2
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
                                                   []
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
                                    3
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
                                                   []
                                              ]
                                         ]
                                    ]
                               ],
                               [
                                    "bag",
                                    0
                               ]
                          ]
                     ]
                ]
    self.case5_out = '0'

    self.case6_in = [
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
                                                   "carnivore"
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
                                                   "carnivore"
                                              ]
                                         ]
                                    ],
                                    [
                                         [
                                              "food",
                                              2
                                         ],
                                         [
                                              "body",
                                              0
                                         ],
                                         [
                                              "population",
                                              2
                                         ],
                                         [
                                              "traits",
                                              [
                                                   "carnivore"
                                              ]
                                         ]
                                    ],
                                    [
                                         [
                                              "food",
                                              3
                                         ],
                                         [
                                              "body",
                                              0
                                         ],
                                         [
                                              "population",
                                              3
                                         ],
                                         [
                                              "traits",
                                              []
                                         ]
                                    ]
                               ]
                          ],
                          [
                               "bag",
                               0
                          ]
                     ],
                     4,
                     [
                          [
                               [
                                    "id",
                                    2
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
                                                   1
                                              ],
                                              [
                                                   "population",
                                                   2
                                              ],
                                              [
                                                   "traits",
                                                   []
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
                                                   2
                                              ],
                                              [
                                                   "traits",
                                                   []
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
                                    4
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
                                                   []
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
                                                        "warning-call",
                                                        "hard-shell"
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
                                    3
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
                                                   2
                                              ],
                                              [
                                                   "traits",
                                                   []
                                              ]
                                         ],
                                         [
                                              [
                                                   "food",
                                                   0
                                              ],
                                              [
                                                   "body",
                                                   1
                                              ],
                                              [
                                                   "population",
                                                   2
                                              ],
                                              [
                                                   "traits",
                                                   [
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
                     ]
                ]
    self.case6_out = '[0, 0, 0]'

    self.case7_in = [
                      [
                        ["id", 1],
                        ["species", [
                          [
                            ["food", 2],
                            ["body", 2],
                            ["population", 5],
                            ["traits", ["fat-tissue", "horns"]],
                            ["fat-food", 0]
                          ],
                    [
                            ["food", 2],
                            ["body", 5],
                            ["population", 2],
                            ["traits", ["ambush", "fat-tissue", "warning-call"]],
                            ["fat-food", 0]
                          ],
                    [
                            ["food", 0],
                            ["body", 2],
                            ["population", 4],
                            ["traits", ["carnivore"]]
                          ]
                        ]
                    ],
                        ["bag", 3]
                      ],
                      3, [
                        [
                          ["id", 2],
                          ["species", [
                            [
                              ["food", 0],
                              ["body", 2],
                              ["population", 3],
                              ["traits", ["warning-call", "horns"]]
                            ],
                            [
                              ["food", 4],
                              ["body", 2],
                              ["population", 4],
                              ["traits", ["carnivore"]]
                            ]
                          ]],
                          ["bag", 3]
                        ]
                      ]
                    ]
    self.case7_out = '[1, 3]'

    self.case8_in = [
                      [
                        ["id", 1],
                        ["species", [
                          [
                            ["food", 5],
                            ["body", 2],
                            ["population", 5],
                            ["traits", ["horns"]]
                          ],
                    [
                            ["food", 0],
                            ["body", 2],
                            ["population", 4],
                            ["traits", ["carnivore"]]
                          ]
                        ]
                    ],
                        ["bag", 3]
                      ],
                      5, [
                        [
                          ["id", 2],
                          ["species", [
                            [
                              ["food", 3],
                              ["body", 2],
                              ["population", 3],
                              ["traits", ["burrowing", "horns"]]
                            ]
                          ]],
                          ["bag", 3]
                        ]
                      ]
                    ]
    self.case8_out = 'false'

    self.case9_in = [
                      [
                        ["id", 1],
                        ["species", [
                          [
                            ["food", 1],
                            ["body", 2],
                            ["population", 3],
                            ["traits", ["carnivore", "horns"]]
                          ],
                    [
                            ["food", 0],
                            ["body", 2],
                            ["population", 4],
                            ["traits", ["carnivore", "ambush"]]
                          ]
                        ]
                    ],
                        ["bag", 1]
                      ],
                      5, [
                        [
                          ["id", 2],
                          ["species", [
                            [
                              ["food", 3],
                              ["body", 2],
                              ["population", 7],
                              ["traits", ["climbing", "ambush"]]
                            ],
                    [
                              ["food", 3],
                              ["body", 2],
                              ["population", 3],
                              ["traits", ["fertile", "carnivore"]]
                            ]
                          ]],
                          ["bag", 6]
                        ],
                    [
                          ["id", 3],
                          ["species", [
                            [
                              ["food", 0],
                              ["body", 2],
                              ["population", 3],
                              ["traits", ["burrowing", "horns"]]
                            ],
                    [
                              ["food", 3],
                              ["body", 2],
                              ["population", 5],
                              ["traits", ["pack-hunting", "long-neck"]]
                            ]
                          ]],
                          ["bag", 3]
                        ],
                    [
                          ["id", 4],
                          ["species", [
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 7],
                              ["traits", ["burrowing", "foraging"]]
                            ],
                    [
                              ["food", 3],
                              ["body", 2],
                              ["population", 3],
                              ["traits", ["warning-call", "hard-shell"]]
                            ]
                          ]],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case9_out = '[1, 2, 0]'

    self.case10_in = [
                      [
                        ["id", 1],
                        ["species", [
                          [
                            ["food", 1],
                            ["body", 2],
                            ["population", 3],
                            ["traits", ["carnivore", "horns"]]
                          ],
                    [
                            ["food", 0],
                            ["body", 2],
                            ["population", 4],
                            ["traits", ["ambush"]]
                          ]
                        ]
                    ],
                        ["bag", 1]
                      ],
                      5, [
                        [
                          ["id", 2],
                          ["species", [
                            [
                              ["food", 3],
                              ["body", 2],
                              ["population", 7],
                              ["traits", ["climbing", "ambush"]]
                            ],
                    [
                              ["food", 3],
                              ["body", 2],
                              ["population", 3],
                              ["traits", ["fertile", "carnivore"]]
                            ]
                          ]],
                          ["bag", 6]
                        ]
                      ]
                    ]
    self.case10_out = '1'

    self.case11_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 0],
                              ["body", 0],
                              ["population", 1],
                              ["traits",[]]
                            ],
                            [
                              ["food", 0],
                              ["body", 0],
                              ["population", 1],
                              ["traits",[]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case11_out = '0'

    self.case12_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 0],
                              ["body", 0],
                              ["population", 1],
                              ["traits",[]]
                            ],
                            [
                              ["food", 2],
                              ["body", 1],
                              ["population", 2],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 0]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case12_out = '[1, 1]'

    self.case13_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 7],
                              ["body", 7],
                              ["population", 7],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 7]
                            ],
                            [
                              ["food", 2],
                              ["body", 2],
                              ["population", 2],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 0]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case13_out = '[1, 2]'

    self.case14_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 2],
                              ["body", 5],
                              ["population", 2],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 3]
                            ],
                            [
                              ["food", 2],
                              ["body", 2],
                              ["population", 2],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 0]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case14_out = '[0, 2]'

    self.case15_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 2],
                              ["body", 5],
                              ["population", 3],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 3]
                            ],
                            [
                              ["food", 3],
                              ["body", 2],
                              ["population", 3],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 0]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case15_out = '[1, 2]'

    self.case16_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 2],
                              ["body", 5],
                              ["population", 3],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 3]
                            ],
                            [
                              ["food", 3],
                              ["body", 5],
                              ["population", 3],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 3]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case16_out = '[1, 2]'

    self.case17_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 2],
                              ["body", 5],
                              ["population", 2],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 3]
                            ],
                            [
                              ["food", 2],
                              ["body", 7],
                              ["population", 7],
                              ["traits",[]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case17_out = '[0, 2]'

    self.case18_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 2],
                              ["body", 5],
                              ["population", 2],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 3]
                            ],
                            [
                              ["food", 2],
                              ["body", 5],
                              ["population", 3],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 3]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case18_out = '[1, 2]'

    self.case19_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 7],
                              ["body", 7],
                              ["population", 7],
                              ["traits",[]]
                            ],
                            [
                              ["food", 1],
                              ["body", 0],
                              ["population", 7],
                              ["traits",[]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case19_out = '1'

    self.case20_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 2],
                              ["body", 2],
                              ["population", 6],
                              ["traits",[]]
                            ],
                            [
                              ["food", 1],
                              ["body", 0],
                              ["population", 7],
                              ["traits",[]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case20_out = '1'

    self.case21_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 2],
                              ["body", 2],
                              ["population", 6],
                              ["traits",[]]
                            ],
                            [
                              ["food", 1],
                              ["body", 3],
                              ["population", 6],
                              ["traits",[]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case21_out = '0'

    self.case22_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 2],
                              ["body", 2],
                              ["population", 6],
                              ["traits",[]]
                            ],
                            [
                              ["food", 2],
                              ["body", 3],
                              ["population", 6],
                              ["traits",[]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case22_out = '1'

    self.case23_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 2],
                              ["body", 2],
                              ["population", 6],
                              ["traits",[]]
                            ],
                            [
                              ["food", 6],
                              ["body", 2],
                              ["population", 6],
                              ["traits",[]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case23_out = '0'

    self.case24_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 1],
                              ["body", 1],
                              ["population", 1],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 0]
                            ],
                            [
                              ["food", 6],
                              ["body", 7],
                              ["population", 7],
                              ["traits",["carnivore"]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case24_out = '[0, 1]'

    self.case25_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 1],
                              ["body", 0],
                              ["population", 1],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 0]
                            ],
                            [
                              ["food", 6],
                              ["body", 7],
                              ["population", 7],
                              ["traits",["carnivore"]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case25_out = '[1, 0, 0]'

    self.case26_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 0],
                              ["body", 1],
                              ["population", 1],
                              ["traits",["fat-tissue", "carnivore"]],
                              ["fat-food", 0]
                            ],
                            [
                              ["food", 6],
                              ["body", 7],
                              ["population", 7],
                              ["traits",["carnivore"]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case26_out = '[0, 1]'

    self.case27_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 2],
                              ["body", 7],
                              ["population", 3],
                              ["traits",["carnivore"]]
                            ],
                            [
                              ["food", 1],
                              ["body", 1],
                              ["population", 7],
                              ["traits",["carnivore"]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case27_out = '[1, 0, 0]'

    self.case28_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits",["carnivore"]]
                            ],
                            [
                              ["food", 2],
                              ["body", 1],
                              ["population", 3],
                              ["traits",["carnivore"]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case28_out = '[1, 0, 0]'

    self.case29_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 1],
                              ["body", 1],
                              ["population", 3],
                              ["traits",["carnivore"]]
                            ],
                            [
                              ["food", 2],
                              ["body", 1],
                              ["population", 3],
                              ["traits",["carnivore"]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case29_out = '[1, 0, 0]'

    self.case30_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 1],
                              ["body", 1],
                              ["population", 3],
                              ["traits",["carnivore"]]
                            ],
                            [
                              ["food", 2],
                              ["body", 1],
                              ["population", 3],
                              ["traits",["carnivore"]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 1],
                                ["body", 1],
                                ["population", 1],
                                ["traits",["burrowing"]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case30_out = 'false'

    self.case31_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 1],
                              ["body", 7],
                              ["population", 2],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 0]
                            ],
                            [
                              ["food", 2],
                              ["body", 2],
                              ["population", 2],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 0]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 0],
                                ["body", 0],
                                ["population", 1],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case31_out = '[0, 7]'

    self.case32_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 2],
                              ["body", 3],
                              ["population", 3],
                              ["traits",["carnivore"]]
                            ],
                            [
                              ["food", 2],
                              ["body", 3],
                              ["population", 3],
                              ["traits",["carnivore","pack-hunting","ambush"]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 2],
                                ["body", 3],
                                ["population", 2],
                                ["traits",["hard-shell"]]
                              ],
                              [
                                ["food", 2],
                                ["body", 3],
                                ["population", 2],
                                ["traits",["hard-shell", "warning-call", "climbing"]]
                              ],
                              [
                                ["food", 2],
                                ["body", 3],
                                ["population", 2],
                                ["traits",["hard-shell"]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case32_out = 'false'

    self.case33_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 2],
                              ["body", 3],
                              ["population", 3],
                              ["traits",["carnivore"]]
                            ],
                            [
                              ["food", 2],
                              ["body", 3],
                              ["population", 3],
                              ["traits",["carnivore","pack-hunting","ambush"]]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                            [
                              [
                                ["food", 2],
                                ["body", 3],
                                ["population", 2],
                                ["traits",["hard-shell"]]
                              ],
                              [
                                ["food", 2],
                                ["body", 3],
                                ["population", 2],
                                ["traits",["hard-shell", "warning-call", "climbing"]]
                              ],
                              [
                                ["food", 2],
                                ["body", 3],
                                ["population", 2],
                                ["traits",["hard-shell"]]
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
                                ["population", 2],
                                ["traits",["hard-shell"]]
                              ],
                              [
                                ["food", 2],
                                ["body", 3],
                                ["population", 2],
                                ["traits",["hard-shell", "warning-call", "climbing"]]
                              ],
                              [
                                ["food", 2],
                                ["body", 3],
                                ["population", 2],
                                ["traits",[]]
                              ]
                            ]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case33_out = '[1, 1, 2]'

    self.case34_in = [
                      [
                        ["id", 2],
                        ["species",
                          [[
                            ["food", 1],
                            ["body", 1],
                            ["population", 5],
                            ["traits", ["carnivore", "climbing"]]
                          ],
                          [
                            ["food", 3],
                            ["body", 1],
                            ["population", 3],
                            ["traits", ["foraging"]]
                          ]
                        ]],
                        ["bag", 1]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species",
                          [
                            [
                              ["food", 1],
                              ["body", 1],
                              ["population", 5],
                              ["traits", ["climbing"]]
                          ]]],
                          ["bag", 0]]
                      ]
                    ]
    self.case34_out = '[0, 0, 0]'

    self.case34_in = [
                      [
                        ["id", 2],
                        ["species",
                          [[
                            ["food", 1],
                            ["body", 1],
                            ["population", 5],
                            ["traits", ["burrowing"]]
                          ],
                          [
                            ["food", 1],
                            ["body", 1],
                            ["population", 3],
                            ["traits", ["foraging"]]
                          ],
                          [
                            ["food", 2],
                            ["body", 3],
                            ["population", 7],
                            ["traits", ["fat-tissue"]],
                            ["fat-food", 1]
                          ]
                        ]],
                        ["bag", 1]
                      ],
                      10,
                      [
                        [["id", 1],
                          ["species", []],
                          ["bag", 0]]
                      ]
                    ]
    self.case34_out = '[2, 2]'

    self.case35_in = [
                      [
                        ["id", 1],
                        ["species", [
                          [
                            ["food", 2],
                            ["body", 2],
                            ["population", 3],
                            ["traits", ["carnivore"]]
                          ]]
                        ],
                        ["bag", 1]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species", [
                            [
                              ["food", 2],
                              ["body", 3],
                              ["population", 4],
                              ["traits", ["climbing", "burrowing"]]
                          ]]
                        ],
                          ["bag", 2]
                        ],
                        [
                          ["id", 3],
                          ["species", [
                            [
                              ["food", 2],
                              ["body", 2],
                              ["population", 2],
                              ["traits", ["climbing", "burrowing"]]
                            ]]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case35_out = 'false'

    self.case36_in = [
                      [
                        ["id", 1],
                        ["species", [
                          [
                            ["food", 2],
                            ["body", 2],
                            ["population", 3],
                            ["traits", []]
                          ],
                          [
                            ["food", 2],
                            ["body", 2],
                            ["population", 5],
                            ["traits", []]
                          ]
                          ]
                        ],
                        ["bag", 1]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species", [
                            [
                              ["food", 2],
                              ["body", 3],
                              ["population", 4],
                              ["traits", ["climbing", "burrowing"]]
                          ]]
                        ],
                          ["bag", 2]
                        ],
                        [
                          ["id", 3],
                          ["species", [
                            [
                              ["food", 2],
                              ["body", 2],
                              ["population", 2],
                              ["traits", ["climbing", "burrowing"]]
                            ]]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case36_out = '1'

    self.case37_in = [
                      [
                        ["id", 1],
                        ["species", [
                          [
                            ["food", 2],
                            ["body", 2],
                            ["population", 3],
                            ["traits", ["fat-tissue"]]
                          ],
                          [
                            ["food", 2],
                            ["body", 2],
                            ["population", 5],
                            ["traits", []]
                          ]
                          ]
                        ],
                        ["bag", 1]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species", [
                            [
                              ["food", 2],
                              ["body", 3],
                              ["population", 4],
                              ["traits", ["climbing", "carnivore"]]
                          ]]
                        ],
                          ["bag", 2]
                        ],
                        [
                          ["id", 3],
                          ["species", [
                            [
                              ["food", 2],
                              ["body", 2],
                              ["population", 2],
                              ["traits", ["climbing", "burrowing"]]
                            ]]
                          ],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case37_out = '[0, 2]'

    self.case38_in = [
                      [
                        ["id",1],
                        ["species",[
                          [
                            ["food",3],
                            ["body",3],
                            ["population",3],
                            ["traits",["fat-tissue", "carnivore"]],
                            ["fat-food", 3]
                          ]
                        ]],
                        ["bag",0]
                      ],
                      1,
                      []
                    ]
    self.case38_out = 'null'

    self.case39_in = [
                      [
                        ["id",1],
                        ["species",[
                          [
                            ["food",3],
                            ["body",3],
                            ["population",3],
                            ["traits",["fat-tissue", "carnivore"]],
                            ["fat-food", 3]
                          ]
                        ]],
                        ["bag",0]
                      ],
                      1,
                      []
                    ]
    self.case39_out = 'null'

    self.case40_in = [
                      [
                        ["id",1],
                        ["species",[
                          [
                            ["food",3],
                            ["body",3],
                            ["population",3],
                            ["traits",["fat-tissue", "carnivore"]],
                            ["fat-food", 3]
                          ]
                        ]],
                        ["bag",0]
                      ],
                      1,
                      []
                    ]
    self.case40_out = 'null'

    self.case41_in = [
                      [
                        ["id",1],
                        ["species",[
                          [
                            ["food",0],
                            ["body",3],
                            ["population",3],
                            ["traits",["fat-tissue", "carnivore"]],
                            ["fat-food", 3]
                          ]
                        ]],
                        ["bag",0]
                      ],
                      1,
                      [
                        [
                          ["id",2],
                          ["species",[
                            [
                              ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 3]
                            ],
                            [
                              ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["fat-tissue", "warning-call"]],
                              ["fat-food", 3]
                            ]
                          ]],
                          ["bag",0]
                        ]
                      ]
                    ]
    self.case41_out = '[0, 0, 1]'

    self.case42_in = [
                      [
                        ["id",1],
                        ["species",[
                          [
                            ["food",0],
                            ["body",3],
                            ["population",3],
                            ["traits",["fat-tissue", "carnivore"]],
                            ["fat-food", 3]
                          ],
                          [
                            ["food",0],
                            ["body",3],
                            ["population",5],
                            ["traits",["fat-tissue", "carnivore"]],
                            ["fat-food", 3]
                          ]
                        ]],
                        ["bag",0]
                      ],
                      1,
                      [
                        [
                          ["id",2],
                          ["species",[
                            [
                              ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 3]
                            ],
                            [
                              ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["fat-tissue", "warning-call"]],
                              ["fat-food", 3]
                            ]
                          ]],
                          ["bag",0]
                        ]
                      ]
                    ]
    self.case42_out = '[1, 0, 1]'

    self.case43_in = [
                      [
                        ["id",1],
                        ["species",[
                          [
                            ["food",0],
                            ["body",3],
                            ["population",3],
                            ["traits",["fat-tissue", "carnivore"]],
                            ["fat-food", 3]
                          ]
                        ]],
                        ["bag",0]
                      ],
                      1,
                      [
                        [
                          ["id",2],
                          ["species",[
                            [
                              ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 3]
                            ],
                            [
                              ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["fat-tissue", "warning-call"]],
                              ["fat-food", 3]
                            ]
                          ]],
                          ["bag",0]
                        ],
                        [
                          ["id",1231],
                          ["species",[
                            [
                              ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 3]
                            ],
                            [
                              ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["fat-tissue", "warning-call"]],
                              ["fat-food", 3]
                            ]
                          ]],
                          ["bag",0]
                        ]
                      ]
                    ]
    self.case43_out = '[0, 0, 1]'

    self.case44_in = [
                      [
                        ["id",1],
                        ["species",[
                          [
                            ["food",0],
                            ["body",3],
                            ["population",3],
                            ["traits",["fat-tissue", "carnivore"]],
                            ["fat-food", 3]
                          ]
                        ]],
                        ["bag",0]
                      ],
                      1,
                      [
                        [
                          ["id",2],
                          ["species",[
                            [
                              ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 3]
                            ],
                            [
                              ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["fat-tissue", "warning-call"]],
                              ["fat-food", 3]
                            ]
                          ]],
                          ["bag",0]
                        ],
                        [
                          ["id",1231],
                          ["species",[
                            [
                              ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["fat-tissue"]],
                              ["fat-food", 3]
                            ],
                            [
                              ["food",3],
                              ["body",3],
                              ["population",7],
                              ["traits",["fat-tissue", "warning-call"]],
                              ["fat-food", 3]
                            ]
                          ]],
                          ["bag",0]
                        ]
                      ]
                    ]
    self.case44_out = '[0, 1, 1]'

    self.case45_in = [
                      [
                        ["id",1],
                        ["species",[
                          [
                            ["food",3],
                            ["body",3],
                            ["population",3],
                            ["traits",["fat-tissue"]],
                            ["fat-food", 0]
                          ]
                        ]],
                        ["bag",0]
                      ],
                      1,
                      []
                    ]
    self.case45_out = '[0, 1]'

    self.case46_in = [
                      [
                        ["id",1],
                        ["species",[
                          [
                            ["food",3],
                            ["body",3],
                            ["population",3],
                            ["traits",["fat-tissue"]],
                            ["fat-food", 1]
                          ]
                        ]],
                        ["bag",0]
                      ],
                      4,
                      []
                    ]
    self.case46_out = '[0, 2]'

    self.case47_in = [
                      [
                        ["id",1],
                        ["species",[
                          [
                            ["food",3],
                            ["body",5],
                            ["population",3],
                            ["traits",["fat-tissue"]],
                            ["fat-food", 2]
                          ],
                          [
                            ["food",3],
                            ["body",3],
                            ["population",3],
                            ["traits",["fat-tissue"]],
                            ["fat-food", 0]
                          ]
                        ]],
                        ["bag",0]
                      ],
                      4,
                      []
                    ]
    self.case47_out = '[0, 3]'

    self.case48_in = [
                      [
                        ["id",1],
                        ["species",[
                          [
                            ["food",0],
                            ["body",3],
                            ["population",2],
                            ["traits",["fat-tissue"]],
                            ["fat-food", 0]
                          ],
                          [
                            ["food",0],
                            ["body",3],
                            ["population",2],
                            ["traits",["fat-tissue", "climbing"]],
                            ["fat-food", 0]
                          ]
                        ]],
                        ["bag",0]
                      ],
                      4,
                      []
                    ]
    self.case48_out = '[0, 3]'

    self.case49_in = [
                      [
                        ["id",1],
                        ["species",[
                          [
                            ["food",2],
                            ["body",3],
                            ["population",3],
                            ["traits",["horns", "burrowing"]]
                          ]
                        ]],
                        ["bag",0]
                      ],
                      1,
                      []
                    ]
    self.case49_out = '0'

    self.case50_in = [
                      [
                        ["id",1],
                        ["species",[
                          [
                            ["food",2],
                            ["body",3],
                            ["population",3],
                            ["traits",["horns", "climbing"]]
                          ],
                          [
                            ["food",2],
                            ["body",3],
                            ["population",3],
                            ["traits",["horns", "ambush"]]
                          ]
                        ]],
                        ["bag",0]
                      ],
                      1,
                      []
                    ]
    self.case50_out = '0'

    self.case51_in = [
                      [
                        ["id", 1],
                        ["species", [
                          [
                            ["food", 0],
                            ["body", 6],
                            ["population", 7],
                            ["traits", ["climbing", "fat-tissue"]],
                                    ["fat-food", 0]
                          ],
                          [
                            ["food", 0],
                            ["body", 6],
                            ["population", 6],
                            ["traits", ["fertile"]]
                          ],
                          [
                            ["food", 0],
                            ["body", 5],
                            ["population", 2],
                            ["traits", ["fat-tissue"]],
                                    ["fat-food", 0]
                          ]
                        ]],
                        ["bag", 10]
                      ],

                      19, [
                        [
                          ["id", 2],
                          ["species", [
                            [
                              ["food", 0],
                              ["body", 6],
                              ["population", 6],
                              ["traits", ["carnivore", "climbing"]]
                            ]
                          ]],
                          ["bag", 10]
                        ],
                        [
                          ["id", 3],
                          ["species", [
                            [
                              ["food", 0],
                              ["body", 6],
                              ["population", 6],
                              ["traits", ["climbing"]]
                            ]
                          ]],
                          ["bag", 10]
                        ]
                      ]
                    ]
    self.case51_out = '[0, 6]'

    self.case52_in = [
                      [
                        ["id", 1],
                        ["species", [
                          [
                            ["food", 0],
                            ["body", 5],
                            ["population", 7],
                            ["traits", ["climbing", "fertile"]]
                          ],
                          [
                            ["food", 0],
                            ["body", 4],
                            ["population", 6],
                            ["traits", ["horns"]]
                          ],
                          [
                            ["food", 0],
                            ["body", 5],
                            ["population", 5],
                            ["traits", ["fertile"]]
                          ]
                        ]],
                        ["bag", 10]
                      ],
                      20, [
                        [
                          ["id", 2],
                          ["species", [
                            [
                              ["food", 0],
                              ["body", 5],
                              ["population", 5],
                              ["traits", ["carnivore", "climbing"]]
                            ]
                          ]],
                          ["bag", 10]
                        ],
                        [
                          ["id", 3],
                          ["species", [
                            [
                              ["food", 0],
                              ["body", 5],
                              ["population", 5],
                              ["traits", ["climbing"]]
                            ]
                          ]],
                          ["bag", 10]
                        ]
                      ]
                    ]
    self.case52_out = '0'

    self.case53_in = [
                      [
                        ["id", 1],
                        ["species", [
                          [
                            ["food", 7],
                            ["body", 5],
                            ["population", 7],
                            ["traits", ["climbing", "fat-tissue"]],
                            ["fat-food", 5]
                          ],
                          [
                            ["food", 6],
                            ["body", 4],
                            ["population", 6],
                            ["traits", ["fat-tissue"]],
                            ["fat-food", 4]
                          ],
                          [
                            ["food", 0],
                            ["body", 5],
                            ["population", 5],
                            ["traits", ["fertile", "carnivore", "climbing"]]
                          ]
                        ]],
                        ["bag", 10]
                      ],
                      19, [
                        [
                          ["id", 2],
                          ["species", [
                            [
                              ["food", 0],
                              ["body", 3],
                              ["population", 5],
                              ["traits", ["horns", "fat-tissue"]],
                              ["fat-food", 0]
                            ],
                            [
                              ["food", 0],
                              ["body", 6],
                              ["population", 5],
                              ["traits", ["horns", "climbing"]]
                            ]
                          ]],
                          ["bag", 10]
                        ],
                        [
                          ["id", 3],
                          ["species", [
                            [
                              ["food", 0],
                              ["body", 5],
                              ["population", 4],
                              ["traits", ["climbing"]]
                            ]
                          ]],
                          ["bag", 10]
                        ]
                      ]
                    ]
    self.case53_out = '[2, 0, 1]'

    self.case54_in = [
                      [
                        ["id", 1],
                        ["species", [
                          [
                            ["food", 7],
                            ["body", 5],
                            ["population", 7],
                            ["traits", ["climbing", "fat-tissue"]],
                            ["fat-food", 5]
                          ],
                          [
                            ["food", 6],
                            ["body", 4],
                            ["population", 6],
                            ["traits", ["fat-tissue"]],
                            ["fat-food", 4]
                          ],
                          [
                            ["food", 5],
                            ["body", 5],
                            ["population", 5],
                            ["traits", ["fertile"]]
                          ]
                        ]],
                        ["bag", 10]
                      ],
                      19, [
                        [
                          ["id", 2],
                          ["species", [
                            [
                              ["food", 0],
                              ["body", 5],
                              ["population", 5],
                              ["traits", ["carnivore", "climbing"]]
                            ]
                          ]],
                          ["bag", 10]
                        ],
                        [
                          ["id", 3],
                          ["species", [
                            [
                              ["food", 0],
                              ["body", 5],
                              ["population", 5],
                              ["traits", ["climbing"]]
                            ]
                          ]],
                          ["bag", 10]
                        ]
                      ]
                    ]
    self.case54_out = 'null'

    self.case55_in = [
                      [
                        ["id", 1],
                        ["species", [
                          [
                            ["food", 7],
                            ["body", 5],
                            ["population", 7],
                            ["traits", ["climbing", "fat-tissue"]],
                            ["fat-food", 5]
                          ],
                          [
                            ["food", 6],
                            ["body", 4],
                            ["population", 6],
                            ["traits", ["fat-tissue"]],
                            ["fat-food", 4]
                          ],
                          [
                            ["food", 3],
                            ["body", 5],
                            ["population", 5],
                            ["traits", ["carnivore", "climbing"]]
                          ]
                        ]],
                        ["bag", 10]
                      ],
                      10, [
                        [
                          ["id", 2],
                          ["species", [
                            [
                              ["food", 0],
                              ["body", 5],
                              ["population", 5],
                              ["traits", ["carnivore", "climbing"]]
                            ]
                          ]],
                          ["bag", 10]
                        ],
                        [
                          ["id", 3],
                          ["species", [
                            [
                              ["food", 0],
                              ["body", 5],
                              ["population", 4],
                              ["traits", ["climbing"]]
                            ]
                          ]],
                          ["bag", 10]
                        ]
                      ]
                    ]
    self.case55_out = '[2, 0, 0]'

    self.case56_in = [[["id",10],
                      ["species",[[["food",0],
                                     ["body",1],
                                     ["population",1],
                                     ["traits",["carnivore"]]]]],
                      ["bag",10]],
                     7,
                     [[["id",11],
                       ["species",[[["food",1],
                                    ["body",1],
                                    ["population",1],
                                    ["traits",[]]]]],
                       ["bag",10]],
                      [["id",12],
                       ["species",[[["food",1],
                                    ["body",1],
                                    ["population",1],
                                    ["traits",["burrowing"]]]]],
                       ["bag",10]]]]
    self.case56_out = '[0, 0, 0]'

    self.case57_in = [[["id",10],
                      ["species",[[["food",0],
                                   ["body",1],
                                   ["population",1],
                                   ["traits",[]]]]],
                      ["bag",10]],
                     7,
                     [[["id",11],
                       ["species",[[["food",1],
                                    ["body",1],
                                    ["population",1],
                                    ["traits",[]]]]],
                       ["bag",10]],
                      [["id",12],
                       ["species",[[["food",1],
                                    ["body",1],
                                    ["population",1],
                                    ["traits",[]]]]],
                       ["bag",10]]]]
    self.case57_out = '0'

    self.case58_in = [[["id",10],
                        ["species",[[["food",1],
                                     ["body",1],
                                     ["population",1],
                                     ["traits",[]]]]],
                        ["bag",10]],
                       7,
                       [[["id",11],
                         ["species",[[["food",1],
                                      ["body",1],
                                      ["population",1],
                                      ["traits",[]]]]],
                         ["bag",10]],
                        [["id",12],
                         ["species",[[["food",1],
                                      ["body",1],
                                      ["population",1],
                                      ["traits",[]]]]],
                         ["bag",10]]]]
    self.case58_out = 'null'

    self.case59_in = [[["id",10],
                        ["species",[[["food",1],
                                     ["body",1],
                                     ["population",1],
                                     ["traits",["fat-tissue"]],
                                     ["fat-food",0]]]],
                        ["bag",10]],
                       7,
                       [[["id",11],
                         ["species",[[["food",1],
                                      ["body",1],
                                      ["population",1],
                                      ["traits",[]]]]],
                         ["bag",10]],
                        [["id",12],
                         ["species",[[["food",1],
                                      ["body",1],
                                      ["population",1],
                                      ["traits",[]]]]],
                         ["bag",10]]]]
    self.case59_out = '[0, 1]'

    self.case60_in = [[["id",10],
                      ["species",[[["food",1],
                                   ["body",4],
                                   ["population",1],
                                   ["traits",["fat-tissue"]],
                                   ["fat-food",0]]]],
                      ["bag",10]],
                     2,
                     [[["id",11],
                       ["species",[[["food",1],
                                    ["body",1],
                                    ["population",1],
                                    ["traits",[]]]]],
                       ["bag",10]],
                      [["id",12],
                       ["species",[[["food",1],
                                    ["body",1],
                                    ["population",1],
                                    ["traits",[]]]]],
                       ["bag",10]]]]
    self.case60_out = '[0, 2]'

    self.case61_in = [[["id",10],
                      ["species",[[["food",1],
                                   ["body",4],
                                   ["population",1],
                                   ["traits",["fat-tissue"]],
                                   ["fat-food",2]]]],
                      ["bag",10]],
                     12,
                     [[["id",11],
                       ["species",[[["food",1],
                                    ["body",1],
                                    ["population",1],
                                    ["traits",[]]]]],
                       ["bag",10]],
                      [["id",12],
                       ["species",[[["food",1],
                                    ["body",1],
                                    ["population",1],
                                    ["traits",[]]]]],
                       ["bag",10]]]]
    self.case61_out = '[0, 2]'

    self.case62_in = [[["id",10],
                      ["species",[[["food",1],
                                   ["body",4],
                                   ["population",1],
                                   ["traits",["fat-tissue"]],
                                   ["fat-food",4]]]],
                      ["bag",10]],
                     12,
                     [[["id",11],
                       ["species",[[["food",1],
                                    ["body",1],
                                    ["population",1],
                                    ["traits",[]]]]],
                       ["bag",10]],
                      [["id",12],
                       ["species",[[["food",1],
                                    ["body",1],
                                    ["population",1],
                                    ["traits",[]]]]],
                       ["bag",10]]]]
    self.case62_out = 'null'

    self.case63_in = [[["id",10],
                          ["species",[[["food",0],
                                         ["body",1],
                                         ["population",1],
                                         ["traits",["carnivore"]]],
                                      [["food",1],
                                       ["body",1],
                                       ["population",1],
                                       ["traits",[]]]]],
                          ["bag",10]],
                         7,
                         [[["id",11],
                           ["species",[[["food",1],
                                        ["body",1],
                                        ["population",1],
                                        ["traits",["burrowing"]]]]],
                           ["bag",10]],
                          [["id",12],
                           ["species",[[["food",1],
                                        ["body",1],
                                        ["population",1],
                                        ["traits",["burrowing"]]]]],
                           ["bag",10]]]]
    self.case63_out = 'false'

    self.case64_in = [[["id",10],
                        ["species",[[["food",1],
                                     ["body",2],
                                     ["population",1],
                                     ["traits",["fat-tissue"]],
                                     ["fat-food",1]],
                                    [["food",1],
                                     ["body",5],
                                     ["population",1],
                                     ["traits",["fat-tissue"]],
                                     ["fat-food",1]]]],
                        ["bag",10]],
                       7,
                       [[["id",11],
                         ["species",[[["food",1],
                                      ["body",1],
                                      ["population",1],
                                      ["traits",[]]]]],
                         ["bag",10]],
                        [["id",12],
                         ["species",[[["food",1],
                                      ["body",1],
                                      ["population",1],
                                      ["traits",[]]]]],
                         ["bag",10]]]]
    self.case64_out = '[1, 4]'

    self.case65_in = [[["id",10],
                      ["species",[[["food",0],
                                   ["body",5],
                                   ["population",1],
                                   ["traits",[]]],
                                  [["food",0],
                                   ["body",2],
                                   ["population",1],
                                   ["traits",[]]]]],
                      ["bag",10]],
                     7,
                     [[["id",11],
                       ["species",[[["food",1],
                                    ["body",1],
                                    ["population",1],
                                    ["traits",["burrowing"]]]]],
                       ["bag",10]],
                      [["id",12],
                       ["species",[[["food",1],
                                    ["body",1],
                                    ["population",1],
                                    ["traits",["burrowing"]]]]],
                       ["bag",10]]]]
    self.case65_out = '0'

    self.case66_in = [[["id",1],
                      ["species",
                          [[["food",0],
                          ["body",4],
                          ["population",2],
                          ["traits",
                            ["carnivore"]]]]],
                      ["bag",0]],
                     10,
                     [[["id",2],
                       ["species",
                          [[["food",1],
                        ["body",3],
                            ["population",3],
                        ["traits",
                            ["herding"]]],
                         [["food",1],
                        ["body",2],
                        ["population",4],
                        ["traits",
                            ["carnivore", "ambush"]]]]],
                       ["bag",0]],

                       [["id",3],
                        ["species",
                          [[["food",0],
                          ["body",1],
                          ["population",2],
                          ["traits",[]]]]],
                        ["bag",0]]]]
    self.case66_out = '[0, 0, 1]'

    self.case67_in = [[["id",1],
                      ["species",
                         [[["food",0],
                         ["body",1],
                         ["population",1],
                         ["traits",
                            ["symbiosis"]]],
                        [["food",0],
                         ["body",3],
                           ["population",1],
                           ["traits",
                           ["warning-call"]]]]],
                      ["bag",0]],
                      10,
                      [[["id",2],
                        ["species",
                           [[["food",2],
                         ["body",2],
                         ["population",2],
                         ["traits",[]]],
                        [["food",0],
                         ["body",1],
                         ["population",1],
                         ["traits", []]]]],
                        ["bag",0]],

                       [["id",3],
                        ["species",
                           [[["food",0],
                         ["body",1],
                         ["population",1],
                         ["traits",[]]]]],
                        ["bag",0]]]]
    self.case67_out = '1'

    self.case68_in = [[["id",1],
                        ["species",
                           [[["food",0],
                           ["body",5],
                           ["population",1],
                           ["traits",
                              ["fat-tissue"]],
                           ["fat-food", 3]],
                          [["food",0],
                           ["body",6],
                           ["population",1],
                           ["traits",
                              ["warning-call"]]]]],
                        ["bag",0]],
                       10,
                        [[["id",2],
                          ["species",
                            [[["food",2],
                            ["body",2],
                            ["population",2],
                            ["traits", []]],
                           [["food",0],
                            ["body",1],
                            ["population",1],
                            ["traits", []]]]],
                          ["bag",0]],

                         [["id",3],
                          ["species",
                            [[["food",0],
                            ["body",1],
                            ["population",1],
                            ["traits",[]]]]],
                          ["bag",0]]]]
    self.case68_out = '[0, 2]'

    self.case69_in = [[["id", 1], ["species", [[["food", 1], ["body", 2], ["population", 4], ["traits", ["fat-tissue", "carnivore"]], ["fat-food", 2]], [["food", 1], ["body", 2], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 2]], 10, [[["id", 2], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]], [["id", 6], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]]]]
    self.case69_out = '[0, 0, 0]'

    self.case70_in = [[["id", 1], ["species", [[["food", 2], ["body", 2], ["population", 2], ["traits", ["fat-tissue"]], ["fat-food", 2]], [["food", 1], ["body", 2], ["population", 2], ["traits", ["carnivore"]]]]], ["bag", 2]], 10, [[["id", 2], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]], [["id", 6], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]]]]
    self.case70_out = '[1, 0, 0]'

    self.case71_in = [[["id", 1], ["species", [[["food", 1], ["body", 6], ["population", 2], ["traits", ["fat-tissue"]], ["fat-food", 2]], [["food", 1], ["body", 2], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 2]], 2, [[["id", 3], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]], [["id", 6], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]]]]
    self.case71_out = '[0, 2]'

    self.case72_in = [[["id", 1], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", ["fat-tissue"]], ["fat-food", 1]], [["food", 1], ["body", 2], ["population", 2], ["traits", ["fat-tissue"]], ["fat-food", 1]]]], ["bag", 2]], 10, [[["id", 2], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]], [["id", 6], ["species", [[["food", 1], ["body", 2], ["population", 2], ["traits", []]]]], ["bag", 2]]]]
    self.case72_out = '[0, 1]'

    self.case73_in = [
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
                                2
                              ],
                              [
                                "population",
                                3
                              ],
                              [
                                "traits",
                                []
                              ]
                            ],
                            [
                              [
                                "food",
                                3
                              ],
                              [
                                "body",
                                4
                              ],
                              [
                                "population",
                                6
                              ],
                              [
                                "traits",
                                []
                              ]
                            ]
                          ]
                        ],
                        [
                          "bag",
                          2
                        ]
                      ],
                      3,
                      [
                        [
                          [
                            "id",
                            2
                          ],
                          [
                            "species",
                            []
                          ],
                          [
                            "bag",
                            0
                          ]
                        ],
                        [
                          [
                            "id",
                            3
                          ],
                          [
                            "species",
                            []
                          ],
                          [
                            "bag",
                            0
                          ]
                        ]
                      ]
                    ]
    self.case73_out = '1'

    self.case74_in = [[["id",1],["species",[[["food",2],["body",4],["population",6],["traits",["fat-tissue"]]]]],["bag",2]],8,[[["id",2],["species",[]],["bag",0]],[["id",3],["species",[]],["bag",0]]]]
    self.case74_out = '[0, 4]'

    self.case75_in = [[["id", 1], ["species", [[["food", 2], ["body", 2], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 2]], 3, [[["id", 2], ["species", [[["food", 3], ["body", 4], ["population", 6], ["traits", ["carnivore"]]]]], ["bag", 0]], [["id", 3], ["species", []], ["bag", 0]]]]
    self.case75_out = '[0, 0, 0]'

    self.case76_in = [
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
                                2
                              ],
                              [
                                "population",
                                3
                              ],
                              [
                                "traits",
                                [
                                  "carnivore"
                                ]
                              ]
                            ],
                            [
                              [
                                "food",
                                3
                              ],
                              [
                                "body",
                                4
                              ],
                              [
                                "population",
                                6
                              ],
                              [
                                "traits",
                                [
                                  "carnivore"
                                ]
                              ]
                            ]
                          ]
                        ],
                        [
                          "bag",
                          2
                        ]
                      ],
                      3,
                      [
                        [
                          [
                            "id",
                            2
                          ],
                          [
                            "species",
                            []
                          ],
                          [
                            "bag",
                            0
                          ]
                        ],
                        [
                          [
                            "id",
                            3
                          ],
                          [
                            "species",
                            []
                          ],
                          [
                            "bag",
                            0
                          ]
                        ]
                      ]
                    ]
    self.case76_out = 'false'

    self.case77_in = [[["id", 1], ["species", [[["food", 3], ["body", 3], ["population", 3], ["traits", []]], [["food", 3], ["body", 4], ["population", 6], ["traits", ["carnivore"]]]]], ["bag", 2]], 3, [[["id", 2], ["species", [[["food", 2], ["body", 3], ["population", 3], ["traits", []]]]], ["bag", 0]], [["id", 3], ["species", []], ["bag", 0]]]]
    self.case77_out = '[1, 0, 0]'

    self.case78_in = [
                      [
                        ["id", 1],
                        ["species",
                          [
                            [
                              ["food", 3],
                              ["body", 2],
                              ["population", 4],
                              ["traits", ["hard-shell"]],
                              ["fat-food", 0]
                            ],
                            [
                              ["food", 3],
                              ["body", 2],
                              ["population", 4],
                              ["traits", []]
                            ],
                            [
                              ["food", 3],
                              ["body", 1],
                              ["population", 4],
                              ["traits", []]
                            ],
                            [
                              ["food", 1],
                              ["body", 1],
                              ["population", 2],
                              ["traits", []]
                            ]
                          ]
                        ],
                        ["bag", 0]
                      ],
                      10,
                      [
                        [
                          ["id", 2],
                          ["species", []],
                          ["bag", 0]
                        ]
                      ]
                    ]
    self.case78_out = '0'

    self.case79_in = [[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],1,[]]
    self.case79_out = '0'

    self.case80_in = [[["id",1],["species",[[["food",0],["body",4],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],5,[]]
    self.case80_out = 'false'

    self.case81_in = [[["id",5],["species",[[["food",3],["body",6],["population",5],["traits",["fat-tissue","climbing"]],["fat-food",2]]]],["bag",0]],7,[]]
    self.case81_out = '[0, 4]'

    self.case82_in = [[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],1,[[["id",10],["species",[]],["bag",0]],[["id",3],["species",[[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",5],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",9],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]]]]
    self.case82_out = '[0, 2, 0]'

    self.case83_in = [
                      [
                          ["id",1],
                          ["species",
                              [
                                  [["food",2],["body",4],["population",4],["traits",["carnivore"]]],
                                  [["food",2],["body",4],["population",4],["traits",["carnivore","ambush"]]],
                                  [["food",2],["body",4],["population",4],["traits",["warning-call"]]],
                                  [["food",2],["body",4],["population",4],["traits",["symbiosis"]]]
                              ]
                          ],
                          ["bag",4]
                      ],
                      10,
                      [
                          [
                              ["id",2],
                              ["species",
                                  [
                                      [["food",2],["body",4],["population",4],["traits",["carnivore"]]]
                                  ]
                              ],
                              ["bag",4]
                          ],
                          [
                              ["id",3],
                              ["species",
                                  [
                                      [["food",2],["body",4],["population",4],["traits",["symbiosis"]]]
                                  ]
                              ],
                              ["bag",4]
                          ],
                          [
                              ["id",4],
                              ["species",
                                  [
                                      [["food",3],["body",5],["population",5],["traits",["fat-tissue"]],["fat-food",2]],
                                      [["food",3],["body",5],["population",5],["traits",["fat-tissue"]],["fat-food",2]],
                                      [["food",2],["body",4],["population",4],["traits",["carnivore"]]],
                                      [["food",2],["body",4],["population",4],["traits",["carnivore","ambush"]]],
                                      [["food",2],["body",4],["population",4],["traits",["warning-call"]]],
                                      [["food",2],["body",4],["population",4],["traits",["symbiosis"]]]
                                  ]
                              ],
                              ["bag",4]
                          ]
                      ]
                  ]
    self.case83_out = '2'

    self.case84_in = [
                      [
                          ["id",1],
                          ["species",
                              [
                                  [["food",3],["body",5],["population",5],["traits",["fat-tissue"]],["fat-food",2]],
                                  [["food",3],["body",5],["population",5],["traits",["fat-tissue"]],["fat-food",2]],
                                  [["food",2],["body",4],["population",4],["traits",["carnivore"]]],
                                  [["food",2],["body",4],["population",4],["traits",["carnivore","ambush"]]],
                                  [["food",2],["body",4],["population",4],["traits",["warning-call"]]],
                                  [["food",2],["body",4],["population",4],["traits",["symbiosis"]]]
                              ]
                          ],
                          ["bag",4]
                      ],
                      10,
                      [
                          [
                              ["id",2],
                              ["species",
                                  [
                                      [["food",2],["body",4],["population",4],["traits",["carnivore"]]]
                                  ]
                              ],
                              ["bag",4]
                          ],
                          [
                              ["id",3],
                              ["species",
                                  [
                                      [["food",3],["body",5],["population",5],["traits",["fat-tissue"]],["fat-food",2]],
                                      [["food",3],["body",5],["population",5],["traits",["fat-tissue"]],["fat-food",2]],
                                      [["food",2],["body",4],["population",4],["traits",["carnivore"]]],
                                      [["food",2],["body",4],["population",4],["traits",["carnivore","ambush"]]],
                                      [["food",2],["body",4],["population",4],["traits",["warning-call"]]],
                                      [["food",2],["body",4],["population",4],["traits",["symbiosis"]]]
                                  ]
                              ],
                              ["bag",4]
                          ],
                          [
                              ["id",4],
                              ["species",
                                  [
                                      [["food",2],["body",4],["population",4],["traits",["symbiosis"]]],
                                      [["food",2],["body",4],["population",4],["traits",["warning-call"]]]
                                  ]
                              ],
                              ["bag",4]
                          ]
                      ]
                  ]
    self.case84_out = '[0, 3]'

    self.case85_in = [
                      [
                          ["id",1],
                          ["species",
                              [
                                  [["food",3],["body",5],["population",5],["traits",["fat-tissue"]],["fat-food",2]],
                                  [["food",3],["body",5],["population",5],["traits",["fat-tissue"]],["fat-food",2]],
                                  [["food",2],["body",4],["population",4],["traits",["carnivore"]]],
                                  [["food",2],["body",4],["population",4],["traits",["carnivore","ambush"]]],
                                  [["food",2],["body",4],["population",4],["traits",["warning-call"]]],
                                  [["food",2],["body",4],["population",4],["traits",["symbiosis"]]]
                              ]
                          ],
                          ["bag",4]
                      ],
                      2,
                      [
                          [
                              ["id",2],
                              ["species",
                                  [
                                      [["food",2],["body",4],["population",4],["traits",["carnivore"]]]
                                  ]
                              ],
                              ["bag",4]
                          ],
                          [
                              ["id",3],
                              ["species",
                                  [
                                      [["food",3],["body",5],["population",5],["traits",["fat-tissue"]],["fat-food",2]],
                                      [["food",3],["body",5],["population",5],["traits",["fat-tissue"]],["fat-food",2]],
                                      [["food",2],["body",4],["population",4],["traits",["carnivore"]]],
                                      [["food",2],["body",4],["population",4],["traits",["carnivore","ambush"]]],
                                      [["food",2],["body",4],["population",4],["traits",["warning-call"]]],
                                      [["food",2],["body",4],["population",4],["traits",["symbiosis"]]]
                                  ]
                              ],
                              ["bag",4]
                          ],
                          [
                              ["id",4],
                              ["species",
                                  [
                                      [["food",2],["body",4],["population",4],["traits",["symbiosis"]]],
                                      [["food",2],["body",4],["population",4],["traits",["warning-call"]]]
                                  ]
                              ],
                              ["bag",4]
                          ]
                      ]
                  ]
    self.case85_out = '[0, 2]'

    self.caseM1_in = [[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],1,[]]
    self.caseM1_out = '0'

    self.caseM2_in = [[["id",55],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],1,[]]
    self.caseM2_out = '0'

    self.caseM3_in = [[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],1,[]]
    self.caseM3_out = 'false'

    self.caseM4_in = [[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],1,[[["id",100],["species",[]],["bag",0]],[["id",3],["species",[[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",1],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]]]
    self.caseM4_out = '[0, 2, 1]'

    self.caseM5_in = [[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]],[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],1,[[["id",100],["species",[]],["bag",0]],[["id",3],["species",[[["food",0],["body",3],["population",1],["traits",["climbing"]]]]],["bag",0]],[["id",4],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",5],["species",[[["food",1],["body",3],["population",1],["traits",[]]]]],["bag",0]],[["id",6],["species",[[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]]]]
    self.caseM5_out = '[0, 2, 0]'

    self.caseM6_in = [[["id",7],["species",[[["food",0],["body",3],["population",1],["traits",[]]],[["food",0],["body",2],["population",3],["traits",["fat-tissue"]]],[["food",1],["body",3],["population",1],["traits",[]]],[["food",0],["body",3],["population",1],["traits",["carnivore"]]]]],["bag",0]],2,[[["id",100],["species",[]],["bag",0]]]]
    self.caseM6_out = '[1, 2]'

    self.caseM7_in = [[["id",8],["species",[[["food",0],["body",2],["population",3],["traits",["fat-tissue"]]],[["food",0],["body",5],["population",3],["traits",["fat-tissue"]]]]],["bag",0]],2,[[["id",100],["species",[]],["bag",0]]]]
    self.caseM7_out = '[1, 2]'

    self.caseM8_in = [[["id",9],["species",[[["food",0],["body",3],["population",2],["traits",["fat-tissue"]]],[["food",0],["body",3],["population",3],["traits",["fat-tissue"]]]]],["bag",0]],2,[]]
    self.caseM8_out = '[1, 2]'

    self.caseM9_in = [[["id",10],["species",[[["food",0],["body",3],["population",3],["traits",["fat-tissue","climbing"]]],[["food",0],["body",3],["population",3],["traits",["fat-tissue"]]]]],["bag",0]],3,[]]
    self.caseM9_out = '[0, 3]'

    self.caseM10_in = [[["id",11],["species",[[["food",3],["body",3],["population",3],["traits",["fat-tissue","climbing"]],["fat-food",2]]]],["bag",0]],3,[]]
    self.caseM10_out = '[0, 1]'

    self.caseM11_in = [[["id",11],["species",[[["food",3],["body",3],["population",3],["traits",["fat-tissue","climbing"]],["fat-food",1]]]],["bag",0]],2,[]]
    self.caseM11_out = '[0, 2]'

    self.caseM12_in = [[["id",501],["species",[[["food",2],["body",3],["population",4],["traits",["carnivore"]]]]],["bag",0]],9,[[["id",502],["species",[[["food",3],["body",1],["population",4],["traits",[]]]]],["bag",0]]]]
    self.caseM12_out = '[0, 0, 0]'

    self.caseM13_in = [[["id",501],["species",[[["food",2],["body",3],["population",4],["traits",["carnivore"]]]]],["bag",0]],1,[[["id",503],["species",[[["food",1],["body",1],["population",1],["traits",["burrowing"]]]]],["bag",0]]]]
    self.caseM13_out = 'false'

    self.caseM14_in = [[["id",501],["species",[[["food",2],["body",3],["population",4],["traits",["carnivore"]]]]],["bag",0]],1,[[["id",504],["species",[[["food",3],["body",1],["population",4],["traits",["burrowing"]]]]],["bag",0]]]]
    self.caseM14_out = '[0, 0, 0]'

    self.caseM15_in = [[["id",501],["species",[[["food",2],["body",3],["population",4],["traits",["carnivore"]]]]],["bag",0]],1,[[["id",512],["species",[[["food",3],["body",1],["population",4],["traits",["climbing"]]]]],["bag",0]]]]
    self.caseM15_out = 'false'

    self.caseM16_in = [[["id",511],["species",[[["food",2],["body",3],["population",4],["traits",["carnivore","climbing"]]]]],["bag",0]],1,[[["id",512],["species",[[["food",3],["body",1],["population",4],["traits",["climbing"]]]]],["bag",0]]]]
    self.caseM16_out = '[0, 0, 0]'

    self.caseM17_in = [[["id",501],["species",[[["food",2],["body",3],["population",4],["traits",["carnivore"]]]]],["bag",0]],1,[[["id",521],["species",[[["food",2],["body",2],["population",3],["traits",["hard-shell"]]]]],["bag",0]]]]
    self.caseM17_out = 'false'

    self.caseM18_in = [[["id",531],["species",[[["food",2],["body",7],["population",3],["traits",["carnivore"]]]]],["bag",0]],1,[[["id",521],["species",[[["food",2],["body",2],["population",3],["traits",["hard-shell"]]]]],["bag",0]]]]
    self.caseM18_out = '[0, 0, 0]'

    self.caseM19_in = [[["id",532],["species",[[["food",2],["body",3],["population",4],["traits",["carnivore","pack-hunting"]]]]],["bag",0]],1,[[["id",521],["species",[[["food",2],["body",2],["population",3],["traits",["hard-shell"]]]]],["bag",0]]]]
    self.caseM19_out = '[0, 0, 0]'

    self.caseM20_in = [[["id",501],["species",[[["food",2],["body",3],["population",4],["traits",["carnivore"]]]]],["bag",0]],1,[[["id",542],["species",[[["food",2],["body",2],["population",3],["traits",["climbing","warning-call"]]],[["food",3],["body",1],["population",4],["traits",[]]]]],["bag",0]]]]
    self.caseM20_out = 'false'

    self.caseM21_in = [[["id",501],["species",[[["food",2],["body",3],["population",4],["traits",["carnivore"]]]]],["bag",0]],1,[[["id",543],["species",[[["food",3],["body",1],["population",4],["traits",[]]],[["food",2],["body",2],["population",3],["traits",["climbing","warning-call"]]]]],["bag",0]]]]
    self.caseM21_out = 'false'

    self.caseM22_in = [[["id",501],["species",[[["food",2],["body",3],["population",4],["traits",["carnivore"]]]]],["bag",0]],1,[[["id",543],["species",[[["food",2],["body",2],["population",3],["traits",["climbing","warning-call"]]],[["food",3],["body",1],["population",4],["traits",[]]],[["food",2],["body",2],["population",3],["traits",["climbing","warning-call"]]]]],["bag",0]]]]
    self.caseM22_out = 'false'

    self.caseM23_in = [[["id",541],["species",[[["food",2],["body",3],["population",4],["traits",["carnivore","ambush"]]]]],["bag",0]],1,[[["id",543],["species",[[["food",3],["body",1],["population",4],["traits",[]]],[["food",2],["body",2],["population",3],["traits",["climbing","warning-call"]]]]],["bag",0]]]]
    self.caseM23_out = '[0, 0, 0]'

    self.caseM24_in = [[["id",551],["species",[[["food",2],["body",3],["population",4],["traits",["carnivore","ambush","pack-hunting"]]]]],["bag",0]],1,[[["id",552],["species",[[["food",2],["body",2],["population",3],["traits",["climbing","warning-call"]]],[["food",2],["body",2],["population",2],["traits",["hard-shell"]]]]],["bag",0]]]]
    self.caseM24_out = '[0, 0, 1]'

    self.caseM25_in = [[["id",551],["species",[[["food",2],["body",3],["population",4],["traits",["carnivore","ambush","pack-hunting"]]]]],["bag",0]],1,[[["id",553],["species",[[["food",2],["body",2],["population",3],["traits",["climbing","warning-call"]]],[["food",2],["body",2],["population",2],["traits",["hard-shell","climbing"]]]]],["bag",0]]]]
    self.caseM25_out = 'false'

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
    del self.case66_in
    del self.case66_out
    del self.case67_in
    del self.case67_out
    del self.case68_in
    del self.case69_out
    del self.case70_in
    del self.case70_out
    del self.case71_in
    del self.case71_out
    del self.case72_in
    del self.case72_out
    del self.case73_in
    del self.case73_out
    del self.case74_in
    del self.case74_out
    del self.case75_in
    del self.case75_out
    del self.case76_in
    del self.case76_out
    del self.case77_in
    del self.case77_out
    del self.case78_in
    del self.case78_out
    del self.case79_in
    del self.case79_out
    del self.case80_in
    del self.case80_out
    del self.case81_in
    del self.case81_out
    del self.case82_in
    del self.case82_out
    del self.case83_in
    del self.case83_out
    del self.case84_in
    del self.case84_out
    del self.case85_in
    del self.case85_out

    del self.caseM1_in
    del self.caseM1_out
    del self.caseM2_in
    del self.caseM2_out
    del self.caseM3_in
    del self.caseM3_out
    del self.caseM4_in
    del self.caseM4_out
    del self.caseM5_in
    del self.caseM5_out
    del self.caseM6_in
    del self.caseM6_out
    del self.caseM7_in
    del self.caseM7_out
    del self.caseM8_in
    del self.caseM8_out
    del self.caseM9_in
    del self.caseM9_out
    del self.caseM10_in
    del self.caseM10_out
    del self.caseM11_in
    del self.caseM11_out
    del self.caseM12_in
    del self.caseM12_out
    del self.caseM13_in
    del self.caseM13_out
    del self.caseM14_in
    del self.caseM14_out
    del self.caseM15_in
    del self.caseM15_out
    del self.caseM16_in
    del self.caseM16_out
    del self.caseM17_in
    del self.caseM17_out
    del self.caseM18_in
    del self.caseM18_out
    del self.caseM19_in
    del self.caseM19_out
    del self.caseM20_in
    del self.caseM20_out
    del self.caseM21_in
    del self.caseM21_out
    del self.caseM22_in
    del self.caseM22_out
    del self.caseM23_in
    del self.caseM23_out
    del self.caseM24_in
    del self.caseM24_out
    del self.caseM25_in
    del self.caseM25_out

  def test_case_1(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case1_in), self.case1_out)
  def test_case_2(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case2_in), self.case2_out)
  def test_case_3(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case3_in), self.case3_out)
  def test_case_4(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case4_in), self.case4_out)
  def test_case_5(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case5_in), self.case5_out)
  def test_case_6(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case6_in), self.case6_out)
  def test_case_7(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case7_in), self.case7_out)
  def test_case_8(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case8_in), self.case8_out)
  def test_case_9(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case9_in), self.case9_out)
  def test_case_10(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case10_in), self.case10_out)
  def test_case_11(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case11_in), self.case11_out)
  def test_case_12(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case12_in), self.case12_out)
  def test_case_13(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case13_in), self.case13_out)
  def test_case_14(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case14_in), self.case14_out)
  def test_case_15(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case15_in), self.case15_out)
  def test_case_16(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case16_in), self.case16_out)
  def test_case_17(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case17_in), self.case17_out)
  def test_case_18(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case18_in), self.case18_out)
  def test_case_19(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case19_in), self.case19_out)
  def test_case_20(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case20_in), self.case20_out)
  def test_case_21(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case21_in), self.case21_out)
  def test_case_22(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case22_in), self.case22_out)
  def test_case_23(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case23_in), self.case23_out)
  def test_case_24(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case24_in), self.case24_out)
  def test_case_25(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case25_in), self.case25_out)
  def test_case_26(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case26_in), self.case26_out)
  def test_case_27(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case27_in), self.case27_out)
  def test_case_28(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case28_in), self.case28_out)
  def test_case_29(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case29_in), self.case29_out)
  def test_case_30(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case30_in), self.case30_out)
  def test_case_31(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case31_in), self.case31_out)
  def test_case_32(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case32_in), self.case32_out)
  def test_case_33(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case33_in), self.case33_out)
  def test_case_34(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case34_in), self.case34_out)
  def test_case_35(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case35_in), self.case35_out)
  def test_case_36(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case36_in), self.case36_out)
  def test_case_37(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case37_in), self.case37_out)
  def test_case_38(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case38_in), self.case38_out)
  def test_case_39(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case39_in), self.case39_out)
  def test_case_40(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case40_in), self.case40_out)
  def test_case_41(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case41_in), self.case41_out)
  def test_case_42(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case42_in), self.case42_out)
  def test_case_43(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case43_in), self.case43_out)
  def test_case_44(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case44_in), self.case44_out)
  def test_case_45(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case45_in), self.case45_out)
  def test_case_46(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case46_in), self.case46_out)
  def test_case_47(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case47_in), self.case47_out)
  def test_case_48(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case48_in), self.case48_out)
  def test_case_49(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case49_in), self.case49_out)
  def test_case_50(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case50_in), self.case50_out)
  def test_case_51(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case51_in), self.case51_out)
  def test_case_52(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case52_in), self.case52_out)
  def test_case_53(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case53_in), self.case53_out)
  def test_case_54(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case54_in), self.case54_out)
  def test_case_55(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case55_in), self.case55_out)
  def test_case_56(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case56_in), self.case56_out)
  def test_case_57(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case57_in), self.case57_out)
  def test_case_58(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case58_in), self.case58_out)
  def test_case_59(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case59_in), self.case59_out)
  def test_case_60(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case60_in), self.case60_out)
  def test_case_61(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case61_in), self.case61_out)
  def test_case_62(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case62_in), self.case62_out)
  def test_case_63(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case63_in), self.case63_out)
  def test_case_64(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case64_in), self.case64_out)
  def test_case_65(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case65_in), self.case65_out)
  def test_case_66(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case66_in), self.case66_out)
  def test_case_67(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case67_in), self.case67_out)
  def test_case_68(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case68_in), self.case68_out)
  def test_case_69(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case69_in), self.case69_out)
  def test_case_70(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case70_in), self.case70_out)
  def test_case_71(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case71_in), self.case71_out)
  def test_case_72(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case72_in), self.case72_out)
  def test_case_73(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case73_in), self.case73_out)
  def test_case_74(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case74_in), self.case74_out)
  def test_case_75(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case75_in), self.case75_out)
  def test_case_76(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case76_in), self.case76_out)
  def test_case_77(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case77_in), self.case77_out)
  def test_case_78(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case78_in), self.case78_out)
  def test_case_79(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case79_in), self.case79_out)
  def test_case_80(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case80_in), self.case80_out)
  def test_case_81(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case81_in), self.case81_out)
  def test_case_82(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case82_in), self.case82_out)
  def test_case_83(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case83_in), self.case83_out)
  def test_case_84(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case84_in), self.case84_out)
  def test_case_85(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.case85_in), self.case85_out)

  def test_case_M1(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM1_in), self.caseM1_out)
  def test_case_M2(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM2_in), self.caseM2_out)
  def test_case_M3(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM3_in), self.caseM3_out)
  def test_case_M4(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM4_in), self.caseM4_out)
  def test_case_M5(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM5_in), self.caseM5_out)
  def test_case_M6(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM6_in), self.caseM6_out)
  def test_case_M7(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM7_in), self.caseM7_out)
  def test_case_M8(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM8_in), self.caseM8_out)
  def test_case_M9(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM9_in), self.caseM9_out)
  def test_case_M10(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM10_in), self.caseM10_out)
  def test_case_M11(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM11_in), self.caseM11_out)
  def test_case_M12(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM12_in), self.caseM12_out)
  def test_case_M13(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM13_in), self.caseM13_out)
  def test_case_M14(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM14_in), self.caseM14_out)
  def test_case_M15(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM15_in), self.caseM15_out)
  def test_case_M16(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM16_in), self.caseM16_out)
  def test_case_M17(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM17_in), self.caseM17_out)
  def test_case_M18(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM18_in), self.caseM18_out)
  def test_case_M19(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM19_in), self.caseM19_out)
  def test_case_M20(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM20_in), self.caseM20_out)
  def test_case_M21(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM21_in), self.caseM21_out)
  def test_case_M22(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM22_in), self.caseM22_out)
  def test_case_M23(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM23_in), self.caseM23_out)
  def test_case_M24(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM24_in), self.caseM24_out)
  def test_case_M25(self):
    self.assertEqual(self.tester_xfeed.testMethod(self.caseM25_in), self.caseM25_out)


if __name__ == '__main__':
  unittest.main()
