class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        print(count)
        # for num, count in count.items():
        #     if count == 2:
        #         occursTwice = num

        for i in range(1, len(nums)+1):
            if i in count:
                if count[i] == 2:
                    dupe = i
            else:
                missing = i

        return[dupe, missing]

        