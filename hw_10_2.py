"""
Завдання полягає в обчисленні значення інтеграла функції методом Монте-Карло.
"""
import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    """Default func"""
    return x ** 2

def get_locations(coordinates, ):
    """Функція повертає списки з точками які знаходяться під фкнцією та вище неї"""
    inside_x , inside_y, outside_x, outside_y = [], [], [], []
    for x, y in coordinates:
        calc_y = f(x)
        # print(f"Random x{x:2f} y{y:2f} f(x) = {calc_y:2f}, {calc_y > y}")
        if calc_y <= y:
            outside_x.append(x)
            outside_y.append(y)
        else:
            inside_x.append(x)
            inside_y.append(y)
    return inside_x, inside_y, outside_x, outside_y


count, test_total = 100000, 10
length_a = 2
length_b = 4

# Генеруємо випадкові значення x, y для методу Монте-Карло
# Обчислення інтеграла
# Площа за методом Монте-Карло
total = 0 
for _ in range(test_total):
    randoms = [(random.uniform(0.0, 2.0), random.uniform(0.0, 4.0)) for _ in range(count)]
    inside_x, inside_y, outside_x, outside_y = get_locations(randoms)
    M = len(inside_x)
    monte = (M / count) * (length_a * length_b)
    total += monte
    print(f"Загальна кількість точок під інтегралом {M}, площа за методом Монте-Карло: {monte:2f}")
mid = total/test_total
print(f"Середнє значення площі за методом Монте-Карло за {test_total} експеремнів: {mid:2f}")

# Створення графіка
a = 0  # Нижня межа
b = 2  # Верхня межа
# Створення діапазону значень для x
x = np.linspace(0, 2)
y = f(x)
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)
# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка

# print(f"X{inside_x} {len(inside_x)}, Y{inside_y} {len(inside_y)}")
# Додаємо точки на графік
ax.scatter(inside_x, inside_y, color='green', zorder=5)
ax.scatter( outside_x, outside_y, color='blue', zorder=5)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')


# Площа програмним методом
result, error = spi.quad(f, a, b)
ax.set_title(f"Загальна кількість точок: {count}, під інтегралом {M},  інтеграл: {result:2f}, площа за методом Монте-Карло: {mid:2f}")
plt.grid()
plt.show()
