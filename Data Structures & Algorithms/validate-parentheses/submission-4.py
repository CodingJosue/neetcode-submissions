class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        parDict = {
            '(' : ')',
            '{' : '}',
            '[': ']'
        }

        for char in s:
            if char in parDict:
                stack.append(char)
            else:
                check = len(stack) != 0
                if not check and char: 
                    return False
                if check and parDict[stack.pop()] != char:
                    return False
        print(stack)
        return len(stack) == 0
    

        