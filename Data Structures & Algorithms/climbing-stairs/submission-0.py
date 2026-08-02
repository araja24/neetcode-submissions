class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            prev1 = 2
            prev2 = 3
            current = 0

            for i in range(4, n+1):
                current = prev1 + prev2
                prev1 = prev2
                prev2 = current
            return current
        