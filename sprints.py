def myFunc(numList):
    sum = 0
    intCount = 0
    maxValue = 0
    for i in numList:
        if isinstance(i, int):
            if i % 2 == 0:
                sum += i
                intCount += 1
        elif isinstance(i, float):
            floatList = [i]
            maxValue = max(floatList)
        else:
            return 0
    avgEven = sum / intCount
    results = [avgEven, maxValue]
    return results