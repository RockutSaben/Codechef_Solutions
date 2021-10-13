#Question
'''
You're given two numbers L and R. Print all odd numbers between L and R 
(both inclusive) in a single line separated by space, in ascending (increasing) order.

INPUT:
First-line will contain two numbers L and R.

Output:
Print all odd numbers in a single line separated by space, in ascending (increasing) order.

Constraints:
1 ≤ L < R ≤ 10^6

Sample Input 1:
2 9

Sample Output 1:
3 5 7 9

Sample Input 2:
3 4

Sample Output 2:
3

Explanation:
 - In the first example, odd numbers between 2 and 9 are 3,5,7,9.
 - In the second example, the only odd number in the range is 3.
'''

#NOTE: Please do not copy and paste, kindly try to understand and apply on your own.

#Solution

#use try and except as without them you might get EOF (End of file) error
try:
    #using input().split() to split the total input string into a list of multiple strings containing the individual numbers
    # Applying map(int, input().split()) to convert every individual strings into integers
    # Realloting the integers into respective variables
    left, right = list(map(int, input().split()))

    #If left is odd, print all alternate numbers from left as alternate numbers
    #from a odd number is a odd number (e.g. 3+2 = 5(odd))
    if(left%2!=0):
        for i in range(left, right+1, 2):
            print(i, end=" ")
    #If left is not odd, print all alternate numbers from number next of left
    else:
        for i in range(left+1,right+1,2):
            print(i, end=" ")
except:
    pass

