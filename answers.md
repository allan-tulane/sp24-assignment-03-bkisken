
# CMPS 2200 Assignment 3
## Answers

**Name:**____Brian Kisken_____


Place all written answers from `assignment-03.md` here for easier grading.

1a) To produce as few coins as possible that sum to n dollars, we can use a greedy algorithm that selects the largest denominaiton coin less than or equal to the remaining amount until the remaining amount becomes 0

1b) The greedy algorithm always selects the largest denomination coin that can be used without exceeding the remaining amount. This choice is locally optimal because it maximizes the amount that can be subtracted from the remaining amount at each step.

1c) work complexity is O(1) because the number of operations performed by the greedy algorithm is independent of the size of the input value n. It is fixed and determined solely by the available number of coin denominaitons. the span is also O(1) because each step can be executed independently. 

2a) The greedy algorithm fails for denominations {5, 3, 2} and 𝑛 = 7 n=7. It would select one coin of denomination 5 and two coins of denomination 1, resulting in three coins. However, the optimal solution is two coins of denomination 3, resulting in two coins.

2b) The optimal solution would be to find the minimum number of coins to get 
 dollars. For any amount and denomination list [D0, D1, ..., Dk], the optimal solution can be recursively determined by considering all choices of using or not using each denomination. So, making change with arbitrary denominations exhibits optimal substructure because the optimal solution for 𝑛 dollars can be obtained by combining the optimal solutions for smaller amounts.

 2c) By using a bottom-up approach, it would start by initializing a table to store minimum coins for subproblems, ensuring optimal solutions to smaller subproblems are calculated first. Then, we iteratively fill in the table by considering all possible choices of using or not using each denomination for each amount from 0 to 𝑛 dollars. The work of this algorithm is O(𝑛⋅𝑚) where m is the number of denominations. The span depends on the implementation strategy but can be O(n) with appropriate parallelization.
