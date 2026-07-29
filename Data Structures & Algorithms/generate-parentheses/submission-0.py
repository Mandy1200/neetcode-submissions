class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backTrack(openN, closeN):

            if openN == closeN == n:
                res.append("".join(path))
                return

            if openN < n:
                path.append("(")
                backTrack(openN + 1, closeN)
                path.pop()

            if closeN < openN:
                path.append(")")
                backTrack(openN, closeN + 1)
                path.pop()

        backTrack(0, 0)
        return res