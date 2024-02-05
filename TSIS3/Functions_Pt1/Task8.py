def spy_game(nums):
    has_0 = False
    has_0_0 = False
    
    for num in nums:
        if num == 0:
            # If we haven't seen a 0 yet, mark it as seen
            if not has_0:
                has_0 = True
            # If we've seen a 0 before, mark the occurrence of 0, 0
            elif has_0 and not has_0_0:
                has_0_0 = True
        elif num == 7:
            # If we've seen both 0 and 0, 0 before, and we encounter 7, return True
            if has_0 and has_0_0:
                return True
    # If we don't find the sequence, return False
    return False

print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7]))  
print(spy_game([1,7,2,0,4,5,0]))  
