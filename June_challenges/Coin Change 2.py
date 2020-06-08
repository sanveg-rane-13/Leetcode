class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        if n == 0: return 1 if n == amount else 0
        
        dp_sum = [[0] * n for _ in range(amount + 1)]
        for i in range(n): dp_sum[0][i] = 1
        
        for i,j in product(range(amount), range(n)):
            dp_sum[i+1][j] = dp_sum[i+1][j-1]
            
            if i+1 - coins[j] >= 0:
                dp_sum[i+1][j] += dp_sum[i+1-coins[j]][j]           
                    
        return dp_sum[-1][-1]