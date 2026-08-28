class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        current = 0
        maxx = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
                maxx = max(current, maxx)
            else:
                current = 0
    
        return maxx