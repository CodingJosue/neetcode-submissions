class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
        p2 = len(numbers)  -1 
        p1 = 0

        while True:
        # since the array is sorted if the sum of p1 and p2 is greather than
        # that means the number is to big so we need to decrease our sum by decreasing left pointer

            if numbers[p1] + numbers[p2] > target:

                p2 -= 1
            elif numbers[p1] + numbers[p2] < target:
                p1 += 1
            else:
                return [p1 + 1, p2 + 1]
