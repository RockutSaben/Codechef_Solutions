#Question
'''
You're given a number N. Print the first N
lines of the below-given pattern.

    *
   **
  ***
 ****
*****

INPUT:
 - First-line will contain the number N.

Output:
Print the first N lines of the given pattern.

Constraints:
1 ≤ N ≤ 200

Sample Input 1:
4

Sample Output 1:
    *
   **
  ***
 ****

Sample Input 2:
2

Sample Output 2:
    *
   **

Explanation:
 - In the first example, we'll print the first 4 lines of the given pattern.
 - In the second example, we'll print the first 2 lines of the given pattern.
'''

#NOTE: Please do not copy and paste, kindly try to understand and apply on your own.

#Solution

#use try and except as without them you might get EOF (End of file) error
try:
    #storing no. of integers in n as an integer
    n = int(input())

    #using loop to print the series
    for i in range(1,n+1):
    #printing a string to print using i number of '*' and (n-i) number of ' ' (empty spaces)
        print(' '*(n-i) + '*'*i)
except:
    pass