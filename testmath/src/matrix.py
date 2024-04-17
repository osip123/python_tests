
def validMatrix(matrix:int) -> int:
    for mat in matrix:
        print(mat)

def search_on_matrix(matrix:int, ref:int) -> int:
    for mat in range(0, len(matrix)):
        for i in matrix[mat]:
            print(i)


def main() -> int:
    matrix = [[1, 2, 3],
              [1, 2, 4],
              [2, 5, 8]]
    print(validMatrix(matrix))
    return 0

main()