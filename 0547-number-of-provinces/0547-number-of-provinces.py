class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n
        provinces = 0

        def dfs(city_id):
            visited[city_id] = True
            for j in range(n):
                if isConnected[city_id][j] == 1 and not visited[j]:
                    dfs(j)
        for i in range(n):
            if not visited[i]:
                provinces+=1
                dfs(i)
        return provinces


        