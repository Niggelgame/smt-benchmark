from matplotlib import pyplot as plt
import numpy as np

font_size = 10

def draw_plot(datas, pos, axis_ticks=None, output=None):
    """Create a violin plot
    
    data: nested array (for each compared data point) of nested array of data points, for each violin plot point in the array
    pos: array of x-axis positions for each violin plot, e. g. leave out space between test results
    output: file name of the output file
    """
    fig, ax = plt.subplots()
    for data in datas:
        ax.violinplot(data, pos, points=100, widths=0.3, showmeans=True, showextrema=True, showmedians=True, bw_method=0.5)
    # ax.violinplot([[v + 500 for v in d] for d in data], pos, points=100, widths=0.3, showmeans=True, showextrema=True, showmedians=True, bw_method=0.5)
    ax.set_yscale("log")
    if axis_ticks is not None:
        plt.xticks(rotation=-70)
        ax.set_xticks([i for i in range(0, len(axis_ticks))], labels=axis_ticks)

    ax.set_title("Results", fontsize=font_size)
    plt.show()
    # fig = plt.figure()
    if output is not None:
        fig.savefig(output)

# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html
def draw_bar_plot(data, axis_ticks, output=None):
    x = np.arange(len(tuple(axis_ticks)))
    width = 1 / (len(data) + 1)  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for runner, measurement in data:
        print(runner, measurement, x + width * multiplier)
        # only take first measurement
        measurement = [m[0] for m in measurement]

        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=runner)
        # ax.bar_label(rects, padding=3)
        multiplier += 1
    
    ax.set_yscale("log")
    plt.xticks(rotation=-70)
    ax.set_xticks(x + width, axis_ticks)

    ax.legend(loc='upper left', ncols=3)

    ax.set_ylabel('Time (s)')

    plt.show()

    if output is not None:
        fig.savefig(output)


