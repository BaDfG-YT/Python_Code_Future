import numpy as np

# # Задание 1
# array = np.random.randint(1,10,size = 100)
# print(f'{int(np.mean(array > 7)*100)}%')

# # Задание 2

# k = []
# for i in range(1000):
#     array = np.random.randint(1,10,size = 100)
#     p = int(np.mean(array > 7)*100)
#     k.append(p)
    
# print(k.count(20)/len(k))


# Задание 3 и 4
matrix = np.tile(np.arange(1, 11), (10, 1))
print(matrix)
print('\n')
print(np.sum(matrix, axis=0))
