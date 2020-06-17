class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0] * 3
        
        for i in range(len(nums)):
            counter[nums[i]] += 1
        
        idx = 0
        
        for i in range(3):
            for j in range(0, counter[i]):
                nums[idx] = i
                idx += 1