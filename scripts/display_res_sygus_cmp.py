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


# results = {'HacksynthHackdelExtendedSygus': [{'p01_d1': 485306859, 'p01_d5': 1134595141, 'p02_d0': 450197579, 'p02_d1': 647734807, 'p02_d5': 2617871765, 'p03_d0': 362003230, 'p03_d1': 581104460, 'p03_d5': 1180876923, 'p04_d0': 372857139, 'p04_d1': 521544871, 'p04_d5': 1407682088, 'p05_d0': 390956751, 'p05_d1': 516141595, 'p05_d5': 1398797447, 'p06_d0': 378798037, 'p06_d1': 532757542, 'p06_d5': 1359567154, 'p07_d0': 636697512, 'p07_d1': 1141359453, 'p07_d5': 4650526530, 'p08_d0': 692293383, 'p08_d1': 1127460765, 'p08_d5': 4034647673, 'p09_d0': 875567989, 'p09_d1': 1535754798, 'p09_d5': 4085814456, 'p13_d0': 1072085714, 'p13_d1': 18039207718, 'p13_d5': 28484053057, 'p14_d0': 97981141626, 'p14_d1': 149753240051, 'p14_d5': 552779349799, 'p15_d0': 148759153608, 'p15_d1': 167591590054, 'p15_d5': 166636375334, 'p17_d0': 2189958860, 'p17_d1': 4059021031, 'p17_d5': 136936090964, 'p19_d0': 32003535852, 'p19_d1': 516056220519, 'p19_d5': 'timeout', 'p20_d0': 2160871412346, 'p20_d1': 'timeout', 'p20_d5': 'timeout'}], 'HacksynthHackdelFullSygus': [{'p01_d1': 484399345, 'p01_d5': 1143510753, 'p02_d0': 421832021, 'p02_d1': 557763605, 'p02_d5': 1635657355, 'p03_d0': 357445989, 'p03_d1': 585758987, 'p03_d5': 1170975680, 'p04_d0': 376412416, 'p04_d1': 510490570, 'p04_d5': 1400513551, 'p05_d0': 386732924, 'p05_d1': 514410725, 'p05_d5': 1381744365, 'p06_d0': 381003602, 'p06_d1': 531287920, 'p06_d5': 1330276955, 'p07_d0': 639592443, 'p07_d1': 1141078535, 'p07_d5': 4715845161, 'p08_d0': 684982794, 'p08_d1': 1122788440, 'p08_d5': 3966500107, 'p09_d0': 770766788, 'p09_d1': 1357575987, 'p09_d5': 4752075425, 'p13_d0': 317948933, 'p13_d1': 419993993, 'p13_d5': 582968933, 'p14_d0': 79536170165, 'p14_d1': 10952332044, 'p14_d5': 259044110973, 'p15_d0': 1314567441, 'p15_d1': 7147825377, 'p15_d5': 107633152564, 'p17_d0': 2142050586, 'p17_d1': 4052450906, 'p17_d5': 140184339597, 'p19_d0': 775358380278, 'p19_d1': 725902887085, 'p19_d5': 'timeout', 'p20_d0': 'timeout', 'p20_d1': 'timeout', 'p20_d5': 'timeout'}], 'cvc5-8bit-benchmark': [{'hd-01-d1-prog.sl': 7144530, 'hd-01-d5-prog.sl': 2036851847, 'hd-02-d0-prog.sl': 5029161, 'hd-02-d1-prog.sl': 6348687, 'hd-02-d5-prog.sl': 716927148, 'hd-03-d0-prog.sl': 4599835, 'hd-03-d1-prog.sl': 7163595, 'hd-03-d5-prog.sl': 4071069958, 'hd-04-d0-prog.sl': 6050568, 'hd-04-d1-prog.sl': 10193916, 'hd-04-d5-prog.sl': 667204934, 'hd-05-d0-prog.sl': 6693675, 'hd-05-d1-prog.sl': 9995411, 'hd-05-d5-prog.sl': 5183331746, 'hd-06-d0-prog.sl': 6056505, 'hd-06-d1-prog.sl': 8780617, 'hd-06-d5-prog.sl': 4809639028, 'hd-07-d0-prog.sl': 8423487, 'hd-07-d1-prog.sl': 37519642, 'hd-07-d5-prog.sl': 39972811464, 'hd-08-d0-prog.sl': 10359624, 'hd-08-d1-prog.sl': 13827980, 'hd-08-d5-prog.sl': 312728900732, 'hd-09-d0-prog.sl': 130028936, 'hd-09-d1-prog.sl': 51656203188, 'hd-09-d5-prog.sl': 2960498925706, 'hd-13-d0-prog.sl': 6144969, 'hd-13-d1-prog.sl': 6943117, 'hd-13-d5-prog.sl': 66063796, 'hd-14-d0-prog.sl': 3322604400, 'hd-14-d1-prog.sl': 110504773723, 'hd-14-d5-prog.sl': 'timeout', 'hd-15-d0-prog.sl': 5203768218, 'hd-15-d1-prog.sl': 116475051094, 'hd-15-d5-prog.sl': 'timeout', 'hd-17-d0-prog.sl': 21204260, 'hd-17-d1-prog.sl': 128107889, 'hd-17-d5-prog.sl': 'timeout', 'hd-19-d0-prog.sl': 'timeout', 'hd-19-d1-prog.sl': 'timeout', 'hd-19-d5-prog.sl': 'timeout', 'hd-20-d0-prog.sl': 'timeout', 'hd-20-d1-prog.sl': 'timeout', 'hd-20-d5-prog.sl': 'timeout'}], 'HacksynthStdHackdelBenchmark': [{'p01': 379447391, 'p02': 499612579, 'p03': 492246314, 'p04': 376415299, 'p05': 395870365, 'p06': 403792646, 'p07': 765856111, 'p08': 766214172, 'p09': 726024984, 'p10': 759562682, 'p11': 733699583, 'p12': 755601162, 'p13': 5898854384, 'p14': 1834742340, 'p15': 2832595098, 'p16': 1379855407, 'p17': 2187167734, 'p18': 561411574, 'p19': 10171062365, 'p20': 'timeout', 'p21': 2155054080229, 'p22': 2579063730231, 'p23': 'timeout', 'p24': 298674131790}]}

