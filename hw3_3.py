import numpy as np
A = np.array([[1,54],
             [1, 6],
             [2, 7]])
print(A.transpose())

A = np.array([[1, 7, 8],
             [4, 2, 9],
             [5, 6, 3]])
print(A.transpose())


# Будет ошибка т.к. не совпадают размеры
# A = np.array([[1,2],
#               [4,5],
#               [7,8]])

# B = np.array([[1,1,0],
#               [0,1,1],
#               [1,0,1]])

# print(A @ B)

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

B = np.array([[1,1,0],
              [0,1,1],
              [1,0,1]])

print(A @ B)



x = np.array([[1, 145],
              [2, 163],
              [3, 240],
              [3, 350],
              [4, 421],
              [4, 397],
              [5, 620]])

xt = x.transpose()

y = np.array([80, 170, 100, 220, 200, 270, 500])

A = xt @ y
B = xt @ x


print(A/B)
