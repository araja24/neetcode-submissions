class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = []

        for letter in s:
            counts.append(s.count(letter))

        i = 0
        found = False

        while i < len(counts) and not found:
            if counts[i] == 1:
                return i
                found = True
            i += 1

        if not found:
            return -1
        