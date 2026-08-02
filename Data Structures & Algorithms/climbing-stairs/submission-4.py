class Solution:
    def climbStairs(self, n: int) -> int:
        #memory optimised

        def dfs(n):
            if n<=2:
                return n

            pre2 = 1
            pre1 = 2

            for i in range(3,n+1):
                curr = pre1+pre2
                pre2 = pre1
                pre1 = curr

            return curr
        return dfs(n)            