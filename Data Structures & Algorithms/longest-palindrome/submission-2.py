class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        le = 0

        print(counts)
    
        hasOdd = False

        for count in counts.values():
            if count % 2 == 0:
                le += count
            else:
                le += count-1
                hasOdd = True
        
        if hasOdd == True:
            le += 1
            
        return le
            

        