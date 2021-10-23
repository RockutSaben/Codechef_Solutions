#Question
'''
You're given the length of three sides a, b, and c respectively. 
Now check if these three sides can form a triangle or not. 
Print "YES"(without quotes) if it can form a valid triangle with an area 
greater than 0, otherwise print "NO" (without quotes).

INPUT:
 - First-line will contain three numbers a, b, and c separated by space.

Output:
Print "YES"(without quotes) if these sides can form a valid triangle, 
otherwise print "NO" (without quotes).

Constraints:
1 ≤ a, b, c ≤ 10^6

Sample Input 1:
2 4 3

Sample Output 1:
YES

Sample Input 2:
1 1 4

Sample Output 2:
NO

Explanation:
 - In the first example, (2, 4, 3) can form a triangle with an area greater than 0.
 - In the second example, (1, 1, 4) will never form a valid triangle.
'''

#NOTE: Please do not copy and paste, kindly try to understand and apply on your own.

#Solution

#use try and except as without them you might get EOF (End of file) error
try:
    #using input().split() to split the total input string into a list of multiple strings containing the individual numbers
    # Applying map(int, input().split()) to convert every individual strings into integers
    # storing all the sides in a list
    sides = list(map(int, input().split()))

    #sorting so that we can take the minimum sides as a and b
    sides.sort()

    #checking the least length of a side is > 0
    if(sides[0]<1):
        print("NO")
    else:
        #checking if the sides form a valid triangle i.e. a+b>c
        if(sides[0]+sides[1]>sides[2]):
            print("YES")

        #not valid triangle
        else:
            print("NO")
except:
    pass