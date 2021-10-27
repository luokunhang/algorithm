import numpy as np
import pprint

def create(n, p):
	to_return = dict()
	for i in range(n):
		to_return[i] = set()

	for i in range(n):
		for j in range(i + 1, n):
			prob = np.random.uniform()
			if (prob < p):
				to_return[i].add(j)
				to_return[j].add(i)
	return to_return

n = 10
p = 0.2
graph1 = create(n, p)
graph2 = create(n, p)

open('graph1.txt', 'w').write(pprint.pformat(graph1))
open('graph2.txt', 'w').write(pprint.pformat(graph2))