results = {'HacksynthHackdelExtendedSygus': [{'p01_d1': 485306859, 'p01_d5': 1134595141, 'p02_d0': 450197579, 'p02_d1': 647734807, 'p02_d5': 2617871765, 'p03_d0': 362003230, 'p03_d1': 581104460, 'p03_d5': 1180876923, 'p04_d0': 372857139, 'p04_d1': 521544871, 'p04_d5': 1407682088, 'p05_d0': 390956751, 'p05_d1': 516141595, 'p05_d5': 1398797447, 'p06_d0': 378798037, 'p06_d1': 532757542, 'p06_d5': 1359567154, 'p07_d0': 636697512, 'p07_d1': 1141359453, 'p07_d5': 4650526530, 'p08_d0': 692293383, 'p08_d1': 1127460765, 'p08_d5': 4034647673, 'p09_d0': 875567989, 'p09_d1': 1535754798, 'p09_d5': 4085814456, 'p13_d0': 1072085714, 'p13_d1': 18039207718, 'p13_d5': 28484053057, 'p14_d0': 97981141626, 'p14_d1': 149753240051, 'p14_d5': 552779349799, 'p15_d0': 148759153608, 'p15_d1': 167591590054, 'p15_d5': 166636375334, 'p17_d0': 2189958860, 'p17_d1': 4059021031, 'p17_d5': 136936090964, 'p19_d0': 32003535852, 'p19_d1': 516056220519, 'p19_d5': 'timeout', 'p20_d0': 2160871412346, 'p20_d1': 'timeout', 'p20_d5': 'timeout'}], 'HacksynthHackdelFullSygus': [{'p01_d1': 484399345, 'p01_d5': 1143510753, 'p02_d0': 421832021, 'p02_d1': 557763605, 'p02_d5': 1635657355, 'p03_d0': 357445989, 'p03_d1': 585758987, 'p03_d5': 1170975680, 'p04_d0': 376412416, 'p04_d1': 510490570, 'p04_d5': 1400513551, 'p05_d0': 386732924, 'p05_d1': 514410725, 'p05_d5': 1381744365, 'p06_d0': 381003602, 'p06_d1': 531287920, 'p06_d5': 1330276955, 'p07_d0': 639592443, 'p07_d1': 1141078535, 'p07_d5': 4715845161, 'p08_d0': 684982794, 'p08_d1': 1122788440, 'p08_d5': 3966500107, 'p09_d0': 770766788, 'p09_d1': 1357575987, 'p09_d5': 4752075425, 'p13_d0': 317948933, 'p13_d1': 419993993, 'p13_d5': 582968933, 'p14_d0': 79536170165, 'p14_d1': 10952332044, 'p14_d5': 259044110973, 'p15_d0': 1314567441, 'p15_d1': 7147825377, 'p15_d5': 107633152564, 'p17_d0': 2142050586, 'p17_d1': 4052450906, 'p17_d5': 140184339597, 'p19_d0': 775358380278, 'p19_d1': 725902887085, 'p19_d5': 'timeout', 'p20_d0': 'timeout', 'p20_d1': 'timeout', 'p20_d5': 'timeout'}], 'cvc5-8bit-benchmark': [{'hd-01-d1-prog.sl': 7144530, 'hd-01-d5-prog.sl': 2036851847, 'hd-02-d0-prog.sl': 5029161, 'hd-02-d1-prog.sl': 6348687, 'hd-02-d5-prog.sl': 716927148, 'hd-03-d0-prog.sl': 4599835, 'hd-03-d1-prog.sl': 7163595, 'hd-03-d5-prog.sl': 4071069958, 'hd-04-d0-prog.sl': 6050568, 'hd-04-d1-prog.sl': 10193916, 'hd-04-d5-prog.sl': 667204934, 'hd-05-d0-prog.sl': 6693675, 'hd-05-d1-prog.sl': 9995411, 'hd-05-d5-prog.sl': 5183331746, 'hd-06-d0-prog.sl': 6056505, 'hd-06-d1-prog.sl': 8780617, 'hd-06-d5-prog.sl': 4809639028, 'hd-07-d0-prog.sl': 8423487, 'hd-07-d1-prog.sl': 37519642, 'hd-07-d5-prog.sl': 39972811464, 'hd-08-d0-prog.sl': 10359624, 'hd-08-d1-prog.sl': 13827980, 'hd-08-d5-prog.sl': 312728900732, 'hd-09-d0-prog.sl': 130028936, 'hd-09-d1-prog.sl': 51656203188, 'hd-09-d5-prog.sl': 2960498925706, 'hd-13-d0-prog.sl': 6144969, 'hd-13-d1-prog.sl': 6943117, 'hd-13-d5-prog.sl': 66063796, 'hd-14-d0-prog.sl': 3322604400, 'hd-14-d1-prog.sl': 110504773723, 'hd-14-d5-prog.sl': 'timeout', 'hd-15-d0-prog.sl': 5203768218, 'hd-15-d1-prog.sl': 116475051094, 'hd-15-d5-prog.sl': 'timeout', 'hd-17-d0-prog.sl': 21204260, 'hd-17-d1-prog.sl': 128107889, 'hd-17-d5-prog.sl': 'timeout', 'hd-19-d0-prog.sl': 'timeout', 'hd-19-d1-prog.sl': 'timeout', 'hd-19-d5-prog.sl': 'timeout', 'hd-20-d0-prog.sl': 'timeout', 'hd-20-d1-prog.sl': 'timeout', 'hd-20-d5-prog.sl': 'timeout'}], 'HacksynthStdHackdelBenchmark': [{'p01': 379447391, 'p02': 499612579, 'p03': 492246314, 'p04': 376415299, 'p05': 395870365, 'p06': 403792646, 'p07': 765856111, 'p08': 766214172, 'p09': 726024984, 'p10': 759562682, 'p11': 733699583, 'p12': 755601162, 'p13': 5898854384, 'p14': 1834742340, 'p15': 2832595098, 'p16': 1379855407, 'p17': 2187167734, 'p18': 561411574, 'p19': 10171062365, 'p20': 'timeout', 'p21': 2155054080229, 'p22': 2579063730231, 'p23': 'timeout', 'p24': 298674131790}]}

