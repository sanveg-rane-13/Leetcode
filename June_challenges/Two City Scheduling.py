class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total, tot_prof = 0, 0
        diff = []
        
        # calculate cost in sending 2N people to A
        for cost in costs:
            total += cost[0]
            # profit / loss if person sent to B
            diff.append(cost[0] - cost[1])
            
        # get total profit if we send the person to B
        diff.sort(reverse=True)
        for i in range(len(costs) // 2):
            tot_prof += diff[i]
        
        # total cost - the profit earned sending to other city
        return total - tot_prof