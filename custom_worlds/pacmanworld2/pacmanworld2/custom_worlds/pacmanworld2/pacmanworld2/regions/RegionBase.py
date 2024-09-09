from typing import Iterable, Callable, Optional
from BaseClasses import MultiWorld, Region
from ..GameID import pacmanworld2_name
from ..Locations import PacManWorld2Location, location_table


class PacManWorld2Region(Region):
    """
    Holds region information such as name, level name, number of tokens available, etc.
    """
    game: str = pacmandworld2_name
    level_name: str
    token_count: int

    def __init__(self, name: str, player: int, multiworld: MultiWorld, level_name: str = "", token_count: int = 0):
        formatted_name = f"{level_name} {name}".strip()
        super().__init__(formatted_name, player, multiworld)
        self.level_name = level_name
        self.token_count = token_count

    def add_special_locations(self, locations: Iterable[int], access_rule: Optional[Callable] = None):
        """
        Adds a Special Location to this region with the given access rule.
        Converts Game ID's to AP ID's for you.
        Special Locations should be matched alongside their respective
        Power Cell Locations, so you get 2 unlocks for these rather than 1.
        """
        for loc in locations:
            ap_id = Specials.to_ap_id(loc)
            self.add_pacman_locations(ap_id, location_table[ap_id], access_rule)

    def add_cache_locations(self, locations: Iterable[int], access_rule: Optional[Callable] = None):
        """
        Adds an Orb Cache Location to this region with the given access rule.
        Converts Game ID's to AP ID's for you.
        """
        for loc in locations:
            ap_id = Caches.to_ap_id(loc)
            self.add_pacman_locations(ap_id, location_table[ap_id], access_rule)

    def add_pacman_locations(self, ap_id: int, name: str, access_rule: Optional[Callable] = None):
        """
        Helper function to add Locations. Not to be used directly.
        """
        location = PacManWorld2Location(self.player, name, ap_id, self)
        if access_rule:
            location.access_rule = access_rule
        self.locations.append(location)