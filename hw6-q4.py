import numpy as np

def find_k(a, k):
	if (a.size >= k):
		pivot = np.random.choice(a)
		s1 = np.array([])
		s2 = np.array([])
		s3 = np.array([])
		for e in a:
			if (e < pivot):
				s1 = np.append(s1, e)
			elif (e > pivot):
				s2 = np.append(s2, e)
			else:
				s3 = np.append(s3, e)
		if (s2.size >= k):
			return find_k(s2, k)
		elif ((s2.size + s3.size) >= k):
			return pivot
		else:
			return find_k(s1, k - s2.size - s3.size)

n = 10
arr = np.random.randint(n, size = n)
print(find_k(arr, 4))