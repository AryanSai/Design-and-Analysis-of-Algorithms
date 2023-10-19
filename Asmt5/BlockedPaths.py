def count_shortest_paths(grid):
    M = len(grid)
    N = len(grid[0])
    dp = [[0] * N for _ in range(M)]
    dp[0][0] = 1
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:  # Blocked area
                dp[i][j] = 0
            else:  # normal region
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]

    return dp[M - 1][N - 1]


grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
num_paths = count_shortest_paths(grid)
print("Number of different shortest paths from A to B: {}".format(num_paths))
