class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        sorted_counts = {}
        output = []
        # countsArrDec = []
        for i in range(len(nums)):
            counts[nums[i]] = 1 + counts.get(nums[i], 0)

        # for value in counts.values():
        #     countsArrDec.append(value)

        print(counts)
        while len(counts) > 0:
            largest_key = list(counts.keys())[0]
            
            for key in counts:
                if counts[key] > counts[largest_key]:
                    largest_key = key
                    
            sorted_counts[largest_key] = counts.pop(largest_key)   


        for key, value in sorted_counts.items():
            if k > 0:
                output.append(key)
            k -=1
        return output

        # i = 0
        # while k > 0:
        #     output.append(countsReversed[i])
        #     k -= 1
        #     i += 1
        # return output
        