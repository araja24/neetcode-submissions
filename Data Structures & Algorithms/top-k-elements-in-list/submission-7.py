class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqList = []
        output = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        print(count)

        for num, freq in count.items():
            freqList.append((freq,num))

        print(freqList)

        freqList.sort(reverse=True)
        print(freqList)

        for i in range(k):
            output.append(freqList[i][1])

        return output

