class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in hmap:
                #index is index of diff
                return [hmap[diff], index]
            hmap[num] = index
            