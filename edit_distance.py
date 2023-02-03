import sys
# Read in gene sequence strings x and y from file
x = sys.stdin.readline().strip()
y = sys.stdin.readline().strip()
M = len(x)
N = len(y)

# Create (M + 1) x (N + 1) matrix with elements initialized to 0, where
# M and N are lengths of x and y respectively.
matrix = [[0] * (N + 1) for _ in range(M + 1)]


# Initialize matrix to appropriate values.

for i in range(M):
    matrix[i][N] = 2 * (M - i)
for j in range(N):
    matrix[M][j] = 2 * (N - j)

# Compute rest of matrix using dynamic programming, starting from the bottom right, 
# and working way up to matrix[0][0] where the edit distance is located.
for i in range(M-1, -1, -1):
    for j in range(N-1, -1, -1):
        penalty = 0
        if x[i] != y[j]:
            penalty = 1
        matrix[i][j] = min(matrix[i + 1][j + 1] + penalty, matrix[i + 1][j] + 2, matrix[i][j + 1] + 2)

# Write x, y, and matrix
sys.stdout.write(x + "\n")
sys.stdout.write(y + "\n")
sys.stdout.write(str(M) + " " + str(N) + "\n")
for i in range(M + 1):
    for j in range(N + 1):
        sys.stdout.write("{0},".format(matrix[i][j]))
    sys.stdout.write("\n")