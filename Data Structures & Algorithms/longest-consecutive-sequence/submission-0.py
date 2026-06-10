class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        longestStreak  = 0
        for n in nums :    
            if n -1 not in res:
                currentNum = n
                currentStreak = 1
                while currentNum + 1 in res:
                    currentNum +=  1 
                    currentStreak  += 1
                longestStreak = max(longestStreak, currentStreak)
        return longestStreak    
                
            