class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3 or not height:
            return 0

        l, r = 0, n-1
        maxL = height[l]
        maxR = height[r]
        res = 0
        while l < r :
            if maxL< maxR:
                l+=1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res
             
            
            
                

        