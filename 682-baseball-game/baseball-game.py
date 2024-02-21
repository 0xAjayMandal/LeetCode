class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum1 = 0
        for op in operations:
            if op == '+':
                stack.append(stack[-1]+stack[-2])
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        for i in range(len(stack)):
            sum1 +=  stack[i]
        return sum1
