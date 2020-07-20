class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        s=0
        d=len(A)
        e=[]
        g=[]
        
        for i in range(d):
            s=(s*10)+A[i]
        f=s+K
        f=str(f)
        for i  in  f:
            e.append(i)
        return e    
