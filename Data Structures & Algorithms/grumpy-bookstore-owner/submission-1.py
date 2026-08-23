class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        best = 0

        for start in range(len(grumpy) - minutes + 1):
            satisfy = 0

            for forward in range(minutes):

                index = start + forward

                if grumpy[index] == 1:
                    satisfy += customers[index]
                
                best = max(satisfy, best)
                

        satisfy = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfy += customers[i]

        return satisfy+best


