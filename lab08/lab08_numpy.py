import numpy as np

# =============================================================================
# Задание 1. Создание векторов и матриц — 0,3 балла
# =============================================================================

# 1. hours — числа от 0 до 21 с шагом 3
hours = np.arange(0, 22, 3)
print("hours:", hours)
print("hours.shape:", hours.shape)
print("hours.ndim:", hours.ndim)
print("hours.size:", hours.size)
print("hours.dtype:", hours.dtype)
print()

# 2. line — пять равноудалённых чисел от 0 до 1 включительно
line = np.linspace(0, 1, 5)
print("line:", line)
print()

# 3. zeros — вектор из шести нулей целого типа
zeros = np.zeros(6, dtype=int)
print("zeros:", zeros)
print()

# 4. unknown_table — матрица формы (2, 3), заполненная числом -1
unknown_table = np.full((2, 3), -1)
print("unknown_table:\n", unknown_table)
print()

# 5. identity — единичная матрица размера 3×3
identity = np.eye(3)
print("identity:\n", identity)
print()

# =============================================================================
# Задание 2. Индексы и срезы в векторе — 0,3 балла
# =============================================================================

print("Третий элемент hours:", hours[2])
print("Последний элемент hours:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("Массив в обратном порядке:", hours[::-1])
print()

# =============================================================================
# Задание 3. Строки и столбцы таблицы — 0,4 балла
# =============================================================================

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("temperatures.shape:", temperatures.shape)
print("temperatures.ndim:", temperatures.ndim)
print("temperatures.size:", temperatures.size)
print("Значение из второй строки и третьего столбца:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("Центральный фрагмент 2×2 (строки 0,1; столбцы 1,2):\n", temperatures[0:2, 1:3])
print()

# =============================================================================
# Задание 4. Прямоугольные срезы — 0,3 балла
# =============================================================================

matrix = np.arange(1, 26).reshape(5, 5)
print("matrix:\n", matrix)
print()

print("Первые три строки:\n", matrix[:3])
print("shape:", matrix[:3].shape)
print()

print("Последние две строки:\n", matrix[-2:])
print("shape:", matrix[-2:].shape)
print()

print("Первые два столбца:\n", matrix[:, :2])
print("shape:", matrix[:, :2].shape)
print()

print("Фрагмент строки 1–3, столбцы 2–4:\n", matrix[1:4, 2:5])
print("shape:", matrix[1:4, 2:5].shape)
print()

print("Угловой блок 2×2 в правом нижнем углу:\n", matrix[-2:, -2:])
print("shape:", matrix[-2:, -2:].shape)
print()

# =============================================================================
# Задание 5. Изменение массива с помощью срезов — 0,4 балла
# =============================================================================

# Примеры из задания
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("vector после изменения:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small_matrix после изменения:\n", small_matrix)
print()

# changed_hours
changed_hours = hours.copy()
# .copy() нужна, потому что без неё changed_hours был бы просто ссылкой
# на тот же массив hours, и все изменения изменили бы исходный массив.
# .copy() создаёт независимую копию данных.
changed_hours[2:5] = 99
changed_hours[::2] = -1
print("changed_hours:", changed_hours)
print("исходный hours:", hours)
print()

# changed_matrix
changed_matrix = matrix.copy()
changed_matrix[1, :] = 0          # вся вторая строка (индекс 1) на нули
changed_matrix[:, -1] = -1        # последний столбец на -1
changed_matrix[1:4, 1:4] = 100    # центральный блок 3×3 (строки и столбцы 1–3) на 100
print("changed_matrix:\n", changed_matrix)
print("исходная matrix:\n", matrix)
print()

# =============================================================================
# Задание 6. Изменение формы — 0,3 балла
# =============================================================================

numbers = np.arange(0, 12)
table = numbers.reshape(3, 4)
transposed = table.T

print("numbers.shape:", numbers.shape)
print("table.shape:", table.shape)
print("transposed.shape:", transposed.shape)
print()

# reshape(3, 4) работает, потому что 3 × 4 = 12, что равно числу элементов
# в массиве numbers (12 элементов: от 0 до 11).
# reshape(5, 3) вызовет ошибку, потому что 5 × 3 = 15 ≠ 12.
# NumPy не может разместить 12 элементов в матрицу на 15 ячеек —
# общее число элементов должно совпадать.