class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        if len(s) != len(t):
            return False


        for letter in s:
            counts[letter] = s.count(letter)

        is_anagram = True
        for letter in t:
            if letter in counts:
                counts[letter] -= 1
            else:
                is_anagram = False

 
        for x in counts:
            if counts[x] != 0:
                is_anagram = False
            
                
        if is_anagram:
            return True
        else:
            return False
            
      
            