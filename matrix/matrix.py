import numpy as np

X = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

# print(dir(X))

# 전치행렬
print(X.transpose())

X = np.array([[1,0,1],
              [0,1,0],
              [1,1,0]])

# 역행렬 : 행과 열의 수가 같을 때
print(np.linalg.inv(X))

X = np.array([[1,0,1],
              [0,1,0]])

# 무어-펜로즈 역행렬(유사 역행렬) : 행과 열의 수가 다를 때
# 행의 개수가 열의 개수보다 많을 때  A+ =(AT*A)^-1*AT
# 열의 개수가 행의 개수보다 많을 때  A+ = AT(A*AT)^-1
print(np.linalg.pinv(X))