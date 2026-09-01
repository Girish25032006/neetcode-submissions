class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(char for char in s if char.isalnum() or char=="").replace(" ","").lower()
        left=0
        right=len(new_s)-1
        if right == 1:
            if new_s[left] == new_s[right] :
                 return True
            else:
                return False  
        while left < right :
            centre=(left+right)//2

            if left == centre:
                

                if new_s[left] == new_s[right]:
                    return True
                else:
                    return False

            elif new_s[left]==new_s[right]:
                left+=1
                right-=1
            else:
                return False
        return True
    