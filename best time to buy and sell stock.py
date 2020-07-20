class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        l=maxf=0
        for i in range(len(prices)):
            maxf=max(maxf,prices[i]-prices[l])
            if prices[i]<prices[l]:
                l=i
        return(maxf)   
        
        
