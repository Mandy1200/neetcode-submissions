class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for brac in s:

            if brac in dict:

                # Current bracket is closing bracket
                if stack and stack[-1] == dict[brac]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(brac)

        return len(stack) == 0