class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for toks in tokens:
            if toks == '+' :
                stack.append(stack.pop()+stack.pop())
            elif toks == '-' : 
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif toks == '*' : 
                stack.append(stack.pop()*stack.pop())

            elif toks == '/' :
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else :
                stack.append(int(toks))
        return stack[0]
