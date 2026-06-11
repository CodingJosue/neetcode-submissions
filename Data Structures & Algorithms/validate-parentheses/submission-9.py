class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictPar = {
             '(':')',
             '{':'}',
             '[':']'
        }
   
        for char in s:
          
            if char in dictPar:
                stack.append(char)
            else:
                check = len(stack) != 0
                if not check and char:
                    return False
                elif check and (char != dictPar[stack.pop()]) :
                    return False
            
        return not stack

