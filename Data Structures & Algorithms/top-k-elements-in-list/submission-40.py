class Solution:
   def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]  # Fixed typo: 'num' → 'nums'
    
    for num in nums:
        # Count each element into a dictionary
        count[num] = 1 + count.get(num, 0)  # Corrected indentation
    
    for num, cnt in count.items():
        # Append numbers to their frequency bucket
        freq[cnt].append(num)  # Corrected indentation
    
    res = []
    
    for i in range(len(freq) - 1, 0, -1):  # Go from highest freq to lowest
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res


                        
                   

