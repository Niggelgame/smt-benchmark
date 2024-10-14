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
        
        if runner != "HacksynthHackdelFullSygusDownscaling64":
            measurement = [m[0] for m in measurement]

            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=runner)
            # ax.bar_label(rects, padding=3)
            multiplier += 1
        else:
            print(measurement)
            sh_measurement = [m['shell_time'] for m in measurement]

            offset = width * multiplier
            rects = ax.bar(x + offset, sh_measurement, width, label=runner)
            # ax.bar_label(rects, padding=3)
            multiplier += 1

            bottom = np.zeros(len(measurement))
            # add the timing measuremnts on top:
            downscaled_synth_times = [m['downscaled_synth_time'] if 'downscaled_synth_time' in m else 0 for m in measurement ]
            finding_constants_times = [m['finding_constants_time'] if 'finding_constants_time' in m else 0 for m in measurement ]
            other_synth_times = [m['other_synth_time'] if 'other_synth_time' in m else 0 for m in measurement ]

            ax.bar(x + offset, finding_constants_times, width, bottom=bottom, label=(runner+"const_time"))
            bottom += finding_constants_times
            ax.bar(x + offset, downscaled_synth_times, width, bottom=bottom, label=(runner+"ds_time"))
            bottom += downscaled_synth_times
            ax.bar(x + offset, other_synth_times, width, bottom=bottom, label=(runner+"other_time"))
            bottom += other_synth_times
            

        # print(runner, measurement, x + width * multiplier)
        # only take first measurement
        #print(measurement)
        
    
    ax.set_yscale("log")
    plt.xticks(rotation=-70)
    ax.set_xticks(x + width, axis_ticks)

    ax.legend(loc='upper left', ncols=3)

    ax.set_ylabel('Time (s)')

    plt.show()

    if output is not None:
        fig.savefig(output)


