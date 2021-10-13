#Question
'''
Given three distinct integers A, B and C, print the second largest number among them.

INPUT:
 - The input consists of three lines.
 - The first line contains a single integer A
 - The second line contains a single integer B
 - The third line contains a single integer C

Output:
Print the second largest number among A, B and C, in a separate line.

Constraints:
1 ≤ A, B, C ≤ 10^9

Sample Input 1:
2
7
21

Sample Output 1:
7

Sample Input 2:
14
28
16

Sample Output 2:
16

Explanation:
 - In the first example, 7 is the second largest number among the given three numbers.
 - In the second example, 16 is the second largest number among the given three numbers.
'''

#NOTE: Please do not copy and paste, kindly try to understand and apply on your own.

#Solution

#use try and except as without them you might get EOF (End of file) error
try:
    #Creating an empty list to store the inputs
    num = []

    #Appending the inputs into num[]
    num.append(int(input())) #A
    num.append(int(input())) #B
    num.append(int(input())) #C

    #sorting the list
    num.sort()

    #printing the second largest number (i.e. the second last element of the list as the list is sorted 
    #in ascending order)
    print(num[-2])
except:
    pass

