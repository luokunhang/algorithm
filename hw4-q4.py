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

n = 1000
p = np.linspace(0.002, 0.02, 5)

for i in range(5):
	result = create(n, p[i])
	to_hist = []
	for s in result.values():
		to_hist.append(len(s))
	to_hist = np.array(to_hist)
	
	plt.figure(i)
	plt.hist(to_hist, bins = "auto")
	plt.title("Histogram p=" + str(p[i]))
	plt.savefig("Hist" + str(i) + ".png")