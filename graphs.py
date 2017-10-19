import numpy as np
import matplotlib.pyplot as pl

def graph(problem, nr):
    e = []
    g = []
    n = []
    t = []
    colours = []
    keys = []
    min_plan = float('inf')
    for k in problem:
        min_plan = min(min_plan, problem[k]['plan'])

    for k in problem:
        if problem[k]['expansions'] < 99999:
            keys.append(k)
            e.append(problem[k]['expansions'])
            g.append(problem[k]['goal_tests'])
            n.append(problem[k]['new_nodes'])
            t.append(problem[k]['time'])
            colours.append('g' if problem[k]['plan'] == min_plan else 'r')
    x = range(len(keys))

    pl.figure(nr, figsize=(10.24, 7.4))

    pl.subplot(221)
    pl.bar(x, e, color=colours, align="center")
    pl.xticks(x, keys)
    pl.title('Expansions')
    pl.grid(True)

    pl.subplot(222)
    pl.bar(x, g, color=colours, align="center")
    pl.xticks(x, keys)
    pl.title('Goals')
    pl.grid(True)

    pl.subplot(223)
    pl.bar(x, n, color=colours, align="center")
    pl.xticks(x, keys)
    pl.title('New nodes')
    pl.grid(True)

    pl.subplot(224)
    pl.bar(x, t, color=colours, align="center")
    pl.xticks(x, keys)
    pl.title('Execution time')
    pl.grid(True)

    pl.subplots_adjust(top=0.92, bottom=0.08, left=0.05, right=0.95, hspace=0.2,
                        wspace=0.15)
    #pl.show()
    pl.savefig('p{}.png'.format(nr))


