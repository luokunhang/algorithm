import numpy as np
import matplotlib.pyplot as plt

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

def evaluate(ms, ws, ans):
	m_eval = np.array([0 for i in range(len(ans))])
	w_eval = np.array([0 for i in range(len(ans))])

	for i in range(len(ans)):
		m_eval[i] = np.where(ms[ans[i], :] == i)[0]
		w_eval[i] = np.where(ws[i, :] == ans[i])[0]
	Mgoodness = np.average(m_eval) + 1
	Wgoodness = np.average(w_eval) + 1
	return [Mgoodness, Wgoodness]

goodnesses = []

for i in range(2, 1500, 150):
	ms = create(i)
	ws = create(i)
	ans = find_match(ms, ws)
	evals = evaluate(ms, ws, ans)
	goodnesses.append([i, evals[0], evals[1]])

goodnesses = np.array(goodnesses)
plt.plot(goodnesses[:, 0], goodnesses[:, 1:3])
plt.xlabel("n")
plt.ylabel("Goodness score")
plt.legend(["M", "W"])
plt.savefig('fairness.png')