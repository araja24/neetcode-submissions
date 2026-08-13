class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_chars = set(s)
        needed = []
     
        for char in order:
            if char in s_chars:
                needed.append(char)
        print(needed)

        count = Counter(s)

        output = []

        for char in needed:
            rep = char * count[char]
            output.append(rep)

        for char in s:
            if char not in order:
                output.append(char)

        return "".join(output)
            