class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        
        zero = nums.count(0)

        totalProduct = 1
        for num in nums:
            totalProduct *= num

        if zero >= 2:
            return res
        
        if zero == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    res[i] = 0
                else:
                    totalProduct = 1
                    for num in nums:
                        if num != 0:
                            totalProduct *= num
                            print(totalProduct)
                    res[nums.index(0)] = totalProduct
        else:
            for i in range(len(nums)):
                res[i] = totalProduct//nums[i]

        return res