# 32 Bit results
data = {'results': {'cvc5-32bit-benchmark': [{'hd-01-d1-prog.sl': 8134190, 'hd-01-d5-prog.sl': 12457190534, 'hd-02-d0-prog.sl': 5633817, 'hd-02-d1-prog.sl': 7627595, 'hd-02-d5-prog.sl': 15368212950, 'hd-03-d0-prog.sl': 5368262, 'hd-03-d1-prog.sl': 8117742, 'hd-03-d5-prog.sl': 14799483482, 'hd-04-d0-prog.sl': 7023948, 'hd-04-d1-prog.sl': 11893651, 'hd-04-d5-prog.sl': 19844588004, 'hd-05-d0-prog.sl': 8129372, 'hd-05-d1-prog.sl': 11271400, 'hd-05-d5-prog.sl': 12991388676, 'hd-06-d0-prog.sl': 7128930, 'hd-06-d1-prog.sl': 9925489, 'hd-06-d5-prog.sl': 6090044743, 'hd-07-d0-prog.sl': 9621951, 'hd-07-d1-prog.sl': 50469084, 'hd-07-d5-prog.sl': 'timeout', 'hd-08-d0-prog.sl': 12206207, 'hd-08-d1-prog.sl': 18007650, 'hd-08-d5-prog.sl': 162858042384, 'hd-09-d0-prog.sl': 143561840, 'hd-09-d1-prog.sl': 60452156084, 'hd-09-d5-prog.sl': 'timeout', 'hd-13-d0-prog.sl': 293536851, 'hd-13-d1-prog.sl': 68529513583, 'hd-13-d5-prog.sl': 'timeout', 'hd-14-d0-prog.sl': 3254563415, 'hd-14-d1-prog.sl': 122605982922, 'hd-14-d5-prog.sl': 'timeout', 'hd-15-d0-prog.sl': 5175543824, 'hd-15-d1-prog.sl': 108708836264, 'hd-15-d5-prog.sl': 'timeout', 'hd-17-d0-prog.sl': 40118180, 'hd-17-d1-prog.sl': 153896042, 'hd-17-d5-prog.sl': 'timeout', 'hd-19-d0-prog.sl': 'timeout', 'hd-19-d1-prog.sl': 'timeout', 'hd-19-d5-prog.sl': 'timeout', 'hd-20-d0-prog.sl': 'timeout', 'hd-20-d1-prog.sl': 'timeout', 'hd-20-d5-prog.sl': 'timeout'}], 'HacksynthHackdelFullSygus': [{'p01_d1': 595855809, 'p01_d5': 1035417864, 'p02_d0': 467092735, 'p02_d1': 633063154, 'p02_d5': 1112359449, 'p03_d0': 461852922, 'p03_d1': 583423373, 'p03_d5': 1107975225, 'p04_d0': 447391268, 'p04_d1': 622045670, 'p04_d5': 1151836708, 'p05_d0': 476853279, 'p05_d1': 686184717, 'p05_d5': 1120558652, 'p06_d0': 487829079, 'p06_d1': 643269278, 'p06_d5': 1169114577, 'p07_d0': 643127563, 'p07_d1': 970195774, 'p07_d5': 1706419044, 'p08_d0': 710383633, 'p08_d1': 1011680256, 'p08_d5': 2195361500, 'p09_d0': 'timeout', 'p09_d1': 25692589088, 'p09_d5': 2511821380, 'p13_d0': 1961742034, 'p13_d1': 6851794291, 'p13_d5': 5974066264, 'p14_d0': 263036326056, 'p14_d1': 17403683351, 'p14_d5': 'timeout', 'p15_d0': 11078993397, 'p15_d1': 51007217583, 'p15_d5': 493550464465, 'p17_d0': 1341040394, 'p17_d1': 1697777791, 'p17_d5': 6723191259, 'p19_d0': 16264506202, 'p19_d1': 1307325063887, 'p19_d5': 'timeout', 'p20_d0': 'timeout', 'p20_d1': 'timeout', 'p20_d5': 'timeout'}], 'HacksynthHackdelFullSygusDownscaling': [{'p01_d1': 448568626, 'p01_d5': 2752561548, 'p02_d0': 404058560, 'p02_d1': 505159916, 'p02_d5': 6286025808, 'p03_d0': 368540591, 'p03_d1': 549909955, 'p03_d5': 2906688753, 'p04_d0': 378168189, 'p04_d1': 582319983, 'p04_d5': 2922133452, 'p05_d0': 382966660, 'p05_d1': 539117811, 'p05_d5': 2880536623, 'p06_d0': 358194448, 'p06_d1': 506856544, 'p06_d5': 4038576117, 'p07_d0': 493600117, 'p07_d1': 909867743, 'p07_d5': 23202449590, 'p08_d0': 642138049, 'p08_d1': 1059491181, 'p08_d5': 8463338781, 'p09_d0': 701645387, 'p09_d1': 1536222648, 'p09_d5': 37123518963, 'p13_d0': 1433305902, 'p13_d1': 724393839, 'p13_d5': 3386545650, 'p14_d0': 289815252220, 'p14_d1': 8408751267, 'p14_d5': 1252749904582, 'p15_d0': 2040000819, 'p15_d1': 3806894726, 'p15_d5': 944869409354, 'p17_d0': 1442432287, 'p17_d1': 4877829957, 'p17_d5': 532923019910, 'p19_d0': 5919740555, 'p19_d1': 713022698822, 'p19_d5': 'timeout', 'p20_d0': 109005220665, 'p20_d1': 742678238091, 'p20_d5': 'timeout'}]}, 'arguments': 'benchmark=cvc5_32,sygus_32bit_down,sygus_32bit.py output=outfile_sygus_32 intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}
results = data['results']

# 64 bit results
#data = {'results': {'HacksynthHackdelFullSygusDownscaling64': [{'p01_d1': 581140651, 'p01_d5': 1096472149, 'p02_d0': 463845516, 'p02_d1': 621335152, 'p02_d5': 1138303554, 'p03_d0': 454553816, 'p03_d1': 594317542, 'p03_d5': 1227515660, 'p04_d0': 397584762, 'p04_d1': 634524105, 'p04_d5': 1024110995, 'p05_d0': 454218947, 'p05_d1': 611789096, 'p05_d5': 1147821198, 'p06_d0': 451625965, 'p06_d1': 612512041, 'p06_d5': 1143163956, 'p07_d0': 584292882, 'p07_d1': 858424205, 'p07_d5': 1799198998, 'p08_d0': 691261908, 'p08_d1': 998714572, 'p08_d5': 1792477261, 'p09_d0': 275049648453, 'p09_d1': 47252497605, 'p09_d5': 2172053947, 'p13_d0': 4236207309, 'p13_d1': 5651829201, 'p13_d5': 2232136972, 'p14_d0': 228142908135, 'p14_d1': 'timeout', 'p14_d5': 'timeout', 'p15_d0': 48209158272, 'p15_d1': 'timeout', 'p15_d5': 256579756714, 'p17_d0': 1039368734, 'p17_d1': 1782240963, 'p17_d5': 3619188326, 'p19_d0': 13243348668, 'p19_d1': 1074457449195, 'p19_d5': 'timeout', 'p20_d0': 'timeout', 'p20_d1': 'timeout', 'p20_d5': 'timeout'}], 'HacksynthHackdelFullSygus64': [{'p01_d1': 519362391, 'p01_d5': 5389914934, 'p02_d0': 386453871, 'p02_d1': 646750309, 'p02_d5': 6066281101, 'p03_d0': 344963335, 'p03_d1': 571277767, 'p03_d5': 4597133751, 'p04_d0': 379105533, 'p04_d1': 709371226, 'p04_d5': 5942206015, 'p05_d0': 419991982, 'p05_d1': 616932414, 'p05_d5': 12272101225, 'p06_d0': 336729738, 'p06_d1': 530254471, 'p06_d5': 3575226290, 'p07_d0': 505264839, 'p07_d1': 1008483133, 'p07_d5': 29358621614, 'p08_d0': 724920762, 'p08_d1': 1292304965, 'p08_d5': 11721604422, 'p09_d0': 650087018, 'p09_d1': 1374026716, 'p09_d5': 16437969320, 'p13_d0': 1773133562, 'p13_d1': 1091757243, 'p13_d5': 5243444595, 'p14_d0': 74557950177, 'p14_d1': 11417738149, 'p14_d5': 1602065603585, 'p15_d0': 1827395280, 'p15_d1': 7140072792, 'p15_d5': 694448283549, 'p17_d0': 1589125267, 'p17_d1': 2920534322, 'p17_d5': 774558451949, 'p19_d0': 38629702296, 'p19_d1': 342027097646, 'p19_d5': 'timeout', 'p20_d0': 103503027380, 'p20_d1': 864214768371, 'p20_d5': 'timeout'}], 'cvc5-64bit-benchmark': [{'hd-01-d1-prog.sl': 84223128, 'hd-01-d5-prog.sl': 10117909904, 'hd-02-d0-prog.sl': 6540212, 'hd-02-d1-prog.sl': 9721489, 'hd-02-d5-prog.sl': 166022952829, 'hd-03-d0-prog.sl': 6547050, 'hd-03-d1-prog.sl': 9974566, 'hd-03-d5-prog.sl': 77491208022, 'hd-04-d0-prog.sl': 8191242, 'hd-04-d1-prog.sl': 14367783, 'hd-04-d5-prog.sl': 52390153283, 'hd-05-d0-prog.sl': 9451158, 'hd-05-d1-prog.sl': 12993150, 'hd-05-d5-prog.sl': 68403607977, 'hd-06-d0-prog.sl': 9130281, 'hd-06-d1-prog.sl': 11545779, 'hd-06-d5-prog.sl': 41255325239, 'hd-07-d0-prog.sl': 11562276, 'hd-07-d1-prog.sl': 56373804, 'hd-07-d5-prog.sl': 'timeout', 'hd-08-d0-prog.sl': 14341715, 'hd-08-d1-prog.sl': 25498337, 'hd-08-d5-prog.sl': 'timeout', 'hd-09-d0-prog.sl': 137756026, 'hd-09-d1-prog.sl': 98732923205, 'hd-09-d5-prog.sl': 'timeout', 'hd-13-d0-prog.sl': 315667482, 'hd-13-d1-prog.sl': 74248003229, 'hd-13-d5-prog.sl': 'timeout', 'hd-14-d0-prog.sl': 3378817666, 'hd-14-d1-prog.sl': 134415028181, 'hd-14-d5-prog.sl': 'timeout', 'hd-15-d0-prog.sl': 5453485692, 'hd-15-d1-prog.sl': 170511617263, 'hd-15-d5-prog.sl': 'timeout', 'hd-17-d0-prog.sl': 108308860, 'hd-17-d1-prog.sl': 186265124, 'hd-17-d5-prog.sl': 'timeout', 'hd-19-d0-prog.sl': 'timeout', 'hd-19-d1-prog.sl': 'timeout', 'hd-19-d5-prog.sl': 'timeout', 'hd-20-d0-prog.sl': 20534993, 'hd-20-d1-prog.sl': 10486462, 'hd-20-d5-prog.sl': 10109642}]}, 'arguments': 'benchmark=hacksynth_full_sygus_64bit_downscaling_cegis.py,hacksynth_full_sygus_64bit.py,cvc5_64bit_benchmark.py output=outfile_sygus_64 intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}
#results = data['results']

# optimizer results
# 



# Brahma comparison
# data = {'results': {'HacksynthStdHackdelBenchmarkBrahmaExact': [{'p01': 206332096, 'p02': 351381590, 'p03': 214631218, 'p04': 171114590, 'p05': 170871233, 'p06': 169217568, 'p07': 301002296, 'p08': 244739631, 'p09': 210031773, 'p10': 919398980, 'p11': 1367575893, 'p12': 1333746247, 'p13': 917754834, 'p14': 567137116, 'p15': 779278357, 'p16': 679345443, 'p17': 1479320652, 'p18': 432351644, 'p19': 91901421745, 'p20': 183224638231, 'p21': 'timeout', 'p22': 349905692006, 'p23': 'timeout', 'p24': 12803080359}], 'HacksynthStdHackdelBenchmarkExact': [{'p01': 257837562, 'p02': 472603711, 'p03': 192636655, 'p04': 261910621, 'p05': 230485168, 'p06': 188804703, 'p07': 326360399, 'p08': 442341301, 'p09': 374896143, 'p10': 296837494, 'p11': 404069176, 'p12': 327412349, 'p13': 1244443167, 'p14': 2743899525, 'p15': 666685564, 'p16': 958124027, 'p17': 5324322324, 'p18': 248205279, 'p19': 26314055222, 'p20': 600266082994, 'p21': 'timeout', 'p22': 366701281551, 'p23': 'timeout', 'p24': 2185459273}], 'HacksynthStdHackdelBenchmarkBrahmaPaper': [{'p01': 2594316638, 'p02': 44830328562, 'p03': 2313758265, 'p04': 11095510701, 'p05': 701548333, 'p06': 11064504444, 'p07': 9064585712, 'p08': 17066226758, 'p09': 40839730757, 'p10': 10062789150, 'p11': 19528177687, 'p12': 6157752962, 'p13': 27672503523, 'p14': 268200203389, 'p15': 880772585472, 'p16': 43124484774, 'p17': 184057095495, 'p18': 11021095230, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 291068881022}], 'HacksynthStdHackdelBenchmark': [{'p01': 909042225, 'p02': 1978077730, 'p03': 1355255585, 'p04': 885121279, 'p05': 1007673925, 'p06': 933822675, 'p07': 1729542022, 'p08': 1621956917, 'p09': 2045918611, 'p10': 105708363072, 'p11': 25205620732, 'p12': 104399577683, 'p13': 3621686581, 'p14': 16675826252, 'p15': 7490137787, 'p16': 64640965294, 'p17': 4288572421, 'p18': 4724227590, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 899804533023}]}, 'arguments': 'benchmark=hacksynth_std_hackdel_benchmark_brahma_exact.py,hacksynth_std_hackdel_benchmark_exact.py,hacksynth_std_hackdel_benchmark_brahma_paper.py,hacksynth_std_hackdel_hard.py output=exact_mode intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}
# results = data['results']

#data = {'results': {'cvc5-32bit-benchmark': [{'hd-01-d1-prog.sl': 8134190, 'hd-01-d5-prog.sl': 12457190534, 'hd-02-d0-prog.sl': 5633817, 'hd-02-d1-prog.sl': 7627595, 'hd-02-d5-prog.sl': 15368212950, 'hd-03-d0-prog.sl': 5368262, 'hd-03-d1-prog.sl': 8117742, 'hd-03-d5-prog.sl': 14799483482, 'hd-04-d0-prog.sl': 7023948, 'hd-04-d1-prog.sl': 11893651, 'hd-04-d5-prog.sl': 19844588004, 'hd-05-d0-prog.sl': 8129372, 'hd-05-d1-prog.sl': 11271400, 'hd-05-d5-prog.sl': 12991388676, 'hd-06-d0-prog.sl': 7128930, 'hd-06-d1-prog.sl': 9925489, 'hd-06-d5-prog.sl': 6090044743, 'hd-07-d0-prog.sl': 9621951, 'hd-07-d1-prog.sl': 50469084, 'hd-07-d5-prog.sl': 'timeout', 'hd-08-d0-prog.sl': 12206207, 'hd-08-d1-prog.sl': 18007650, 'hd-08-d5-prog.sl': 162858042384, 'hd-09-d0-prog.sl': 143561840, 'hd-09-d1-prog.sl': 60452156084, 'hd-09-d5-prog.sl': 'timeout', 'hd-13-d0-prog.sl': 293536851, 'hd-13-d1-prog.sl': 68529513583, 'hd-13-d5-prog.sl': 'timeout', 'hd-14-d0-prog.sl': 3254563415, 'hd-14-d1-prog.sl': 122605982922, 'hd-14-d5-prog.sl': 'timeout', 'hd-15-d0-prog.sl': 5175543824, 'hd-15-d1-prog.sl': 108708836264, 'hd-15-d5-prog.sl': 'timeout', 'hd-17-d0-prog.sl': 40118180, 'hd-17-d1-prog.sl': 153896042, 'hd-17-d5-prog.sl': 'timeout', 'hd-19-d0-prog.sl': 'timeout', 'hd-19-d1-prog.sl': 'timeout', 'hd-19-d5-prog.sl': 'timeout', 'hd-20-d0-prog.sl': 'timeout', 'hd-20-d1-prog.sl': 'timeout', 'hd-20-d5-prog.sl': 'timeout'}], 'HacksynthHackdelFullSygus': [{'p01_d1': 595855809, 'p01_d5': 1035417864, 'p02_d0': 467092735, 'p02_d1': 633063154, 'p02_d5': 1112359449, 'p03_d0': 461852922, 'p03_d1': 583423373, 'p03_d5': 1107975225, 'p04_d0': 447391268, 'p04_d1': 622045670, 'p04_d5': 1151836708, 'p05_d0': 476853279, 'p05_d1': 686184717, 'p05_d5': 1120558652, 'p06_d0': 487829079, 'p06_d1': 643269278, 'p06_d5': 1169114577, 'p07_d0': 643127563, 'p07_d1': 970195774, 'p07_d5': 1706419044, 'p08_d0': 710383633, 'p08_d1': 1011680256, 'p08_d5': 2195361500, 'p09_d0': 'timeout', 'p09_d1': 25692589088, 'p09_d5': 2511821380, 'p13_d0': 1961742034, 'p13_d1': 6851794291, 'p13_d5': 5974066264, 'p14_d0': 263036326056, 'p14_d1': 17403683351, 'p14_d5': 'timeout', 'p15_d0': 11078993397, 'p15_d1': 51007217583, 'p15_d5': 493550464465, 'p17_d0': 1341040394, 'p17_d1': 1697777791, 'p17_d5': 6723191259, 'p19_d0': 16264506202, 'p19_d1': 1307325063887, 'p19_d5': 'timeout', 'p20_d0': 'timeout', 'p20_d1': 'timeout', 'p20_d5': 'timeout'}], 'HacksynthHackdelFullSygusDownscaling': [{'p01_d1': 448568626, 'p01_d5': 2752561548, 'p02_d0': 404058560, 'p02_d1': 505159916, 'p02_d5': 6286025808, 'p03_d0': 368540591, 'p03_d1': 549909955, 'p03_d5': 2906688753, 'p04_d0': 378168189, 'p04_d1': 582319983, 'p04_d5': 2922133452, 'p05_d0': 382966660, 'p05_d1': 539117811, 'p05_d5': 2880536623, 'p06_d0': 358194448, 'p06_d1': 506856544, 'p06_d5': 4038576117, 'p07_d0': 493600117, 'p07_d1': 909867743, 'p07_d5': 23202449590, 'p08_d0': 642138049, 'p08_d1': 1059491181, 'p08_d5': 8463338781, 'p09_d0': 701645387, 'p09_d1': 1536222648, 'p09_d5': 37123518963, 'p13_d0': 1433305902, 'p13_d1': 724393839, 'p13_d5': 3386545650, 'p14_d0': 289815252220, 'p14_d1': 8408751267, 'p14_d5': 1252749904582, 'p15_d0': 2040000819, 'p15_d1': 3806894726, 'p15_d5': 944869409354, 'p17_d0': 1442432287, 'p17_d1': 4877829957, 'p17_d5': 532923019910, 'p19_d0': 5919740555, 'p19_d1': 713022698822, 'p19_d5': 'timeout', 'p20_d0': 109005220665, 'p20_d1': 742678238091, 'p20_d5': 'timeout'}]}, 'arguments': 'benchmark=cvc5_32,sygus_32bit_down,sygus_32bit.py output=outfile_sygus_32 intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}
#results = data['results']


data = {'results': {'HacksynthHackdelFullSygusDownscaling64': [{'p01_d1': 581140651, 'p01_d5': 1096472149, 'p02_d0': 463845516, 'p02_d1': 621335152, 'p02_d5': 1138303554, 'p03_d0': 454553816, 'p03_d1': 594317542, 'p03_d5': 1227515660, 'p04_d0': 397584762, 'p04_d1': 634524105, 'p04_d5': 1024110995, 'p05_d0': 454218947, 'p05_d1': 611789096, 'p05_d5': 1147821198, 'p06_d0': 451625965, 'p06_d1': 612512041, 'p06_d5': 1143163956, 'p07_d0': 584292882, 'p07_d1': 858424205, 'p07_d5': 1799198998, 'p08_d0': 691261908, 'p08_d1': 998714572, 'p08_d5': 1792477261, 'p09_d0': 275049648453, 'p09_d1': 47252497605, 'p09_d5': 2172053947, 'p13_d0': 4236207309, 'p13_d1': 5651829201, 'p13_d5': 2232136972, 'p14_d0': 228142908135, 'p14_d1': 'timeout', 'p14_d5': 'timeout', 'p15_d0': 48209158272, 'p15_d1': 'timeout', 'p15_d5': 256579756714, 'p17_d0': 1039368734, 'p17_d1': 1782240963, 'p17_d5': 3619188326, 'p19_d0': 13243348668, 'p19_d1': 1074457449195, 'p19_d5': 'timeout', 'p20_d0': 'timeout', 'p20_d1': 'timeout', 'p20_d5': 'timeout'}], 'HacksynthHackdelFullSygus64': [{'p01_d1': 519362391, 'p01_d5': 5389914934, 'p02_d0': 386453871, 'p02_d1': 646750309, 'p02_d5': 6066281101, 'p03_d0': 344963335, 'p03_d1': 571277767, 'p03_d5': 4597133751, 'p04_d0': 379105533, 'p04_d1': 709371226, 'p04_d5': 5942206015, 'p05_d0': 419991982, 'p05_d1': 616932414, 'p05_d5': 12272101225, 'p06_d0': 336729738, 'p06_d1': 530254471, 'p06_d5': 3575226290, 'p07_d0': 505264839, 'p07_d1': 1008483133, 'p07_d5': 29358621614, 'p08_d0': 724920762, 'p08_d1': 1292304965, 'p08_d5': 11721604422, 'p09_d0': 650087018, 'p09_d1': 1374026716, 'p09_d5': 16437969320, 'p13_d0': 1773133562, 'p13_d1': 1091757243, 'p13_d5': 5243444595, 'p14_d0': 74557950177, 'p14_d1': 11417738149, 'p14_d5': 1602065603585, 'p15_d0': 1827395280, 'p15_d1': 7140072792, 'p15_d5': 694448283549, 'p17_d0': 1589125267, 'p17_d1': 2920534322, 'p17_d5': 774558451949, 'p19_d0': 38629702296, 'p19_d1': 342027097646, 'p19_d5': 'timeout', 'p20_d0': 103503027380, 'p20_d1': 864214768371, 'p20_d5': 'timeout'}], 'cvc5-64bit-benchmark': [{'hd-01-d1-prog.sl': 84223128, 'hd-01-d5-prog.sl': 10117909904, 'hd-02-d0-prog.sl': 6540212, 'hd-02-d1-prog.sl': 9721489, 'hd-02-d5-prog.sl': 166022952829, 'hd-03-d0-prog.sl': 6547050, 'hd-03-d1-prog.sl': 9974566, 'hd-03-d5-prog.sl': 77491208022, 'hd-04-d0-prog.sl': 8191242, 'hd-04-d1-prog.sl': 14367783, 'hd-04-d5-prog.sl': 52390153283, 'hd-05-d0-prog.sl': 9451158, 'hd-05-d1-prog.sl': 12993150, 'hd-05-d5-prog.sl': 68403607977, 'hd-06-d0-prog.sl': 9130281, 'hd-06-d1-prog.sl': 11545779, 'hd-06-d5-prog.sl': 41255325239, 'hd-07-d0-prog.sl': 11562276, 'hd-07-d1-prog.sl': 56373804, 'hd-07-d5-prog.sl': 'timeout', 'hd-08-d0-prog.sl': 14341715, 'hd-08-d1-prog.sl': 25498337, 'hd-08-d5-prog.sl': 'timeout', 'hd-09-d0-prog.sl': 137756026, 'hd-09-d1-prog.sl': 98732923205, 'hd-09-d5-prog.sl': 'timeout', 'hd-13-d0-prog.sl': 315667482, 'hd-13-d1-prog.sl': 74248003229, 'hd-13-d5-prog.sl': 'timeout', 'hd-14-d0-prog.sl': 3378817666, 'hd-14-d1-prog.sl': 134415028181, 'hd-14-d5-prog.sl': 'timeout', 'hd-15-d0-prog.sl': 5453485692, 'hd-15-d1-prog.sl': 170511617263, 'hd-15-d5-prog.sl': 'timeout', 'hd-17-d0-prog.sl': 108308860, 'hd-17-d1-prog.sl': 186265124, 'hd-17-d5-prog.sl': 'timeout', 'hd-19-d0-prog.sl': 'timeout', 'hd-19-d1-prog.sl': 'timeout', 'hd-19-d5-prog.sl': 'timeout', 'hd-20-d0-prog.sl': 20534993, 'hd-20-d1-prog.sl': 10486462, 'hd-20-d5-prog.sl': 10109642}]}, 'arguments': 'benchmark=hacksynth_full_sygus_64bit_downscaling_cegis.py,hacksynth_full_sygus_64bit.py,cvc5_64bit_benchmark.py output=outfile_sygus_64 intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}
results = data['results']


data = {'results': {'HacksynthOptimizeDepthOptimizer': [{'simple_depth_optimization': {'p01': 1282749255, 'p02': 4293610466, 'p03': 422976827, 'p04': 951661693, 'p05': 977517705, 'p06': 588165161, 'p07': 1951595100, 'p08': 2436420201, 'p09': 1917312976, 'p10': 709237383, 'p11': 1412853280, 'p12': 1303457273, 'p13': 17747459998, 'p14': 75710556519, 'p15': 87802316688, 'p16': 2208282542, 'p17': 'timeout', 'p18': 891205540, 'p19': 'timeout', 'p20': 'timeout', 'p21': 870336071253, 'p22': 'timeout', 'p23': 'timeout', 'p24': 428204763}, 'iterated_depth_optimization': {'p01': 936287321, 'p02': 3597987582, 'p03': 1235093877, 'p04': 941604698, 'p05': 913829009, 'p06': 881009338, 'p07': 1794333479, 'p08': 1300063458, 'p09': 4122240970, 'p10': 1670663323, 'p11': 4402879381, 'p12': 3884686890, 'p13': 126336281526, 'p14': 9619168798, 'p15': 33018873112, 'p16': 7761309901, 'p17': 1446970235917, 'p18': 2271523398, 'p19': 'timeout', 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}}]}, 'arguments': 'benchmark=hacksynth_optimize_depth_optimizer.py,hacksynth_std_hackdel_benchmark_brahma.py output=outfile_depth_opt_and_brahma intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}
data = data['results']['HacksynthOptimizeDepthOptimizer']

results = {
    'simple_depth_optimization': [data[0]['simple_depth_optimization']],
    'iterated_depth_optimization': [data[0]['iterated_depth_optimization']]
}

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

print(merged_data)

new_cvc5_results = {}
""" # as sygus tests have weird names, transform them here
for (test_name, results) in merged_data['cvc5-64bit-benchmark'].items():
    # hd-04-d0-prog.sl
    new_name = "p" + test_name[3:5] + "_d" + test_name[7]
    new_cvc5_results[new_name] = results
merged_data['cvc5-64bit-benchmark'] = new_cvc5_results
 """
# to dat format
keys = ['iterated_depth_optimization']
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


exit(0)



# remove HackStdHackdelBenchmark, as it is incomparable
# del merged_data['HacksynthStdHackdelBenchmark']

double_array_format = {} # {benchmark_name: [[result1, result2, ...], [result1, result2, ...]]}
for (key, data) in merged_data.items():
    double_array_format[key] = [v for v in data.values()]



draw_bar_plot(
    [('simple_depth_optimization', double_array_format["simple_depth_optimization"]), 
     ('iterated_depth_optimization', double_array_format["iterated_depth_optimization"]), 
     ], 
     # [i for i in range(0, 44)], 
     axis_ticks=merged_data["simple_depth_optimization"].keys(), output="output_cmp_sygus.svg")