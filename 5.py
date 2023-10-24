matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

max_val = float('-inf')  # инициализируем начальное максимальное значение как отрицательную бесконечность

for row in matrix:
    for j in range(1, len(row), 2): 
        if row[j] > max_val:
            max_val = row[j]

print(f"максимальное значение элемента среди четных столбцов матрицы: {max_val}")