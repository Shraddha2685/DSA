class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for i in accounts:
            sum_rows = sum(i)
            max_wealth = max(sum_rows,max_wealth)

        return max_wealth