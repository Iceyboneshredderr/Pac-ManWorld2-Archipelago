from enum import IntEnum
from typing import NamedTuple, Optional
from BaseClasses import Location, Item, ItemClassification

class PacManWorld2Location(Location):
    game = "Pac-Man World 2"

class PacManWorld2Item(Item):
    game = "Pac-Man World 2"

class LevelType(IntEnum):
    pv = 1 # Pac-Village
    tbb = 2 # The Bear Basics
    cc = 3 # Canyon Chaos
    pdp = 4 # Pac-Dot Pond
    bf = 5 # Blinky's Frog
    bdw = 6 # B-Doing Woods
    tf = 7 # Treewood Forest
    bp = 8 # Butane Pain
    ibm = 9 # Inky's Blade-o-Matic
    irr = 10 # Ice River Run
    aa = 11 # Avalanhce Alley
    bm = 12 # Blade Mountain
    pr = 13 # Pinky's Revenge
    itv = 14 # Into the Volcano
    vp = 15 # Volcanic Panic
    mo = 16 # Magma Opus
    ctc = 17 # Clyde in the Caldera
    sd = 18 # Scuba Duba
    sa = 19 # Shark Attack
    ypm = 20 # Yellow Pac-Marine
    ws = 21 # Whale on a Sub
    hb = 22 # Haunted Boardwalk
    nc = 23 # Night Crawling
    gb = 24 # Ghost Bayou
    s = 25 # Spooky

class ItemData(NamedTuple):
    ap_code: Optional[int]
    classification: ItemClassification
    count: Optional[int] = 1

class EventData(NamedTuple):
    name:       str
    ap_code:    Optional[int] = None

class LocData(NamedTuple):
    ap_code: Optional[int]
    region: Optional[str]
    key_type: Optional[EpisodeType] = None
    key_requirement: Optional[int] = 0

level_type_to_name = {
    LevelType.pv:       "Pac-Village",
    LevelType.tbb:      "The Bear Basics",
    LevelType.cc:       "Canyon Chaos",
    LevelType.pdp:      "Pac-Dot Pond",
    LevelType.bf:       "Blinky's Frog",
    LevelType.bdw:      "B-Doing Woods",
    LevelType.tf:       "Treewood Forest",
    LevelType.bp:       "Butane Pain",
    LevelType.ibm:      "Inky's Blade-o-Matic",
    LevelType.irr:      "Ice River Run",
    LevelType.aa:       "Avalanche Alley",
    LevelType.bm:       "Blade Mountain",
    LevelType.pr:       "Pinky's Revenge",
    LevelType.itv:      "Into the Volcano",
    LevelType.vp:       "Volcanic Panic",
    LevelType.mo:       "Magma Opus",
    LevelType.ctc:      "Clyde in the Caldera",
    LevelType.sd:       "Scuba Duba",
    LevelType.sa:       "Shark Attack",
    LevelType.ypm:      "Yellow Pac-Marine",
    LevelType.ws:       "Whale on a Sub",
    LevelType.hb:       "Haunted Boardwalk",
    LevelType.nc:       "Night Crawling",
    LevelType.gb:       "Ghost Bayou",
    LevelType.s:        "Spooky"

}

level_type_to_shortened_name = {
    LevelType.pv:    "PV",
    LevelType.tbb:    "TBB",
    LevelType.cc:     "CC",
    LevelType.pdp:   "PDP",
    LevelType.bf:   "BF",
    LevelType.bdw:    "BDW",
    LevelType.tf:   "TF",
    LevelType.bp:   "BP",
    LevelType.ibm:  "IBM",
    LevelType.irr:  "IRR",
    LevelType.aa:   "AA",
    LevelType.bm:   "BM",
    LevelType.pr:   "PR",
    LevelType.itv:  "ITV",
    LevelType.vp:   "VP",
    LevelType.mo:   "MO",
    LevelType.ctc:  "CTC",
    LevelType.sd:   "SD",
    LevelType.sa:   "SA",
    LevelType.ypm:  "YPM",
    LevelType.ws:   "WS",
    LevelType.hb:   "HB",
    LevelType.nc:   "NC",
    LevelType.gb:   "GB",
    LevelType.s:    "S"

}