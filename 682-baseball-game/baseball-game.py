class Solution(object):
    def calPoints(self, operations):
        stack =[]
        total =0
        ops=operations
        for  i in range(len(ops)):
            if ops[i] not in ["C", "D", "+"]:
                stack.append(int(ops[i]))
            elif ops[i] =="C":
                stack.pop()
            elif ops[i] =="D":
                e =stack[-1]*2
                stack.append(e)
            elif ops[i]=="+":
                a=stack[-1]+stack[-2]
                stack.append(a)
            

        return sum(stack)



        