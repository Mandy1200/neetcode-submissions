class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        maxArea = 0

        def bfs(r, c):
            q = deque([])
            q.append((r,c))
            grid[r][c] = 0

            area = 0
            while q :
                r,c = q.popleft()
                area += 1
                direction_vec = [[1,0],[0,1],[0,-1],[-1,0]]
                for dRow , dCol in direction_vec:
                    rFinal = dRow + r
                    cFinal = dCol + c

                    if(0<= rFinal<rows and 0<=cFinal<cols and 
                    grid[rFinal][cFinal] == 1 ):

                        q.append((rFinal,cFinal))
                        grid[rFinal][cFinal] = 0

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea , bfs(r,c))
        return maxArea

       