# results = {'HacksynthDownscalingCegis': [{'p01': 1391184408, 'p02': 1548986215, 'p03': 1196410789, 'p04': 1248714601, 'p05': 1268107498, 'p06': 1206015310, 'p07': 2071962737, 'p08': 2200933214, 'p09': 2136157346, 'p10': 92364158746, 'p11': 33856707486, 'p12': 17787772852, 'p13': 2663775894, 'p14': 5837056393, 'p15': 3257385411, 'p16': 145837926648, 'p17': 9370402343, 'p18': 17443796284, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 139972070}, {'p01': 1395263790, 'p02': 1552686404, 'p03': 1209669813, 'p04': 1258556007, 'p05': 1280120701, 'p06': 1199393896, 'p07': 2081707120, 'p08': 2189783587, 'p09': 2157811191, 'p10': 90418614412, 'p11': 34318725367, 'p12': 17490517464, 'p13': 2650894517, 'p14': 5849805974, 'p15': 3277436672, 'p16': 144965283472, 'p17': 9121169215, 'p18': 17714488501, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 139174559}, {'p01': 1403562911, 'p02': 1563310309, 'p03': 1204667771, 'p04': 1253613035, 'p05': 1286257765, 'p06': 1212066186, 'p07': 2071934712, 'p08': 2203805615, 'p09': 2109752722, 'p10': 91503923026, 'p11': 33927193734, 'p12': 17647281853, 'p13': 2640596895, 'p14': 5762908188, 'p15': 3266102581, 'p16': 145552930566, 'p17': 9270378705, 'p18': 17679627347, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 140166684}]}

