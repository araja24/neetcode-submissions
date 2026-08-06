class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for letter in s:
            count[letter] = count.get(letter, 0) - 1
        
        for letter in t:
            count[letter] = count.get(letter, 0) + 1

        for n in count.values():
            if n != 0:
                return False
        return True