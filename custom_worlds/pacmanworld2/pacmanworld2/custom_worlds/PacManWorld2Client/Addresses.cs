using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PacManWorld2AP

{
    public class Addresses
    {
        public int CurrentApples = 0x005f8d7c;
        public int CurrentCherries = 0x005f8d70;
        public int CurrentGalaxians = 0x005f8d84;
        public int CurrentMelons = 0x005f8d80;
        public int CurrentOranges = 0x005f8d78;
        public int CurrentGalaxians = 0x005f8d84;

        public int CurrentPacDots = 0x005b9f50;
        public int GalaxianMazeFlag = 0x005b7564;

        /*Note 1 = In a Galaxian Maze
        Use for Galaxian Maze achievements, and for Trigger*/

        public int LevelID = 0x0048f094;

        // 0x00 = Pac Village
        // 0x01 = The Bear Basics
        // 0x02 = Canyon Chaos
        // 0x03 = Pac-Dot Pond
        // 0x04 = Blinky's Frog - Boss
        // 0x05 = B-Doing Woods
        // 0x06 = Treewood Forest
        // 0x07 = Butane Pain
        // 0x08 = Inky's Blade-o-Matic - Boss
        // 0x09 = Ice River Run
        // 0x0a = Avalanche Valley
        // 0x0b = Blade Mountain
        // 0x0c = Pinky's Revenge - Boss
        // 0x0d = Into the Volcano
        // 0x0e = Volcanic Panic
        // 0x0f = Magma Opus
        // 0x10 = Clyde in the Caldera - Boss
        // 0x11 = Scuba Duba
        // 0x12 = Shark Attack
        // 0x13 = Yellow Pac-Marine
        // 0x14 = Whale on a Sub - Boss
        // 0x15 = Haunted Boardwalk
        // 0x16 = Night Crawling
        // 0x17 = Ghost Bayou
        // 0x18 = Spooky - Final Boss
        // 0x19 = Pac-Village Warp
        // 0x1a = Ghost Bayou Warp
        
        /*Notes:
        -Flips to 0 briefly when the player completes or exits a level.
        -This value is also applicable when Pac-Man is standing over the level dot in the overworld.*/
        
    }
}