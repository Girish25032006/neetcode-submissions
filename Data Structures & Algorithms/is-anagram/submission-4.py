class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_str = list(s)
        t_str = list(t)
        s_str.sort()
        t_str.sort()
        if s_str == t_str:
            return True
        else:
            return False
                
        
        
        