class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            # ❌ Out of bounds OR water → stop
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            # ✅ Mark visited
            grid[r][c] = "0"
            
            # Explore 4 directions
            dfs(r+1, c)  # down
            dfs(r-1, c)  # up
            dfs(r, c+1)  # right
            dfs(r, c-1)  # left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count