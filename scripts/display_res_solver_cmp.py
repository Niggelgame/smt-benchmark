

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


data = {'results': {'HacksynthSolverComp (invalid due to missing binary)': [{'solve_external_yices': {'p01': 1329630618, 'p02': 1310047971, 'p03': 1318705632, 'p04': 1322241328, 'p05': 1336643642, 'p06': 1250696565, 'p07': 1523800532, 'p08': 1619856899, 'p09': 1683040712, 'p10': 1892525777, 'p11': 1931810241, 'p12': 1911801302, 'p13': 1986426795, 'p14': 1969971160, 'p15': 1979927520, 'p16': 1881516390, 'p17': 1867132960, 'p18': 1571698729, 'p19': 2289968178, 'p20': 2694717886, 'p21': 1832037296, 'p22': 1908096127, 'p23': 1934258117, 'p24': 1963028385}, 'solve_z3': {'p01': 383463790, 'p02': 806650728, 'p03': 487205053, 'p04': 375429348, 'p05': 412486345, 'p06': 391266551, 'p07': 698946175, 'p08': 918490599, 'p09': 830376042, 'p10': 940613575, 'p11': 770765105, 'p12': 901960672, 'p13': 2714284824, 'p14': 2153483597, 'p15': 2168740057, 'p16': 1310810940, 'p17': 2885882482, 'p18': 587443494, 'p19': 9033189162, 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_external_bitwuzla': {'p01': 1338350074, 'p02': 1323658716, 'p03': 1335380625, 'p04': 1356586814, 'p05': 1343835473, 'p06': 1255612366, 'p07': 1527937876, 'p08': 1653049302, 'p09': 1660105778, 'p10': 1896327911, 'p11': 1926206928, 'p12': 1892053570, 'p13': 1948631140, 'p14': 1983214872, 'p15': 2011150754, 'p16': 1880008480, 'p17': 1883961883, 'p18': 1598787737, 'p19': 2297511027, 'p20': 2700466859, 'p21': 1841744782, 'p22': 1927287400, 'p23': 1963817849, 'p24': 1958184535}, 'solve_external_cvc5': {'p01': 536483760, 'p02': 946092692, 'p03': 685663762, 'p04': 447207480, 'p05': 495313055, 'p06': 499037397, 'p07': 960974886, 'p08': 918530822, 'p09': 1696859706, 'p10': 1615987699, 'p11': 1364879780, 'p12': 1154884934, 'p13': 246920061165, 'p14': 159334918098, 'p15': 'timeout', 'p16': 11831587040, 'p17': 8469327932, 'p18': 786689894, 'p19': 'timeout', 'p20': 2906663099, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 3501975836}}], 'HacksynthOptimizeDepthOptimizer': [None], 'HacksynthSolverComp32': [{'solve_external_yices': {'p01': 1321832124, 'p02': 1984197206, 'p03': 1317953711, 'p04': 1302483096, 'p05': 1313494383, 'p06': 1249200638, 'p07': 1493453926, 'p08': 1595285301, 'p09': 1613662824, 'p10': 2586658207, 'p11': 2515901836, 'p12': 2576788378, 'p13': 1935043994, 'p14': 1938483409, 'p15': 1975050471, 'p16': 1844082634, 'p17': 1832770406, 'p18': 1686926591, 'p19': 2298695652, 'p20': 3418239016, 'p21': 1815281718, 'p22': 2057807664, 'p23': 2083887015, 'p24': 4128894249}, 'solve_z3': {'p01': 480767772, 'p02': 55651171293, 'p03': 491649694, 'p04': 415874540, 'p05': 416803502, 'p06': 376036284, 'p07': 1324316803, 'p08': 736257760, 'p09': 989463271, 'p10': 1167075521, 'p11': 1402258393, 'p12': 1330381045, 'p13': 106388739306, 'p14': 4114213191, 'p15': 10243065094, 'p16': 2020389156, 'p17': 16331667980, 'p18': 756235977, 'p19': 35313095032, 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_external_bitwuzla': {'p01': 1321151111, 'p02': 2001815179, 'p03': 1328541837, 'p04': 1324842615, 'p05': 1304405525, 'p06': 1243112902, 'p07': 1522818309, 'p08': 1599101853, 'p09': 1644608235, 'p10': 2568887083, 'p11': 2578029661, 'p12': 2529124802, 'p13': 1943317235, 'p14': 1955356562, 'p15': 1999458692, 'p16': 1866034691, 'p17': 1862836941, 'p18': 1700619522, 'p19': 2294092766, 'p20': 3387130755, 'p21': 1808858780, 'p22': 2040183693, 'p23': 2081278897, 'p24': 4160558010}, 'solve_external_cvc5': {'p01': 635208891, 'p02': 45134246870, 'p03': 625141477, 'p04': 507466377, 'p05': 502966431, 'p06': 432273863, 'p07': 1028095001, 'p08': 976542498, 'p09': 1577402955, 'p10': 2107746545, 'p11': 2102318843, 'p12': 1832627594, 'p13': 1747693282422, 'p14': 228720742299, 'p15': 'timeout', 'p16': 11876276778, 'p17': 15453929007, 'p18': 806425477, 'p19': 'timeout', 'p20': 3589160772, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}}], 'HacksynthStdHackdelBenchmark': [{'p01': 414513493, 'p02': 814015189, 'p03': 485499114, 'p04': 379734915, 'p05': 410653511, 'p06': 392453823, 'p07': 694194635, 'p08': 932414591, 'p09': 829966609, 'p10': 949680029, 'p11': 779771452, 'p12': 889818224, 'p13': 2700928421, 'p14': 2122685835, 'p15': 2144246600, 'p16': 1329545394, 'p17': 2915764929, 'p18': 624130995, 'p19': 9131945077, 'p20': 'timeout', 'p21': 1362475807981, 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}]}, 'arguments': 'benchmark=hacksynth_solver_comp.py,hacksynth_optimize_depth_optimizer.py,hacksynth_solver_comp_32bit.py,hacksynth_std_hackdel_benchmark.py output=outfile_solver_cmp_depth_opt intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}
data = {'results': {'HacksynthSolverComp': [{'solve_external_yices': {'p01': 433133650, 'p02': 575313419, 'p03': 613884250, 'p04': 432057680, 'p05': 463687686, 'p06': 402223836, 'p07': 849466778, 'p08': 1486503454, 'p09': 891544123, 'p10': 872348167, 'p11': 1128273226, 'p12': 1181305092, 'p13': 3174411930, 'p14': 3295069486, 'p15': 3842193035, 'p16': 2079801847, 'p17': 5668890180, 'p18': 709133335, 'p19': 10231313210, 'p20': 2884883761, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_z3': {'p01': 381237859, 'p02': 797937797, 'p03': 491843436, 'p04': 380514138, 'p05': 414047728, 'p06': 388808767, 'p07': 690177551, 'p08': 933625928, 'p09': 831200429, 'p10': 945995848, 'p11': 778958640, 'p12': 898746445, 'p13': 2707757462, 'p14': 2122645491, 'p15': 2126704936, 'p16': 1305959793, 'p17': 2896675296, 'p18': 590284844, 'p19': 9158810654, 'p20': 117123805803, 'p21': 303241963398, 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_external_bitwuzla': {'p01': 473207458, 'p02': 798785048, 'p03': 560992840, 'p04': 450970149, 'p05': 474453507, 'p06': 431234699, 'p07': 782820105, 'p08': 731976839, 'p09': 1150416063, 'p10': 1133009223, 'p11': 936065147, 'p12': 957380794, 'p13': 6781684658, 'p14': 2654786415, 'p15': 2893403070, 'p16': 2118360292, 'p17': 3255743359, 'p18': 764080589, 'p19': 12144730287, 'p20': 2823290160, 'p21': 'timeout', 'p22': 382405304772, 'p23': 'timeout', 'p24': 162623755905}, 'solve_external_cvc5': {'p01': 495216648, 'p02': 949274769, 'p03': 688179957, 'p04': 449816776, 'p05': 495515837, 'p06': 494264402, 'p07': 980436048, 'p08': 917385907, 'p09': 1695808350, 'p10': 1540369888, 'p11': 1374227063, 'p12': 1150816834, 'p13': 246711770095, 'p14': 158760301657, 'p15': 'timeout', 'p16': 11562632991, 'p17': 8472336153, 'p18': 804697148, 'p19': 'timeout', 'p20': 2919583554, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 3593574055}}], 'HacksynthSolverComp32': [{'solve_external_yices': {'p01': 481774539, 'p02': 1089565412, 'p03': 544164374, 'p04': 414399011, 'p05': 403836420, 'p06': 415963970, 'p07': 884169199, 'p08': 3303139581, 'p09': 858877438, 'p10': 1417957841, 'p11': 1456265040, 'p12': 1336523387, 'p13': 13659300586, 'p14': 3574423802, 'p15': 6596961555, 'p16': 1699355765, 'p17': 4557612645, 'p18': 770914426, 'p19': 114832323433, 'p20': 3456761092, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_z3': {'p01': 481600648, 'p02': 56012506158, 'p03': 502378680, 'p04': 418269532, 'p05': 419025577, 'p06': 376867980, 'p07': 1329927098, 'p08': 730411397, 'p09': 984937385, 'p10': 1180124356, 'p11': 1394385899, 'p12': 1335821543, 'p13': 108198061693, 'p14': 4125290910, 'p15': 10523045941, 'p16': 2059874875, 'p17': 16249186530, 'p18': 749964052, 'p19': 36027851152, 'p20': 'timeout', 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_external_bitwuzla': {'p01': 506308435, 'p02': 84978206715, 'p03': 561308548, 'p04': 460345033, 'p05': 420004406, 'p06': 409736251, 'p07': 848658946, 'p08': 1122858720, 'p09': 2026494666, 'p10': 1705689459, 'p11': 1651187796, 'p12': 1564960337, 'p13': 47701451936, 'p14': 5187388621, 'p15': 8202842622, 'p16': 2433589822, 'p17': 5376530487, 'p18': 860287498, 'p19': 11141686723, 'p20': 3510736765, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}, 'solve_external_cvc5': {'p01': 647298665, 'p02': 45271452413, 'p03': 611471193, 'p04': 506956172, 'p05': 502652017, 'p06': 432275537, 'p07': 1017277237, 'p08': 985998629, 'p09': 1526525392, 'p10': 2077137320, 'p11': 2145393570, 'p12': 1764075181, 'p13': 1752288368929, 'p14': 221684327246, 'p15': 'timeout', 'p16': 11858483201, 'p17': 15577385020, 'p18': 806157408, 'p19': 'timeout', 'p20': 3577069758, 'p21': 'timeout', 'p22': 'timeout', 'p23': 'timeout', 'p24': 'timeout'}}]}, 'arguments': 'benchmark=hacksynth_solver_comp.py,hacksynth_solver_comp_32bit.py output=outfile_solver_cmp intermediate_output=True repeats=1', 'environment': {'TIMEOUT': '1800s', 'LOG_LEVEL': 2, 'KEEP_TEMP': True, 'CVC5_PATH': '/home/edelmann/cvc5/cvc5-Linux-static/bin/cvc5'}}


results = {
    'solve_external_yices': [data['results']['HacksynthSolverComp'][0]['solve_external_yices']],
    'solve_z3': [data['results']['HacksynthSolverComp'][0]['solve_z3']],
    'solve_external_bitwuzla': [data['results']['HacksynthSolverComp'][0]['solve_external_bitwuzla']],
    'solve_external_cvc5': [data['results']['HacksynthSolverComp'][0]['solve_external_cvc5']],
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