# results = {'HacksynthDownscalingCegis': [{'p01': 1391184408, 'p02': 1548986215, 'p03': 1196410789, 'p04': 1248714601, 'p05': 1268107498, 'p06': 1206015310, 'p07': 2071962737, 'p08': 2200933214, 'p09': 2136157346, 'p10': 92364158746, 'p11': 33856707486, 'p12': 17787772852, 'p13': 2663775894, 'p14': 5837056393, 'p15': 3257385411, 'p16': 145837926648, 'p17': 9370402343, 'p18': 17443796284, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 139972070}, {'p01': 1395263790, 'p02': 1552686404, 'p03': 1209669813, 'p04': 1258556007, 'p05': 1280120701, 'p06': 1199393896, 'p07': 2081707120, 'p08': 2189783587, 'p09': 2157811191, 'p10': 90418614412, 'p11': 34318725367, 'p12': 17490517464, 'p13': 2650894517, 'p14': 5849805974, 'p15': 3277436672, 'p16': 144965283472, 'p17': 9121169215, 'p18': 17714488501, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 139174559}, {'p01': 1403562911, 'p02': 1563310309, 'p03': 1204667771, 'p04': 1253613035, 'p05': 1286257765, 'p06': 1212066186, 'p07': 2071934712, 'p08': 2203805615, 'p09': 2109752722, 'p10': 91503923026, 'p11': 33927193734, 'p12': 17647281853, 'p13': 2640596895, 'p14': 5762908188, 'p15': 3266102581, 'p16': 145552930566, 'p17': 9270378705, 'p18': 17679627347, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 140166684}], 'HacksynthDownscalingFA': [{'p01': 1392196357, 'p02': 1554332622, 'p03': 1201421367, 'p04': 1251878360, 'p05': 1267125798, 'p06': 1187473832, 'p07': 2055280573, 'p08': 2196505585, 'p09': 2122381794, 'p10': 90723870838, 'p11': 33922388793, 'p12': 17540797655, 'p13': 2664689871, 'p14': 5856140525, 'p15': 3238113110, 'p16': 179613179349, 'p17': 9406693552, 'p18': 12248070306, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 139802618}, {'p01': 1382279002, 'p02': 1562496959, 'p03': 1200256281, 'p04': 1251144957, 'p05': 1273547533, 'p06': 1187623682, 'p07': 2074758090, 'p08': 2201153244, 'p09': 2092622005, 'p10': 90914310125, 'p11': 34121934236, 'p12': 17759325603, 'p13': 2634320307, 'p14': 5805080820, 'p15': 3249334254, 'p16': 179144629385, 'p17': 9140053406, 'p18': 12105287611, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 140448402}, {'p01': 1397152735, 'p02': 1563733399, 'p03': 1209966092, 'p04': 1243998001, 'p05': 1276401866, 'p06': 1200848470, 'p07': 2051594980, 'p08': 2189679790, 'p09': 2104187614, 'p10': 91074543799, 'p11': 34420988101, 'p12': 17634381971, 'p13': 2663422988, 'p14': 5870153668, 'p15': 3260503143, 'p16': 180502646898, 'p17': 9278311146, 'p18': 11980057543, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 142605216}], 'HacksynthStdHackdelBenchmark': [{'p01': 376705721, 'p02': 503948745, 'p03': 492851238, 'p04': 375678877, 'p05': 394253995, 'p06': 410443094, 'p07': 768834977, 'p08': 759477316, 'p09': 725909877, 'p10': 757883022, 'p11': 740107058, 'p12': 757691487, 'p13': 6033868670, 'p14': 1824053517, 'p15': 2819863776, 'p16': 1390056488, 'p17': 2203734303, 'p18': 574515423, 'p19': 10156787226, 'p20': 'timeout', 'p21': 516587373133, 'p22': 'timeout', 'p23': 'timeout', 'p24': 302291121485}, {'p01': 377804644, 'p02': 494701718, 'p03': 496321005, 'p04': 375727295, 'p05': 395999184, 'p06': 406108172, 'p07': 765612120, 'p08': 771595789, 'p09': 725851079, 'p10': 752246473, 'p11': 741435530, 'p12': 745745606, 'p13': 5957517121, 'p14': 1828519289, 'p15': 2869439164, 'p16': 1380313234, 'p17': 2192628441, 'p18': 568349566, 'p19': 10105645762, 'p20': 'timeout', 'p21': 516496661383, 'p22': 'timeout', 'p23': 'timeout', 'p24': 299686999016}]}

# r ={'results': {'HacksynthDownscalingCegis': [{'p01': 1040652759, 'p02': 18826141025, 'p03': 1042896777, 'p04': 988109385, 'p05': 994664880, 'p06': 940123161, 'p07': 1721190544, 'p08': 1759811983, 'p09': 3706603053, 'p10': 277656421408, 'p11': 120313603037, 'p12': 203486059123, 'p13': 1794364613, 'p14': 'timeout', 'p15': 'timeout', 'p16': 19182622833, 'p17': 3516092227, 'p18': 8864422974, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}], 'HacksynthDownscalingFA': [{'p01': 1023043550, 'p02': 18864956801, 'p03': 1014610985, 'p04': 973965430, 'p05': 977544788, 'p06': 917758667, 'p07': 1700335989, 'p08': 1710204023, 'p09': 3677180064, 'p10': 275616721116, 'p11': 120647025353, 'p12': 203034817192, 'p13': 1795349009, 'p14': 'timeout', 'p15': 'timeout', 'p16': 19086091985, 'p17': 3493531365, 'p18': 48359699654, 'p19': 251837321, 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}], 'HacksynthStdHackdelBenchmark': [{'p01': 1032019720, 'p02': 19594077188, 'p03': 1504098011, 'p04': 1062318959, 'p05': 955562957, 'p06': 1186375567, 'p07': 3599718813, 'p08': 1877803989, 'p09': 2195919686, 'p10': 275413097235, 'p11': 121753126468, 'p12': 203751389345, 'p13': 1874115297, 'p14': 69309058986, 'p15': 24209691162, 'p16': 145195698533, 'p17': 41409602415, 'p18': 6574612836, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}]}, 'arguments': 'benchmark=cegis_hard_16,fa_hard_16,del_hard_16 output=outfile_downscaling_16 intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}

