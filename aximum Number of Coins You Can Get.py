
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        itemsPicked = len(piles)/3
        sortedPiles = piles.sort(reverse=True)
        
        index = 1
        picked = 0
        sum = 0
        while picked < itemsPicked:
            sum = sum + piles[index]
            index = index + 2
            picked = picked + 1
        return sum
    
    

            
            
        
        
        