results = {'HacksynthHackdelExtendedSygus': [{'p01_d1': 485306859, 'p01_d5': 1134595141, 'p02_d0': 450197579, 'p02_d1': 647734807, 'p02_d5': 2617871765, 'p03_d0': 362003230, 'p03_d1': 581104460, 'p03_d5': 1180876923, 'p04_d0': 372857139, 'p04_d1': 521544871, 'p04_d5': 1407682088, 'p05_d0': 390956751, 'p05_d1': 516141595, 'p05_d5': 1398797447, 'p06_d0': 378798037, 'p06_d1': 532757542, 'p06_d5': 1359567154, 'p07_d0': 636697512, 'p07_d1': 1141359453, 'p07_d5': 4650526530, 'p08_d0': 692293383, 'p08_d1': 1127460765, 'p08_d5': 4034647673, 'p09_d0': 875567989, 'p09_d1': 1535754798, 'p09_d5': 4085814456, 'p13_d0': 1072085714, 'p13_d1': 18039207718, 'p13_d5': 28484053057, 'p14_d0': 97981141626, 'p14_d1': 149753240051, 'p14_d5': 552779349799, 'p15_d0': 148759153608, 'p15_d1': 167591590054, 'p15_d5': 166636375334, 'p17_d0': 2189958860, 'p17_d1': 4059021031, 'p17_d5': 136936090964, 'p19_d0': 32003535852, 'p19_d1': 516056220519, 'p19_d5': 'timeout', 'p20_d0': 2160871412346, 'p20_d1': 'timeout', 'p20_d5': 'timeout'}], 'HacksynthHackdelFullSygus': [{'p01_d1': 484399345, 'p01_d5': 1143510753, 'p02_d0': 421832021, 'p02_d1': 557763605, 'p02_d5': 1635657355, 'p03_d0': 357445989, 'p03_d1': 585758987, 'p03_d5': 1170975680, 'p04_d0': 376412416, 'p04_d1': 510490570, 'p04_d5': 1400513551, 'p05_d0': 386732924, 'p05_d1': 514410725, 'p05_d5': 1381744365, 'p06_d0': 381003602, 'p06_d1': 531287920, 'p06_d5': 1330276955, 'p07_d0': 639592443, 'p07_d1': 1141078535, 'p07_d5': 4715845161, 'p08_d0': 684982794, 'p08_d1': 1122788440, 'p08_d5': 3966500107, 'p09_d0': 770766788, 'p09_d1': 1357575987, 'p09_d5': 4752075425, 'p13_d0': 317948933, 'p13_d1': 419993993, 'p13_d5': 582968933, 'p14_d0': 79536170165, 'p14_d1': 10952332044, 'p14_d5': 259044110973, 'p15_d0': 1314567441, 'p15_d1': 7147825377, 'p15_d5': 107633152564, 'p17_d0': 2142050586, 'p17_d1': 4052450906, 'p17_d5': 140184339597, 'p19_d0': 775358380278, 'p19_d1': 725902887085, 'p19_d5': 'timeout', 'p20_d0': 'timeout', 'p20_d1': 'timeout', 'p20_d5': 'timeout'}], 'cvc5-8bit-benchmark': [{'hd-01-d1-prog.sl': 7144530, 'hd-01-d5-prog.sl': 2036851847, 'hd-02-d0-prog.sl': 5029161, 'hd-02-d1-prog.sl': 6348687, 'hd-02-d5-prog.sl': 716927148, 'hd-03-d0-prog.sl': 4599835, 'hd-03-d1-prog.sl': 7163595, 'hd-03-d5-prog.sl': 4071069958, 'hd-04-d0-prog.sl': 6050568, 'hd-04-d1-prog.sl': 10193916, 'hd-04-d5-prog.sl': 667204934, 'hd-05-d0-prog.sl': 6693675, 'hd-05-d1-prog.sl': 9995411, 'hd-05-d5-prog.sl': 5183331746, 'hd-06-d0-prog.sl': 6056505, 'hd-06-d1-prog.sl': 8780617, 'hd-06-d5-prog.sl': 4809639028, 'hd-07-d0-prog.sl': 8423487, 'hd-07-d1-prog.sl': 37519642, 'hd-07-d5-prog.sl': 39972811464, 'hd-08-d0-prog.sl': 10359624, 'hd-08-d1-prog.sl': 13827980, 'hd-08-d5-prog.sl': 312728900732, 'hd-09-d0-prog.sl': 130028936, 'hd-09-d1-prog.sl': 51656203188, 'hd-09-d5-prog.sl': 2960498925706, 'hd-13-d0-prog.sl': 6144969, 'hd-13-d1-prog.sl': 6943117, 'hd-13-d5-prog.sl': 66063796, 'hd-14-d0-prog.sl': 3322604400, 'hd-14-d1-prog.sl': 110504773723, 'hd-14-d5-prog.sl': 'timeout', 'hd-15-d0-prog.sl': 5203768218, 'hd-15-d1-prog.sl': 116475051094, 'hd-15-d5-prog.sl': 'timeout', 'hd-17-d0-prog.sl': 21204260, 'hd-17-d1-prog.sl': 128107889, 'hd-17-d5-prog.sl': 'timeout', 'hd-19-d0-prog.sl': 'timeout', 'hd-19-d1-prog.sl': 'timeout', 'hd-19-d5-prog.sl': 'timeout', 'hd-20-d0-prog.sl': 'timeout', 'hd-20-d1-prog.sl': 'timeout', 'hd-20-d5-prog.sl': 'timeout'}], 'HacksynthStdHackdelBenchmark': [{'p01': 379447391, 'p02': 499612579, 'p03': 492246314, 'p04': 376415299, 'p05': 395870365, 'p06': 403792646, 'p07': 765856111, 'p08': 766214172, 'p09': 726024984, 'p10': 759562682, 'p11': 733699583, 'p12': 755601162, 'p13': 5898854384, 'p14': 1834742340, 'p15': 2832595098, 'p16': 1379855407, 'p17': 2187167734, 'p18': 561411574, 'p19': 10171062365, 'p20': 'timeout', 'p21': 2155054080229, 'p22': 2579063730231, 'p23': 'timeout', 'p24': 298674131790}]}