if __name__ == '__main__':
    p1 = {'bfs': {
        'expansions': 43,
        'goal_tests': 56,
        'new_nodes': 180,
        'time': 0.05834912300633732,
        'plan': 6
    }, 'bfts': {
        'expansions': float('inf'),  # 1458,
        'goal_tests': 1459,
        'new_nodes': 5960,
        'time': 1.2397624810000707,
        'plan': 6
    }, 'dfgs': {
        'expansions': 21,
        'goal_tests': 22,
        'new_nodes': 84,
        'time': 0.01806985899747815,
        'plan': 20
    }, 'dls': {
        'expansions': 101,
        'goal_tests': 271,
        'new_nodes': 414,
        'time': 0.12292709199755336,
        'plan': 50
    }, 'ucs': {
        'expansions': 55,
        'goal_tests': 57,
        'new_nodes': 224,
        'time': 0.051972073000797536,
        'plan': 6
    }, 'rbfs': {
        'expansions': float('inf'),  # 4229,
        'goal_tests': 4230,
        'new_nodes': 17023,
        'time': 3.574356502998853,
        'plan': 6
    }, 'gbfgs': {
        'expansions': 7,
        'goal_tests': 9,
        'new_nodes': 28,
        'time': 0.006714879000355722,
        'plan': 6
    }, 'ash1': {
        'expansions': 35,
        'goal_tests': 57,
        'new_nodes': 224,
        'time': 0.04831534099866985,
        'plan': 6
    }, 'aship': {
        'expansions': 41,
        'goal_tests': 43,
        'new_nodes': 170,
        'time': 0.048865853997995146,
        'plan': 6
    }, 'apglev': {
        'expansions': 11,
        'goal_tests': 13,
        'new_nodes': 50,
        'time': 1.2660968879972643,
        'plan': 6
    }}

    graph(p1, 1)

    p2 = {'bfs': {
        'expansions': 3343,
        'goal_tests': 4609,
        'new_nodes': 30509,
        'time': 15.670493121997424,
        'plan': 9
    }, 'bfts': {
        'expansions': float('inf'),
        'goal_tests': float('inf'),
        'new_nodes': float('inf'),
        'time': float('inf'),
        'plan': float('inf')
    }, 'dfgs': {
        'expansions': 624,
        'goal_tests': 625,
        'new_nodes': 5602,
        'time': 3.9397765979992982,
        'plan': 619
    }, 'dls': {
        'expansions': float('inf'),
        'goal_tests': float('inf'),
        'new_nodes': float('inf'),
        'time': float('inf'),
        'plan': float('inf')
    }, 'ucs': {
        'expansions': 4852,
        'goal_tests': 4854,
        'new_nodes': 44030,
        'time': 13.970111028000247,
        'plan': 9
    }, 'rbfs': {
        'expansions': float('inf'),
        'goal_tests': float('inf'),
        'new_nodes': float('inf'),
        'time': float('inf'),
        'plan': float('inf')
    }, 'gbfgs': {
        'expansions': 990,
        'goal_tests': 992,
        'new_nodes': 8910,
        'time': 2.7889175370000885,
        'plan': 21
    }, 'ash1': {
        'expansions': 4852,
        'goal_tests': 4854,
        'new_nodes': 44030,
        'time': 13.972369421997428,
        'plan': 9
    }, 'aship': {
        'expansions': 1450,
        'goal_tests': 1452,
        'new_nodes': 13303,
        'time': 5.247129077000864,
        'plan': 9
    }, 'apglev': {
        'expansions': 86,
        'goal_tests': 88,
        'new_nodes': 841,
        'time': 230.21047930900022,
        'plan': 9
    }}

    graph(p2, 2)

    p3 = {'bfs': {
        'expansions': 14663,
        'goal_tests': 18098,
        'new_nodes': 129631,
        'time': 115.32113834100164,
        'plan': 12
    }, 'bfts': {
        'expansions': float('inf'),
        'goal_tests': float('inf'),
        'new_nodes': float('inf'),
        'time': float('inf'),
        'plan': float('inf')
    }, 'dfgs': {
        'expansions': 408,
        'goal_tests': 409,
        'new_nodes': 3364,
        'time': 2.0269329539987666,
        'plan': 392
    }, 'dls': {
        'expansions': float('inf'),
        'goal_tests': float('inf'),
        'new_nodes': float('inf'),
        'time': float('inf'),
        'plan': float('inf')
    }, 'ucs': {
        'expansions': 18235,
        'goal_tests': 18237,
        'new_nodes': 159716,
        'time': 60.60187196100014,
        'plan': 12
    }, 'rbfs': {
        'expansions': float('inf'),
        'goal_tests': float('inf'),
        'new_nodes': float('inf'),
        'time': float('inf'),
        'plan': float('inf')
    }, 'gbfgs': {
        'expansions': 5614,
        'goal_tests': 5616,
        'new_nodes': 49429,
        'time': 18.411833062997175,
        'plan': 27
    }, 'ash1': {
        'expansions': 18235,
        'goal_tests': 18237,
        'new_nodes': 159716,
        'time': 60.111281982000946,
        'plan': 12
    }, 'aship': {
        'expansions': 5040,
        'goal_tests': 5042,
        'new_nodes': 44944,
        'time': 19.663440437001555,
        'plan': 12
    }, 'apglev': {
        'expansions': 315,
        'goal_tests': 317,
        'new_nodes': 2902,
        'time': 1415.2401898969983,
        'plan': 12
    }}

    graph(p3, 3)
# timeout 100s for all the following
# python run_search.py -p 3 -s 1 > p3.results.1 ; python run_search.py -p 3 -s 2 > p3.results.2 ; python run_search.py -p 3 -s 3 > p3.results.3 ; python run_search.py -p 3 -s 9 > p3.results.9 ; python run_search.py -p 3 -s 8 > p3.results.8 ; python run_search.py -p 3 -s 7 > p3.results.7 ; python run_search.py -p 3 -s 6 > p3.results.6 ; python run_search.py -p 3 -s 5 > p3.results.5 ; python run_search.py -p 3 -s 4 > p3.results.4 ;