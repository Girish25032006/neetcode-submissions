class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right=len(s)-1
        
        while left < right :
            centre = (left +right)//2
            if centre == 0:
                s[left],s[right]=s[right],s[left]
                return s
            elif left == centre:
                s[left],s[right]=s[right],s[left]
                break 
            else:
                s[left],s[right] = s[right],s[left]
                left+=1
                right-=1
        return s
        
            

            
        