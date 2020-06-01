class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # converting to set for O(1) access
        check, count = set(J), 0 
        
        # checking each stone we have
        for c in S: 
            if c in check: count += 1   
                
        return count