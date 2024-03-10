from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as LinearRegression_sklearn

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # один признак
y = 4 + 3 * X + np.random.randn(100, 1)  # целевая переменная с небольшим шумом

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression_sklearn()
model.fit(X_train, y_train)
preds = model.predict(X_test)

plt.scatter(X_train, y_train, color = 'green', label = 'train')
plt.scatter(X_test, y_test, color = 'yellow', label = 'test', alpha = 0.8)
plt.plot(X_test, preds, label = 'LR')

plt.title('Линейная регрессия. Train&Test')
plt.xlabel('Признак')
plt.ylabel('Целевая переменная')
plt.grid()
plt.legend()

plt.show()
