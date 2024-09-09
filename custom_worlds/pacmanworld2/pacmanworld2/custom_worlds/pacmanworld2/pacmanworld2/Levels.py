# This contains the list of levels in Pac-Man World 2.
#Region 1
level_table = {
    "Pac Village": {
        "level_index": 0,
        "pac-dots": 142,
        "apples": 4,
        "cherries": 6,
        "melons": 8,
        "strawberries": 6,
        "tokens": 8,
    },
    "The Bear Basics": {
        "level_index": 1,
        "pac-dots": 327,
        "apples": 3,
        "cherries": 6,
        "melons": 2,
        "oranges": 1,
        "strawberries": 6,
        "tokens": 8,
    },
    "Canyon Chaos": {
        "level_index": 2,
        "pac-dots": 178,
        "apples": 5,
        "cherries": 14,
        "melons": 3,
        "oranges": 7,
        "strawberries": 8,
        "tokens": 8,
    },
    "Pac-Dot Pond": {
        "pac-dots": 142,
        "apples": 9,
        "cherries": 9,
        "melons": 5,
        "oranges": 9,
        "strawberries": 7,
        "tokens": 8,
    },
    "Blinky's Frog": {
        "level_index": 4,
    },

#Region 2
    "B-Doing Woods": {
        "level_index": 5,
        "pac-dots": 217,
        "apples": 4,
        "cherries": 6,
        "melons": 2,
        "oranges": 9,
        "strawberries": 9,
        "tokens": 8,
    },
    "Treewood Forest": {
        "level_index": 6,
        "pac-dots": 194,
        "apples": 4,
        "cherries": 5,
        "melons": 3,
        "oranges": 5,
        "strawberries": 6,
        "tokens": 8,
    },
    "Butane Pain": {
        "level_index": 7,
        "pac-dots": 243,
        "apples": 2,
        "cherries": 5,
        "melons": 2,
        "oranges": 8,
        "strawberries": 4,
        "tokens": 8,
    },
    "Inky's Blade-o-Matic": {
        "level_index": 8,
    },

#Region 3
    "Ice River Run": {
        "level_index": 9,
        "pac-dots": 333,
        "apples": 8,
        "cherries": 6,
        "oranges": 2,
        "strawberries": 11,
        "tokens": 8,
    },
    "Avalanche Alley": {
        "level_index": 10,
        "pac-dots": 297,
        "apples": 36,
        "cherries": 24,
        "melons": 4,
        "strawberries": 33,
        "tokens": 8,
    },
    "Blade Mountain": {
        "level_index": 11,
        "pac-dots": 216,
        "apples": 7,
        "cherries": 22,
        "melons": 1,
        "oranges": 1,
        "strawberries": 23,
        "tokens": 8,
    },
    "Pinky's Revenge": {
        "level_index": 12,
    },
  
  #Region 4
    "Into the Volcano": {
        "level_index": 13,
        "pac-dots": 200,
        "apples": 3,
        "cherries": 3,
        "melons": 1,
        "oranges": 2,
        "strawberries": 2,
        "tokens": 8,
    },
    "Volcanic Panic": {
        "level_index": 14,
        "pac-dots": 310,
        "apples": 5,
        "cherries": 4,
        "melons": 3,
        "oranges": 2,
        "strawberries": 6,
        "tokens": 8,
    },
    "Magma Opus": {
        "level_index": 15,
        "pac-dots": 226,
        "apples": 4,
        "cherries": 5,
        "melons": 2,
        "oranges": 5,
        "tokens": 8,
    },
    "Clyde in the Caldera": {
        "level_index": 16,
    },
  
  #Region 5
    "Scuba Duba": {
        "level_index": 17,
        "pac-dots": 133,
        "apples": 4,
        "cherries": 7,
        "melons": 6,
        "oranges": 4,
        "strawberries": 8,
        "tokens": 8,
    },
    "Shark Attack": {
        "level_index": 18,
        "pac-dots": 111,
        "apples": 5,
        "cherries": 10,
        "melons": 3,
        "oranges": 5,
        "strawberries": 7,
        "tokens": 8,
    },
    "Yellow Pac-Marine": {
        "level_index": 19,
        "apples": 2,
        "cherries": 20,
        "oranges": 5,
    },
    "Whale on a Sub": {
        "level_index": 20,
    },
  
#Region 6
    "Haunted Boardwalk": {
        "level_index": 21,
        "pac-dots": 153,
        "apples": 8,
        "cherries": 13,
        "melons": 9,
        "oranges": 6,
        "strawberries": 4,
        "tokens": 8,
    },
    "Night Crawling": {
        "level_index": 22,
        "pac-dots": 255,
        "apples": 4,
        "cherries": 2,
        "melons": 2,
        "oranges": 1,
        "strawberries": 1,
        "tokens": 8,
    },
    "Ghost Bayou": {
        "level_index": 23,
        "pac-dots": 535,
        "apples": 13,
        "cherries": 12,
        "melons": 13,
        "strawberries": 21,
        "tokens": 8,
    },
    "Spooky": {
        "level_index": 24,
    },


    # Not sure if the info below for the Warps is needed.
    "Pac Village Warp": {
        "level_index": 25,
    },
    "Ghost Bayou Warp": {
        "level_index": 26,
    },
},

level_table_with_global = {
    **level_table,
    "": {
        "level_index": 27,  # Global
        "tokens": 144, # Unsure if needed/token count is totaled.
    },
},
