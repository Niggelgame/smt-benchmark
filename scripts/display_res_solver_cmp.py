

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


data_invalid = {'results': {'HacksynthSolverComp (invalid due to missing binary)': [{'solve_external_yices': {'p01': 1329630618, 'p02': 1310047971, 'p03': 1318705632, 'p04': 1322241328, 'p05': 1336643642, 'p06': 1250696565, 'p07': 1523800532, 'p08': 1619856899, 'p09': 1683040712, 'p10': 1892525777, 'p11': 1931810241, 'p12': 1911801302, 'p13': 1986426795, 'p14': 1969971160, 'p15': 1979927520, 'p16': 1881516390, 'p17': 1867132960, 'p18': 1571698729, 'p19': 2289968178, 'p20': 2694717886, 'p21': 1832037296, 'p22': 1908096127, 'p23': 1934258117, 'p24': 1963028385}, 'solve_z3': {'p01': 383463790, 'p02': 806650728, 'p03': 487205053, 'p04': 375429348, 'p05': 412486345, 'p06': 391266551, 'p07': 698946175, 'p08': 918490599, 'p09': 830376042, 'p10': 940613575, 'p11': 770765105, 'p12': 901960672, 'p13': 2714284824, 'p14': 2153483597, 'p15': 2168740057, 'p16': 1310810940, 'p17': 2885882482, 'p18': 587443494, 'p19': 9033189162, 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_external_bitwuzla': {'p01': 1338350074, 'p02': 1323658716, 'p03': 1335380625, 'p04': 1356586814, 'p05': 1343835473, 'p06': 1255612366, 'p07': 1527937876, 'p08': 1653049302, 'p09': 1660105778, 'p10': 1896327911, 'p11': 1926206928, 'p12': 1892053570, 'p13': 1948631140, 'p14': 1983214872, 'p15': 2011150754, 'p16': 1880008480, 'p17': 1883961883, 'p18': 1598787737, 'p19': 2297511027, 'p20': 2700466859, 'p21': 1841744782, 'p22': 1927287400, 'p23': 1963817849, 'p24': 1958184535}, 'solve_external_cvc5': {'p01': 536483760, 'p02': 946092692, 'p03': 685663762, 'p04': 447207480, 'p05': 495313055, 'p06': 499037397, 'p07': 960974886, 'p08': 918530822, 'p09': 1696859706, 'p10': 1615987699, 'p11': 1364879780, 'p12': 1154884934, 'p13': 246920061165, 'p14': 159334918098, 'p15': 'timeout', 'p16': 11831587040, 'p17': 8469327932, 'p18': 786689894, 'p19': 'timeout', 'p20': 2906663099, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 3501975836}}], 'HacksynthOptimizeDepthOptimizer': [None], 'HacksynthSolverComp32': [{'solve_external_yices': {'p01': 1321832124, 'p02': 1984197206, 'p03': 1317953711, 'p04': 1302483096, 'p05': 1313494383, 'p06': 1249200638, 'p07': 1493453926, 'p08': 1595285301, 'p09': 1613662824, 'p10': 2586658207, 'p11': 2515901836, 'p12': 2576788378, 'p13': 1935043994, 'p14': 1938483409, 'p15': 1975050471, 'p16': 1844082634, 'p17': 1832770406, 'p18': 1686926591, 'p19': 2298695652, 'p20': 3418239016, 'p21': 1815281718, 'p22': 2057807664, 'p23': 2083887015, 'p24': 4128894249}, 'solve_z3': {'p01': 480767772, 'p02': 55651171293, 'p03': 491649694, 'p04': 415874540, 'p05': 416803502, 'p06': 376036284, 'p07': 1324316803, 'p08': 736257760, 'p09': 989463271, 'p10': 1167075521, 'p11': 1402258393, 'p12': 1330381045, 'p13': 106388739306, 'p14': 4114213191, 'p15': 10243065094, 'p16': 2020389156, 'p17': 16331667980, 'p18': 756235977, 'p19': 35313095032, 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_external_bitwuzla': {'p01': 1321151111, 'p02': 2001815179, 'p03': 1328541837, 'p04': 1324842615, 'p05': 1304405525, 'p06': 1243112902, 'p07': 1522818309, 'p08': 1599101853, 'p09': 1644608235, 'p10': 2568887083, 'p11': 2578029661, 'p12': 2529124802, 'p13': 1943317235, 'p14': 1955356562, 'p15': 1999458692, 'p16': 1866034691, 'p17': 1862836941, 'p18': 1700619522, 'p19': 2294092766, 'p20': 3387130755, 'p21': 1808858780, 'p22': 2040183693, 'p23': 2081278897, 'p24': 4160558010}, 'solve_external_cvc5': {'p01': 635208891, 'p02': 45134246870, 'p03': 625141477, 'p04': 507466377, 'p05': 502966431, 'p06': 432273863, 'p07': 1028095001, 'p08': 976542498, 'p09': 1577402955, 'p10': 2107746545, 'p11': 2102318843, 'p12': 1832627594, 'p13': 1747693282422, 'p14': 228720742299, 'p15': 'timeout', 'p16': 11876276778, 'p17': 15453929007, 'p18': 806425477, 'p19': 'timeout', 'p20': 3589160772, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}}], 'HacksynthStdHackdelBenchmark': [{'p01': 414513493, 'p02': 814015189, 'p03': 485499114, 'p04': 379734915, 'p05': 410653511, 'p06': 392453823, 'p07': 694194635, 'p08': 932414591, 'p09': 829966609, 'p10': 949680029, 'p11': 779771452, 'p12': 889818224, 'p13': 2700928421, 'p14': 2122685835, 'p15': 2144246600, 'p16': 1329545394, 'p17': 2915764929, 'p18': 624130995, 'p19': 9131945077, 'p20': 'timeout', 'p21': 1362475807981, 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}]}, 'arguments': 'benchmark=hacksynth_solver_comp.py,hacksynth_optimize_depth_optimizer.py,hacksynth_solver_comp_32bit.py,hacksynth_std_hackdel_benchmark.py output=outfile_solver_cmp_depth_opt intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}

# results for hacksynth tests on each solver, 8 and 32 bit
data_hacksynth = {'results': {'HacksynthSolverComp': [{'solve_external_yices': {'p01': 433133650, 'p02': 575313419, 'p03': 613884250, 'p04': 432057680, 'p05': 463687686, 'p06': 402223836, 'p07': 849466778, 'p08': 1486503454, 'p09': 891544123, 'p10': 872348167, 'p11': 1128273226, 'p12': 1181305092, 'p13': 3174411930, 'p14': 3295069486, 'p15': 3842193035, 'p16': 2079801847, 'p17': 5668890180, 'p18': 709133335, 'p19': 10231313210, 'p20': 2884883761, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_z3': {'p01': 381237859, 'p02': 797937797, 'p03': 491843436, 'p04': 380514138, 'p05': 414047728, 'p06': 388808767, 'p07': 690177551, 'p08': 933625928, 'p09': 831200429, 'p10': 945995848, 'p11': 778958640, 'p12': 898746445, 'p13': 2707757462, 'p14': 2122645491, 'p15': 2126704936, 'p16': 1305959793, 'p17': 2896675296, 'p18': 590284844, 'p19': 9158810654, 'p20': 117123805803, 'p21': 303241963398, 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_external_bitwuzla': {'p01': 473207458, 'p02': 798785048, 'p03': 560992840, 'p04': 450970149, 'p05': 474453507, 'p06': 431234699, 'p07': 782820105, 'p08': 731976839, 'p09': 1150416063, 'p10': 1133009223, 'p11': 936065147, 'p12': 957380794, 'p13': 6781684658, 'p14': 2654786415, 'p15': 2893403070, 'p16': 2118360292, 'p17': 3255743359, 'p18': 764080589, 'p19': 12144730287, 'p20': 2823290160, 'p21': 'timeout', 'p22': 382405304772, 'p23': 'timeout', 'p24': 162623755905}, 'solve_external_cvc5': {'p01': 495216648, 'p02': 949274769, 'p03': 688179957, 'p04': 449816776, 'p05': 495515837, 'p06': 494264402, 'p07': 980436048, 'p08': 917385907, 'p09': 1695808350, 'p10': 1540369888, 'p11': 1374227063, 'p12': 1150816834, 'p13': 246711770095, 'p14': 158760301657, 'p15': 'timeout', 'p16': 11562632991, 'p17': 8472336153, 'p18': 804697148, 'p19': 'timeout', 'p20': 2919583554, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 3593574055}}], 'HacksynthSolverComp32': [{'solve_external_yices': {'p01': 481774539, 'p02': 1089565412, 'p03': 544164374, 'p04': 414399011, 'p05': 403836420, 'p06': 415963970, 'p07': 884169199, 'p08': 3303139581, 'p09': 858877438, 'p10': 1417957841, 'p11': 1456265040, 'p12': 1336523387, 'p13': 13659300586, 'p14': 3574423802, 'p15': 6596961555, 'p16': 1699355765, 'p17': 4557612645, 'p18': 770914426, 'p19': 114832323433, 'p20': 3456761092, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_z3': {'p01': 481600648, 'p02': 56012506158, 'p03': 502378680, 'p04': 418269532, 'p05': 419025577, 'p06': 376867980, 'p07': 1329927098, 'p08': 730411397, 'p09': 984937385, 'p10': 1180124356, 'p11': 1394385899, 'p12': 1335821543, 'p13': 108198061693, 'p14': 4125290910, 'p15': 10523045941, 'p16': 2059874875, 'p17': 16249186530, 'p18': 749964052, 'p19': 36027851152, 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_external_bitwuzla': {'p01': 506308435, 'p02': 84978206715, 'p03': 561308548, 'p04': 460345033, 'p05': 420004406, 'p06': 409736251, 'p07': 848658946, 'p08': 1122858720, 'p09': 2026494666, 'p10': 1705689459, 'p11': 1651187796, 'p12': 1564960337, 'p13': 47701451936, 'p14': 5187388621, 'p15': 8202842622, 'p16': 2433589822, 'p17': 5376530487, 'p18': 860287498, 'p19': 11141686723, 'p20': 3510736765, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_external_cvc5': {'p01': 647298665, 'p02': 45271452413, 'p03': 611471193, 'p04': 506956172, 'p05': 502652017, 'p06': 432275537, 'p07': 1017277237, 'p08': 985998629, 'p09': 1526525392, 'p10': 2077137320, 'p11': 2145393570, 'p12': 1764075181, 'p13': 1752288368929, 'p14': 221684327246, 'p15': 'timeout', 'p16': 11858483201, 'p17': 15577385020, 'p18': 806157408, 'p19': 'timeout', 'p20': 3577069758, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}}]}, 'arguments': 'benchmark=hacksynth_solver_comp.py,hacksynth_solver_comp_32bit.py output=outfile_solver_cmp intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}
data_hacksynth32 = data_hacksynth['results']['HacksynthSolverComp32']
data_hacksynth8 = data_hacksynth['results']['HacksynthSolverComp']

# Sygus Tests with diffs for each solver
data_sygus = {'HacksynthSolverSygusComp': [{'solve_external_yices': {'p01_d1': 589194841, 'p01_d5': 5452496628, 'p02_d0': 403758469, 'p02_d1': 630745220, 'p02_d5': 5689240646, 'p03_d0': 95913808, 'p03_d1': 542632090, 'p03_d5': 5615151058, 'p04_d0': 413212023, 'p04_d1': 642509125, 'p04_d5': 5465066035, 'p05_d0': 471647090, 'p05_d1': 647066736, 'p05_d5': 5546107759, 'p06_d0': 437686467, 'p06_d1': 709680846, 'p06_d5': 5526762801, 'p07_d0': 452919598, 'p07_d1': 675098267, 'p07_d5': 5489581162, 'p08_d0': 689270745, 'p08_d1': 1063330769, 'p08_d5': 5529660090, 'p09_d0': 731762982, 'p09_d1': 1495618912, 'p09_d5': 5546970599, 'p13_d0': 508476261, 'p13_d1': 4921617788, 'p13_d5': 5565516926, 'p14_d0': 95782885086, 'p14_d1': 4446339565, 'p14_d5': 5863228050, 'p15_d0': 2003680350, 'p15_d1': 4998976919, 'p15_d5': 6006057554, 'p17_d0': 1357552045, 'p17_d1': 1789090564, 'p17_d5': 5501546304, 'p19_d0': 99995642, 'p19_d1': 101624573, 'p19_d5': 7145194564, 'p20_d0': 2881559957, 'p20_d1': 3866960868, 'p20_d5': 5597242602}, 'solve_z3': {'p01_d1': 480896056, 'p01_d5': 968342432, 'p02_d0': 405693168, 'p02_d1': 539195980, 'p02_d5': 973112973, 'p03_d0': 98490794, 'p03_d1': 499354601, 'p03_d5': 1051161006, 'p04_d0': 348138971, 'p04_d1': 610636870, 'p04_d5': 1207912544, 'p05_d0': 384006086, 'p05_d1': 567967916, 'p05_d5': 1396774505, 'p06_d0': 422380888, 'p06_d1': 632467394, 'p06_d5': 1527186262, 'p07_d0': 470597788, 'p07_d1': 773070098, 'p07_d5': 2062829817, 'p08_d0': 666581977, 'p08_d1': 909345014, 'p08_d5': 2074115883, 'p09_d0': 659215582, 'p09_d1': 1192819631, 'p09_d5': 2160196104, 'p13_d0': 636509623, 'p13_d1': 1738245524, 'p13_d5': 3133579326, 'p14_d0': 74902533397, 'p14_d1': 2993592622, 'p14_d5': 89535680903, 'p15_d0': 1463294500, 'p15_d1': 4481657403, 'p15_d5': 34524293330, 'p17_d0': 1024266487, 'p17_d1': 1530985339, 'p17_d5': 26876007062, 'p19_d0': 98623371, 'p19_d1': 102858388, 'p19_d5': 'timeout', 'p20_d0': 13411878057, 'p20_d1': 774064469490, 'p20_d5': 'timeout'}, 'solve_external_bitwuzla': {'p01_d1': 545876769, 'p01_d5': 5535359281, 'p02_d0': 438517536, 'p02_d1': 643055340, 'p02_d5': 5681887244, 'p03_d0': 98479033, 'p03_d1': 555091602, 'p03_d5': 5564738204, 'p04_d0': 382428738, 'p04_d1': 604412312, 'p04_d5': 5599695445, 'p05_d0': 470277568, 'p05_d1': 660248303, 'p05_d5': 5529614824, 'p06_d0': 433034422, 'p06_d1': 646394638, 'p06_d5': 5565217661, 'p07_d0': 512312114, 'p07_d1': 896616709, 'p07_d5': 5488573565, 'p08_d0': 651443901, 'p08_d1': 1194126129, 'p08_d5': 5523876379, 'p09_d0': 842196936, 'p09_d1': 1245176996, 'p09_d5': 5609919150, 'p13_d0': 717224144, 'p13_d1': 2752389826, 'p13_d5': 5614051121, 'p14_d0': 70210934736, 'p14_d1': 3471828960, 'p14_d5': 5950397443, 'p15_d0': 1705492878, 'p15_d1': 8724032755, 'p15_d5': 6048142324, 'p17_d0': 1255007686, 'p17_d1': 2134769239, 'p17_d5': 5496620176, 'p19_d0': 98957434, 'p19_d1': 101880820, 'p19_d5': 7147503736, 'p20_d0': 2936553586, 'p20_d1': 3889504665, 'p20_d5': 5606603184}, 'solve_external_cvc5': {'p01_d1': 691279562, 'p01_d5': 5649341302, 'p02_d0': 467440861, 'p02_d1': 738692252, 'p02_d5': 5851025188, 'p03_d0': 98134100, 'p03_d1': 657505825, 'p03_d5': 5665046954, 'p04_d0': 413325612, 'p04_d1': 653081237, 'p04_d5': 5663623499, 'p05_d0': 492500355, 'p05_d1': 641971190, 'p05_d5': 5650748462, 'p06_d0': 477224619, 'p06_d1': 673937039, 'p06_d5': 5688175402, 'p07_d0': 519238452, 'p07_d1': 913371746, 'p07_d5': 5623631131, 'p08_d0': 778130123, 'p08_d1': 1252260009, 'p08_d5': 5669974319, 'p09_d0': 1036168485, 'p09_d1': 7658169397, 'p09_d5': 5742145794, 'p13_d0': 546844655, 'p13_d1': 'timeout', 'p13_d5': 5732581111, 'p14_d0': 'timeout', 'p14_d1': 696722743603, 'p14_d5': 5988075010, 'p15_d0': 11071166662, 'p15_d1': 920875080053, 'p15_d5': 6131768895, 'p17_d0': 2611444525, 'p17_d1': 12558939390, 'p17_d5': 5722674184, 'p19_d0': 101924748, 'p19_d1': 100982360, 'p19_d5': 7238544274, 'p20_d0': 3045411673, 'p20_d1': 3973524042, 'p20_d5': 5615496666}}]}
data_sygus = data_sygus['HacksynthSolverSygusComp']

# hackdel tests with -c COUNT
data_const_count = {'HacksynthSolverCompConstantModesCount': [{'solve_external_yices': {'p01': 409812286, 'p02': 739636931, 'p03': 99073483, 'p04': 429787717, 'p05': 438176198, 'p06': 455829044, 'p07': 618505373, 'p08': 698091999, 'p09': 774428822, 'p10': 111747389, 'p11': 110611534, 'p12': 110833661, 'p13': 2415434811, 'p14': 1075241867, 'p15': 1966358644, 'p16': 94644900, 'p17': 2054655387, 'p18': 97058004, 'p19': 99925158, 'p20': 2729552378, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_z3': {'p01': 411970257, 'p02': 506796939, 'p03': 97419822, 'p04': 392735404, 'p05': 396407564, 'p06': 362953277, 'p07': 606458907, 'p08': 613634402, 'p09': 754792650, 'p10': 115345076, 'p11': 111404078, 'p12': 114333049, 'p13': 2521278822, 'p14': 1471072875, 'p15': 2928163494, 'p16': 96859103, 'p17': 3098973806, 'p18': 95786534, 'p19': 98282260, 'p20': 'timeout', 'p21': 'timeout', 'p22': 1740474014254, 'p23': 'timeout', 'p24': 'timeout'}, 'solve_external_bitwuzla': {'p01': 426106962, 'p02': 745835619, 'p03': 95917299, 'p04': 411372781, 'p05': 509905535, 'p06': 422594806, 'p07': 683256225, 'p08': 668232420, 'p09': 909401580, 'p10': 116013992, 'p11': 111230783, 'p12': 111334672, 'p13': 3535864537, 'p14': 1233452036, 'p15': 2018964230, 'p16': 94948420, 'p17': 1853854509, 'p18': 100327583, 'p19': 98746620, 'p20': 2810906853, 'p21': 165305918498, 'p22': 'timeout', 'p23': 'timeout', 'p24': 1213279014531}, 'solve_external_cvc5': {'p01': 479434632, 'p02': 838612836, 'p03': 94348726, 'p04': 443124068, 'p05': 437101546, 'p06': 448715308, 'p07': 708362188, 'p08': 773910775, 'p09': 1246175251, 'p10': 111359676, 'p11': 113997176, 'p12': 111753831, 'p13': 65568086634, 'p14': 19223673526, 'p15': 24977978895, 'p16': 100070826, 'p17': 3623597397, 'p18': 99249195, 'p19': 98364352, 'p20': 2874529582, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}}]}
data_const_count = data_const_count['HacksynthSolverCompConstantModesCount']

# hackdel tests with more stuff (free then set)
data_const_set = {'results': {'HacksynthSolverSygusComp': [{'solve_external_yices': {'p01_d1': 589194841, 'p01_d5': 5452496628, 'p02_d0': 403758469, 'p02_d1': 630745220, 'p02_d5': 5689240646, 'p03_d0': 95913808, 'p03_d1': 542632090, 'p03_d5': 5615151058, 'p04_d0': 413212023, 'p04_d1': 642509125, 'p04_d5': 5465066035, 'p05_d0': 471647090, 'p05_d1': 647066736, 'p05_d5': 5546107759, 'p06_d0': 437686467, 'p06_d1': 709680846, 'p06_d5': 5526762801, 'p07_d0': 452919598, 'p07_d1': 675098267, 'p07_d5': 5489581162, 'p08_d0': 689270745, 'p08_d1': 1063330769, 'p08_d5': 5529660090, 'p09_d0': 731762982, 'p09_d1': 1495618912, 'p09_d5': 5546970599, 'p13_d0': 508476261, 'p13_d1': 4921617788, 'p13_d5': 5565516926, 'p14_d0': 95782885086, 'p14_d1': 4446339565, 'p14_d5': 5863228050, 'p15_d0': 2003680350, 'p15_d1': 4998976919, 'p15_d5': 6006057554, 'p17_d0': 1357552045, 'p17_d1': 1789090564, 'p17_d5': 5501546304, 'p19_d0': 99995642, 'p19_d1': 101624573, 'p19_d5': 7145194564, 'p20_d0': 2881559957, 'p20_d1': 3866960868, 'p20_d5': 5597242602}, 'solve_z3': {'p01_d1': 480896056, 'p01_d5': 968342432, 'p02_d0': 405693168, 'p02_d1': 539195980, 'p02_d5': 973112973, 'p03_d0': 98490794, 'p03_d1': 499354601, 'p03_d5': 1051161006, 'p04_d0': 348138971, 'p04_d1': 610636870, 'p04_d5': 1207912544, 'p05_d0': 384006086, 'p05_d1': 567967916, 'p05_d5': 1396774505, 'p06_d0': 422380888, 'p06_d1': 632467394, 'p06_d5': 1527186262, 'p07_d0': 470597788, 'p07_d1': 773070098, 'p07_d5': 2062829817, 'p08_d0': 666581977, 'p08_d1': 909345014, 'p08_d5': 2074115883, 'p09_d0': 659215582, 'p09_d1': 1192819631, 'p09_d5': 2160196104, 'p13_d0': 636509623, 'p13_d1': 1738245524, 'p13_d5': 3133579326, 'p14_d0': 74902533397, 'p14_d1': 2993592622, 'p14_d5': 89535680903, 'p15_d0': 1463294500, 'p15_d1': 4481657403, 'p15_d5': 34524293330, 'p17_d0': 1024266487, 'p17_d1': 1530985339, 'p17_d5': 26876007062, 'p19_d0': 98623371, 'p19_d1': 102858388, 'p19_d5': 'timeout', 'p20_d0': 13411878057, 'p20_d1': 774064469490, 'p20_d5': 'timeout'}, 'solve_external_bitwuzla': {'p01_d1': 545876769, 'p01_d5': 5535359281, 'p02_d0': 438517536, 'p02_d1': 643055340, 'p02_d5': 5681887244, 'p03_d0': 98479033, 'p03_d1': 555091602, 'p03_d5': 5564738204, 'p04_d0': 382428738, 'p04_d1': 604412312, 'p04_d5': 5599695445, 'p05_d0': 470277568, 'p05_d1': 660248303, 'p05_d5': 5529614824, 'p06_d0': 433034422, 'p06_d1': 646394638, 'p06_d5': 5565217661, 'p07_d0': 512312114, 'p07_d1': 896616709, 'p07_d5': 5488573565, 'p08_d0': 651443901, 'p08_d1': 1194126129, 'p08_d5': 5523876379, 'p09_d0': 842196936, 'p09_d1': 1245176996, 'p09_d5': 5609919150, 'p13_d0': 717224144, 'p13_d1': 2752389826, 'p13_d5': 5614051121, 'p14_d0': 70210934736, 'p14_d1': 3471828960, 'p14_d5': 5950397443, 'p15_d0': 1705492878, 'p15_d1': 8724032755, 'p15_d5': 6048142324, 'p17_d0': 1255007686, 'p17_d1': 2134769239, 'p17_d5': 5496620176, 'p19_d0': 98957434, 'p19_d1': 101880820, 'p19_d5': 7147503736, 'p20_d0': 2936553586, 'p20_d1': 3889504665, 'p20_d5': 5606603184}, 'solve_external_cvc5': {'p01_d1': 691279562, 'p01_d5': 5649341302, 'p02_d0': 467440861, 'p02_d1': 738692252, 'p02_d5': 5851025188, 'p03_d0': 98134100, 'p03_d1': 657505825, 'p03_d5': 5665046954, 'p04_d0': 413325612, 'p04_d1': 653081237, 'p04_d5': 5663623499, 'p05_d0': 492500355, 'p05_d1': 641971190, 'p05_d5': 5650748462, 'p06_d0': 477224619, 'p06_d1': 673937039, 'p06_d5': 5688175402, 'p07_d0': 519238452, 'p07_d1': 913371746, 'p07_d5': 5623631131, 'p08_d0': 778130123, 'p08_d1': 1252260009, 'p08_d5': 5669974319, 'p09_d0': 1036168485, 'p09_d1': 7658169397, 'p09_d5': 5742145794, 'p13_d0': 546844655, 'p13_d1': 'timeout', 'p13_d5': 5732581111, 'p14_d0': 'timeout', 'p14_d1': 696722743603, 'p14_d5': 5988075010, 'p15_d0': 11071166662, 'p15_d1': 920875080053, 'p15_d5': 6131768895, 'p17_d0': 2611444525, 'p17_d1': 12558939390, 'p17_d5': 5722674184, 'p19_d0': 101924748, 'p19_d1': 100982360, 'p19_d5': 7238544274, 'p20_d0': 3045411673, 'p20_d1': 3973524042, 'p20_d5': 5615496666}}], 'HacksynthSolverCompConstantModes': [{'solve_external_yices': {'p01': 409812286, 'p02': 739636931, 'p03': 99073483, 'p04': 429787717, 'p05': 438176198, 'p06': 455829044, 'p07': 618505373, 'p08': 698091999, 'p09': 774428822, 'p10': 111747389, 'p11': 110611534, 'p12': 110833661, 'p13': 2415434811, 'p14': 1075241867, 'p15': 1966358644, 'p16': 94644900, 'p17': 2054655387, 'p18': 97058004, 'p19': 99925158, 'p20': 2729552378, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_z3': {'p01': 411970257, 'p02': 506796939, 'p03': 97419822, 'p04': 392735404, 'p05': 396407564, 'p06': 362953277, 'p07': 606458907, 'p08': 613634402, 'p09': 754792650, 'p10': 115345076, 'p11': 111404078, 'p12': 114333049, 'p13': 2521278822, 'p14': 1471072875, 'p15': 2928163494, 'p16': 96859103, 'p17': 3098973806, 'p18': 95786534, 'p19': 98282260, 'p20': 'timeout', 'p21': 'timeout', 'p22': 1740474014254, 'p23': 'timeout', 'p24': 'timeout'}, 'solve_external_bitwuzla': {'p01': 426106962, 'p02': 745835619, 'p03': 95917299, 'p04': 411372781, 'p05': 509905535, 'p06': 422594806, 'p07': 683256225, 'p08': 668232420, 'p09': 909401580, 'p10': 116013992, 'p11': 111230783, 'p12': 111334672, 'p13': 3535864537, 'p14': 1233452036, 'p15': 2018964230, 'p16': 94948420, 'p17': 1853854509, 'p18': 100327583, 'p19': 98746620, 'p20': 2810906853, 'p21': 165305918498, 'p22': 'timeout', 'p23': 'timeout', 'p24': 1213279014531}, 'solve_external_cvc5': {'p01': 479434632, 'p02': 838612836, 'p03': 94348726, 'p04': 443124068, 'p05': 437101546, 'p06': 448715308, 'p07': 708362188, 'p08': 773910775, 'p09': 1246175251, 'p10': 111359676, 'p11': 113997176, 'p12': 111753831, 'p13': 65568086634, 'p14': 19223673526, 'p15': 24977978895, 'p16': 100070826, 'p17': 3623597397, 'p18': 99249195, 'p19': 98364352, 'p20': 2874529582, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}}, {'solve_external_yices': {'p01': 408773449, 'p02': 542978103, 'p03': 523156506, 'p04': 402502151, 'p05': 401747058, 'p06': 382758173, 'p07': 809956782, 'p08': 1405836384, 'p09': 858347779, 'p10': 3180963829, 'p11': 2579798445, 'p12': 4322388667, 'p13': 3011611973, 'p14': 3241674080, 'p15': 3792722959, 'p16': 2781249281, 'p17': 5640588116, 'p18': 1356897468, 'p19': 'timeout', 'p20': 2747022415, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_z3': {'p01': 377780781, 'p02': 775791593, 'p03': 411566725, 'p04': 379289335, 'p05': 399341453, 'p06': 379808639, 'p07': 692277078, 'p08': 920461224, 'p09': 821970134, 'p10': 1873708698, 'p11': 2312203620, 'p12': 2318269819, 'p13': 2688887294, 'p14': 2099478576, 'p15': 2150436734, 'p16': 3130245926, 'p17': 2938319726, 'p18': 646354812, 'p19': 1602753296185, 'p20': 118722207724, 'p21': 286326829537, 'p22': 'timeout', 'p23': 'timeout', 'p24': 1619527852185}, 'solve_external_bitwuzla': {'p01': 450904731, 'p02': 802744975, 'p03': 477344865, 'p04': 446887846, 'p05': 464066741, 'p06': 426232559, 'p07': 754675066, 'p08': 706059660, 'p09': 1124262576, 'p10': 4369339809, 'p11': 3115656943, 'p12': 3034024931, 'p13': 6675500975, 'p14': 2643951400, 'p15': 2922021408, 'p16': 4773439699, 'p17': 3243078579, 'p18': 1162754663, 'p19': 723260832671, 'p20': 2788823610, 'p21': 'timeout', 'p22': 393443749267, 'p23': 'timeout', 'p24': 162430419086}, 'solve_external_cvc5': {'p01': 486921095, 'p02': 953306247, 'p03': 760220715, 'p04': 445356920, 'p05': 482165685, 'p06': 491738204, 'p07': 968815473, 'p08': 925198522, 'p09': 1683280374, 'p10': 7518680205, 'p11': 36949206800, 'p12': 15179998601, 'p13': 246687325238, 'p14': 158491713636, 'p15': 'timeout', 'p16': 'timeout', 'p17': 8577044180, 'p18': 2254345019, 'p19': 'timeout', 'p20': 2864076543, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 3541354597}}, {'solve_external_yices': {'p01': 367610051, 'p02': 431900028, 'p03': 586404004, 'p04': 341627198, 'p05': 408575623, 'p06': 396544647, 'p07': 506374126, 'p08': 684865234, 'p09': 816409450, 'p10': 829829321, 'p11': 1075229764, 'p12': 1142226035, 'p13': 1370313254, 'p14': 1497078111, 'p15': 1271982109, 'p16': 2026809850, 'p17': 1423836091, 'p18': 671966482, 'p19': 10036919441, 'p20': 2893640028, 'p21': 349386262087, 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_z3': {'p01': 364113488, 'p02': 412772277, 'p03': 485448069, 'p04': 337433836, 'p05': 368262770, 'p06': 365657623, 'p07': 462573953, 'p08': 615255919, 'p09': 641093810, 'p10': 950861976, 'p11': 778432287, 'p12': 901997193, 'p13': 1177349827, 'p14': 1077422924, 'p15': 1503970262, 'p16': 1298662818, 'p17': 880531163, 'p18': 580552974, 'p19': 9272642290, 'p20': 123392044971, 'p21': 48204897308, 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_external_bitwuzla': {'p01': 401682676, 'p02': 508742018, 'p03': 549798673, 'p04': 374408686, 'p05': 452060851, 'p06': 430395599, 'p07': 508309247, 'p08': 612046824, 'p09': 794443926, 'p10': 1109224740, 'p11': 925652901, 'p12': 933232735, 'p13': 1797072804, 'p14': 1613335805, 'p15': 1853342710, 'p16': 2061078997, 'p17': 1676342546, 'p18': 753370194, 'p19': 12205194244, 'p20': 2862037755, 'p21': 108358516943, 'p22': 'timeout', 'p23': 'timeout', 'p24': 19530796323}, 'solve_external_cvc5': {'p01': 467844066, 'p02': 516508930, 'p03': 683991333, 'p04': 397519272, 'p05': 484837968, 'p06': 502558655, 'p07': 564352085, 'p08': 747569890, 'p09': 896751196, 'p10': 1535344000, 'p11': 1354819731, 'p12': 1146560357, 'p13': 6994738271, 'p14': 45332252370, 'p15': 40395544111, 'p16': 11579329135, 'p17': 2762156926, 'p18': 780609224, 'p19': 'timeout', 'p20': 2941952768, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}}]}, 'arguments': 'benchmark=hacksynth_solver_sygus_comp.py,hacksynth_solver_comp_constant_modes_count.py,hacksynth_solver_comp_constant_modes_free.py,hacksynth_solver_comp_constant_modes_set.py output=otherdiff_cmp_constset_cmp intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}


data = data_const_count

results = {
    'solve_external_yices': [data[0]['solve_external_yices']],
    'solve_z3': [data[0]['solve_z3']],
    'solve_external_bitwuzla': [data[0]['solve_external_bitwuzla']],
    'solve_external_cvc5': [data[0]['solve_external_cvc5']],
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

# remove HackStdHackdelBenchmark, as it is incomparable
# del merged_data['HacksynthStdHackdelBenchmark']

double_array_format = {} # {benchmark_name: [[result1, result2, ...], [result1, result2, ...]]}
for (key, data) in merged_data.items():
    double_array_format[key] = [v for v in data.values()]

draw_bar_plot(
    [('solve_external_yices', double_array_format["solve_external_yices"]), 
     ('solve_z3', double_array_format["solve_z3"]), 
     ('solve_external_bitwuzla', double_array_format["solve_external_bitwuzla"]), 
     ('solve_external_cvc5', double_array_format["solve_external_cvc5"]), 
     ], 
     # [i for i in range(0, 44)], 
     axis_ticks=merged_data["solve_external_yices"].keys(), output="output_cmp_solvers.svg")