import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit

def find_k(a, k, count):
	if (a.size >= k):
		pivot = np.random.choice(a)
		s1 = np.array([])
		s2 = np.array([])
		s3 = np.array([])
		for e in a:
			count = count + 1
			if (e < pivot):
				s1 = np.append(s1, e)
			elif (e > pivot):
				s2 = np.append(s2, e)
			else:
				s3 = np.append(s3, e)
		if (s2.size >= k):
			return find_k(s2, k, count)
		elif ((s2.size + s3.size) >= k):
			return count
		else:
			return find_k(s1, k - s2.size - s3.size, count)

n = range(1, 10001, 500)
ntrials = 10
to_plot = np.array([])

for i in n:
	to_mean = np.array([])
	for j in range(0, ntrials):
		to_mean = np.append(to_mean, find_k(np.random.randint(i, size = i), i/2, 0))
	to_plot = np.append(to_plot, np.mean(to_mean))

b, m = polyfit(n, to_plot, 1)

plt.figure(0)
plt.plot(n, to_plot, '.')
plt.plot(n, b + m * n, '-')
plt.xlabel("n")
plt.ylabel("cn")
plt.annotate("c = " + str(m), xy = (5000, 1000))
plt.savefig('c.png')