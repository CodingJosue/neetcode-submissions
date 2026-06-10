class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # create count dictionaries for s and t
        count_s = {}
        count_t = {}

        ## A loop that checks the character in s which are keys and assign the number of time they are repeated for each strings
        # the 0 inside of .get is the default value if of that so the first iteration it will return 0 because its the first occcurence
        for ch in s :
            count_s[ch] = count_s.get(ch, 0) + 1

        for ch in t:
            count_t[ch] = count_t.get(ch, 0) +  1
        return count_s == count_t

        