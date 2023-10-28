t = int(input())
def check_col(mat, col, row, n):
    if col == n - 1:
        return False
    return mat[row][col + 1] == "0"
def check_row(mat, col, row, n):
    if row == n - 1:
        return False
    return mat[row + 1][col] == "0"

def solve(mat, n):
    for row in range(n):
        for col in range(n):
            if mat[row][col] == "1" and check_col(mat, col, row, n) and check_row(mat, col, row, n):
                return "NO"
    return "YES"
for _ in range(t):
    n = int(input())

    mat = []
    for i in range(n):
        mat.append(input())
    
    
    print(solve(mat, n))
    
    
