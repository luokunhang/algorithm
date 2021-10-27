import numpy as np
import copy as cp

def create(n):
	A = np.array([[i for i in range(n)] for j in range(n)])
	for i in range(n):
		A[i, :] = np.random.permutation(A[i, :])
	return(A)

def find_match(ms, ws):
	match = np.array([-1 for i in range(np.size(ms, 0))])
	m_free = []
	for i in range(np.size(ms, 0)):
		m_free.append(i)

	while (m_free):
		curr = m_free.pop(0)
		curr_pref = ms[curr, :]
		is_matched = False
		i = 0
		while ((not is_matched) & (i < curr_pref.size)):
			w_curr = curr_pref[i]
			if match[w_curr] == -1:
				match[w_curr] = curr
				is_matched = not is_matched
			else:
				w_pref = ws[w_curr, :]
				if np.where(w_pref == curr)[0] < np.where(w_pref == match[curr_pref[i]])[0]:
					m_free.append(match[w_curr])
					match[curr_pref[i]] = curr
					is_matched = not is_matched
			i = i + 1
		if (not is_matched):
			m_free.append(curr)
	return match

while True:
	ms = create(3)
	ws = create(3)
	ws1 = cp.deepcopy(ws)
	a = ws1[0, 1]
	ws1[0, 1] = ws1[0, 2]
	ws1[0, 2] = a
	match = find_match(ms, ws)
	match1 = find_match(ms, ws1)
	if np.where(ws[0, :] == match[0]) > np.where(ws[0, :] == match1[0]):
		print(ms)
		print(ws)
		print(match)
		print(ws1)
		print(match1)
		break