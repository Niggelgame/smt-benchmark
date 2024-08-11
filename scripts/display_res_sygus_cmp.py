from matplotlib import pyplot as plt


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

results = {'HacksynthHackdelExtendedSygus': [{'p01_d1': 485306859, 'p01_d5': 1134595141, 'p02_d0': 450197579, 'p02_d1': 647734807, 'p02_d5': 2617871765, 'p03_d0': 362003230, 'p03_d1': 581104460, 'p03_d5': 1180876923, 'p04_d0': 372857139, 'p04_d1': 521544871, 'p04_d5': 1407682088, 'p05_d0': 390956751, 'p05_d1': 516141595, 'p05_d5': 1398797447, 'p06_d0': 378798037, 'p06_d1': 532757542, 'p06_d5': 1359567154, 'p07_d0': 636697512, 'p07_d1': 1141359453, 'p07_d5': 4650526530, 'p08_d0': 692293383, 'p08_d1': 1127460765, 'p08_d5': 4034647673, 'p09_d0': 875567989, 'p09_d1': 1535754798, 'p09_d5': 4085814456, 'p13_d0': 1072085714, 'p13_d1': 18039207718, 'p13_d5': 28484053057, 'p14_d0': 97981141626, 'p14_d1': 149753240051, 'p14_d5': 552779349799, 'p15_d0': 148759153608, 'p15_d1': 167591590054, 'p15_d5': 166636375334, 'p17_d0': 2189958860, 'p17_d1': 4059021031, 'p17_d5': 136936090964, 'p19_d0': 32003535852, 'p19_d1': 516056220519, 'p19_d5': 'timeout', 'p20_d0': 2160871412346, 'p20_d1': 'timeout', 'p20_d5': 'timeout'}], 'HacksynthHackdelFullSygus': [{'p01_d1': 484399345, 'p01_d5': 1143510753, 'p02_d0': 421832021, 'p02_d1': 557763605, 'p02_d5': 1635657355, 'p03_d0': 357445989, 'p03_d1': 585758987, 'p03_d5': 1170975680, 'p04_d0': 376412416, 'p04_d1': 510490570, 'p04_d5': 1400513551, 'p05_d0': 386732924, 'p05_d1': 514410725, 'p05_d5': 1381744365, 'p06_d0': 381003602, 'p06_d1': 531287920, 'p06_d5': 1330276955, 'p07_d0': 639592443, 'p07_d1': 1141078535, 'p07_d5': 4715845161, 'p08_d0': 684982794, 'p08_d1': 1122788440, 'p08_d5': 3966500107, 'p09_d0': 770766788, 'p09_d1': 1357575987, 'p09_d5': 4752075425, 'p13_d0': 317948933, 'p13_d1': 419993993, 'p13_d5': 582968933, 'p14_d0': 79536170165, 'p14_d1': 10952332044, 'p14_d5': 259044110973, 'p15_d0': 1314567441, 'p15_d1': 7147825377, 'p15_d5': 107633152564, 'p17_d0': 2142050586, 'p17_d1': 4052450906, 'p17_d5': 140184339597, 'p19_d0': 775358380278, 'p19_d1': 725902887085, 'p19_d5': 'timeout', 'p20_d0': 'timeout', 'p20_d1': 'timeout', 'p20_d5': 'timeout'}], 'cvc5-8bit-benchmark': [{'hd-01-d1-prog.sl': 7144530, 'hd-01-d5-prog.sl': 2036851847, 'hd-02-d0-prog.sl': 5029161, 'hd-02-d1-prog.sl': 6348687, 'hd-02-d5-prog.sl': 716927148, 'hd-03-d0-prog.sl': 4599835, 'hd-03-d1-prog.sl': 7163595, 'hd-03-d5-prog.sl': 4071069958, 'hd-04-d0-prog.sl': 6050568, 'hd-04-d1-prog.sl': 10193916, 'hd-04-d5-prog.sl': 667204934, 'hd-05-d0-prog.sl': 6693675, 'hd-05-d1-prog.sl': 9995411, 'hd-05-d5-prog.sl': 5183331746, 'hd-06-d0-prog.sl': 6056505, 'hd-06-d1-prog.sl': 8780617, 'hd-06-d5-prog.sl': 4809639028, 'hd-07-d0-prog.sl': 8423487, 'hd-07-d1-prog.sl': 37519642, 'hd-07-d5-prog.sl': 39972811464, 'hd-08-d0-prog.sl': 10359624, 'hd-08-d1-prog.sl': 13827980, 'hd-08-d5-prog.sl': 312728900732, 'hd-09-d0-prog.sl': 130028936, 'hd-09-d1-prog.sl': 51656203188, 'hd-09-d5-prog.sl': 2960498925706, 'hd-13-d0-prog.sl': 6144969, 'hd-13-d1-prog.sl': 6943117, 'hd-13-d5-prog.sl': 66063796, 'hd-14-d0-prog.sl': 3322604400, 'hd-14-d1-prog.sl': 110504773723, 'hd-14-d5-prog.sl': 'timeout', 'hd-15-d0-prog.sl': 5203768218, 'hd-15-d1-prog.sl': 116475051094, 'hd-15-d5-prog.sl': 'timeout', 'hd-17-d0-prog.sl': 21204260, 'hd-17-d1-prog.sl': 128107889, 'hd-17-d5-prog.sl': 'timeout', 'hd-19-d0-prog.sl': 'timeout', 'hd-19-d1-prog.sl': 'timeout', 'hd-19-d5-prog.sl': 'timeout', 'hd-20-d0-prog.sl': 'timeout', 'hd-20-d1-prog.sl': 'timeout', 'hd-20-d5-prog.sl': 'timeout'}], 'HacksynthStdHackdelBenchmark': [{'p01': 379447391, 'p02': 499612579, 'p03': 492246314, 'p04': 376415299, 'p05': 395870365, 'p06': 403792646, 'p07': 765856111, 'p08': 766214172, 'p09': 726024984, 'p10': 759562682, 'p11': 733699583, 'p12': 755601162, 'p13': 5898854384, 'p14': 1834742340, 'p15': 2832595098, 'p16': 1379855407, 'p17': 2187167734, 'p18': 561411574, 'p19': 10171062365, 'p20': 'timeout', 'p21': 2155054080229, 'p22': 2579063730231, 'p23': 'timeout', 'p24': 298674131790}]}


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


new_cvc5_results = {}
# as sygus tests have weird names, transform them here
for (test_name, results) in merged_data['cvc5-8bit-benchmark'].items():
    # hd-04-d0-prog.sl
    new_name = "p" + test_name[3:5] + "_d" + test_name[7]
    new_cvc5_results[new_name] = results

# remove HackStdHackdelBenchmark, as it is incomparable
del merged_data['HacksynthStdHackdelBenchmark']

double_array_format = {} # {benchmark_name: [[result1, result2, ...], [result1, result2, ...]]}
for (key, data) in merged_data.items():
    double_array_format[key] = [v for v in data.values()]

draw_plot(
    [double_array_format["HacksynthHackdelFullSygus"], 
     double_array_format["cvc5-8bit-benchmark"], 
     # double_array_format["HacksynthStdHackdelBenchmark"]
     ], 
     [i for i in range(0, 44)], axis_ticks=merged_data["HacksynthHackdelFullSygus"].keys(), output="output_cmp_sygus.svg")