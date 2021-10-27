import numpy as np

ms = np.array([[2, 1, 3, 0], [0, 1, 3, 2], [0, 1, 2, 3], [0, 1, 2, 3]])
ws = np.array([[0, 2, 1, 3], [2, 0, 3, 1], [3, 2, 1, 0], [2, 3, 1, 0]])
match = np.array([-1 for i in range(np.size(ms, 0))])

m_free = []
for i in range(np.size(ms, 0)):
	m_free.append(i)

propose = []

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
			propose.append("m" + str(curr + 1) + " proposed to w" + str(w_curr + 1) + " successfully.")
		else:
			w_pref = ws[w_curr, :]
			if np.where(w_pref == curr)[0] < np.where(w_pref == match[curr_pref[i]])[0]:
				propose.append("m" + str(curr + 1) + " proposed to w" + str(w_curr + 1) + " successfully, " 
					+ "m" + str(match[w_curr] + 1) + " dumped.")
				m_free.append(match[w_curr])
				match[curr_pref[i]] = curr
				is_matched = not is_matched
			propose.append("m" + str(curr + 1) + " proposed to w" + str(w_curr + 1) + " but was rejected.")
		i = i + 1
	if (not is_matched):
		m_free.append(curr)

print("The order of m for w in ascending order: ", match + 1)
for i in range(len(propose)):
	print(propose[i])