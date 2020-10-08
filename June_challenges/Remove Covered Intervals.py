# Remove Covered Intervals

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        
        intervals.sort(key=lambda x:x[1], reverse=True)
        intervals.sort(key=lambda x:x[0])
        cl = [True for i in range(len(intervals))]
        length = len(cl)
        
        for i in range(length):
            if not cl[i]:
                continue
            
            for j in range(i + 1, length):
                if not cl[j]:
                    continue
                    
                if intervals[i][1] >= intervals[j][1]:
                    cl[j] = False
                    
        ans = 0
        
        for i in cl:
            if i:
                ans += 1
                
        return ans