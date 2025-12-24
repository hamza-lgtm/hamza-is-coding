class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n,m = len(image) , len(image[0])
        adj = image[sr][sc]
        def dfs(r,c):
            if 0<=r<n and 0<=c<m and image[r][c] == adj and image[r][c] != color  :
                image[r][c] = color
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        dfs(sr,sc)
        return image



        