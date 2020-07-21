class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed) :
            if flowerbed[i] == 1 :                                   #case 1 : i th is one and the next one must be zero
                i+=2 
            elif i+1 < len(flowerbed) and flowerbed[i+1] == 1 :      #case 2 : i th is zero and i+1 th is one. the i + 2 must be zero
                i+=3
            else :                                                   #case 3 : the first two are zeros, so the first one can be planted.
                i += 2
                n -= 1
        return n <= 0
