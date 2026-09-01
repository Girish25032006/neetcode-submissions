class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums1[j] == 0:
                    nums1.pop(j)
                    nums1.append(nums2[i])
                    break

        return nums1.sort()
        

        
        