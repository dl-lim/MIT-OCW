###########################
# 6.0002 Problem Set 1b: Space Change
# Name: DL Lim
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================
import sys, time

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    s
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    least = sys.maxsize
    if target_weight == 0:
        return 0 
    elif target_weight in memo:
        return memo[target_weight]
    elif target_weight > 0:
        for weight in egg_weights:
            sub = dp_make_weight(egg_weights,target_weight - weight) # reduces target_weight to 0
            least = min(least, sub) # target_weight will always reach 0 eventually, thus returning 0
    memo[target_weight] = least +1
    return least + 1 # add one egg for each take, to be added to the sub result at the top



def dp_make_weight_no_memo(egg_weights, target_weight):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    least = sys.maxsize
    if target_weight == 0:
        return 0 
    elif target_weight > 0:
        for weight in egg_weights:
            sub = dp_make_weight(egg_weights,target_weight - weight) # reduces target_weight to 0
            least = min(least, sub) # target_weight will always reach 0 eventually, thus returning 0
    return least + 1 # add one egg for each take, to be added to the sub result at the top


def greedy_make_weight(egg_weights, target_weight):
    eggno = 0
    i = len(egg_weights)-1 # assuming egg weights are sorted from smallest to largest
    remainder_weight = target_weight
    while remainder_weight > 0 and i >= 0:
        if egg_weights[i] > remainder_weight:
            i -= 1
        else:
            eggno += 1
            remainder_weight -= egg_weights[i]
    return eggno


def compare_algorithms(func,egg_weights,target_weight):
    print("Egg weights = " + str(egg_weights))
    print("Target weight = " + str(target_weight) + "\n")
    for f in func:
        print(f.__name__ + " output:")
        start = time.time()
        print(f(egg_weights,target_weight))
        end = time.time()
        print(f.__name__ + " took " + str(end - start) + " seconds \n")
        


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    func = [greedy_make_weight,dp_make_weight_no_memo,dp_make_weight]
    print('QUICK TEST CASE')
    egg_weights = (1, 6, 9)
    target_weight = 14
    print("Expected output: 4 (2 * 6 + 2 * 1 = 14) \n")
    compare_algorithms(func,egg_weights,target_weight)

    print('DEFAULT CASE')
    egg_weights = (1, 5, 10, 25)
    target_weight = 99
    print("Expected output: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99) \n")
    compare_algorithms(func,egg_weights,target_weight)


