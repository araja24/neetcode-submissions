class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        output = []
        for s in strs:
            keyList = sorted(s)
            keyString = ''.join(keyList)
            if keyString in anagrams:
                anagrams[keyString].append(s)
            else:
                anagrams[keyString] = [s]
   
        for value in anagrams.values():
            output.append(value)

        return output
      