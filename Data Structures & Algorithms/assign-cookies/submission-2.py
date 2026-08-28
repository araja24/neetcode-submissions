class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0

        # two pointers, one for each list
        g.sort()
        s.sort()

        gidx = 0
        cidx = 0

        while gidx < len(g) and cidx < len(s):
            if s[cidx] >= g[gidx]:
                gidx += 1
            cidx += 1

        return gidx