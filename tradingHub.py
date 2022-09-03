def lastStoneWeight(weights):
    # Write your code here
    while len(weights) > 1:
        maxWeight = max(weights)
        weights.remove(maxWeight) 
        secondMaxWeight = max(weights)

        diff = abs(maxWeight - secondMaxWeight)
        if diff == 0:
            if len(weights) < 2:
                return 0
            weights.remove(secondMaxWeight)

            
        else:
            weights.remove(secondMaxWeight)
            weights.append(diff)

    return weights[0]
    





w1 = [1, 2, 3, 6, 7, 7]
w2 = [2, 2, 3, 6, 7, 7]
w3 = [2, 4, 5]
w4 = [46188086,
339992587,
742976890,
801915058,
393898202,
717833291,
843435009,
361066046,
884145908,
668431192,
586679703,
792103686,
85425451,
246993674,
134274127,
586374055,
923288873,
292845117,
399188845,
842456591,
410257930,
333998862,
16561419,
624279391,
459765367,
969764608,
508221973,
82956997,
437034793,
553121267,
554066040,
199416087]


print(lastStoneWeight(w1))
print(lastStoneWeight(w4))