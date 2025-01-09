

listNumber = [5, -3, 2, -7, 8]
numCompare = 0

def getNumer(listNumber, numCompare):
    n = len(listNumber)
    array_last = []

    def back(start, current):
        nonlocal array_last
        if sum(current) == numCompare:
            if len(current) > len(array_last):
                array_last = current[:]
                
        if start > n:
            return
            
        for i in range(start, n):
            back(i + 1, current + [listNumber[i]])
                    
    back(0, [])
    return array_last
    
            
result = getNumer(listNumber, numCompare)
    
print(f"val result: {result}")