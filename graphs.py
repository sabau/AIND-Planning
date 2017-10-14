import numpy as np
import matplotlib.pyplot as pl

p1 = {}
p1['bfs'] = {
    'expansions': 43,
    'goal_tests': 56,
    'new_nodes': 180,
    'time': 0.05834912300633732,
    'plan': 6
}

# Excluded as it will result oversized
p1['bfts'] = {
    'expansions': 1458,
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

# Excluded as it will result oversized
p1['rbfs'] = {
    'expansions': 4229,
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
e = []
g = []
n = []
t = []
keys = []
for k in p1:
    if p1[k]['expansions'] < 1000 and p1[k]['plan'] == 6:
        keys.append(k)
        e.append(p1[k]['expansions'])
        g.append(p1[k]['goal_tests'])
        n.append(p1[k]['new_nodes'])
        t.append(p1[k]['time'])
x = range(len(keys))

pl.figure(1)

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
# pl.show()
pl.savefig('p1.png')


# python run_search.py -p 3 -s 1 > p3.results.1 ; python run_search.py -p 3 -s 2 > p3.results.2 ; python run_search.py -p 3 -s 3 > p3.results.3 ; python run_search.py -p 3 -s 9 > p3.results.9 ; python run_search.py -p 3 -s 8 > p3.results.8 ; python run_search.py -p 3 -s 7 > p3.results.7 ; python run_search.py -p 3 -s 6 > p3.results.6 ; python run_search.py -p 3 -s 5 > p3.results.5 ; python run_search.py -p 3 -s 4 > p3.results.4 ;