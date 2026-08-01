class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # countsS = {}
        # countsT = {}

        # for letter in s:
        #     countsS[letter] = s.count(letter)

        # for letter in t:
        #     countsT[letter] = t.count(letter)
        
        # for x in countsS:
        #     print(x)


        counts = {}

        for letter in s:
            counts[letter] = s.count(letter)

        is_anagram = True
        for letter in t:
            if letter in counts:
                counts[letter] -= 1
            else:
                is_anagram = False
        print(counts)


        if len(s) != len(t):
            return False
            
        else:
            for x in counts:
                if counts[x] != 0:
                    is_anagram = False
                    
        if is_anagram:
            return True
        else:
            return False
            
      
            