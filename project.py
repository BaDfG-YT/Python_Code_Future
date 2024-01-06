import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Часть 1

df = pd.read_csv('Housing.csv')

print('Количество спален в самом дешёвом доме')
print(df[df['price']== df['price'].min()]['bedrooms'].min())

print('\nКоличество домов, в которых количество спален не больше количества ванных')
print(len(df[df['bedrooms'] <= df['bathrooms']]))

print('\nСтоимость самого дешёвого дома с гостевой комнатой')
print(df[df['guestroom'] == 'yes']['price'].min())

print('\nКоличество домов с системой кондиционирования воздуха стоимостью меньше 2000000 или больше 5000000')
print(len(df[(df['price'] <= 2000000) | (df['price'] >= 5000000)]['airconditioning']))


# Часть 2

a = 0.1

x = np.array(df[(df['parking']) == 0]['price'])
y = np.array(df[(df['parking']) == 0]['area'])

plt.scatter(x,y,marker='o', alpha=a, color='blue', label='0 парковочных мест')

x = np.array(df[(df['parking']) == 1]['price'])
y = np.array(df[(df['parking']) == 1]['area'])

plt.scatter(x,y,marker='o', alpha=a, color='purple', label='1 парковочное место')

x = np.array(df[(df['parking']) == 2]['price'])
y = np.array(df[(df['parking']) == 2]['area'])

plt.scatter(x,y,marker='o', alpha=a, color='red', label='2 парковочных места')

x = np.array(df[(df['parking']) == 3]['price'])
y = np.array(df[(df['parking']) == 3]['area'])

plt.scatter(x,y,marker='o', alpha=a, color='orange', label='3 парковочных места')

plt.legend()
plt.xlabel('Цена')
plt.ylabel('Площадь')
plt.show()


# Часть 3
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(18, 10))

titles = ['Гостевая комната', 'Подвал', 'Обогрев горячей водой', 'Предбанник']
elements = ['guestroom', 'basement', 'hotwaterheating', 'prefarea']


for i in range(2):
    for j in range(2):
        x = np.array(df[(df[elements[2*i + j]]) == 'yes']['price'])
        y = np.array(df[(df[elements[2*i + j]]) == 'yes']['area'])
        axes[i, j].scatter(x, y, label='Наличие', color='blue', alpha=a)
        
        x = np.array(df[(df[elements[2*i + j]]) == 'no']['price'])
        y = np.array(df[(df[elements[2*i + j]]) == 'no']['area'])
        axes[i, j].scatter(x, y, label='Отсутствие', color = 'red', alpha=a)
        
        axes[i, j].set_xlabel('Цена')
        axes[i, j].set_ylabel('Площадь')
        
        axes[i, j].set_title(titles[2*i + j])
        axes[i, j].grid()
        axes[i, j].legend()

plt.tight_layout()
plt.title('Наличие/отсутствие разных параметров у домов')
plt.show()

# Часть 4

airconditioningYes = np.array(df[(df['airconditioning'] == 'yes')]['price'])
plt.hist(airconditioningYes, color='g', alpha = 0.5, bins=30, label='Наличие', edgecolor='black')

airconditioningNo = np.array(df[(df['airconditioning'] == 'no')]['price'])
plt.hist(airconditioningNo, color='r', alpha = 0.5, bins=30, label='Отсутствие', edgecolor='black')

plt.xlabel('Цена')
plt.ylabel('Кол-во домов')
plt.legend()
plt.title('Дома с наличием/отсутствием кондиционирования')
plt.grid()
plt.show()
