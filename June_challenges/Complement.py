# Complement of Base 10 Integer

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bin_str = bin(N)[2:]
        inv_str = ''
        
        for c in bin_str:
            if c == '1': inv_str += '0'
            else: inv_str += '1'
                
        return int(inv_str, 2)