class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        leng = sum(matchsticks)//4
        sides = [0]*4
        if sum(matchsticks)/4 != leng:
            return False
        matchsticks.sort(reverse=True)
        def Track(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= leng :
                    sides[j] += matchsticks[i]
                    if Track(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            
            return False
        return Track(0)
                           