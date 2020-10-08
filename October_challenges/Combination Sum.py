# Combination sum

from copy import copy

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        self.sol = []
        candidates.sort()
        
        pos = 0
        for i in range(len(candidates)):
            if candidates[i] > target: break
            pos = i
        
        for i in range(pos + 1):
            self.findCombinations(candidates, i, [], 0, target)
            
        return self.sol
    
    def findCombinations(self, candidates, pos, curr, tot, target):
        if pos >= len(candidates):
            return 
        
        val = candidates[pos]
        tot += val
               
        if tot == target:
            curr.append(val)
            self.sol.append(copy(curr))
            del curr[-1]
            return
        
        if tot > target:
            return
            
        for i in range(pos, len(candidates)):
            curr.append(val)
            self.findCombinations(candidates, i, curr, tot, target)
            del curr[-1]