# r = {'results': {'HacksynthDownscalingCegis32': [{'p01': 1042001012, 'p02': 169125832281, 'p03': 1032710503, 'p04': 996860928, 'p05': 979480539, 'p06': 931551683, 'p07': 1721759311, 'p08': 1729307117, 'p09': 3778663768, 'p10': 727782505590, 'p11': 506955631623, 'p12': 270607286502, 'p13': 2110667787, 'p14': 'timeout', 'p15': 'timeout', 'p16': 19174502939, 'p17': 3662107181, 'p18': 82669348162, 'p19': 'timeout', 'p20': 196524735219, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}], 'HacksynthDownscalingFA32': [{'p01': 1015881824, 'p02': 167788213491, 'p03': 1020874504, 'p04': 976802019, 'p05': 976163217, 'p06': 922218434, 'p07': 1715216952, 'p08': 1718026647, 'p09': 3664334091, 'p10': 727811578263, 'p11': 510522202734, 'p12': 273253248390, 'p13': 1903800183, 'p14': 'timeout', 'p15': 'timeout', 'p16': 19205067594, 'p17': 3480547403, 'p18': 46079306855, 'p19': 254736474, 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}], 'HacksynthStdHackdelBenchmark32': [{'p01': 1353500108, 'p02': 169365561450, 'p03': 1300612740, 'p04': 1100990932, 'p05': 1094071056, 'p06': 965384924, 'p07': 2225997813, 'p08': 4924698921, 'p09': 6060437620, 'p10': 736974887030, 'p11': 282589524893, 'p12': 609817228552, 'p13': 4410303042, 'p14': 87254612147, 'p15': 36116567575, 'p16': 428731218194, 'p17': 123268425395, 'p18': 49660584174, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}]}, 'arguments': 'benchmark=cegis_hard_32,fa_hard_32,del_hard_32 output=outfile_downscaling_32 intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}

