#Question
'''
You are given a list of N integers and a value K. Print 1 if K exists
in the given list of N integers, otherwise print −1.

INPUT:
 - First-line will contain two numbers N and K
 - Next line contains N space-separated numbers. 

Output:
Print the answer in a new line.

Constraints:
1 ≤ N, K, Ai ≤ 10^5

Sample Input 1:
4 2
1 2 3 4

Sample Output 1:
1

Sample Input 2:
4 4
1 2 6 9

Sample Output 2:
-1

Explanation:
 - In the first example, as 2 is present in the list.
 - In the second example, 4 is not present in the list.
'''

#NOTE: Please do not copy and paste, kindly try to understand and apply on your own.

#Solution

#use try and except as without them you might get EOF (End of file) error
try:
    #using input().split() to split the total input string into a list of multiple strings containing the individual numbers
    # Applying map(int, input().split()) to convert every individual strings into integers
    # Realloting the integers into respective variables
    n, k = list(map(int, input().split()))

    #using list() to create a list containing the integers
    num = list(map(int, input().split()))

    #determining existence of k in the list of integers
    if(num.count(k)>0): #i.e. k is present atleast once, then print 1
        print(1)
    else:               #else print -1
        print(-1)
except:
    pass

