#Question
'''
You're given the length of three sides a, b, and c respectively. Now If 
these three sides can form an Equilateral Triangle then print 1, if these 
three sides can form an Isosceles Triangle then print 2, if these three sides 
can form a Scalene Triangle then print 3, otherwise print −1.

INPUT:
 - First-line will contain three numbers a, b, and c separated by space.

Output:
Print the answer in a new line.

Constraints:
1 ≤ a, b, c ≤ 10^3

Sample Input 1:
2 4 3

Sample Output 1:
3

Sample Input 2:
4 4 4

Sample Output 2:
1

Sample Input 3:
4 4 9

Sample Output 3:
-1

Explanation:
 - In the first example, (2, 4, 3) will form a Scalene Triangle.
 - In the second example, (4, 4, 4) will form an Equilateral Triangle.
 - In the third example, (4, 4, 9) will not form a triangle.
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
        print(-1)
    else:
        #checking if the sides form a valid triangle i.e. a+b>c
        if(sides[0]+sides[1]>sides[2]):

            #condition for equilateral
            if(sides[0]==sides[1] and sides[1]==sides[2]):
                print(1)

            #condition for isosceles
            elif(sides[0]==sides[1] or sides[1]==sides[2] or sides[0]==sides[2]):
                print(2)

            #else scalene
            else:
                print(3)

        #not valid triangle
        else:
            print(-1)
except:
    pass