class Solution:
    def maxDepth(self, s: str) -> int:
        currentDepth = 0
        maxDepth = 0

        for char in s:
            if char == "(":
                currentDepth +=1
                if currentDepth > maxDepth:
                    maxDepth = currentDepth

            elif char == ")":
                currentDepth -= 1
        
        return maxDepth




            
