class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #AYAAN SOLUTION
        d = {} 
        s = [] 

        for i, name in enumerate(names): 
            d[heights[i]] = name 

        print(d)

        cool = sorted(d, reverse=True) 
        print(cool)

        for num in cool:
            s.append(d[num])
        print(cool)

        return s