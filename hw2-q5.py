import numpy as np
import matplotlib.pyplot as plt

stats = []

def calculate(i):
	counter = 0
	checker = 0
	coupons = set()
	while (i != checker):
		temp = np.random.randint(0, i)
		counter = counter + 1
		if (temp not in coupons):
			checker = checker + 1
			coupons.add(temp)
	return counter

for i in range(100, 4001, 100):
	store = []
	for j in range(10):
		store.append(calculate(i))
	stats.append([i, sum(store) / len(store), sum(store) / len(store) * 1.0 / i])

stats = np.array(stats)
plt.figure(0)
plt.plot(stats[:, 0], stats[:, 1])
plt.xlabel("n")
plt.ylabel("C")
plt.savefig('coupons5C.png')

plt.figure(1)
plt.plot(stats[:, 0], stats[:, 2])
plt.xlabel("n")
plt.ylabel("C/n")
plt.savefig('coupons5Cn.png')