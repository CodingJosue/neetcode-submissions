class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in d:
                return True
            else:
                d.add(nums[i])
        
        return False
            
        