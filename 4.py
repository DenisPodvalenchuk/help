matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

max_val = float('-inf')  # инициализируем начальное максимальное значение как отрицательную бесконечность

for i in range(1, len(matrix), 2):
    for element in matrix[i]:
        if element > max_val:
            max_val = element

print(f"максимальное значение элемента среди четных строк матрицы: {max_val}")