# 32 Bit results
# data = {'results': {'cvc5-32bit-benchmark': [{'hd-01-d1-prog.sl': 8134190, 'hd-01-d5-prog.sl': 12457190534, 'hd-02-d0-prog.sl': 5633817, 'hd-02-d1-prog.sl': 7627595, 'hd-02-d5-prog.sl': 15368212950, 'hd-03-d0-prog.sl': 5368262, 'hd-03-d1-prog.sl': 8117742, 'hd-03-d5-prog.sl': 14799483482, 'hd-04-d0-prog.sl': 7023948, 'hd-04-d1-prog.sl': 11893651, 'hd-04-d5-prog.sl': 19844588004, 'hd-05-d0-prog.sl': 8129372, 'hd-05-d1-prog.sl': 11271400, 'hd-05-d5-prog.sl': 12991388676, 'hd-06-d0-prog.sl': 7128930, 'hd-06-d1-prog.sl': 9925489, 'hd-06-d5-prog.sl': 6090044743, 'hd-07-d0-prog.sl': 9621951, 'hd-07-d1-prog.sl': 50469084, 'hd-07-d5-prog.sl': 'timeout', 'hd-08-d0-prog.sl': 12206207, 'hd-08-d1-prog.sl': 18007650, 'hd-08-d5-prog.sl': 162858042384, 'hd-09-d0-prog.sl': 143561840, 'hd-09-d1-prog.sl': 60452156084, 'hd-09-d5-prog.sl': 'timeout', 'hd-13-d0-prog.sl': 293536851, 'hd-13-d1-prog.sl': 68529513583, 'hd-13-d5-prog.sl': 'timeout', 'hd-14-d0-prog.sl': 3254563415, 'hd-14-d1-prog.sl': 122605982922, 'hd-14-d5-prog.sl': 'timeout', 'hd-15-d0-prog.sl': 5175543824, 'hd-15-d1-prog.sl': 108708836264, 'hd-15-d5-prog.sl': 'timeout', 'hd-17-d0-prog.sl': 40118180, 'hd-17-d1-prog.sl': 153896042, 'hd-17-d5-prog.sl': 'timeout', 'hd-19-d0-prog.sl': 'timeout', 'hd-19-d1-prog.sl': 'timeout', 'hd-19-d5-prog.sl': 'timeout', 'hd-20-d0-prog.sl': 'timeout', 'hd-20-d1-prog.sl': 'timeout', 'hd-20-d5-prog.sl': 'timeout'}], 'HacksynthHackdelFullSygus': [{'p01_d1': 595855809, 'p01_d5': 1035417864, 'p02_d0': 467092735, 'p02_d1': 633063154, 'p02_d5': 1112359449, 'p03_d0': 461852922, 'p03_d1': 583423373, 'p03_d5': 1107975225, 'p04_d0': 447391268, 'p04_d1': 622045670, 'p04_d5': 1151836708, 'p05_d0': 476853279, 'p05_d1': 686184717, 'p05_d5': 1120558652, 'p06_d0': 487829079, 'p06_d1': 643269278, 'p06_d5': 1169114577, 'p07_d0': 643127563, 'p07_d1': 970195774, 'p07_d5': 1706419044, 'p08_d0': 710383633, 'p08_d1': 1011680256, 'p08_d5': 2195361500, 'p09_d0': 'timeout', 'p09_d1': 25692589088, 'p09_d5': 2511821380, 'p13_d0': 1961742034, 'p13_d1': 6851794291, 'p13_d5': 5974066264, 'p14_d0': 263036326056, 'p14_d1': 17403683351, 'p14_d5': 'timeout', 'p15_d0': 11078993397, 'p15_d1': 51007217583, 'p15_d5': 493550464465, 'p17_d0': 1341040394, 'p17_d1': 1697777791, 'p17_d5': 6723191259, 'p19_d0': 16264506202, 'p19_d1': 1307325063887, 'p19_d5': 'timeout', 'p20_d0': 'timeout', 'p20_d1': 'timeout', 'p20_d5': 'timeout'}], 'HacksynthHackdelFullSygusDownscaling': [{'p01_d1': 448568626, 'p01_d5': 2752561548, 'p02_d0': 404058560, 'p02_d1': 505159916, 'p02_d5': 6286025808, 'p03_d0': 368540591, 'p03_d1': 549909955, 'p03_d5': 2906688753, 'p04_d0': 378168189, 'p04_d1': 582319983, 'p04_d5': 2922133452, 'p05_d0': 382966660, 'p05_d1': 539117811, 'p05_d5': 2880536623, 'p06_d0': 358194448, 'p06_d1': 506856544, 'p06_d5': 4038576117, 'p07_d0': 493600117, 'p07_d1': 909867743, 'p07_d5': 23202449590, 'p08_d0': 642138049, 'p08_d1': 1059491181, 'p08_d5': 8463338781, 'p09_d0': 701645387, 'p09_d1': 1536222648, 'p09_d5': 37123518963, 'p13_d0': 1433305902, 'p13_d1': 724393839, 'p13_d5': 3386545650, 'p14_d0': 289815252220, 'p14_d1': 8408751267, 'p14_d5': 1252749904582, 'p15_d0': 2040000819, 'p15_d1': 3806894726, 'p15_d5': 944869409354, 'p17_d0': 1442432287, 'p17_d1': 4877829957, 'p17_d5': 532923019910, 'p19_d0': 5919740555, 'p19_d1': 713022698822, 'p19_d5': 'timeout', 'p20_d0': 109005220665, 'p20_d1': 742678238091, 'p20_d5': 'timeout'}]}, 'arguments': 'benchmark=cvc5_32,sygus_32bit_down,sygus_32bit.py output=outfile_sygus_32 intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}
# results = data['results']

