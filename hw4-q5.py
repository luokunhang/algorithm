import numpy as np
import matplotlib.pyplot as plt

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

trials = 20
n = 1000
p = np.linspace(0.002, 0.02, trials)

c = range(1, n + 1)

def calculate(n, p, graph):
	graph = create(n, p)
	color = dict()
	for v in graph.keys():
		color[v] = -1
	for v in color.keys():
		counter = 0
		while (color[v] == -1):
			temp = c[counter]
			to_color = True
			for n in graph[v]:
				if temp == color[n]:
					to_color = False
			if to_color:
				color[v] = temp
			counter = counter + 1

	return max(color.values())

def calculate2(n, p, graph):
	graph = create(n, p)
	color = dict()
	for v in graph.keys():
		color[v] = -1
	for v in sorted(graph.keys(), key=lambda k: len(graph[k]), reverse=True):
		counter = 0
		while (color[v] == -1):
			temp = c[counter]
			to_color = True
			for n in graph[v]:
				if temp == color[n]:
					to_color = False
			if to_color:
				color[v] = temp
			counter = counter + 1

	return max(color.values())

to_plot = []
for i in range(trials):
	print(i)
	same_p = []
	same_p2 = []
	for j in range(5):
		graph = create(n, p[i])
		same_p.append(calculate(n, p[i], graph))
		same_p2.append(calculate2(n, p[i], graph))
	to_plot.append([np.mean(same_p), np.mean(same_p2)])

plt.figure(0)
plt.plot(p, to_plot)
plt.xlabel("p")
plt.ylabel("# of colors")
plt.legend(["q5", "q6"])
plt.savefig('colors.png')