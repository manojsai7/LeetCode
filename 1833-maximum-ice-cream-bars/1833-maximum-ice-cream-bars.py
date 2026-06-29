class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        if not costs:
            return 0
            
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        
        for cost in costs:
            freq[cost] += 1
            
        total_bars = 0
        
        for cost in range(1, max_cost + 1):
            if freq[cost] == 0:
                continue
                
            if coins < cost:
                break
                
            count_to_buy = min(freq[cost], coins // cost)
            
            total_bars += count_to_buy
            coins -= count_to_buy * cost
            
        return total_bars
        