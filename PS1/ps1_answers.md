# A.5

## 1. What were your results from `compare_cow_transport_algorithms`? Which algorithm runs faster? Why?

Results:
```
greedy_cow_transport output:
[['Betsy', 'Henrietta'], ['Herman', 'Oreo'], ['Millie', 'Maggie', 'Moo Moo'], ['Milkshake', 'Lola', 'Florence']]
greedy_cow_transport took 0.0010004043579101562 seconds

brute_force_cow_transport output:
[['Henrietta'], ['Lola', 'Millie', 'Moo Moo'], ['Betsy'], ['Milkshake', 'Herman'], ['Florence', 'Maggie'], ['Oreo']]
brute_force_cow_transport took 4.000895261764526 seconds
```
`greedy_cow_transport` is the faster of the two algorithms.

It did not have to go through every permutation of the result set, but focuses on getting there with a logically more effective way.

## 2. Does the greedy algorithm return the optimal solution? Why/why not?
In this situation and problem space, and practically speaking, it finds the largest values first within the set constrains.

## 3. Does the brute force algorithm return the optimal solution? Why/why not?
Brute forcing will always result in a higher Big-O computation time. It should be avoided when there are more optimal solutions available, such as the greedy algorithm in this scenario.

# B.2

## 1. Explain why it would be difficult to use a brute force algorithm to solve this problem if there were 30 different egg weights. You do not need to implement a brute force algorithm in order to answer this.
There would be a high computation time required to solve this problem, as it would have to iterate through all the different egg weights, and perhaps a combination of all the different egg weights. The Big-O will be high to the exponent of 30.

## 2. If you were to implement a greedy algorithm for finding the minimum number of eggs needed, what would the objective function be? What would the constraints be? What strategy would your greedy algorithm follow to pick which coins to take? You do not need to implement a greedy algorithm in order to answer this.
The greedy algorithm takes the largest weights first, but does not take into account that taking a smaller item but multiplying it may reduce the total number of eggs taken. Consider the QUICK TEST CASE below, where 2 eggs weighing 6 instead of selecting 1 egg weighing 9 can actually bring us closer to the objective, and a correct answer.

## 3. Will a greedy algorithm always return the optimal solution to this problem? Explain why it is optimal or give an example of when it will not return the optimal solution. Again, you do not need to implement a greedy algorithm in order to answer this.
Based on the answer in B.2.2, greedy algorithm is suboptimal here and will yield a wrong answer.


```
QUICK TEST CASE
Expected output: 4 (2 * 6 + 2 * 1 = 14) 

Egg weights = (1, 6, 9)
Target weight = 14

greedy_make_weight output:
6
greedy_make_weight took 0.0 seconds

dp_make_weight_no_memo output:
4
dp_make_weight_no_memo took 0.0009996891021728516 seconds

dp_make_weight output:
4
dp_make_weight took 0.0 seconds

DEFAULT CASE
Expected output: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)

Egg weights = (1, 5, 10, 25)
Target weight = 99

greedy_make_weight output:
9
greedy_make_weight took 0.0 seconds

dp_make_weight_no_memo output:
6
dp_make_weight_no_memo took 0.0010001659393310547 seconds

dp_make_weight output:
6
dp_make_weight took 0.0 seconds
```