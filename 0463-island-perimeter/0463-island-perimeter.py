class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r,c = len(grid),len(grid[0])
        queue = deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    queue.append((i,j))
        t = 0
        diractions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            tr,tc = queue.popleft()
            for nr,nc in diractions:
                x,y =  tr+nr,tc+nc
                if  x >=r or x <0 :
                    t+=1
                if  y >=c or y <0 :
                    t+=1
                if 0<=x<r and 0<=y<c and grid[x][y] == 0:
                    t +=1
        return t



        