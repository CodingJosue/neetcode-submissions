class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) -1
    

        while p1 < p2:
            v1 = ord(s[p1])
            v2 = ord(s[p2])
            if not((65 <= v1 <= 90) or (97 <= v1 <= 122) or (48 <= v1 <= 57)):
                p1 += 1
                continue
            if   not((65 <= v2 <= 90) or (97 <= v2 <= 122) or (48 <= v2 <= 57)):
                p2 -= 1
                continue
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1 
            p2 -= 1


        return True