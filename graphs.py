import numpy as np
import matplotlib.pyplot as pl

def graph(problem, nr):
    e = []
    g = []
    n = []
    t = []
    keys = []
    for k in problem:
        if problem[k]['expansions'] < 99999 and problem[k]['plan'] < 30:
            keys.append(k)
            e.append(problem[k]['expansions'])
            g.append(problem[k]['goal_tests'])
            n.append(problem[k]['new_nodes'])
            t.append(problem[k]['time'])
    x = range(len(keys))

    pl.figure(nr)

    pl.subplot(221)
    pl.bar(x, e, align="center")
    pl.xticks(x, keys)
    pl.title('Expansions')
    pl.grid(True)

    pl.subplot(222)
    pl.bar(x, g, align="center")
    pl.xticks(x, keys)
    pl.title('Goals')
    pl.grid(True)

    pl.subplot(223)
    pl.bar(x, n, align="center")
    pl.xticks(x, keys)
    pl.title('New nodes')
    pl.grid(True)

    pl.subplot(224)
    pl.bar(x, t, align="center")
    pl.xticks(x, keys)
    pl.title('Execution time')
    pl.grid(True)

    pl.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                        wspace=0.35)
    #pl.show()
    pl.savefig('p{}.png'.format(nr))


if __name__ == '__main__':
    p1 = {}
    p1['bfs'] = {
        'expansions': 43,
        'goal_tests': 56,
        'new_nodes': 180,
        'time': 0.05834912300633732,
        'plan': 6
    }

    p1['bfts'] = {
        'expansions': float('inf'), #1458,
        'goal_tests': 1459,
        'new_nodes': 5960,
        'time': 1.2687281070029712,
        'plan': 6
    }

    p1['dfgs'] = {
        'expansions': 21,
        'goal_tests': 22,
        'new_nodes': 84,
        'time': 0.01806985899747815,
        'plan': 20
    }

    p1['dls'] = {
        'expansions': 101,
        'goal_tests': 271,
        'new_nodes': 414,
        'time': 0.11867141699622152,
        'plan': 50
    }

    p1['ucs'] = {
        'expansions': 55,
        'goal_tests': 57,
        'new_nodes': 224,
        'time': 0.04757036600494757,
        'plan': 6
    }

    p1['rbfs'] = {
        'expansions': float('inf'), #4229,
        'goal_tests': 4230,
        'new_nodes': 17023,
        'time': 3.6596700299996883,
        'plan': 6
    }

    p1['gbfgs'] = {
        'expansions': 7,
        'goal_tests': 9,
        'new_nodes': 28,
        'time': 0.006540886999573559,
        'plan': 6
    }

    p1['ash1'] = {
        'expansions': 35,
        'goal_tests': 57,
        'new_nodes': 224,
        'time': 0.050139736995333806,
        'plan': 6
    }

    p1['aship'] = {
        'expansions': 41,
        'goal_tests': 43,
        'new_nodes': 170,
        'time': 0.050772892995155416,
        'plan': 6
    }
    graph(p1, 1)
    p2 = {}
    p2['bfs'] = {
        'expansions': 3343,
        'goal_tests': 4609,
        'new_nodes': 30509,
        'time': 16.267350781999994,
        'plan': 9
    }

    p2['bfts'] = {
        'expansions': float('inf'),
        'goal_tests': float('inf'),
        'new_nodes': float('inf'),
        'time': float('inf'),
        'plan': float('inf')
    }

    p2['dfgs'] = {
        'expansions': 624,
        'goal_tests': 625,
        'new_nodes': 5602,
        'time': 4.06265643100005,
        'plan': 619
    }

    p2['dls'] = {
        'expansions': float('inf'),
        'goal_tests': float('inf'),
        'new_nodes': float('inf'),
        'time': float('inf'),
        'plan': float('inf')
    }

    p2['ucs'] = {
        'expansions': 4852,
        'goal_tests': 4854,
        'new_nodes': 44030,
        'time': 14.759871609000129,
        'plan': 9
    }

    p2['rbfs'] = {
        'expansions': float('inf'),
        'goal_tests': float('inf'),
        'new_nodes': float('inf'),
        'time': float('inf'),
        'plan': float('inf')
    }

    p2['gbfgs'] = {
        'expansions': 990,
        'goal_tests': 992,
        'new_nodes': 8910,
        'time': 2.9877461870000843,
        'plan': 21
    }

    p2['ash1'] = {
        'expansions': 4852,
        'goal_tests': 4854,
        'new_nodes': 44030,
        'time': 15.206296423999902,
        'plan': 9
    }

    p2['aship'] = {
        'expansions': 1450,
        'goal_tests': 1452,
        'new_nodes': 13303,
        'time': 5.50189205200013,
        'plan': 9
    }
    graph(p2, 2)

    p3 = {}
    p3['bfs'] = {
        'expansions': 13063,
        'goal_tests': 16544,
        'new_nodes': 102013,
        'time': 92.85633008200057,
        'plan': 12
    }

    p3['bfts'] = {
        'expansions': float('inf'),
        'goal_tests': float('inf'),
        'new_nodes': float('inf'),
        'time': float('inf'),
        'plan': float('inf')
    }

    p3['dfgs'] = {
        'expansions': 1292,
        'goal_tests': 1293,
        'new_nodes': 5744,
        'time': 3.9526151539994316,
        'plan': 875
    }

    p3['dls'] = {
        'expansions': float('inf'),
        'goal_tests': float('inf'),
        'new_nodes': float('inf'),
        'time': float('inf'),
        'plan': float('inf')
    }

    p3['ucs'] = {
        'expansions': 17015,
        'goal_tests': 17017,
        'new_nodes': 132157,
        'time': 56.398906055000225,
        'plan': 12
    }

    p3['rbfs'] = {
        'expansions': float('inf'),
        'goal_tests': float('inf'),
        'new_nodes': float('inf'),
        'time': float('inf'),
        'plan': float('inf')
    }

    p3['gbfgs'] = {
        'expansions': 5735,
        'goal_tests': 5737,
        'new_nodes': 42311,
        'time': 17.981334995999532,
        'plan': 27
    }

    p3['ash1'] = {
        'expansions': 17015,
        'goal_tests': 17017,
        'new_nodes': 132157,
        'time': 56.13875912399999,
        'plan': 12
    }

    p3['aship'] = {
        'expansions': 6532,
        'goal_tests': 6534,
        'new_nodes': 51888,
        'time': 25.39526862999992,
        'plan': 13
    }
    graph(p3, 3)
# timeout 100s for all the following
# python run_search.py -p 3 -s 1 > p3.results.1 ; python run_search.py -p 3 -s 2 > p3.results.2 ; python run_search.py -p 3 -s 3 > p3.results.3 ; python run_search.py -p 3 -s 9 > p3.results.9 ; python run_search.py -p 3 -s 8 > p3.results.8 ; python run_search.py -p 3 -s 7 > p3.results.7 ; python run_search.py -p 3 -s 6 > p3.results.6 ; python run_search.py -p 3 -s 5 > p3.results.5 ; python run_search.py -p 3 -s 4 > p3.results.4 ;