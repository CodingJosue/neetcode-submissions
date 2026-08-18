class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        val = {}

        for i  in range(n):
            needed = target - nums[i]
            if needed in val :
                return [val[needed], i]
            else:
                val[nums[i]] = i

        return [0,0]
