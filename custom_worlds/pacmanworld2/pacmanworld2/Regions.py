import typing

from Options import OptionError
from . import PacManWorld2World
from .Items import item_table
from .PacManWorld2Options import CompletionCondition
from .Rules import can_reach_orbs_global
from .regions import (PacVillageRegions as PacVillage,
                   TheBearBasicsRegions as TheBearBasics,
                   CanyonChaosRegions as CanyonChaos,
                   PacDotPondRegions as PacDotPond,
                   BlinkysFrogRegions as BlinkysFrog,
                   BDoingWoodsRegions as BDoingWoods,
                   TreewoodForestRegions as TreewoodForest,
                   ButanePainRegions as ButanePain,
                   InkysBladeoMaticRegions as InkysBladeoMatic,
                   IceRiverRunRegions as IceRiverRun,
                   AvalancheAlleyRegions as AvalancheAlley,
                   BladeMountainRegions as BladeMountain,
                   PinkysRevengeRegions as PinkysRevenge,
                   IntotheVolcanoRegions as IntotheVolcano,
                   VolcanicPanicRegions as VolcanicPanic,
                   MagmaOpusRegions as MagmaOpus,
                   ClydeintheCalderaRegions as ClydeintheCaldera,
                   ScubaDubaRegions as ScubaDuba,
                   SharkAttackRegions as SharkAttack,
                   YellowPacMarineRegions as YellowPacMarine,
                   WhaleonaSubRegions as WhaleonaSub,
                   HauntedBoardwalkRegions as HauntedBoardwalk,
                   NightCrawlingRegions as Nightcrawling,
                   GhostBayouRegions as GhostBayou,
                   SpookyRegions as Spooky,
                   PacVillageWarpRegions as PacVillageWarp,
                   GhostBayouWarpRegions as GhostBayou)
from .regions.RegionBase import PacManWorld2Region


