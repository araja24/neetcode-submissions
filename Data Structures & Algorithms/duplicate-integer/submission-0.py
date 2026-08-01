class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # newarr = set()
        # for num in nums:
        #     if num not in newarr:
        #         newarr.add(num)
        
        # if len(newarr) < len(nums):
        #     return True
        # else:
        #     return False
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                return True
        return False