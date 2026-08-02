class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Fastest Solution
        # Storing subtraction in diff reduces number of times you do the same operation
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff],i ]
            seen[num] = i