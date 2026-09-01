class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1=list(word1)
        w2=list(word2)
        li=[]
        w11=len(w1)
        w22=len(w2)
        maxi=max(w11,w22)
        mini=min(w11,w22)
        for i in range(maxi):
            if i<=mini-1:
                li.append(w1[i])
                li.append(w2[i])
            elif i>=mini:
                if len(w1)>mini:
                    li.append(w1[i])
                elif len(w2)>mini:
                    li.append(w2[i])
            
                   

        result="".join(li)
        return result 



        
        