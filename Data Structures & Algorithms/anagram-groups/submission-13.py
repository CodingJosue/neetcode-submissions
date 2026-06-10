class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for stred in strs:
            freq = [0] * 26
            for char in stred:
                freq[ord(char) - ord('a')] = stred.count(char)
            tupleD = tuple(freq)
            if tupleD not in anagrams:
                anagrams[tupleD] = [stred]
            else:
                anagrams[tupleD].append(stred)
        return list(anagrams.values())                        

                
