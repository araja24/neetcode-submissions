class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            "(": ")",
            "[": "]",
            "{": "}"
        }



        stack = []

        for char in s:
            if char in hmap:
                stack.append(char)
            else:
                if not stack:
                    return False
                current = stack.pop()
    
                if hmap[current] != char:
                    return False
            
        return len(stack) == 0