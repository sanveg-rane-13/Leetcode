class Solution:
    def findComplement(self, num: int) -> int:
        int_fmt = bin(num)[2:]  # converting to binary string
        ans_str = ''
        
        # flipping each characted of the binary string
        for i in int_fmt:
            if i == '0': ans_str += '1'
            else: ans_str += '0'
        
        # converting the base 2 flipped string to interger
        return int(ans_str, 2)