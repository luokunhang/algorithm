import numpy as np

#a)
def generator(n, L, r):
	intervals = []
	for i in range(n):
		start = np.random.uniform(low = 1, high = L, size = 1)[0]
		l = np.random.uniform(low = 1, high = r, size = 1)[0]
		intervals.append([start, start + l])
	return intervals

#b)
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
	return results

#c)
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
	return sorted(results, key = lambda x: x[0])

def compute_intersect(a, b):
	return not ((a[1] <= b[0]) | (b[1] <= a[0]))

prt = open('hw7-q4.txt', 'w') 

i = generator(4, 5, 3)

print("routine b): " + str(schedule(i)) + "\n", file = prt)
print("routine c): " + str(schedule_2(i)), file = prt)