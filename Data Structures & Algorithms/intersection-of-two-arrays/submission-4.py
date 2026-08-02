class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        output = []

        both = set1.intersection(set2)
        
        for n in both:
            output.append(n)

        return output