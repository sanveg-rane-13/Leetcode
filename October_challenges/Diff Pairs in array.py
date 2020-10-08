# K-diff pairs in array
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hmap,result = {}, set()
		
        for i,num in enumerate(nums):
            hmap[num] = i
			
        for j,num in enumerate(nums):
            if num - k in hmap and (num,num-k) not in result and hmap[num-k] != j:
                result.add((num-k,num))
        return len(result)