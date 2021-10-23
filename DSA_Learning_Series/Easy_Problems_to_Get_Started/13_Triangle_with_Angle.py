#Question
'''
You're given the three angles a, b, and c respectively. Now check if these
three angles can form a valid triangle with an area greater than 0 or not. 
Print "YES"(without quotes) if it can form a valid triangle with an area 
greater than 0, otherwise print "NO" (without quotes).

INPUT:
 - First-line will contain three numbers a, b, and c separated by space. 

Output:
Print "YES"(without quotes) if these sides can form a valid triangle,
otherwise print "NO" (without quotes).

Constraints:
0 ≤ a, b, c ≤ 180

Sample Input 1:
20 40 120

Sample Output 1:
YES

Sample Input 2:
100 18 42

Sample Output 2:
NO

Explanation:
 - In the first example, angles set (20, 40, 120) can form a triangle with an area greater than 0.
 - In the second example, angles set (100, 18, 42) will never form a valid triangle.
'''

#NOTE: Please do not copy and paste, kindly try to understand and apply on your own.

#Solution

#use try and except as without them you might get EOF (End of file) error
try:
    #using input().split() to split the total input string into a list of multiple strings containing the individual numbers
    # Applying map(int, input().split()) to convert every individual strings into integers
    # storing all the angles in a list
    angles = list(map(int, input().split()))

    #Triangle is only formed when none of the angles are zero and sum of the three angles is 180
    if(0 not in angles and sum(angles)==180):
        print("YES")
    else:
        print("NO")
except:
    pass