import numpy as np
import matplotlib.pyplot as plt

stats = []

def calculate(i):
	counter = 0
	checker = 0
	coupons = dict()
	while (i != checker):
		temp = np.random.randint(0, i)
		value = np.random.randint(0, i)
		counter = counter + 1
		if (temp not in coupons):
			checker = checker + 1
			coupons[temp] = value
		elif (coupons[temp] > value):
			coupons[temp] = value
	return sum(coupons.values())

for i in range(100, 4001, 100):
	store = []
	for j in range(10):
		store.append(calculate(i))
	stats.append([i, sum(store) / len(store), sum(store) / len(store) * 1.0 / i])

stats = np.array(stats)
plt.figure(0)
plt.plot(stats[:, 0], stats[:, 1])
plt.xlabel("n")
plt.ylabel("V")
plt.savefig('coupons6V.png')

plt.figure(1)
plt.plot(stats[:, 0], stats[:, 2])
plt.xlabel("n")
plt.ylabel("V/n")
plt.savefig('coupons6Vn.png')