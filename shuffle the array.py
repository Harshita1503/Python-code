class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=len(nums)
        b=a//2
        c=[]
        for i in range(a//2):
            c.append(nums[i])
            c.append(nums[b])
            b+=1
        return c   
