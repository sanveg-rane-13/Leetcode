class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_ransm = Counter(ransomNote) # count letters in ransom note
        counter_magzn = Counter(magazine)   # count letters in magazine
        
        # if any letter is required more in the ransom than available in magazine, return false
        for ltr, cnt in counter_ransm.items():
            if cnt > counter_magzn[ltr]: return False
        
        return True