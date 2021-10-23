#Question
'''
You're given a number N. Print the first 
N lines of the below-given pattern.

1 2 3 4 5
10 9 8 7 6
11 12 13 14 15
20 19 18 17 16
21 22 23 24 25
30 29 28 27 26


INPUT:
 - First-line will contain the number N.

Output:
Print the first N lines of the given pattern.

Constraints:
1 ≤ N ≤ 200

Sample Input 1:
4

Sample Output 1:
1 2 3 4 5
10 9 8 7 6
11 12 13 14 15
20 19 18 17 16

Sample Input 2:
2

Sample Output 2:
1 2 3 4 5
10 9 8 7 6

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
    curr = 1
    for i in range(n):
        #creating a list consisting of the numbers(in string format) to be 
        #printed in the next row
        curr_lst = list(map(str, [j for j in range(curr,curr+5)]))

        #increasing the curr value for next row
        curr += 5

        #alternating the order of the numbers based on row number
        if(i%2==0):
            #creating a string using join() function from curr_list directly
            print(" ".join(curr_lst))
        else:
            #creating a string using joi() form the reversed curr_list
            print(" ".join(curr_lst[::-1]))
except:
    pass