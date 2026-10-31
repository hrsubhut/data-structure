class Solution(object):
    def uniquePaths(self, grid):
        """:type grid: List[List[int]] :rtype: int"""
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Helper function to find where a move from (r, c) in direction (dr, dc) ends up
        def get_next(r, c, dr, dc):
            curr_r, curr_r_dir = r + dr, dc  # moving into (r + dr, c + dc)
            curr_c = c + dc
            
            # Follow reflections while we hit mirrors
            while 0 <= curr_r < m and 0 <= curr_c < n and grid[curr_r][curr_c] == 1:
                if curr_r_dir == 1:  # was moving right, turns down
                    curr_r_dir = 0
                    curr_r += 1
                else:  # was moving down, turns right
                    curr_r_dir = 1
                    curr_c += 1
            
            if 0 <= curr_r < m and 0 <= curr_c < n:
                return (curr_r, curr_c)
            return None

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    if i == 0 and j == 0:
                        pass
                    else:
                        continue
                
                # Try moving right (dr=0, dc=1)
                next_right = get_next(i, j, 0, 1)
                if next_right:
                    nr, nc = next_right
                    dp[nr][nc] = (dp[nr][nc] + dp[i][j]) % MOD

                # Try moving down (dr=1, dc=0)
                next_down = get_next(i, j, 1, 0)
                if next_down:
                    nr, nc = next_down
                    dp[nr][nc] = (dp[nr][nc] + dp[i][j]) % MOD

        return dp[m - 1][n - 1]