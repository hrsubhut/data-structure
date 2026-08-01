class Solution(object):
    def isValid(self, s):
        stack =[]
        closeloop = {
            "]":"[","}":"{",
            ")":"("
        }

        for c in s:
            if c in closeloop:
                if stack and stack[-1] == closeloop[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        