def create_regions(world: PacManWorld2World):
    multiworld = world.multiworld
    options = world.options
    player = world.player

    # Always start with Menu.
    menu = PacManWorld2Region("Menu", player, multiworld)
    multiworld.regions.append(menu)

    # Build the special "Free 7 Scout Flies" Region. This is a virtual region always accessible to Menu.
    # The Locations within are automatically checked when you receive the 7th scout fly for the corresponding cell.
    free7 = PacManWorld2Region("'Free 7 Scout Flies' Power Cells", player, multiworld)
    free7.add_cell_locations(Cells.loc7SF_cellTable.keys())
    for scout_fly_cell in free7.locations:

        # Translate from Cell AP ID to Scout AP ID using game ID as an intermediary.
        scout_fly_id = Scouts.to_ap_id(Cells.to_game_id(typing.cast(int, scout_fly_cell.address)))
        scout_fly_cell.access_rule = lambda state, flies=scout_fly_id: state.has(item_table[flies], player, 7)
    multiworld.regions.append(free7)
    menu.connect(free7)

    # If Global Orbsanity is enabled, build the special Orbsanity Region. This is a virtual region always
    # accessible to Menu. The Locations within are automatically checked when you collect enough orbs.
    if options.enable_orbsanity == EnableOrbsanity.option_global:
        orbs = JakAndDaxterRegion("Orbsanity", player, multiworld)

        bundle_count = 2000 // world.orb_bundle_size
        for bundle_index in range(bundle_count):

            # Unlike Per-Level Orbsanity, Global Orbsanity Locations always have a level_index of 16.
            orbs.add_orb_locations(16,
                                   bundle_index,
                                   access_rule=lambda state, bundle=bundle_index:
                                   can_reach_orbs_global(state, player, world, bundle))
        multiworld.regions.append(orbs)
        menu.connect(orbs)

    # Build all regions. Include their intra-connecting Rules, their Locations, and their Location access rules.
    [pv] = PacVillage.build_regions("Pac-Village", world)
    [tbb, bb] = TheBearBasics.build_regions("The Bear Basics", world)
    [cc] = CanyonChaos.build_regions("CanyonChaos", world)
    [pdp, pp] = PacDotPond.build_regions("Pac-Dot Pond", world)
    [bf] = BlinkysFrog.build_regions("Blinky's Frog", world)
    [bdw, bw] = BDoingWoods.build_regions("B-Doing Woods", world)
    [tf] = TreewoodForest.build_regions("Treewood Forest", world)
    [bp] = ButanePain.build_regions("Butane Pain", world)
    [ibm, ib] = InkysBladeoMatic.build_regions("Inky's Blade-o-Matic", world)
    [irr, ir] = IceRiverRun.build_regions("Ice River Run", world)
    [aa] = AvalancheAlley.build_regions("Avalanche Alley", world)
    [bm] = BladeMountain.build_regions("Blade Mountain", world)
    [pr] = PinkysRevenge.build_regions("Pinky's Revenge", world)
    [itv, iv] = IntotheVolcano.build_regions("Into the Volcano", world)
    [vp] = VolcanicPanic.build_regions("Volcanic Panic", world)
    [mo] = MagmaOpus.build_regions("Magma Opus", world)
    [ctc] = ClydeintheCaldera.build_regions("Clyde in the Caldera", world)
    [sd] = ScubaDuba.build_regions("Scuba Duba", world)
    [sa] = SharkAttack.build_regions("Shark Attack", world)
    [ypm, yp] = YellowPacMarine.build_regions("Yellow Pac-Marine", world)
    [ws] = WhaleonaSub.build_regions("Whale on a Sub", world)
    [hb] = HauntedBoardwalk.build_regions("Haunted Boardwalk", world)
    [nc] = Nightcrawling.build_regions("Night Crawling", world)
    [gb] = GhostBayou.build_regions("Ghost Bayou", world)
    [s] = Spooky.build_regions("Spooky", world)

    # Configurable counts of cells for connector levels.
    fc_count = options.fire_canyon_cell_count.value
    mp_count = options.mountain_pass_cell_count.value
    lt_count = options.lava_tube_cell_count.value

    # Define the interconnecting rules.
    menu.connect(pv)
    pv.connect(tbb)
    tbb.connect(cc)
    cc.connect(pdp)
    pdp.connect(bf)
    bf.connect(bdw) # Blinky's Frog Boss Fight 1
    bdw.connect(tf)
    tf.connect(bp)
    bp.connect(ibm)
    ibm.connect(irr) # Inky's Blade-o-Matic Boss Fight 2
    irr.connect(aa)
    aa.connect(bm)
    bm.connect(pr)
    pr.connect(itv) # Pinky's Revenge Boss Fight 3
    itv.connect(vp)
    vp.connect(mo)
    mo.connect(ctc)
    ctc.connect(sd) # Clyde in the Caldera Boss Fight 4
    sd.connect(sa)
    sa.connect(ypm)
    ypm.connect(ws)
    ws.connect(hb) # Whale on a Sub Boss Fight 5
    hb.connect(nc)
    nc.connect(gb)
    gb.connect(s) # Spooky Boss Fight 6; Final

    # Set the completion condition.
    if options.jak_completion_condition == CompletionCondition.option_cross_fire_canyon:
        multiworld.completion_condition[player] = lambda state: state.can_reach(rv, "Region", player)

    elif options.jak_completion_condition == CompletionCondition.option_cross_mountain_pass:
        multiworld.completion_condition[player] = lambda state: state.can_reach(vc, "Region", player)

    elif options.jak_completion_condition == CompletionCondition.option_cross_lava_tube:
        multiworld.completion_condition[player] = lambda state: state.can_reach(gmc, "Region", player)

    elif options.jak_completion_condition == CompletionCondition.option_defeat_dark_eco_plant:
        multiworld.completion_condition[player] = lambda state: state.can_reach(fjp, "Region", player)

    elif options.jak_completion_condition == CompletionCondition.option_defeat_klaww:
        multiworld.completion_condition[player] = lambda state: state.can_reach(mp, "Region", player)

    elif options.jak_completion_condition == CompletionCondition.option_defeat_gol_and_maia:
        multiworld.completion_condition[player] = lambda state: state.can_reach(fb, "Region", player)

    elif options.jak_completion_condition == CompletionCondition.option_open_100_cell_door:
        multiworld.completion_condition[player] = lambda state: state.can_reach(fd, "Region", player)

    else:
        raise OptionError(f"{world.player_name}: Unknown completion goal ID "
                          f"({options.jak_completion_condition.value}).")
