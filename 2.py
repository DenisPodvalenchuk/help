matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

max_val = float('-inf') 

for i in range(0, len(matrix), 2):
    for element in matrix[i]:
        if element > max_val:
            max_val = element

print(f"Максимальное значение среди нечетных строк: {max_val}")
