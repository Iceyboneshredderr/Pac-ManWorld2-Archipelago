from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, DefaultOnToggle

def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in pacmanworld2_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list

class StartingLevel(Choice):
    """
    Determines which level you will have access to at the beginning of the game outside Pac-Village.
    """
    display_name = "Starting Level"
    option_the_bear_basics = 1
    option_b_doing_woods = 2
    option_ice_river_run = 3
    option_into_the_volcano = 4
    option_scuba_duba = 5
    option_all = 6
    default = 1

class AvoidEarlyBK(Toggle):
    """
    Determines if you will start with 1 key for your chosen starting episode.
    If all is selected, you are given 1 key for a random episode.
    """
    display_name = "Avoid Early BK"

class IncludeTimeTrials(Toggle):
    """
    If enabled, Time Trials are included in the locations.
    If Time Trials are disabled then there are more items than locations for this game alone.
    """
    display_name = "Include Time Trials"

@dataclass
class PacManWorld2Options(PerGameCommonOptions):
    StartingLevel:            StartingLevel
    IncludeTimeTrials:         IncludeTimeTrials
    AvoidEarlyBK:               AvoidEarlyBK

pacmanworld2_option_groups: Dict[str, List[Any]] = {
    "General Options": [StartingLevel, IncludeTimeTrials]
}

slot_data_options: List[str] = {
    "StartingLevel",
    "IncludeTimeTrials",
    "AvoidEarlyBK"
}