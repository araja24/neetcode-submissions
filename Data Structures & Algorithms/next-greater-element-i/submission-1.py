class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        
        for i in range(len(nums1)):
            greaterFound = False

            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in range(j+1, len(nums2)): #look all remaining to check +1 match
                        if nums2[k] > nums2[j]:
                            output.append(nums2[k])
                            greaterFound = True
                            break
                    break
            if greaterFound == False:
                output.append(-1)
        return output
