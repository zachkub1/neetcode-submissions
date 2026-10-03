class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        direc = [[0,1], [1,0], [-1,0], [0,-1]]

        def check(r,c):
            #validity
            if (r < 0 or c < 0 or
            r >= rows or 
            c >= cols or 
            grid[r][c] == '0'):
                return 

            grid[r][c] = '0'
            

            for dx, dy in direc:
                check (r + dx, c + dy )

            #return
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    check(r,c)
                    count += 1
        return count