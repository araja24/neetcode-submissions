class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        groupedByCount = {}
        output = []

        for num, count in counts.items():
            if count not in groupedByCount:
                groupedByCount[count] = []

            groupedByCount[count].append(num)
        
        print(groupedByCount)
        #dict of lowest to highest counts
        reversedGroupedByCount = sorted(groupedByCount.items())

        for count, arr in reversedGroupedByCount:
            if len(arr) == 1:
                output.extend([arr[0]]*count)
                print("lol")
            elif len(arr) > 1:
                arr.sort()
                for i in range(len(arr)-1, -1,-1):
                    output.extend([arr[i]]*count)
        
        print(reversedGroupedByCount)
        return output