r = {'results': {'HacksynthStdHackdelBenchmarkBrahma': [{'p01': 422696856, 'p02': 1019827324, 'p03': 618294046, 'p04': 359579596, 'p05': 372752219, 'p06': 365235338, 'p07': 1571901036, 'p08': 1535458173, 'p09': 1283093825, 'p10': 1428873509, 'p11': 1320406904, 'p12': 1309012995, 'p13': 40143216232, 'p14': 7125434407, 'p15': 9613521565, 'p16': 10399364771, 'p17': 31500839130, 'p18': 956888216, 'p19': 221731682051, 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}], 
                 #'HacksynthStdHackdelBenchmark': [{'p01': 414513493, 'p02': 814015189, 'p03': 485499114, 'p04': 379734915, 'p05': 410653511, 'p06': 392453823, 'p07': 694194635, 'p08': 932414591, 'p09': 829966609, 'p10': 949680029, 'p11': 779771452, 'p12': 889818224, 'p13': 2700928421, 'p14': 2122685835, 'p15': 2144246600, 'p16': 1329545394, 'p17': 2915764929, 'p18': 624130995, 'p19': 9131945077, 'p20': 'timeout', 'p21': 1362475807981, 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}]
                 'HacksynthStdHackdelBenchmark': [{'p01': 414513493, 'p02': 814015189, 'p03': 485499114, 'p04': 379734915, 'p05': 410653511, 'p06': 392453823, 'p07': 694194635, 'p08': 932414591, 'p09': 829966609, 'p10': 949680029, 'p11': 779771452, 'p12': 889818224, 'p13': 2700928421, 'p14': 2122685835, 'p15': 2144246600, 'p16': 1329545394, 'p17': 2915764929, 'p18': 624130995, 'p19': 9131945077, 'p20': 'timeout', 'p21': 1362475807981, 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}]}, 'arguments': 'benchmark=hacksynth_std_hackdel_benchmark_brahma.py,hacksynth_solver_sygus_comp.py,hacksynth_solver_comp_constant_modes_count.py,hacksynth_solver_comp_constant_modes_free.py,hacksynth_solver_comp_constant_modes_set.py output=brahma_otherdiff_cmp_constset_cmp intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}
paper = {'results': {'HacksynthStdHackdelBenchmarkBrahmaPaper': [{'p01': 1738659593, 'p02': 35884761653, 'p03': 837017324, 'p04': 1050278080, 'p05': 3111701792, 'p06': 3040827701, 'p07': 16183441698, 'p08': 6048378227, 'p09': 48918563584, 'p10': 65068104791, 'p11': 28418232452, 'p12': 3038712487, 'p13': 1174725541, 'p14': 163945948188, 'p15': 129761542541, 'p16': 'timeout', 'p17': 209596049626, 'p18': 6942822701, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 220644054857}]}, 'arguments': 'benchmark=hacksynth_std_hackdel_benchmark_brahma_paper.py output=brahma_paper_res intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}
results = r['results']
results['HacksynthStdHackdelBenchmarkBrahmaPaper'] = paper['results']['HacksynthStdHackdelBenchmarkBrahmaPaper']
results['HacksynthStdHackdelBenchmarkHard'] = [{'p01': 909042225, 'p02': 1978077730, 'p03': 1355255585, 'p04': 885121279, 'p05': 1007673925, 'p06': 933822675, 'p07': 1729542022, 'p08': 1621956917, 'p09': 2045918611, 'p10': 105708363072, 'p11': 25205620732, 'p12': 104399577683, 'p13': 3621686581, 'p14': 16675826252, 'p15': 7490137787, 'p16': 64640965294, 'p17': 4288572421, 'p18': 4724227590, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 899804533023}]


merged_data = {} # {benchmark_name: { test_name: [result1, result2, ...], test_name2: ...}}
for (key, rounds) in results.items():
    data = {}
    if len(rounds) < 1:
        continue
    for test in rounds[0].keys():
        data[test] = []
        for it in rounds:
            data[test].append(it[test] / (10 ** 9) if it[test] != 'timeout' else 5000)
    merged_data[key] = data

keys = ['HacksynthStdHackdelBenchmarkBrahmaPaper']
# keys = ['cvc5-64bit-benchmark']
diff = ""


dat_data = [["test", "data"]]
columns = []
for test_name in merged_data[keys[0]].keys():
    if not test_name.endswith(diff):
        continue
    dis_name = test_name.replace(diff, "")
    columns.append(dis_name)
    dat_data.append([dis_name] + [str(merged_data[key][test_name][0]) for key in keys])

for line in dat_data:
    print("\t".join(line))

print()
print("{" + (", ".join(columns)) + "}")


# exit(0)


double_array_format = {} # {benchmark_name: [[result1, result2, ...], [result1, result2, ...]]}
for (key, data) in merged_data.items():
    double_array_format[key] = [v for v in data.values()]

print(double_array_format)

draw_bar_plot(
    [('HacksynthStdHackdelBenchmarkBrahma', double_array_format["HacksynthStdHackdelBenchmarkBrahma"]), 
     ('HacksynthStdHackdelBenchmarkHard', double_array_format["HacksynthStdHackdelBenchmarkHard"]), 
     ('HacksynthStdHackdelBenchmarkBrahmaPaper', double_array_format["HacksynthStdHackdelBenchmarkBrahmaPaper"])
     # ('HacksynthDownscalingFA32', double_array_format["HacksynthDownscalingFA32"]), 
     # ('HacksynthStdHackdelBenchmark32', double_array_format["HacksynthStdHackdelBenchmark32"])
     ], 
     # [i for i in range(0, 24)], 
     axis_ticks=merged_data["HacksynthStdHackdelBenchmarkBrahma"].keys(), 
     output="output.svg"
     )