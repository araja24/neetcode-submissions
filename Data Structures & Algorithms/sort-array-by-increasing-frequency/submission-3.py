

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        groupedByCount = {}
        output = []
    
        # Keep your original dictionary building logic
        for num, count in counts.items():
            if count not in groupedByCount:
                groupedByCount[count] = []
            groupedByCount[count].append(num)
        
        # New concise sorting logic
        for count, arr in sorted(groupedByCount.items()):
            # Sort numbers descending and add them to the output
            for num in sorted(arr, reverse=True):
                output.extend([num] * count)
        
        return output
