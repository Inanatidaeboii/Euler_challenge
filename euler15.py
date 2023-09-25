n = 20

# initialize grid with zeros
grid = [[0 for _ in range(n+1)] for _ in range(n+1)]

# set base cases: there is only one path to cells in the first row and column
for i in range(n+1):
    grid[i][0] = 1
for j in range(n+1):
    grid[0][j] = 1

# compute the number of paths to each cell
for i in range(1, n+1):
    for j in range(1, n+1):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

# the answer is the number of paths to the bottom right corner
print(grid[n][n])
