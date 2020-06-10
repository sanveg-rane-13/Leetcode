class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t: return True
        elif s == '': return True
        elif t == '': return False
        
        ptr_s, ptr_t = 0, 0
        len_s, len_t = len(s), len(t)
        
        # straight pass
        while ptr_t < len_t:
            if s[ptr_s] == t[ptr_t]:
                ptr_s += 1
            ptr_t += 1
            if ptr_s == len_s: return True
        
        ptr_s, ptr_t = len_s - 1, len_t - 1
        # reverse pass
        while ptr_t >= 0:
            if s[ptr_s] == t[ptr_t]:
                ptr_s -= 1
            ptr_t -= 1
            if ptr_s == -1: return True
            
        return False