matrix = [[1, 12, 3],
          [8, 5, 6],
          [7, 8, 23]]

min_val = float('inf')  # инициализируем начальное минимальное значение как положительную бесконечность

for i in range(1, len(matrix), 2):  
    for element in matrix[i]:
        if element < min_val:
            min_val = element

print(f"Минимальное значение элемента среди четных строк матрицы: {min_val}")
