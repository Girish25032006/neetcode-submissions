class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)
        while l<r:
            if r==1 or l>=r-1:
                if nums[l]<target:
                    return l+1
                else:
                    return l     
            elif target<=nums[l]:
                return l
            elif nums[l]<target and nums[l+1]>target:
                return l+1
            elif nums[l]==target and nums[l+1]>target:
                return l 
            
            
            l+=1
            

        