# 64 bit results
# data = {'results': {'HacksynthHackdelFullSygusDownscaling64': [{'p01_d1': 581140651, 'p01_d5': 1096472149, 'p02_d0': 463845516, 'p02_d1': 621335152, 'p02_d5': 1138303554, 'p03_d0': 454553816, 'p03_d1': 594317542, 'p03_d5': 1227515660, 'p04_d0': 397584762, 'p04_d1': 634524105, 'p04_d5': 1024110995, 'p05_d0': 454218947, 'p05_d1': 611789096, 'p05_d5': 1147821198, 'p06_d0': 451625965, 'p06_d1': 612512041, 'p06_d5': 1143163956, 'p07_d0': 584292882, 'p07_d1': 858424205, 'p07_d5': 1799198998, 'p08_d0': 691261908, 'p08_d1': 998714572, 'p08_d5': 1792477261, 'p09_d0': 275049648453, 'p09_d1': 47252497605, 'p09_d5': 2172053947, 'p13_d0': 4236207309, 'p13_d1': 5651829201, 'p13_d5': 2232136972, 'p14_d0': 228142908135, 'p14_d1': 'timeout', 'p14_d5': 'timeout', 'p15_d0': 48209158272, 'p15_d1': 'timeout', 'p15_d5': 256579756714, 'p17_d0': 1039368734, 'p17_d1': 1782240963, 'p17_d5': 3619188326, 'p19_d0': 13243348668, 'p19_d1': 1074457449195, 'p19_d5': 'timeout', 'p20_d0': 'timeout', 'p20_d1': 'timeout', 'p20_d5': 'timeout'}], 'HacksynthHackdelFullSygus64': [{'p01_d1': 519362391, 'p01_d5': 5389914934, 'p02_d0': 386453871, 'p02_d1': 646750309, 'p02_d5': 6066281101, 'p03_d0': 344963335, 'p03_d1': 571277767, 'p03_d5': 4597133751, 'p04_d0': 379105533, 'p04_d1': 709371226, 'p04_d5': 5942206015, 'p05_d0': 419991982, 'p05_d1': 616932414, 'p05_d5': 12272101225, 'p06_d0': 336729738, 'p06_d1': 530254471, 'p06_d5': 3575226290, 'p07_d0': 505264839, 'p07_d1': 1008483133, 'p07_d5': 29358621614, 'p08_d0': 724920762, 'p08_d1': 1292304965, 'p08_d5': 11721604422, 'p09_d0': 650087018, 'p09_d1': 1374026716, 'p09_d5': 16437969320, 'p13_d0': 1773133562, 'p13_d1': 1091757243, 'p13_d5': 5243444595, 'p14_d0': 74557950177, 'p14_d1': 11417738149, 'p14_d5': 1602065603585, 'p15_d0': 1827395280, 'p15_d1': 7140072792, 'p15_d5': 694448283549, 'p17_d0': 1589125267, 'p17_d1': 2920534322, 'p17_d5': 774558451949, 'p19_d0': 38629702296, 'p19_d1': 342027097646, 'p19_d5': 'timeout', 'p20_d0': 103503027380, 'p20_d1': 864214768371, 'p20_d5': 'timeout'}], 'cvc5-64bit-benchmark': [{'hd-01-d1-prog.sl': 84223128, 'hd-01-d5-prog.sl': 10117909904, 'hd-02-d0-prog.sl': 6540212, 'hd-02-d1-prog.sl': 9721489, 'hd-02-d5-prog.sl': 166022952829, 'hd-03-d0-prog.sl': 6547050, 'hd-03-d1-prog.sl': 9974566, 'hd-03-d5-prog.sl': 77491208022, 'hd-04-d0-prog.sl': 8191242, 'hd-04-d1-prog.sl': 14367783, 'hd-04-d5-prog.sl': 52390153283, 'hd-05-d0-prog.sl': 9451158, 'hd-05-d1-prog.sl': 12993150, 'hd-05-d5-prog.sl': 68403607977, 'hd-06-d0-prog.sl': 9130281, 'hd-06-d1-prog.sl': 11545779, 'hd-06-d5-prog.sl': 41255325239, 'hd-07-d0-prog.sl': 11562276, 'hd-07-d1-prog.sl': 56373804, 'hd-07-d5-prog.sl': 'timeout', 'hd-08-d0-prog.sl': 14341715, 'hd-08-d1-prog.sl': 25498337, 'hd-08-d5-prog.sl': 'timeout', 'hd-09-d0-prog.sl': 137756026, 'hd-09-d1-prog.sl': 98732923205, 'hd-09-d5-prog.sl': 'timeout', 'hd-13-d0-prog.sl': 315667482, 'hd-13-d1-prog.sl': 74248003229, 'hd-13-d5-prog.sl': 'timeout', 'hd-14-d0-prog.sl': 3378817666, 'hd-14-d1-prog.sl': 134415028181, 'hd-14-d5-prog.sl': 'timeout', 'hd-15-d0-prog.sl': 5453485692, 'hd-15-d1-prog.sl': 170511617263, 'hd-15-d5-prog.sl': 'timeout', 'hd-17-d0-prog.sl': 108308860, 'hd-17-d1-prog.sl': 186265124, 'hd-17-d5-prog.sl': 'timeout', 'hd-19-d0-prog.sl': 'timeout', 'hd-19-d1-prog.sl': 'timeout', 'hd-19-d5-prog.sl': 'timeout', 'hd-20-d0-prog.sl': 20534993, 'hd-20-d1-prog.sl': 10486462, 'hd-20-d5-prog.sl': 10109642}]}, 'arguments': 'benchmark=hacksynth_full_sygus_64bit_downscaling_cegis.py,hacksynth_full_sygus_64bit.py,cvc5_64bit_benchmark.py output=outfile_sygus_64 intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}
# results = data['results']

