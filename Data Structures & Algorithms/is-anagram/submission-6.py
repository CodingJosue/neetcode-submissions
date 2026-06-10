class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # what i could do is make a frquency so loop torugh all the elements of the first one  check f their frquency are equals
        str1 = {}
        str2 = {}

        # loop trough str1 

        for char in s:
            str1[char] = str1.get(char, 0) + 1 

        for char in t:
            str2[char] = str2.get(char, 0) + 1
        
        return str1 == str2

        