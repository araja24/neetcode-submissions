class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        print(nums)

        if nums == []:
            return 0

        maxStreak = 1
        currentStreak = 1
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1]:
                currentStreak += 1
            else:
                if currentStreak > maxStreak:
                    maxStreak = currentStreak
                currentStreak = 1

        if currentStreak > maxStreak:
            return currentStreak
        else:
            return maxStreak