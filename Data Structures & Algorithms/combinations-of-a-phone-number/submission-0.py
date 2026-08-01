class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []

        digToChar = {"2":"abc",
                     "3":"def",
                     "4":"ghi",
                     "5":"jkl",
                     "6":"mno",
                     "7":"pqrs",
                     "8":"tuv",
                     "9":"wxyz"}

        def backTrack(i,curS):
            if len(curS) == len(digits):
                res.append(curS)
                return
                
            for s in digToChar[digits[i]]:
                backTrack(i+1,curS + s)

        if digits:
            backTrack(0,"")

        return res    