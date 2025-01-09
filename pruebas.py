

listNumber = []
target = 0

def get_target_num(listNumber, target):
    max_length = 0
    subarray = []
    
    for start in range(len(listNumber)):
        current_sum = 0
        for end in range(start, len(listNumber)):
            current_sum += listNumber[end]
            
            if current_sum == target:
                current_length = end - start + 1
                
                if current_length > max_length:
                    max_length = current_length
                    subarray = listNumber[start:end + 1]
                    
    return subarray if max_length > 0 else []
    
            
result = get_target_num(listNumber, target)
    
print(f"El subarreglo es: {result}, para el objetivo: {target}")