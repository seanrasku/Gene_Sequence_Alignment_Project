import sys
# Read x, y, and the matrix from the output of edit_distance.py. Matrix comes back in string form, so must convert to int
x = sys.stdin.readline().strip()
y = sys.stdin.readline().strip()
dim = sys.stdin.readline().split()
M = int(dim[0])
N = int(dim[1])
matrix = []
for i in range(M + 1):
    line = sys.stdin.readline().strip()
    strArr = line.split(",")
    nums = []
    for s in strArr:
        if(s != ""):
            nums.append(int(s))
    matrix.append(nums)

sys.stdout.write("Edit distance = {0}\n".format(matrix[0][0]))
i = 0
j = 0

# Use matrix from edit_distance.py to find edit distance path. Gaps move i or j but not both and matches/non-matches move both i and j.
# Output is character from x, character from y, and then penalty
while i < M and j < N:
    if (i < M - 1 and matrix[i][j] == matrix[i + 1][j] + 2):
        sys.stdout.write("{0} {1} {2}\n".format(x[i], "-", 2))
        i += 1
    elif (j < N - 1 and matrix[i][j] == matrix[i][j + 1] + 2):
        sys.stdout.write("{0} {1} {2}\n".format("-", y[j], 2))
        j += 1 
    else:
        if (i < M - 1 and j < N -1 and x[i] == y[j]):
            sys.stdout.write("{0} {1} {2}\n".format(x[i], y[j], 0))  
        else:
            sys.stdout.write("{0} {1} {2}\n".format(x[i], y[j], 1))
        i += 1
        j += 1