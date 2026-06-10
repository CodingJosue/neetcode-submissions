class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        else:
            set1 = []
            set2 = []
            for i in range(len(s)):
                set1.append(s[i])
                set2.append(t[i])

        return sorted(set1) == sorted(set2)

        