class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        sorted_counts = {}
        output = []
        # countsArrDec = []
        for i in range(len(nums)):
            counts[nums[i]] = 1 + counts.get(nums[i], 0)

        # Order dict from largest to smallest (based on value (not key))
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