class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        newS = ""

        j = 0

        for i in range(len(s)):
            if j < len(t) and s[i] == t[j]:
                newS += t[j]
                j+=1

        return len(t)-len(newS)