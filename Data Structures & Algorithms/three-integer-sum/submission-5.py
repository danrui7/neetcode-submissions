class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        store = []
        nums.sort()
        for i,v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
            l=i+1 
            r=len(nums) -1
            while l<r:
                Sum = v + nums[l] + nums[r]
                if Sum < 0:
                    l += 1
                elif Sum > 0:
                    r -= 1
                else:
                    store.append([v,nums[l], nums[r]])
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return store