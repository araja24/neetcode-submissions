class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combs = []

        for i in range(len(names)):
            combs.append([names[i], heights[i]])

        num_items = len(combs)
        for i in range(num_items):
            for j in range(0, num_items - i - 1):
                if combs[j][1] < combs[j + 1][1]:
                    temp = combs[j]
                    combs[j] = combs[j + 1]
                    combs[j + 1] = temp

        output = []
        for i in range(len(combs)):
            output.append(combs[i][0])

        return output

            


        