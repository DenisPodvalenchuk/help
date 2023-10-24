matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

min_val = float('inf')  # инициализируем начальное минимальное значение как положительную бесконечность

for i in range(0, len(matrix), 2):  # итерируемся по нечетным строкам
    for element in matrix[i]:
        if element < min_val:
            min_val = element

print(f"Минимальное значение элемента среди нечетных строк матрицы: {min_val}")
