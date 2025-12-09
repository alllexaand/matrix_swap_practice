def input_matrix(n, m):
    """Функция для ввода матрицы размером n x m."""
    matrix = []
    for i in range(n):
        row = input(f"Введите элементы {i + 1}-й строки через пробел: ").strip().split()
        matrix.append([float(x) for x in row])
    return matrix

def swap_min_max_rows(matrix):
    """Функция для замены строк с максимальным и минимальным элементами в матрице."""
    max_row_index = min_row_index = 0
    max_value = min_value = matrix[0][0]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_row_index = i
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_row_index = i

    matrix[max_row_index], matrix[min_row_index] = matrix[min_row_index], matrix[max_row_index]
    return matrix

def print_matrix(matrix):
    """Функция для вывода матрицы."""
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    try:
        n = int(input("Введите количество строк матрицы n: "))
        m = int(input("Введите количество столбцов матрицы m: "))
        if n <= 0 or m <= 0:
            raise ValueError("Количество строк и столбцов должно быть положительным числом.")

        print("Введите матрицу:")
        matrix = input_matrix(n, m)

        print("\nИсходная матрица:")
        print_matrix(matrix)

        swapped_matrix = swap_min_max_rows(matrix)

        print("\nМатрица после замены строк с максимальным и минимальным элементами:")
        print_matrix(swapped_matrix)

    except ValueError as e:
        print("Ошибка ввода:", e)

if __name__ == "__main__":
    main()