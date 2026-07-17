class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rlen = len(grid)
        clen = len(grid[0])

        visited = set()
        island = 0

        def bfs(r,c):

            qyou = collections.deque()
            visited.add((r,c))
            qyou.append((r,c))
            
            while qyou :
                r,c = qyou.popleft()
                dirc = [[-1,0],[0,-1],[1,0],[0,1]]

                for dRow , dCol in dirc:
                    r_final = dRow + r
                    c_final = dCol + c

                    if (0 <= r_final < rlen and 0 <= c_final < clen
                        and grid[r_final][c_final] == "1" and (r_final,
                        c_final) not in visited):
                        
                        visited.add((r_final,c_final))
                        qyou.append((r_final,c_final))


        for r in range(rlen):
            for c in range(clen):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    island += 1 
        
        return island            

        