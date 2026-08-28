class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        print(nums)
        for num in nums.copy():
            if num == val:
                nums.remove(val)

    
        print(nums)
        return len(nums)