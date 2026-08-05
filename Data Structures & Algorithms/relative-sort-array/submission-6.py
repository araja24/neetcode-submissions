class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        output = []
        notin = []

        arr2Set = set(arr2)

        for num in arr1:
            count[num] = 1 + count.get(num, 0)

        for num in arr1:
            if num not in arr2Set:
                notin.append(num)

        for num in arr2:
            freq = count.get(num)
            for i in range(freq):
                output.append(num)

        output = output + sorted(notin)

        return output