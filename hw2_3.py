import matplotlib.pyplot as plt

x = [1, 3, 7]
y = [2, 6, 14]

lr = 0.01
w = 0
b = 0
y_pred_l = []

for i in range(len(x)):
  y_pred = w * x[i] + b
  w += 2 * lr * x[i] * (y[i] - y_pred)
  b += 2 * lr * (y[i] - y_pred)

print(f'w = {w}, b = {b}')

plt.plot(x, [w * xi + b for xi in x], color = 'green')
plt.scatter(x,y)
plt.xlabel = 'x'
plt.ylabel = 'y'
plt.show()
