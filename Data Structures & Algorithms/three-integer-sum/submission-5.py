class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        nodupes = []
        print(nums)

        for i in range(len(nums)):

            left = i + 1
            right = len(nums)-1

            while left < right:
                comb = nums[i] + nums[left] + nums[right]

                if comb == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1

                elif comb < 0:
                    left += 1
                elif comb > 0:
                    right -= 1

        
        for arr in res:
            if arr not in nodupes:
                nodupes.append(arr)
        
        return nodupes