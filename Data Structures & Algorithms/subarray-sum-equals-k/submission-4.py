class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currentSum = 0
        seenTotals = {0: 1}
        
        for num in nums:
            currentSum += num

            neededPastTotal = currentSum - k

            if neededPastTotal in seenTotals:
                count += seenTotals[neededPastTotal]
            
            if currentSum in seenTotals:
                seenTotals[currentSum] += 1
            else:
                seenTotals[currentSum] = 1

        return count