# 64 bit results without downscaling
data = {'results': {'HacksynthHackdelFullSygusDownscaling64': [{'shell_times': {'p01_d1': 1562865563, 'p01_d5': 2518351271, 'p02_d0': 803608555, 'p02_d1': 1043367742, 'p02_d5': 1742743628, 'p03_d0': 755258218, 'p03_d1': 1010427630, 'p03_d5': 1826690013, 'p04_d0': 785366099, 'p04_d1': 1547242027, 'p04_d5': 2847060649, 'p05_d0': 1256285857, 'p05_d1': 1751269937, 'p05_d5': 3359186912, 'p06_d0': 1264336406, 'p06_d1': 1708709106, 'p06_d5': 1999647954, 'p07_d0': 1084845979, 'p07_d1': 1515325316, 'p07_d5': 2668200851, 'p08_d0': 1817707359, 'p08_d1': 2586990533, 'p08_d5': 3806757694, 'p09_d0': 'timeout', 'p09_d1': 'timeout', 'p09_d5': 3277526206, 'p13_d0': 2616600816, 'p13_d1': 6114618050, 'p13_d5': 'timeout', 'p14_d0': 156204368605, 'p14_d1': 67704855790, 'p14_d5': 'timeout', 'p15_d0': 'timeout', 'p15_d1': 45429186868, 'p15_d5': 316134184206, 'p17_d0': 1317730840, 'p17_d1': 1487897859, 'p17_d5': 6046841808, 'p19_d0': 78564290214, 'p19_d1': 1040098189887, 'p19_d5': 'timeout', 'p20_d0': 96996960341, 'p20_d1': 'timeout', 'p20_d5': 'timeout'}, 'downscaling_times': {'p01_d1': {'downscaled_synth_time': 0, 'finding_constants_time': 0, 'other_synth_time': 1092129275}, 'p01_d5': {'downscaled_synth_time': 0, 'finding_constants_time': 0, 'other_synth_time': 2116776861}, 'p02_d0': {'downscaled_synth_time': 438851947, 'finding_constants_time': 84087404, 'other_synth_time': 0}, 'p02_d1': {'downscaled_synth_time': 681505656, 'finding_constants_time': 92210020, 'other_synth_time': 0}, 'p02_d5': {'downscaled_synth_time': 1352843551, 'finding_constants_time': 94694319, 'other_synth_time': 0}, 'p03_d0': {'downscaled_synth_time': 419808144, 'finding_constants_time': 54528576, 'other_synth_time': 0}, 'p03_d1': {'downscaled_synth_time': 668898732, 'finding_constants_time': 52423906, 'other_synth_time': 0}, 'p03_d5': {'downscaled_synth_time': 1418108848, 'finding_constants_time': 73781755, 'other_synth_time': 0}, 'p04_d0': {'downscaled_synth_time': 0, 'finding_constants_time': 0, 'other_synth_time': 480703327}, 'p04_d1': {'downscaled_synth_time': 1074862972, 'finding_constants_time': 89453208, 'other_synth_time': 0}, 'p04_d5': {'downscaled_synth_time': 0, 'finding_constants_time': 0, 'other_synth_time': 2357154921}, 'p05_d0': {'downscaled_synth_time': 735037644, 'finding_constants_time': 85741036, 'other_synth_time': 0}, 'p05_d1': {'downscaled_synth_time': 1183499656, 'finding_constants_time': 98244881, 'other_synth_time': 0}, 'p05_d5': {'downscaled_synth_time': 2747938948, 'finding_constants_time': 110962774, 'other_synth_time': 0}, 'p06_d0': {'downscaled_synth_time': 749180604, 'finding_constants_time': 78186335, 'other_synth_time': 0}, 'p06_d1': {'downscaled_synth_time': 1242805679, 'finding_constants_time': 84690390, 'other_synth_time': 0}, 'p06_d5': {'downscaled_synth_time': 1615814076, 'finding_constants_time': 66893505, 'other_synth_time': 0}, 'p07_d0': {'downscaled_synth_time': 0, 'finding_constants_time': 0, 'other_synth_time': 771871346}, 'p07_d1': {'downscaled_synth_time': 0, 'finding_constants_time': 0, 'other_synth_time': 1205551084}, 'p07_d5': {'downscaled_synth_time': 0, 'finding_constants_time': 0, 'other_synth_time': 2256218369}, 'p08_d0': {'downscaled_synth_time': 0, 'finding_constants_time': 0, 'other_synth_time': 1342018723}, 'p08_d1': {'downscaled_synth_time': 2130849522, 'finding_constants_time': 60136564, 'other_synth_time': 0}, 'p08_d5': {'downscaled_synth_time': 3324395251, 'finding_constants_time': 108217241, 'other_synth_time': 0}, 'p09_d5': {'downscaled_synth_time': 1754966532, 'finding_constants_time': 1329747717, 'other_synth_time': 0}, 'p13_d0': {'downscaled_synth_time': 807204359, 'finding_constants_time': 30782007, 'other_synth_time': 1622475131}, 'p13_d1': {'downscaled_synth_time': 5321810660, 'finding_constants_time': 55363257, 'other_synth_time': 572091162}, 'p14_d0': {'downscaled_synth_time': 20592652344, 'finding_constants_time': 35321540, 'other_synth_time': 135377212345}, 'p14_d1': {'downscaled_synth_time': 59926573989, 'finding_constants_time': 40680947, 'other_synth_time': 7576218299}, 'p15_d1': {'downscaled_synth_time': 37774582236, 'finding_constants_time': 66059278, 'other_synth_time': 7429069026}, 'p15_d5': {'downscaled_synth_time': 313802718138, 'finding_constants_time': 2070904256, 'other_synth_time': 0}, 'p17_d0': {'downscaled_synth_time': 0, 'finding_constants_time': 0, 'other_synth_time': 1169157837}, 'p17_d1': {'downscaled_synth_time': 0, 'finding_constants_time': 0, 'other_synth_time': 1328672967}, 'p17_d5': {'downscaled_synth_time': 0, 'finding_constants_time': 0, 'other_synth_time': 5886016327}, 'p19_d0': {'downscaled_synth_time': 3930863528, 'finding_constants_time': 37484952, 'other_synth_time': 74411976401}, 'p19_d1': {'downscaled_synth_time': 78100884, 'finding_constants_time': 40721855, 'other_synth_time': 1039730876860}, 'p20_d0': {'downscaled_synth_time': 0, 'finding_constants_time': 0, 'other_synth_time': 96774335160}}}], 'HacksynthHackdelFullSygus64': [{'p01_d1': 523462125, 'p01_d5': 5369848054, 'p02_d0': 387942888, 'p02_d1': 650835720, 'p02_d5': 6010716739, 'p03_d0': 345956319, 'p03_d1': 563680187, 'p03_d5': 4571771552, 'p04_d0': 379943217, 'p04_d1': 694462780, 'p04_d5': 5908385130, 'p05_d0': 420292223, 'p05_d1': 620152890, 'p05_d5': 12218326085, 'p06_d0': 342361773, 'p06_d1': 533009089, 'p06_d5': 3593949358, 'p07_d0': 506481316, 'p07_d1': 1002135261, 'p07_d5': 29558346939, 'p08_d0': 725238646, 'p08_d1': 1340351025, 'p08_d5': 11554625624, 'p09_d0': 650634979, 'p09_d1': 1371698269, 'p09_d5': 16458184660, 'p13_d0': 1771906366, 'p13_d1': 1107235638, 'p13_d5': 5135335893, 'p14_d0': 74729941650, 'p14_d1': 11198228671, 'p14_d5': 1618293880476, 'p15_d0': 1817210954, 'p15_d1': 7113184894, 'p15_d5': 697283680802, 'p17_d0': 1588956469, 'p17_d1': 2940854729, 'p17_d5': 785429643844, 'p19_d0': 38342438205, 'p19_d1': 343812715744, 'p19_d5': 'timeout', 'p20_d0': 103966107250, 'p20_d1': 874161813088, 'p20_d5': 'timeout'}], 'cvc5-64bit-benchmark': [{'hd-01-d1-prog.sl': 9172162, 'hd-01-d5-prog.sl': 10443769281, 'hd-02-d0-prog.sl': 6662080, 'hd-02-d1-prog.sl': 10529236, 'hd-02-d5-prog.sl': 171509602846, 'hd-03-d0-prog.sl': 6569650, 'hd-03-d1-prog.sl': 10072109, 'hd-03-d5-prog.sl': 78768178975, 'hd-04-d0-prog.sl': 8128417, 'hd-04-d1-prog.sl': 14618752, 'hd-04-d5-prog.sl': 53324462802, 'hd-05-d0-prog.sl': 9457076, 'hd-05-d1-prog.sl': 13117443, 'hd-05-d5-prog.sl': 69526440661, 'hd-06-d0-prog.sl': 8951757, 'hd-06-d1-prog.sl': 11842881, 'hd-06-d5-prog.sl': 41019583267, 'hd-07-d0-prog.sl': 11466840, 'hd-07-d1-prog.sl': 57566721, 'hd-07-d5-prog.sl': 'timeout', 'hd-08-d0-prog.sl': 14249225, 'hd-08-d1-prog.sl': 25927306, 'hd-08-d5-prog.sl': 'timeout', 'hd-09-d0-prog.sl': 140646373, 'hd-09-d1-prog.sl': 102319061176, 'hd-09-d5-prog.sl': 'timeout', 'hd-13-d0-prog.sl': 319794124, 'hd-13-d1-prog.sl': 75934048453, 'hd-13-d5-prog.sl': 'timeout', 'hd-14-d0-prog.sl': 3428348380, 'hd-14-d1-prog.sl': 136364702479, 'hd-14-d5-prog.sl': 'timeout', 'hd-15-d0-prog.sl': 5555586671, 'hd-15-d1-prog.sl': 173080254953, 'hd-15-d5-prog.sl': 'timeout', 'hd-17-d0-prog.sl': 108819227, 'hd-17-d1-prog.sl': 188139552, 'hd-17-d5-prog.sl': 'timeout', 'hd-19-d0-prog.sl': 'timeout', 'hd-19-d1-prog.sl': 'timeout', 'hd-19-d5-prog.sl': 'timeout', 'hd-20-d0-prog.sl': 10773828, 'hd-20-d1-prog.sl': 10300868, 'hd-20-d5-prog.sl': 10136480}]}, 'arguments': 'benchmark=hacksynth_full_sygus_64bit_downscaling_cegis.py,hacksynth_full_sygus_64bit.py,cvc5_64bit_benchmark.py output=outfile_sygus_64_stats intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}
results = data['results']


def transform_ds_results(data):
    res = []
    for repetition in data:
        run = {}
        shell_times = repetition["shell_times"]
        downscaling_times = repetition["downscaling_times"]

        for (testcase, time) in shell_times.items():
            run[testcase] = {
                "shell_time": time
            }

            if testcase in downscaling_times:
                run[testcase].update(downscaling_times[testcase])

        res.append(run)
    
    # print(res)
    return res

results['HacksynthHackdelFullSygusDownscaling64'] = transform_ds_results(results['HacksynthHackdelFullSygusDownscaling64'])

# compute ratios
for repetition in results['HacksynthHackdelFullSygusDownscaling64']:
    for (testcase, times) in repetition.items():
        if 'downscaled_synth_time' in times:
            times['downscaled_synth_ratio'] = times['downscaled_synth_time'] / times['shell_time']
            times['finding_constants_ratio'] = times['finding_constants_time'] / times['shell_time']
            times['other_synth_ratio'] = times['other_synth_time'] / times['shell_time']

length = len(results['HacksynthHackdelFullSygus64'][0])
downscaled = 0
finding_c = 0
other = 0

unaccounted = 0

for (testcase, times) in results['HacksynthHackdelFullSygusDownscaling64'][0].items():
    if 'downscaled_synth_time' in times:
        downscaled += times['downscaled_synth_ratio']
        finding_c += times['finding_constants_ratio']
        other += times['other_synth_ratio']
        
print(downscaled / length, finding_c / length, other / length)
print("unaccounted", unaccounted)

# exit(0)

merged_data = {} # {benchmark_name: { test_name: [result1, result2, ...], test_name2: ...}}
for (key, rounds) in results.items():
    data = {}
    if len(rounds) < 1:
        continue
    for test in rounds[0].keys():
        data[test] = []
        for it in rounds:
            if isinstance(it[test], dict):
                data[test] = { key: value / (10**9) if value != 'timeout' else 5000
                    for (key,value) in it[test].items()
                }
            else:
                data[test].append(it[test] / (10 ** 9) if it[test] != 'timeout' else 5000)
                
    merged_data[key] = data

print(merged_data)

new_cvc5_results = {}
# as sygus tests have weird names, transform them here
for (test_name, results) in merged_data['cvc5-64bit-benchmark'].items():
    # hd-04-d0-prog.sl
    new_name = "p" + test_name[3:5] + "_d" + test_name[7]
    new_cvc5_results[new_name] = results

# remove HackStdHackdelBenchmark, as it is incomparable
# del merged_data['HacksynthStdHackdelBenchmark']

double_array_format = {} # {benchmark_name: [[result1, result2, ...], [result1, result2, ...]]}
for (key, data) in merged_data.items():
    double_array_format[key] = [v for v in data.values()]

draw_bar_plot(
    [('HacksynthHackdelFullSygus64', double_array_format["HacksynthHackdelFullSygus64"]), 
     ('HacksynthHackdelFullSygusDownscaling64', double_array_format["HacksynthHackdelFullSygusDownscaling64"]), 
     ('cvc5-64bit-benchmark', double_array_format["cvc5-64bit-benchmark"]), 
     # double_array_format["HacksynthStdHackdelBenchmark"]
     ], 
     # [i for i in range(0, 44)], 
     axis_ticks=merged_data["HacksynthHackdelFullSygus64"].keys(), output="output_cmp_sygus_ds.svg")