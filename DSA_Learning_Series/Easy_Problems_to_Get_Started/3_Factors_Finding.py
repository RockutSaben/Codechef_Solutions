#Question
'''
You are given a number N and find all the distinct factors of N.

INPUT:
First-line will contain the number N. 

Output:
 - In the first line print number of distinct factors of N
 - In the second line print all distinct factors in ascending order separated by space.

Constraints:
1 ≤ N ≤ 10^6

Sample Input 1:
4

Sample Output 1:
3
1 2 4

Sample Input 2:
6

Sample Output 2:
4
1 2 3 6

Explanation:
 - In the first example, all factors of 4 are 1, 2, 4.
 - In the second example, all factors of 6 are 1, 2, 3, 6.
'''

#NOTE: Please do not copy and paste, kindly try to understand and apply on your own.

#Solution

#use try and except as without them you might get EOF (End of file) error
try:
    #storing input in n as an integer
    n = int(input())

    #creating an empty list to store the factors
    factors = []

    #determining the factors
    for i in range(1,n+1):
        if(n%i==0):
            factors.append(i)

    #printing the no of factors (i.e. no. of elements in the list factors)
    print(len(factors))

    #printing the entire list as a single string by using join() function
    #This helps in reducing the usage of loops
    print(" ".join(list(map(str, factors))))

    #We can also use loop instead of the above print statement in the following way
    '''
    for i in factors:
        print(i, end=" ")
    '''
except:
    pass

