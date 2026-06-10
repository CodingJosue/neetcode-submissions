class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hash = set()

        for element in nums:
            if element in my_hash:
                return True
            else:
                my_hash.add(element)
    
        return False