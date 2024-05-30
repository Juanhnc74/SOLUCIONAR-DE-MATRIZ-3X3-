def gauss_jordan(matrix):
    n = len(matrix)

    # Forward Elimination
    for i in range(n):
        # Make the diagonal contain all 1's
        factor = matrix[i][i]
        if factor == 0:
            raise ValueError("No existe solución unica")
        for j in range(n + 1):
            matrix[i][j] /= factor
        
        # Make the elements below the leading 1's to be 0
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(n + 1):
                    matrix[k][j] -= factor * matrix[i][j]

    # Extracting solutions
    solutions = [matrix[i][n] for i in range(n)]
    return solutions

def main():
    matrix = []

    print("Introduce los elementos de la matriz aumentada 3x4 (incluyendo términos independientes):")
    for i in range(3):
        row = list(map(float, input(f"Fila {i+1}: ").split()))
        if len(row) != 4:
            print("Cada fila debe contener 4 elementos.")
            return
        matrix.append(row)

    try:
        solutions = gauss_jordan(matrix)
        print("Las soluciones del sistema son:")
        for i, solution in enumerate(solutions, 1):
            print(f"x{i} = {solution}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

