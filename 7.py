matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

min_val = float('inf')  # инициализируем начальное минимальное значение как положительную бесконечность

for row in matrix:
    for j in range(0, len(row), 2):  
        if row[j] < min_val:
            min_val = row[j]

print(f"Минимальное значение элемента среди нечетных столбцов матрицы: {min_val}")
