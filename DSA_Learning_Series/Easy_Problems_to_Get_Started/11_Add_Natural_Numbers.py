#Question
'''
You are given a number N. Find the sum of all numbers from 1 to N.

INPUT:
 - First-line will contain the number N.

Output:
Print the answer in a single line.

Constraints:
1 ≤ N ≤ 10^9

Sample Input 1:
4

Sample Output 1:
10

Sample Input 2:
8

Sample Output 2:
36

Explanation:
 - In the first example, (1 + 2 + 3 + 4) = 10.
 - In the second example, (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8) = 36.
'''

#NOTE: Please do not copy and paste, kindly try to understand and apply on your own.

#Solution

#use try and except as without them you might get EOF (End of file) error
try:
    #storing no. of integers in n as an integer
    n = int(input())

    #using the formula for sum of Arithmetic series
    #Sum = n(a1 + an)/2
    if(n==1):
        summ=1
    else:
        summ = n*(1+n)//2
    
    #printing the sum
    print(summ)
except:
    pass