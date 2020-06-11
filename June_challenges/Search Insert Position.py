class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        srt, end = 0, len(nums)
        
        while srt < end:
            mid = (srt + end)//2
            if nums[mid] >= target: end = mid
            else: srt = mid + 1
                
        return srt