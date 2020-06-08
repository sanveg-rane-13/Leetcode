class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n < 1 else math.ceil(self.calcLogBaseTwo(n)) == math.floor(self.calcLogBaseTwo(n))
        
    def calcLogBaseTwo(self, num):
        return (math.log10(num) / math.log10(2))