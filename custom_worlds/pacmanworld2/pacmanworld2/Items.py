import random

from BaseClasses import Item, ItemClassification
from .Types import ItemData, PacManWorld2Item, LevelType, level_type_to_name, level_type_to_shortened_name
from .Locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import PacManWorld2World

def create_itempool(world: "PacManWorld2World") -> List[Item]:
    itempool: List[Item] = []

    #Select Starting Level Outside Pac-Village
    starting_level = (level_type_to_name[LevelType(world.options.StartingLevel)])
    if starting_level = "All":
        for level in pacworld2_level.access():
            del item_table[level]
    else:
        del item_table[starting_level]

    for name in item_table.access():
        item_type: ItemClassification = item_table.get(name).classification
        item_amount: int = item_table.get(name).count

        itempool += create_multiple_items(world, name, item_amount, item_type)

    victory = create_item(world, "Victory")
    world.multiworld.get_location("Beat Spooky", world.player).place_locked_item(victory)

    itempool += create_junk_items(world, get_total_locations(world) - len(itempool) - len(event_item_pairs) - 1)
    return itempool

def create_item(world: "PacManWorld2World", name:str) -> Item:
    data = item_table[name]
    return PacManWorld2Item(name, data.classification, data.ap_code, world.player)

def create_multiple_items(world: "PacManWorld2World", name: str, count: int = 1,
                        item_type: ItemClassification = ItemClassification.progression) -> List[Item]:
    data = item_table[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist += [PacManWorld2Item(name, item_type, data.ap_code, world.player)]

    return itemlist

def create_junk_items(world: "PacManWorld2World", count: int) -> List[Item]:
    junk_pool: List[Item] = []
    # For now, all junk has equal weights
    for i in range(count):
        junk_pool.append(world.create_item(world.random.choices(list(junk_items.levels()), l=1)[0]))
    return junk_pool

def set_level(starting_level:str):
    starting_level = f'{starting_level} Access'
    level = item_table [starting_level]
    updated_level = ItemData(level.ap_code, level.classification, level.count - 1)
    item_table.update({starting_level: updated_level})

pacworld2_level = {
    # List of All Levels

    "Pac-Village Access": ItemData(83000001, ItemClassification.progression, 0),
    
    "The Bear Basics Access": ItemData(83000002, ItemClassification.progression, 1),
    "Canyon Chaos Access": ItemData(83000003, ItemClassification.progression, 1),
    "Pac-Dot Pond Access": ItemData(83000004, ItemClassification.progression, 1),
    
    "B-Doing Woods Access": ItemData(83000005, ItemClassification.progression, 1),
    "Treewood Forest Access": ItemData(83000006, ItemClassification.progression, 1),
    "Butane Pain Access": ItemData(83000007, ItemClassification.progression, 1),

    "Ice River Run Access": ItemData(83000008, ItemClassification.progression, 1),
    "Avalanche Valley Access": ItemData(83000009, ItemClassification.progression, 1),
    "Blade Mountain Access": ItemData(83000010, ItemClassification.progression, 1),

    "Into the Volcano Access": ItemData(83000011, ItemClassification.progression, 1),
    "Volcanic Panic Access": ItemData(83000012, ItemClassification.progression, 1),
    "Magma Opus Access": ItemData(83000013, ItemClassification.progression, 1),
    "Scuba Duba Access": ItemData(83000014, ItemClassification.progression, 1),
    "Shark Attack Access": ItemData(83000015, ItemClassification.progression, 1),
    "Yellow Pac-Marine Access": ItemData(83000016, ItemClassification.progression, 1),

    "Haunted Boardwalk Access": ItemData(83000017, ItemClassification.progression, 1),
    "Night Crawling Access": ItemData(83000018, ItemClassification.progression, 1),
    "Ghost Bayou Access": ItemData(83000019, ItemClassification.progression, 1),

pacworld2_fruits = {
    # Level Fruits

    # Pac-Village Fruits
    "Pac-Village Apple": ItemData(83001004, ItemClassification.useful, 4),
    "Pac-Village Cherry": ItemData(83001005, ItemClassification.useful, 6),
    "Pac-Village Melon": ItemData(83001006, ItemClassification.useful, 8),
    "Pac-Village Strawberry": ItemData(83001007, ItemClassification.useful, 6),

    # The Bear Basics Fruits # Requires Jump; Rev Roll Butt-Bounce
    "The Bear Basics Apple": ItemData(83001008, ItemClassification.useful, 3),
    "The Bear Basics Cherry": ItemData(83001009, ItemClassification.useful, 6),
    "The Bear Basics Melon": ItemData(83001010, ItemClassification.useful, 2),
    "The Bear Basics Orange": ItemData(83001011, ItemClassification.useful, 1),
    "The Bear Basics Strawberry": ItemData(83001012, ItemClassification.useful, 6),

    # Canyon Chaos Fruits
    "Canyon Chaos Apple": ItemData(83001013, ItemClassification.useful, 5),
    "Canyon Chaos Cherry": ItemData(83001014, ItemClassification.useful, 14),
    "Canyon Chaos Melon": ItemData(83001015, ItemClassification.useful, 3),
    "Canyon Chaos Orange": ItemData(83001016, ItemClassification.useful, 7),
    "Canyon Chaos Strawberry": ItemData(83001017, ItemClassification.useful, 8),

    #Pac-Dot Pond Fruits
    "Pac-Dot Pond Apple": ItemData(83001018, ItemClassification.useful, 9),
    "Pac-Dot Pond Cherry": ItemData(83001019, ItemClassification.useful, 9),
    "Pac-Dot Pond Melons": ItemData(83001020, ItemClassification.useful, 5),
    "Pac-Dot Pond Orange": ItemData(83001021, ItemClassification.useful, 9),
    "Pac-Dot Pond Strawberry": ItemData(83004022, ItemClassification.useful, 7),

    #B-Doing Woods Fruits
    "B-Doing Woods Apple": ItemData(83001023, ItemClassification.useful, 4),
    "B-Doing Woods Cherry": ItemData(83001024, ItemClassification.useful, 6),
    "B-Doing Woods Melon": ItemData(83001025, ItemClassification.useful, 2),
    "B-Doing Woods Orange": ItemData(83001026, ItemClassification.useful, 9),
    "B-Doing Woods Strawberry": ItemData(83001027, ItemClassification.useful, 9),

    #Treewood Forest Fruits
    "Treewood Forest Apple": ItemData(83001027, ItemClassification.useful, 4),
    "Treewood Forest Cherry": ItemData(83001028, ItemClassification.useful, 5),
    "Treewood Forest Melon": ItemData(83001029, ItemClassification.useful, 3),
    "Treewood Forest Orange": ItemData(83001030, ItemClassification.useful, 5),
    "Treewood Forest Strawberry": ItemData(83001031, ItemClassification.useful, 6),

    #Butane Pain Fruits
    "Butane Pain Apple": ItemData(830010032, ItemClassification.useful, 2),
    "Butane Pain Cherry": ItemData(83001033, ItemClassification.useful, 5),
    "Butane Pain Melon": ItemData(83001034, ItemClassification.useful, 2),
    "Butane Pain Orange": ItemData(83001035, ItemClassification.useful, 8),
    "Butane Pain Strawberry": ItemData(83001036, ItemClassification.useful, 4),

    #Ice River Run Fruits
    "Ice River Run Apple": ItemData(83001037, ItemClassification.useful, 8),
    "Ice River Run Cherry": ItemData(83001038, ItemClassification.useful, 6),
    "Ice River Run Orange": ItemData(83001039, ItemClassification.useful, 2),
    "Ice River Run Strawberry": ItemData(83001040, ItemClassification.useful, 11),

    #Avalanche Alley Fruits
    "Avalanche Alley Apple": ItemData(83001041, ItemClassification.useful, 36),
    "Avalanche Alley Cherry": ItemData(83001042, ItemClassification.useful, 24),
    "Avalanche Alley Melon": ItemData(83001043, ItemClassification.useful, 4),
    "Avalanche Alley Strawberry": ItemData(83001044, ItemClassification.useful, 33),

    #Blade Mountain Fruits
    "Blade Mountain Apple": ItemData(83001045, ItemClassification.useful, 7),
    "Blade Mountain Cherry": ItemData(83001046, ItemClassification.useful, 22),
    "Blade Mountain Melon": ItemData(83001047, ItemClassification.useful, 1),
    "Blade Mountain Orange": ItemData(83001048, ItemClassification.useful, 1),
    "Blade Mountain Strawberry": ItemData(83001049, ItemClassification.useful, 23),

    #Into the Volcano Fruits
    "Into the Volcano Apple": ItemData(83001050, ItemClassification.useful, 3),
    "Into the Volcano Cherry": ItemData(83001051, ItemClassification.useful, 3),
    "Into the Volcano Melon": ItemData(83001052, ItemClassification.useful, 1),
    "Into the Volcano Orange": ItemData(83001053, ItemClassification.useful, 2),
    "Into the Volcano Strawberry": ItemData(83001054, ItemClassification.useful, 2),

    #Volcanic Panic Fruits
    "Volcanic Panic Apple": ItemData(83001055, ItemClassification.useful, 5),
    "Volcanic Panic Cherry": ItemData(83001056, ItemClassification.useful, 4),
    "Volcanic Panic Melon": ItemData(83001057, ItemClassification.useful, 3),
    "Volcanic Panic Orange": ItemData(83001058, ItemClassification.useful, 2),
    "Volcanic Panic Strawberry": ItemData(83001059, ItemClassification.useful, 6),

    #Magma Opus Fruits
    "Magma Opus Apple": ItemData(83001060, ItemClassification.useful, 4),
    "Magma Opus Cherry": ItemData(83001061, ItemClassification.useful, 5),
    "Magma Opus Melon": ItemData(83001062, ItemClassification.useful, 2),
    "Magma Opus Orange": ItemData(83001063, ItemClassification.useful, 5),

    #Scuba Duba Fruits
    "Scuba Duba Apple": ItemData(83001064, ItemClassification.useful, 4),
    "Scuba Duba Cherry": ItemData(83001065, ItemClassification.useful, 7),
    "Scuba Duba Melon": ItemData(83001066, ItemClassification.useful, 6),
    "Scuba Duba Orange": ItemData(83001067, ItemClassification.useful, 4),
    "Scuba Duba Strawberry": ItemData(83001068, ItemClassification.useful, 8),

    #Shark Attack Fruits
    "Shark Attack Apple": ItemData(83001069, ItemClassification.useful, 5),
    "Shark Attack Cherry": ItemData(83001070, ItemClassification.useful, 10),
    "Shark Attack Melon": ItemData(83001071, ItemClassification.useful, 3),
    "Shark Attack Orange": ItemData(83001072, ItemClassification.useful, 5),
    "Shark Attack Strawberry": ItemData(83001073, ItemClassification.useful, 7),

    #Yellow Pac-Marine Fruits
    "Yellow Pac-Marine Apple": ItemData(83001074, ItemClassification.useful, 2),
    "Yellow Pac-Marine Cherry": ItemData(83001075, ItemClassification.useful, 20),
    "Yellow Pac-Marine Orange": ItemData(83001076, ItemClassification.useful, 5),

    #Haunted Boardwalk Fruits
    "Haunted Boardwalk Apple": ItemData(83001077, ItemClassification.useful, 8),
    "Haunted Boardwalk Cherry": ItemData(83001078, ItemClassification.useful, 13),
    "Haunted Boardwalk Melon": ItemData(83001079, ItemClassification.useful, 9),
    "Haunted Boardwalk Orange": ItemData(83001080, ItemClassification.useful, 6),
    "Haunted Boardwalk Strawberry": ItemData(83001081, ItemClassification.useful, 4),

    #Night Crawling Fruits
    "Night Crawling Apple": ItemData(83001082, ItemClassification.useful, 4),
    "Night Crawling Cherry": ItemData(83001083, ItemClassification.useful, 2),
    "Night Crawling Melon": ItemData(83001084, ItemClassification.useful, 2),
    "Night Crawling Orange": ItemData(83001085, ItemClassification.useful, 1),
    "Night Crawling Strawberry": ItemData(83001086, ItemClassification.useful, 1),

    #Ghost Bayou Fruits
    "Ghost Bayou Apple": ItemData(83001087, ItemClassification.useful, 13),
    "Ghost Bayou Cherry": ItemData(83001088, ItemClassification.useful, 12),
    "Ghost Bayou Melon": ItemData(83001089, ItemClassification.useful, 13),
    "Ghost Bayou Strawberry": ItemData(83001090, ItemClassification.useful, 21),
}

pacworld2_tokens = {
    #Tokens
    
    "Pac-Village Token": ItemData(83002091, ItemClassification.useful, 8),
    "The Bear Basics Token": ItemData(83002092, ItemClassification.useful, 8),
    "Canyon Chaos Token": ItemData(83002093, ItemClassification.useful, 8),
    "Pac-Dot Pond Token": ItemData(83002094, ItemClassification.useful, 8),
    "B-Doing Woods Token": ItemData(83002095, ItemClassification.useful, 8),
    "Treewood Forest Token": ItemData(83002096, ItemClassification.useful, 8),
    "Butane Pain Token": ItemData(83002097, ItemClassification.useful, 8),
    "Ice River Run Token": ItemData(83002098, ItemClassification.useful, 8),
    "Avalanche Alley Token": ItemData(83002099, ItemClassification.useful, 8),
    "Blade Mountain Token": ItemData(83002100, ItemClassification.useful, 8),
    "Into the Volcano Token": ItemData(83002101, ItemClassification.useful, 8),
    "Volcanic Panic Token": ItemData(83002102, ItemClassification.useful, 8),
    "Magma Opus Token": ItemData(83002103, ItemClassification.useful, 8),
    "Scuba Duba Token": ItemData(83002104, ItemClassification.useful, 8),
    "Shark Attack Token": ItemData(83002105, ItemClassification.useful, 8),
    "Haunted Boardwalk Token": ItemData(83002106, ItemClassification.useful, 8),
    "Night Crawling Token": ItemData(83002107, ItemClassification.useful, 8),
    "Ghost Bayou Token": ItemData(83002108, ItemClassification.useful, 8),
}

pacworld2_galaxians = {
    #Galaxian Fruits
    
    "Canyon Chaos Galaxian": ItemData(83003109, ItemClassification.useful, 1),
    "Pac-Dot Pond Galaxian": ItemData(83003110, ItemClassification.useful, 1),
    "B-Doing Woods Galaxian": ItemData(83003111, ItemClassification.useful, 1),
    "Treewood Forest Galaxian": ItemData(83003112, ItemClassification.useful, 1),
    "Butane Pain Galaxian": ItemData(83003113, ItemClassification.useful, 1),
    "Ice River Run Galaxian": ItemData(83003114, ItemClassification.useful, 1),
    "Avalanche Alley Galaxian": ItemData(83003115, ItemClassification.useful, 1),
    "Blade Mountain Galaxian": ItemData(83003116, ItemClassification.useful, 1),
    "Into the Volcano Galaxian": ItemData(83003117, ItemClassification.useful, 1),
    "Volcanic Panic Galaxian": ItemData(83003118, ItemClassification.useful, 1),
    "Magma Opus Galaxian": ItemData(83003119, ItemClassification.useful, 1),
    "Scuba Duba Galaxian": ItemData(83003120, ItemClassification.useful, 1),
    "Shark Attack Galaxian": ItemData(83003121, ItemClassification.useful, 1),
    "Haunted Boardwalk Galaxian": ItemData(83003122, ItemClassification.useful, 1),
    "Ghost Bayou Galaxian": ItemData(83003123, ItemClassification.useful, 1)
}

pacworld2_pacdots = {

    #Pac Dots

    "Pac Village Pac-Dot": ItemData(83004124, ItemClassification.filler, 142),
    "The Bear Basics Pac-Dot": ItemData(83004125, ItemClassification.filler, 327),
    "Canyon Chaos Pac-Dot": ItemData(83004126, ItemClassification.filler, 178),
    "Pac-Dot Pond Pac-Dot": ItemData(83004127, ItemClassification.filler, 142),
    "B-Doing Woods Pac-Dot": ItemData(83004128, ItemClassification.filler, 217),
    "Treewood Forest Pac-Dot": ItemData(83004129, ItemClassification.filler, 194),
    "Butane Pain Pac-Dot": ItemData(83004130, ItemClassification.filler, 243),
    "Ice River Run Pac-Dot": ItemData(83004131, ItemClassification.filler, 333),
    "Avalanche Valley Pac-Dot": ItemData(83004132, ItemClassification.filler, 297),
    "Blade Mountain Pac-Dot": ItemData(83004133, ItemClassification.filler, 216),
    "Into the Volcano Pac-Dot": ItemData(83004134, ItemClassification.filler, 200),
    "Volcanic Panic Pac-Dot": ItemData(83004135, ItemClassification.filler, 310),
    "Magma Opus Pac-Dot": ItemData(83004136, ItemClassification.filler, 226),
    "Scuba Duba Pac-Dot": ItemData(83004137, ItemClassification.filler, 133),
    "Shark Attack Pac-Dot": ItemData(83004138, ItemClassification.filler, 111),
    "Haunted Boardwalk Pac-Dot": ItemData(83004139, ItemClassification.filler, 153),
    "Night Crawling Pac-Dot": ItemData(83004140, ItemClassification.filler, 255),
    "Ghost Bayou Pac-Dot": ItemData(83004141, ItemClassification.filler, 535)
}

pacworld2_victory = {
    # Victory
    "Victory": ItemData(83005109, ItemClassification.progression, 0)

}

pac_bosses = {
    # Pac-Man Boss Levels
    "Blinky's Frog": ItemData(83006110, ItemClassification.progression),
    "Inky's Blade-o-Matic": ItemData(83006111, ItemClassification.progression),
    "Pinky's Revenge": ItemData(83006112, ItemClassification.progression),
    "Clyde in the Caldera": ItemData(83006113, ItemClassification.progression),
    "Whale on a Sub": ItemData(83006114, ItemClassification.progression),
    "Spooky": ItemData(83006115, ItemClassification.progression),
}

junk_items = {
    #Junk
    "Extra Life": ItemData(83007116, ItemClassification.filler, 0),
    "Life Wedge": ItemData(83007117, ItemClassification.filler, 0)
}

pacworld2_moves = {

    # Progressive Moves
    "Butt Bounce": ItemData(83000001, ItemClassification.progression),
    "Rev Roll": ItemData(83000002, ItemClassification.progression),
    "Jump": ItemData(83000003, ItemClassification.progression),
    "Flip Kick": ItemData(8300000000000000000, ItemClassification.progression)
}

item_table = {
    **pacworld2_moves,
    **pacworld2_fruits,
    **pacworld2_tokens,
    **pacworld2_galaxians,
    **pacworld2_victory
    **pac_bosses,
    **junk_items
}

event_item_pairs: Dict[str, str] = {
    "Beat Blinky's Frog": "Beat Blinky's Frog",
    "Beat Inky's Blade-o-Matic": "Beat Inky's Blade-o-Matic",
    "Beat Pinky's Revenge": "Beat Pinky's Revenge",
    "Beat Clyde in the Caldera": "Beat Clyde in the Caldera",
    "Beat Whale on a Sub": "Beat Whale on a Sub",
    "Beat Spooky": "Beat Spooky"
}