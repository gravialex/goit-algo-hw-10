import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та меж інтегрування: f(x) = x + sin(x) на [0, 2]
def f(x):
    return x + np.sin(x)


a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло
num_samples = 100_000

# Знаходимо максимальне значення функції на відрізку [0, 2]
ymin = 0
x_check = np.linspace(a, b, 1000)
ymax = np.max(f(x_check))

# Генерація випадкових координат точок (x, y) у прямокутнику
np.random.seed(42)  # Для відтворюваності результатів
x_rand = np.random.uniform(a, b, num_samples)
y_rand = np.random.uniform(ymin, ymax, num_samples)

# Визначаємо, які точки потрапили під криву
under_curve = y_rand <= f(x_rand)
points_under_curve = np.sum(under_curve)

# Площа прямокутника та інтеграл
rectangle_area = (b - a) * (ymax - ymin)
monte_carlo_integral = rectangle_area * (points_under_curve / num_samples)

# Аналітична перевірка
analytical_result, error = spi.quad(f, a, b)

# Абсолютна похибка
absolute_error = abs(monte_carlo_integral - analytical_result)

# Вивід результатів
print(f"---------- Функція: f(x) = x + sin(x) на інтервалі [{a}, {b}]")
print(f"--- Результат методом Монте-Карло ({num_samples} точок): {monte_carlo_integral:.6f}")
print(f"--- Аналітичний результат (точний): {analytical_result:.6f}")
print(f"--- Абсолютна похибка між методами: {absolute_error:.6f}\n")

# --- ВИСНОВКИ ---
print("--- ВИСНОВКИ ---")
print(
    " Результат, отриманий за методом Монте-Карло, дуже близький до точного аналітичного значення."
)
print(
    f" Абсолютна похибка становить менше ніж {absolute_error:.4f}, що демонструє високу достовірність апроксимації при {num_samples} точках."
)

# Побудова графіка ---
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x, y, "r", linewidth=2, label="f(x) = x + sin(x)")

# Заповнення області під кривою
ix = np.linspace(a, b, 200)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3, label="Область інтегрування")

# Відображення випадкових точок Монте-Карло
subset = 3000
ax.scatter(
    x_rand[:subset][under_curve[:subset]],
    y_rand[:subset][under_curve[:subset]],
    color="blue",
    s=1,
    alpha=0.5,
    label="Точки під кривою",
)
ax.scatter(
    x_rand[:subset][~under_curve[:subset]],
    y_rand[:subset][~under_curve[:subset]],
    color="orange",
    s=1,
    alpha=0.5,
    label="Точки над кривою",
)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([ymin - 0.2, ymax + 0.5])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title(
    f"Монте-Карло для f(x) = x + sin(x) [{a}, {b}]\nМК: {monte_carlo_integral:.4f} | Точний: {analytical_result:.4f}"
)
ax.legend(loc="upper left")
plt.grid(True)
plt.show()