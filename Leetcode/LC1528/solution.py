class Solution:
    def replace(self,s,pos,char):
        return s[:pos]+char+s[pos+1:]
    
    def restoreString(self, s: str, indices: List[int]) -> str:
        for i in range(len(indices)):
            minimum=i
            for j in range(i,len(indices)):
                if indices[j]<indices[minimum]:
                    minimum=j
            temp=s[i]
            s=self.replace(s,i,s[minimum])
            s=self.replace(s,minimum,temp)
            indices[i],indices[minimum]=indices[minimum],indices[i]
        return s
            