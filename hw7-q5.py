import numpy as np
import matplotlib.pyplot as plt

def generator(n, L, r):
	intervals = []
	for i in range(n):
		start = np.random.uniform(low = 1, high = L, size = 1)[0]
		l = np.random.uniform(low = 1, high = r, size = 1)[0]
		intervals.append([start, start + l])
	return intervals

def schedule(i):
	results = []
	i = sorted(i, key = lambda x: x[0])
	pointer = 0
	feasible = 0
	while (pointer < len(i)):
		if (i[pointer][0] >= feasible):
			results.append(i[pointer])
			feasible = i[pointer][1]
		pointer = pointer + 1
	return compute_sum(results)

def schedule_2(i):
	results = []
	i = sorted(i, key = lambda x: x[0] - x[1])
	pointer = 0
	while (pointer < len(i)):
		add = True
		for r in results:
			if compute_intersect(i[pointer], r):
				add = False
		if (add | (not results)):
			results.append(i[pointer])
		pointer = pointer + 1
	return compute_sum(results)

def compute_intersect(a, b):
	return not ((a[1] <= b[0]) | (b[1] <= a[0]))

def compute_sum(r):
	sum = 0
	for pair in r:
		sum = sum + pair[1] - pair[0]
	return sum

def dy_schedule(i):
	n = len(i)
	opt = [None] * (n + 1)
	opt[0] = 0
	i = sorted(i, key = lambda x: x[1])
	i.insert(0, [0, 0])
	for j in range(1, n + 1):
		opt[j] = max(opt[j - 1], i[j][1] - i[j][0] + opt[p(i, j)])
	return opt[n]

def p(i, j):
	k = j - 1
	while (k > 0):
		if (i[k][1] <= i[j][0]):
			return k
		k = k - 1
	return 0

s = []
l = []
d = []
for j in range(20):
	i = generator(10000, 1000000, 2000)
	s.append(schedule(i))
	l.append(schedule_2(i))
	d.append(dy_schedule(i))

plt.figure(0)
plt.boxplot([s, l, d])
plt.xaxis(["Start", "Length", "DP"])
plt.savefig("boxplot.png")
