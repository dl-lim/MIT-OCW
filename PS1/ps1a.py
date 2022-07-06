###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import pandas as pd

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    result = {}
    with open(filename, 'r') as f:
        for line in f:
            j = line.strip().split(',')
            result[j[0]] = int(j[1])
    return result

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    new_cows = cows.copy()
    result = []
    while len(new_cows) > 0:
        trip_cows = []
        trip_limit = limit
        while trip_limit > 0 and len(new_cows) > 0:
            big_cow = max(new_cows, key=new_cows.get)
            new_cows.pop(big_cow)
            trip_cows.append(big_cow)
            trip_limit -= cows[big_cow]
        result.append(trip_cows)
    return result

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    for partition in get_partitions(cows):
        trip_busted = False
        for trip in partition:
            if not trip_busted:
                trip_size = sum(cows[cow] for cow in trip)
                if trip_size > limit:
                    trip_busted = True
        if not trip_busted:
            return partition

        
# Problem 4
def compare_cow_transport_algorithms(func,limit=10):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    for f in func:
        start = time.time()
        print(f.__name__ + " output:")
        print(f(cows,limit))
        end = time.time()
        print(f.__name__ + " took " + str(end - start) + " seconds \n")
        

# Test area
cows = load_cows('ps1_cow_data.txt')
func = [greedy_cow_transport,brute_force_cow_transport]
compare_cow_transport_algorithms(func,10)