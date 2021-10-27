import numpy as np
import matplotlib.pyplot as plt
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

def compute(n, p, ind):
	graph = create(n, p)

	group = 1
	unv = set()
	for i in range(n):
		unv.add(i)
	temp = set()
	store = dict()
	while (unv):
		curr = unv.pop()
		temp.add(curr)
		curr_group = set()
		while (temp):
			check = temp.pop()
			curr_group.add(check)
			for v in graph[check]:
				if v in unv:
					temp.add(v)
					unv.remove(v)
		store[group] = curr_group.copy()
		group = group + 1
	if ind == 1:
		return [p, len(store.keys()), len(max(store.values(), key=len))]
	else:
		return store

pt = []
for i in np.linspace(0, 0.006, 50):
	print(i)
	pt.append(compute(1000, i, 1))

pt = np.array(pt)
plt.figure(0)
plt.plot(pt[:, 0], pt[:, 1])
plt.xlabel("p")
plt.ylabel("n")
plt.savefig('Number.png')

plt.figure(1)
plt.plot(pt[:, 0], pt[:, 2])
plt.xlabel("p")
plt.ylabel("size")
plt.savefig('Size.png')

open('label.txt', 'w').write(pprint.pformat(compute(10, 0.2, 0)))