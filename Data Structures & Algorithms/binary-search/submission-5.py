class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            centre = (l+r)//2
            if nums[centre] == target:
                return centre
            elif nums[centre]< target:
                l=l+1
            elif nums[centre]>target:
                r=centre-1
        else: 
            return -1

        