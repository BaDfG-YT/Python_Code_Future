import numpy as np
import matplotlib.pyplot as plt

# Задание 1

# def graph(x):
#     return np.sin(x) ** 2 / (np.cos(x) + 2) + x ** 3 - 5 * x

# x = np.linspace(-10, 10, 1000)

# y = graph(x)

# plt.figure(figsize=(10, 6))
# plt.plot(x, y, linestyle='--', color='green', alpha=0.5, label='Вот такая моя функция')
# plt.title('График сложной алгебраической функции')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.grid()
# plt.legend()
# plt.show()



# # Задание 2

# X = np.random.normal(0, 1, 3000)
# Y = np.random.normal(3, 4, 3000)

# plt.figure(figsize=(10, 6))
# plt.scatter(X, Y, s=10, color='yellow', marker='*', alpha=0.2, label='Звезда')
# plt.gca().set_facecolor('darkblue')
# plt.title('Небо')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.grid()
# plt.legend()
# plt.show()


# # Задание 3

# data = np.random.normal(16, 2, 1000)

# plt.figure(figsize=(10, 6))
# plt.hist(data, color='red', alpha=0.5)

# plt.title('Гистограмма')
# plt.xlabel('Время')
# plt.ylabel('Кол-во участников')
# plt.show()

# # На основе этой гистограммы можно определить кол-во участников, их время забега, среднее время, экстремальные значения и стандарт. отклонение
