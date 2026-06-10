class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        p1 = 0
        p2 = n -1
        currArea = -1

        while p1 < p2:
            h = 0
            calcArea = -1
            if heights[p1] < heights[p2]:
                h = heights[p1]
                calcArea = (p2 - p1) * h
                p1 += 1
            else:
                h = heights[p2]
                calcArea = (p2 - p1) * h
                p2 -= 1
            

            

            if currArea < calcArea:
                currArea = calcArea
        return currArea
            


