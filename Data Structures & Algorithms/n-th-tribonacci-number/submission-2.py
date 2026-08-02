class Solution:
    def tribonacci(self, n: int) -> int:
        #spaceOpti

        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1
                
        pre3 = 0
        pre2 = 1
        pre1 = 1

        for i in range(3,n+1):
            curr = pre3+pre2+pre1
            pre3 = pre2
            pre2 = pre1
            pre1 = curr

            

        return pre1