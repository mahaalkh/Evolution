# Automated unit tests for the step test harness for Evolution game
import unittest
import os, sys
import json
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../executables'))
import xsilly_tester
class TestXStepTests10(unittest.TestCase):
	def setUp(self):
		self.case1_in = [
    [
        ["id", 1],
        ["species", [[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]],
        ["bag", 1],
        ["cards", [[2, "horns"], [1, "horns"], [0, "horns"], [-1, "horns"]]]
    ],
    [],
    []
]



		self.case1_out = json.dumps([3, [["population", 1, 0]], [], [[2, 1]], []]
)
		self.case2_in = [[["id", 1],
  ["species", [[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]],
  ["bag", 1],
  ["cards",
   [[1, "carnivore"], [1, "symbiosis"], [1, "fat-tissue"], [1, "foraging"]]]],
 [[[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]],
 [[[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]]
]

		self.case2_out = json.dumps([0, [["population", 1, 1]], [], [[2, 3]], []]
)
		self.case3_in = [[["id", 1],
  ["species", [[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]],
  ["bag", 1],
  ["cards",
   [[1, "carnivore"],
    [1, "symbiosis"],
    [1, "fat-tissue"],
    [1, "foraging"],
    [1, "horns"]]]],
 [[[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]],
 [[[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]]
]

		self.case3_out = json.dumps([0, [["population", 1, 4]], [["body", 1, 1]], [[2, 3]], []]
)
		self.case4_in = [[["id", 1],
  ["species", [[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]],
  ["bag", 1],
  ["cards",
   [[1, "carnivore"],
    [1, "symbiosis"],
    [1, "fat-tissue"],
    [1, "foraging"],
    [1, "horns"],
    [1, "warning-call"]]]],
 [[[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]],
 [[[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]]
]

		self.case4_out = json.dumps([0, [["population", 1, 4]], [["body", 1, 1]], [[2, 3]], [[1, 0, 5]]]
)
		self.case5_in = [[["id", 1],
  ["species", [[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]],
  ["bag", 1],
  ["cards",
   [[1, "carnivore"],
    [1, "symbiosis"],
    [1, "fat-tissue"],
    [1, "foraging"],
    [1, "horns"],
    [1, "warning-call"],
    [1, "climbing"]]]],
 [[[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]],
 [[[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]]
]

		self.case5_out = json.dumps([0, [["population", 1, 3]], [["body", 1, 4]], [[6, 2]], [[1, 0, 1]]]
)
		self.case6_in = [[["id", 2], ["species", [[["food", 0], ["body", 1], ["population", 3], ["traits", []]], [["food", 0], ["body", 2], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 0], ["cards", [[2, "fertile"], [0, "long-neck"], [0, "ambush"], [0, "cooperation"]]]], [[[["food", 0], ["body", 1], ["population", 1], ["traits", []]], [["food", 0], ["body", 1], ["population", 1], ["traits", []]]]], [[[["food", 2], ["body", 1], ["population", 2], ["traits", []]], [["food", 1], ["body", 1], ["population", 1], ["traits", []]]]]]

		self.case6_out = json.dumps([2, [["population", 2, 1]], [], [[3, 0]], []]
)
		self.case7_in = [[["id", 3], ["species", [[["food", 0], ["body", 1], ["population", 3], ["traits", []]], [["food", 0], ["body", 2], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 0], ["cards", [[2, "fertile"], [0, "long-neck"], [0, "ambush"], [0, "cooperation"], [0, "climbing"]]]], [[[["food", 0], ["body", 1], ["population", 1], ["traits", []]], [["food", 0], ["body", 1], ["population", 1], ["traits", []]]], [[["food", 2], ["body", 1], ["population", 2], ["traits", []]], [["food", 1], ["body", 1], ["population", 1], ["traits", []]]]], []]

		self.case7_out = json.dumps([2, [["population", 2, 0]], [["body", 2, 1]], [[4, 3]], []]
)
		self.case8_in =  [[["id", 1], ["species", [[["food", 0], ["body", 1], ["population", 3], ["traits", []]], [["food", 0], ["body", 2], ["population", 3], ["traits", ["carnivore"]]]]], ["bag", 0], ["cards", [[2, "fertile"], [0, "long-neck"], [0, "ambush"], [0, "cooperation"], [0, "climbing"], [0, "burrowing"], [-1, "cooperation"]]]], [], [[[["food", 0], ["body", 1], ["population", 1], ["traits", []]], [["food", 0], ["body", 1], ["population", 1], ["traits", []]]], [[["food", 2], ["body", 1], ["population", 2], ["traits", []]], [["food", 1], ["body", 1], ["population", 1], ["traits", []]]]]]

		self.case8_out = json.dumps([2, [["population", 2, 6]], [["body", 2, 3]], [[5, 4]], [[2, 0, 0]]]
)
		self.case9_in = [
	[
		["id", 1],
		["species", [
			[
				["food", 0],
				["body", 5],
				["population", 2],
				["traits", ["carnivore", "cooperation"]]
			],
			[
				["food", 0],
				["body", 5],
				["population", 1],
				["traits", ["carnivore"]]
			]
		]],
		["bag", 4],
        ["cards", [
          [-3, "ambush"],
          [-2, "burrowing"],
          [-1, "carnivore"],
          [0, "horns"],
          [1, "pack-hunting"],
          [2, "pack-hunting"],
          [3, "pack-hunting"]
        ]]
	],
	[
		[
			[
				["food", 0],
				["body", 2],
				["population", 2],
				["traits", ["scavenger", "foraging", "cooperation"]]
			],
			[
				["food", 0],
				["body", 5],
				["population", 2],
				["traits", ["carnivore", "cooperation"]]
			]
		]
	],
	[
		[
			[
				["food", 0],
				["body", 4],
				["population", 1],
				["traits", []]
			]
		]
	]
]
		self.case9_out = json.dumps([0, [["population", 2, 3]],[["body", 2, 4]],[[1, 2]],[[2, 0, 5]]])
		self.case10_in = [
	[
		["id", 1],
		["species", [
			[
				["food", 0],
				["body", 5],
				["population", 2],
				["traits", ["carnivore", "cooperation"]]
			],
			[
				["food", 0],
				["body", 5],
				["population", 1],
				["traits", ["carnivore"]]
			]
		]],
		["bag", 4],
        ["cards", [
          [-2, "burrowing"],
          [1, "pack-hunting"],
          [-1, "carnivore"],
          [-3, "ambush"],
          [3, "pack-hunting"],
          [0, "horns"],
          [2, "pack-hunting"]
        ]]
	],
	[
		[
			[
				["food", 0],
				["body", 2],
				["population", 2],
				["traits", ["scavenger", "foraging", "cooperation"]]
			],
			[
				["food", 0],
				["body", 5],
				["population", 2],
				["traits", ["carnivore", "cooperation"]]
			]
		]
	],
	[
		[
			[
				["food", 0],
				["body", 4],
				["population", 1],
				["traits", []]
			]
		]
	]
]
		self.case10_out = json.dumps([3, [["population", 2, 5]],[["body", 2, 1]],[[0, 2]],[[2, 0, 6]]])
		self.case11_in =[
    [
        ["id", 1],
        ["species", [
            [
                ["food", 0],
                ["body", 2],
                ["population", 1],
                ["traits", ["carnivore"]]
            ]
        ]],
        ["bag", 2],
        ["cards", [
            [1, "scavenger"],
            [-2, "long-neck"],
            [-1, "carnivore"],
            [1, "foraging"],
            [-2, "fertile"]
        ]]
    ],
    [],
    []
]

		self.case11_out = json.dumps([2,[["population",1,1]],[["body",1,0]],[[4,3]],[]]
)
		self.case12_in =[
    [
        ["id", 1],
        ["species", [
            [
                ["food", 0],
                ["body", 2],
                ["population", 1],
                ["traits", ["carnivore"]]
            ]
        ]],
        ["bag", 2],
        ["cards", [
            [1, "scavenger"],
            [-2, "scavenger"],
            [-1, "scavenger"],
            [-3, "scavenger"],
            [2, "scavenger"]
        ]]
    ],
    [],
    []

]

		self.case12_out = json.dumps([3,[["population",1,0]],[["body",1,4]],[[1,2]],[]]
)
		self.case13_in = [
    [
        ["id", 1],
        ["species", [
            [
                ["food", 0],
                ["body", 2],
                ["population", 1],
                ["traits", ["carnivore"]]
            ]
        ]],
        ["bag", 2],
        ["cards", [
            [1, "scavenger"],
            [-2, "scavenger"],
            [-1, "scavenger"],
            [-3, "scavenger"],
            [2, "scavenger"],
            [0, "ambush"],
            [5, "carnivore"]
        ]]
    ],
    [],
    []

]

		self.case13_out = json.dumps([5,[["population",1,1]],[["body",1,2]],[[6,3]],[[1,0,0]]]
)
		self.case14_in = [
    [
        ["id", 1],
        ["species", [
            [
                ["food", 0],
                ["body", 2],
                ["population", 1],
                ["traits", ["carnivore"]]
            ]
        ]],
        ["bag", 2],
        ["cards", [
            [1, "scavenger"],
            [-2, "scavenger"],
            [-1, "scavenger"],
            [-3, "scavenger"],
            [2, "scavenger"],
            [0, "ambush"],
            [5, "carnivore"]
        ]]
    ],
    [
        [
            [
                ["food", 0],
                ["body", 2],
                ["population", 1],
                ["traits", ["carnivore"]]
            ]
        ]
    ],
    [
        [
            [
                ["food", 0],
                ["body", 2],
                ["population", 1],
                ["traits", ["carnivore"]]
            ]
        ]
    ]

]

		self.case14_out = json.dumps([5,[["population",1,1]],[["body",1,2]],[[6,3]],[[1,0,0]]]
)
		self.case15_in = [
    [
        ["id", 1],
        ["species", [
            [
                ["food", 0],
                ["body", 2],
                ["population", 1],
                ["traits", ["carnivore"]]
            ]
        ]],
        ["bag", 2],
        ["cards", [
            [1, "scavenger"],
            [-2, "long-neck"],
            [-1, "carnivore"],
            [1, "foraging"]
        ]]
    ],
    [
        [
            [
                ["food", 0],
                ["body", 2],
                ["population", 1],
                ["traits", ["carnivore"]]
            ]
        ]
    ],
    [
        [
            [
                ["food", 0],
                ["body", 2],
                ["population", 1],
                ["traits", ["carnivore"]]
            ]
        ]
    ]
]

		self.case15_out = json.dumps([2,[["population",1,0]],[],[[3,1]],[]]
)
		self.case16_in = [
    [
        ["id", 5],
        ["species", [
            [
                ["food", 1],
                ["body", 2],
                ["population", 1],
                ["traits", ["carnivore"]]
            ]
        ]],
        ["bag", 10],
        ["cards", [
            [3, "climbing"],
            [2, "burrowing"],
            [-3, "ambush"],
            [7, "carnivore"]
        ]]
    ],
    [
        [
            [
                ["food", 1],
                ["body", 5],
                ["population", 3],
                ["traits", ["fat-tissue"]],
                ["fat-food", 4]
            ],
            [
                ["food", 3],
                ["body", 4],
                ["population", 5],
                ["traits", []]
            ]
        ]
    ],
    [
        [
            [
                ["food", 2],
                ["body", 4],
                ["population", 2],
                ["traits", ["carnivore"]]
            ]
        ]
    ]
]

		self.case16_out = json.dumps([
    2,
    [
        ["population", 1, 0]
    ],
    [],
    [
        [1, 3]
    ],
    []
]
)
		self.case17_in = [
    [
        ["id", 5],
        ["species", [
            [
                ["food", 1],
                ["body", 2],
                ["population", 1],
                ["traits", ["carnivore"]]
            ]
        ]],
        ["bag", 10],
        ["cards", [
            [3, "climbing"],
            [2, "burrowing"],
            [-3, "ambush"],
            [7, "carnivore"],
            [2, "symbiosis"],
            [-2, "symbiosis"]
        ]]
    ],
    [
        [
            [
                ["food", 1],
                ["body", 5],
                ["population", 3],
                ["traits", ["fat-tissue"]],
                ["fat-food", 4]
            ],
            [
                ["food", 3],
                ["body", 4],
                ["population", 5],
                ["traits", []]
            ]
        ]
    ],
    [
        [
            [
                ["food", 2],
                ["body", 4],
                ["population", 2],
                ["traits", ["carnivore"]]
            ]
        ]
    ]
]

		self.case17_out = json.dumps([
    2,
    [
        ["population", 1, 0]
    ],
    [
        ["body", 1, 5]
    ],
    [
        [1, 3]
    ],
    [
        [1, 0, 4]
    ]
]
)
		self.case18_in = [
    [
        ["id", 1],
        ["species", []],
        ["bag", 0],
        ["cards", [
            [1, "carnivore"],
            [2, "carnivore"],
            [3, "carnivore"],
            [4, "carnivore"]
        ]]
    ],
    [],
    []
]

						
		self.case18_out = json.dumps([0, [["population", 0, 3]], [], [[1, 2]], []])
		self.case19_in = [
    [
        ["id", 1],
        ["species", []],
        ["bag", 0],
        ["cards", [
            [1, "carnivore"],
            [2, "carnivore"],
            [3, "carnivore"],
            [4, "carnivore"],
            [5, "carnivore"]
        ]]
    ],
    [],
    []
]

		self.case19_out = json.dumps([0, [["population", 0, 3]], [["body", 0, 4]], [[1, 2]], []])
		self.case20_in = [
    [
        ["id", 1],
        ["species", []],
        ["bag", 0],
        ["cards", [
            [1, "carnivore"],
            [2, "carnivore"],
            [3, "carnivore"],
            [4, "carnivore"],
            [5, "carnivore"],
            [6, "carnivore"]
        ]]
    ],
    [],
    []
]

		self.case20_out = json.dumps([0, [["population", 0, 3]], [["body", 0, 4]], [[1, 2]], [[0, 0, 5]]]
)
		self.case21_in = [
    [
        ["id", 1],
        ["species", []],
        ["bag", 0],
        ["cards", [
            [1, "carnivore"],
            [2, "carnivore"],
            [3, "carnivore"],
            [4, "carnivore"],
            [5, "carnivore"],
            [6, "carnivore"],
            [7, "carnivore"]
        ]]
    ],
    [],
    []
]

		self.case21_out = json.dumps([0, [["population", 0, 3]], [["body", 0, 4]], [[1, 2]], [[0, 0, 5]]]
)
		self.case22_in = [[["id", 1],
["species", 
	[[["food", 0], ["body", 2], ["population", 2], ["traits", ["warning-call"]]]]],
["bag", 0],
["cards", [[-3, "carnivore"],
		   [0, "fat-tissue"],
		   [3, "scavenger"],
		   [2, "fertile"]]]],

[],

[
	[[["food", 0], ["body", 0], ["population", 1], ["traits", []]]],
	[[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]
]]

		self.case22_out = json.dumps([0, [["population", 1, 2]], [], [[1, 3]], []]
)
		self.case23_in = [[["id", 1],
["species", 
	[[["food", 0], ["body", 2], ["population", 2], ["traits", ["warning-call"]]]]],
["bag", 0],
["cards", [[-3, "carnivore"],
		   [0, "fat-tissue"],
		   [3, "scavenger"],
		   [2, "fertile"],
		   [-2, "long-neck"]]]],

[],

[
	[[["food", 0], ["body", 0], ["population", 1], ["traits", []]]],
	[[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]
]]

		self.case23_out = json.dumps([0, [["population", 1, 4]], [["body", 1, 2]], [[1, 3]], []]
)
		self.case24_in = [[["id", 1],
["species", 
	[[["food", 0], ["body", 2], ["population", 2], ["traits", ["warning-call"]]]]],
["bag", 0],
["cards", [[-3, "carnivore"],
		   [0, "fat-tissue"],
		   [3, "scavenger"],
		   [2, "fertile"],
		   [-2, "long-neck"],
		   [1, "warning-call"]]]],

[],

[
	[[["food", 0], ["body", 0], ["population", 1], ["traits", []]]],
	[[["food", 0], ["body", 0], ["population", 1], ["traits", []]]]
]]

		self.case24_out = json.dumps([0, [["population", 1, 4]], [["body", 1, 2]], [[1, 3]], [[1, 0, 5]]])
		self.case25_in = [
  [
    ["id",1],
    ["species",[
      [
        ["food",0],
        ["body",0],
        ["population",1],
        ["traits",[]]]]],
    ["bag",0],
    ["cards", [[-4, "carnivore"], [2, "cooperation"], [-3, "foraging"], [-1, "cooperation"]]]],
  [],
  [
    [
      [
        ["food",0],
        ["body",0],
        ["population",1],
        ["traits",[]]
      ]
    ],
    [
      [
        ["food",0],
        ["body",0],
        ["population",1],
        ["traits",[]]
      ]
    ]
  ]
]
		self.case25_out = json.dumps([0, [["population", 1, 2]], [], [[3, 1]], []])
		self.case26_in = [
  [
    ["id",1],
    ["species",[
      [
        ["food",0],
        ["body",0],
        ["population",1],
        ["traits",[]]],
      [
        ["food",0],
        ["body",3],
        ["population",7],
        ["traits",[]]]
    ]],
    ["bag",0],
    ["cards", [[7, "carnivore"], [2, "warning-call"], [-3, "foraging"], [-1, "cooperation"],
      [0, "fat-tissue"], [-3, "symbiosis"], [2, "hard-shell"], [-4, "carnivore"]]]],
  [],
  [
    [
      [
        ["food",0],
        ["body",0],
        ["population",1],
        ["traits",[]]
      ]
    ],
    [
      [
        ["food",0],
        ["body",0],
        ["population",1],
        ["traits",[]]
      ]
    ]
  ]
]
		self.case26_out = json.dumps([7, [["population", 2, 4]], [["body", 2, 2]], [[0, 3]], [[2, 0, 6]]])
		self.case27_in = [
 [["id",1],["species",[[["food",0],["body",0],["population",1],["traits",[]]]]],["bag",0],["cards",[[1,"ambush"],[2,"climbing"],[3,"carnivore"],[1,"hard-shell"]]]],
 [],
 []
]

		self.case27_out = json.dumps([0,[["population",1,3]],[],[[2,1]],[]]
)
		self.case28_in = [
 [["id",1],["species",[[["food",0],["body",0],["population",1],["traits",[]]]]],["bag",0],["cards",[[1,"ambush"],[2,"climbing"],[3,"carnivore"],[1,"hard-shell"],[2,"herding"],[3,"pack-hunting"]]]],
 [],
 []
]

		self.case28_out = json.dumps([0,[["population",1,3]],[["body",1,4]],[[2,1]],[[1,0,5]]]
)
		self.case29_in =[
 [["id",1],["species",[[["food",0],["body",0],["population",1],["traits",[]]]]],["bag",0],["cards",[[1,"ambush"],[2,"climbing"],[3,"carnivore"],[1,"hard-shell"],[2,"herding"]]]],
 [],
 []
]

		self.case29_out = json.dumps([0,[["population",1,3]],[["body",1,4]],[[2,1]],[]]
)
		self.case30_in =[
 [["id",2],["species",[[["food",0],["body",0],["population",1],["traits",[]]],[["food",1],["body",1],["population",1],["traits",[]]]]],["bag",0],["cards",[[1,"ambush"],[2,"climbing"],[3,"carnivore"],[1,"hard-shell"]]]],
 [],
 []
]

		self.case30_out = json.dumps([0,[["population",2,3]],[],[[2,1]],[]]
)
	
		self.case31_in = [
 [["id",2],["species",[[["food",0],["body",0],["population",1],["traits",[]]],[["food",1],["body",1],["population",1],["traits",[]]]]],["bag",0],["cards",[[1,"ambush"],[2,"climbing"],[3,"carnivore"],[1,"hard-shell"],[2,"herding"],[3,"pack-hunting"]]]],
 [],
 []
]

		self.case31_out = json.dumps([0,[["population",2,3]],[["body",2,4]],[[2,1]],[[2,0,5]]]
)
		self.case32_in = [
	[
		["id", 1],
		["species",
			[
				[
					["food",0],
					["body",7],
					["population",7],
					["traits",[]]
				]
			]
		],
		["bag", 0],
		["cards",
			[
				[1, "carnivore"],
				[2, "carnivore"],
				[3, "carnivore"],
				[4, "carnivore"],
				[5, "carnivore"],
				[6, "carnivore"],
				[7, "carnivore"]
			]
		]
	],
	[],
	[]
]

		self.case32_out = json.dumps([
	0,
	[
		["population", 1, 3]
	],
	[
		["body", 1, 4]
	],
	[
		[1, 2]
	],
	[
		[1, 0, 5]
	]
]
)
		self.case33_in = [
	[
		["id", 1],
		["species",
			[
				[
					["food",0],
					["body",7],
					["population",7],
					["traits",[]]
				]
			]
		],
		["bag", 0],
		["cards",
			[
				[1, "fertile"],
				[-3, "foraging"],
				[2, "fat-tissue"],
				[3, "fat-tissue"]
			]
		]
	],
	[],
	[]
]

		self.case33_out = json.dumps([
	2,
	[["population", 1, 1]],
	[],
	[[3, 0]],
	[]
])
		self.case34_in = [
	[
		["id", 1],
		["species",
			[
				[
					["food",0],
					["body",7],
					["population",7],
					["traits",[]]
				]
			]
		],
		["bag", 0],
		["cards",
			[
				[1, "fertile"],
				[-3, "foraging"],
				[2, "fat-tissue"],
				[3, "fat-tissue"],
				[-2, "foraging"]
			]
		]
	],
	[],
	[]
]

		self.case34_out = json.dumps([
	2,
	[["population", 1, 1]],
	[["body", 1, 4]],
	[[3, 0]],
	[]
])
		
		self.m1_in = [[["id",75],["species",[[["food",0],["body",0],["population",1],["traits",[]]]]],["bag",37],["cards",[[-3,"ambush"],[-2,"ambush"],[-1,"ambush"],[0,"ambush"]]]],[[],[]],[[]]]
		self.m1_out = json.dumps([0,[["population",1,3]],[],[[1,2]],[]])
		self.m2_in = [[["id",63],["species",[[["food",0],["body",0],["population",1],["traits",[]]]]],["bag",95],["cards",[[-3,"ambush"],[-2,"ambush"],[-1,"ambush"],[0,"ambush"],[1,"ambush"]]]],[[],[]],[[]]]
		self.m2_out = json.dumps([0,[["population",1,3]],[["body",1,4]],[[1,2]],[]])
		self.m3_in = [[["id",41],["species",[[["food",0],["body",0],["population",1],["traits",[]]]]],["bag",53],["cards",[[-3,"ambush"],[-2,"ambush"],[-1,"ambush"],[0,"ambush"],[1,"ambush"],[2,"ambush"]]]],[[],[]],[[]]]
		self.m3_out = json.dumps([0,[["population",1,3]],[["body",1,4]],[[1,2]],[[1,0,5]]])
		self.m4_in = [[["id",71],["species",[[["food",0],["body",0],["population",1],["traits",[]]]]],["bag",73],["cards",[[-3,"ambush"],[-2,"ambush"],[-1,"ambush"],[0,"ambush"],[1,"ambush"],[2,"ambush"],[3,"ambush"]]]],[[],[]],[[]]]
		self.m4_out = json.dumps([0,[["population",1,3]],[["body",1,4]],[[1,2]],[[1,0,5]]])
		
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
	
		del self.m1_in
		del self.m1_out
		del self.m2_in
		del self.m2_out
		del self.m3_in
		del self.m3_out
		del self.m4_in
		del self.m4_out
		
	def test_case1(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case1_in), self.case1_out)

	def test_case2(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case2_in), self.case2_out)

	def test_case3(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case3_in), self.case3_out)

	def test_case4(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case4_in), self.case4_out)

	def test_case5(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case5_in), self.case5_out)

	def test_case6(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case6_in), self.case6_out)

	def test_case7(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case7_in), self.case7_out)

	def test_case8(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case8_in), self.case8_out)

	def test_case9(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case9_in), self.case9_out)

	def test_case10(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case10_in), self.case10_out)

	def test_case11(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case11_in), self.case11_out)

	def test_case12(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case12_in), self.case12_out)

	def test_case13(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case13_in), self.case13_out)

	def test_case14(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case14_in), self.case14_out)

	def test_case15(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case15_in), self.case15_out)

	def test_case16(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case16_in), self.case16_out)

	def test_case17(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case17_in), self.case17_out)

	def test_case18(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case18_in), self.case18_out)

	def test_case19(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case19_in), self.case19_out)

	def test_case20(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case20_in), self.case20_out)

	def test_case21(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case21_in), self.case21_out)

	def test_case22(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case22_in), self.case22_out)

	def test_case23(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case23_in), self.case23_out)

	def test_case24(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case24_in), self.case24_out)

	def test_case25(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case25_in), self.case25_out)

	def test_case26(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case26_in), self.case26_out)

	def test_case27(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case27_in), self.case27_out)

	def test_case28(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case28_in), self.case28_out)

	def test_case29(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case29_in), self.case29_out)

	def test_case30(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case30_in), self.case30_out)

	def test_case31(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case31_in), self.case31_out)

	def test_case32(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case32_in), self.case32_out)

	def test_case34(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.case34_in), self.case34_out)

	def test_m1(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.m1_in), self.m1_out)

	def test_m2(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.m2_in), self.m2_out)

	def test_m3(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.m3_in), self.m3_out)

	def test_m4(self):
		self.assertEqual(xsilly_tester.xsilly_tester(self.m4_in), self.m4_out)

	
if __name__ == '__main__':
	unittest.main()
