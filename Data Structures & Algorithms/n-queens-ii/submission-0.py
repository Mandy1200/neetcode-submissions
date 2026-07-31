class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDig = set()
        negDig = set()

        res = 0

        # board = [["."]*n for i in range(n)]

        def backTrack(r):
            if r == n:
                nonlocal res
                res += 1 
                return 
            
            for c in range(n):
                if c in cols or (r-c) in negDig or (r+c) in posDig :
                    continue

                cols.add(c)
                negDig.add(r-c)
                posDig.add(r+c)

                backTrack(r+1)

                cols.remove(c)
                negDig.remove(r-c)
                posDig.remove(r+c)

        backTrack(0)
        return res            
            