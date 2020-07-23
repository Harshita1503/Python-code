class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        s=[]
        for i in range(0,len(nums),2):
            a=nums[i]
            b=nums[i+1]
            for j in range(a):
                s.append(b)
        return s       
