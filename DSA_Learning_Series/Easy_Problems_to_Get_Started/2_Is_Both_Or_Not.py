#Question
'''You're given a number N. If N is divisible by 5 or 11 but not both then print
"ONE"(without quotes). If N is divisible by both 5 and 11 then print "BOTH"(without quotes).
If N is not divisible by 5 or 11 then print "NONE"(without quotes).

INPUT:
First-line will contain the number N.

Output:
Print the answer in a new line.

Constraints:
1 ≤ N ≤ 10^3

Sample Input 1:
50

Sample Output 1:
ONE

Sample Input 2:
110

Sample Output 2:
BOTH

Sample Input 3:
16

Sample Output 3:
NONE

Explanation:
 - In the first example, 50 is divisible by 5, but not 11.
 - In the second example, 110 is divisible by both 5 and 11.
 - In the third example, 16 is not divisible by 5 or 11.
'''

#NOTE: Please do not copy and paste, kindly try to understand and apply on your own.

#Solution

#use try and except as without them you might get EOF (End of file) error
try:
    #storing the input in n
    n = int(input())

    #conditions
    #both 5 and 11
    if(n%5==0 and n%11==0):
        print("BOTH")
    #either 5 or 11
    elif(n%5==0 or n%11==0):
        print("ONE")
    #neither 5 nor 11
    else:
        print("NONE")
except:
    pass

