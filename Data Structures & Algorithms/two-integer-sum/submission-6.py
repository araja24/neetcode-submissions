class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            # print("i, num", i, num)
            # print("DIFF: ", diff)
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
            # print("CURRENT SEEN: ", seen)

        # print("FINAL SEEN: ", seen)
          