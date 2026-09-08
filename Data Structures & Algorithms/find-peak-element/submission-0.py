class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)


        if n == 1:
            return 0

        for i in range(0, n):
            if i == 0:
                if nums[i] > nums[i + 1]:
                    return i

            elif i == n - 1:
                if nums[i] > nums[i - 1]:
                    return i

            else:
                if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                    return i