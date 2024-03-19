def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    
    total, res = 0, 0
    for i in range(len(gas)):
        total += gas[i]-cost[i]
        if total < 0:
            total = 0
            res = i+1
    if total >= 0:
        return res
    return -1