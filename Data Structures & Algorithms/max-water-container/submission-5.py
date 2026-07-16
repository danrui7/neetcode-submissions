class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i = 0
        j = len(heights)-1
        while i < j and j <= len(heights)-1:
            water = (j-i) * min(heights[i],heights[j])
            res = max(res,water)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return res




        
        