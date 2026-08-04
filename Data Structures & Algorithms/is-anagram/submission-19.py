class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        if len(s) != len(t):
            return False

        # O(N) Time: Look at each letter exactly once
        for letter in s:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

        # O(N) Time: Decrement counts and exit early if a letter doesn't match
        for letter in t:
            if letter in counts and counts[letter] > 0:
                counts[letter] -= 1
            else:
                return False # Early termination fix

        return True