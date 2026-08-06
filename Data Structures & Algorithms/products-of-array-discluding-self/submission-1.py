class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        zeroCount = nums.count(0)

        if zeroCount > 1:
            return [0]*n

        if zeroCount == 1:
            zeroIndex = nums.index(0)

            productWithoutZero = 1
            for num in nums:
                if num != 0:
                    productWithoutZero *= num
            
            res = [0]*n

            res[zeroIndex] = productWithoutZero
            return res

        if zeroCount < 1:
            totalProduct = 1
            for num in nums:
                totalProduct *= num
            
            res = []
            for num in nums:
                res.append(totalProduct // num)

            return res