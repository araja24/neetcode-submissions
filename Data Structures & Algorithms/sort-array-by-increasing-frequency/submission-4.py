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

        for count, arr in sorted(groupedByCount.items()):
            if len(arr) == 1:
                output.extend([arr[0]]*count)
            elif len(arr) > 1:
                arr.sort()
                for i in range(len(arr)-1, -1, -1):
                    output.extend([arr[i]]*count)
        
        return output