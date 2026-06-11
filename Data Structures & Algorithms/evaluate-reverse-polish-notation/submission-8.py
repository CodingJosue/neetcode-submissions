class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        n = len(tokens)
    
        for op in tokens:
            c1 = 0
            c2 = 0
            match op:
                case "+":
                    c1 = stack.pop()
                    c2 = stack.pop()
                    stack.append(c1 + c2)
                case "-":
                    c1 = stack.pop()
                    c2 = stack.pop()
                    stack.append(c2- c1)
                case "*":
                    c1 = stack.pop()
                    c2 = stack.pop()
                    stack.append(c1 * c2)
                case "/":
                    c1 = stack.pop()
                    c2 = stack.pop()
                    stack.append(int(c2 / c1))
                case _:
                    stack.append(int(op))
        return stack[0]
            

