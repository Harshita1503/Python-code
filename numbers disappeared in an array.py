class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s=len(nums)
        a=set(nums)
        d=[]
        for i in range(1,s+1):
            d.append(i)
        f=set(d)
        r=f-a
        r=list(r)
        return(r)
        
