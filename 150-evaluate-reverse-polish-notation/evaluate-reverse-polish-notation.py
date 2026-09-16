class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
            
            elif tokens[i] == "+":
                a = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(a)
                
            elif tokens[i] == "-":
                b = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(b)
                
            elif tokens[i] == "*":
                c = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(c)
                
            elif tokens[i] == "/":
                d = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(d)
                
        return stack[-1]