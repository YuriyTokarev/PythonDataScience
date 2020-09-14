import numpy as np

print("Задание 1:")
a = np.array([[1, 6],[2, 8],[3,11],[3,10],[1,7]], dtype=int)
mean_a = a.mean(axis=0)
print(mean_a)

print("Задание 2:")
a_centered = a - mean_a
print(a_centered)

print("Задание 3:")
a_centered_sp = a_centered[:,0] @ a_centered[:,1]
a_centered_sp = a_centered_sp / (a.shape[0] - 1)
print(a_centered_sp)

print("Задание 4:")
cov = np.cov(m = a.transpose())
print(cov[0][1])