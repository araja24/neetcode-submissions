class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

   
        nums = list(set(nums))
        nums.sort()


        current = 1
        maxi = 1

        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]-1:
                current+=1
            else:
                maxi = max(current, maxi)
                current = 1
        
        
        return max(maxi, current)