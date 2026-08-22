class Solution:
    def countOdds(self, low: int, high: int) -> int:
        

        oneToHigh = (high+1)//2
        oneToLow = (low)//2

        return oneToHigh-oneToLow