class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        
        visited = {}
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    visited[(i,j)] = False
        diractions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(obj):
            visited[obj] = True
            r,c = obj
            area = 0
            for rn,cn in diractions:
                i,j = r+rn,c+cn
                if 0<=i<n and 0<=j<m and grid[i][j] ==1  and not visited[(i,j)]:
                   area +=1 + dfs((i,j))
            return area
        for obj in visited:
            if not visited[obj]:
                max_area = max(max_area,1+dfs(obj) )
              
        return max_area





        

        