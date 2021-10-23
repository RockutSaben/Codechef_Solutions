#Question
'''
You are given a number N and find the sum of the first N odd and even numbers
in a line separated by space. All even and odd numbers should be greater than 0.

INPUT:
 - First-line will contain the number N.

Output:
Print the sum of the first N odd and even numbers in a line separated by space.

Constraints:
1 ≤ N ≤ 10^6

Sample Input 1:
4

Sample Output 1:
16 20

Sample Input 2:
1

Sample Output 2:
1 2

Explanation:
 - In the first example, (1 + 3 + 5 + 7) = 16 and (2 + 4 + 6 + 8) = 20.
 - In the second example, only one odd that is 1 and only one even that is 2.
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
        print(1,2)
    else:
        #calculating sum of first n odd and even numbers using AP Sum formula
        sum_odd = (n*(1 + (n*2 - 1)))//2
        sum_even = (n*(2 + (n*2)))//2
        print(sum_odd, sum_even)
except:
    pass