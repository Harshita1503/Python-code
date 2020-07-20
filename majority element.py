class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict.fromkeys(nums)
        for u in d:
            if nums.count(u)>len(nums)//2:
                return u
        
