class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rLen = len(grid)
        cLen = len(grid[0])

        q = deque()

        for r in range(rLen):
            for c in range(cLen):
                if grid[r][c] == 0:
                    q.append((r,c))

        direction = [(1,0),(-1,0),(0,1),(0,-1)]

        while q :
            r,c = q.popleft()
            for dr , dc in direction:
                rFinal = dr + r
                cFinal = dc + c

                if(rFinal<0 or cFinal<0 or rFinal == rLen or cFinal == cLen or
                    grid[rFinal][cFinal]!= 2147483647):
                    continue

                grid[rFinal][cFinal] = grid[r][c] + 1 
                q.append((rFinal,cFinal))    