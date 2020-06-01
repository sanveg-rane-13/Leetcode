# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        checked = dict()
        
        srt, end = 1, n
        
        # implementing binary search to check minimum versions
        while srt <= end:
            mid = (srt + end) // 2
            
            res = isBadVersion(mid)
            checked[mid] = res
            
            # if mid is bad version and it's previous isn't then mid is the first bad version
            if res and ((mid - 1 ) in checked and not checked[(mid-1)]):
                return mid
            
            # if mid is not bad but it's next is then the next version is the first bad version
            elif not res and ((mid + 1) in checked and checked[(mid+1)]):
                return mid + 1
            
            # adjust start and end as per binary search
            if not res: srt = mid + 1
            else: end = mid - 1
        
        
        return srt