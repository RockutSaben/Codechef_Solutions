#Question
'''
Raju is planning to visit his favourite restaurant. He shall travel to it by bus.
Only the buses whose numbers are divisible by 5 or by 6 shall take him to his destination.
You are given a bus number N. Find if Raju can take the bus or not. 
Print YES if he can take the bus, otherwise print NO.

INPUT:
The first and only line of the input shall contain an integer N, denoting the bus number.

Output:
Print YES if Raju can take that bus, else print NO.

Constraints:
1 ≤ N ≤ 10^6

Sample Input 1:
60

Sample Output 1:
YES

Sample Input 2:
16

Sample Output 2:
NO

Sample Input 3:
20

Sample Output 2:
YES

Explanation:
 - In the first example, 60 is divisible by 5 and 6 both, so he can take the bus.
 - In the second example, 16 is divisible by neither 5 nor 6, so he can't take the bus.
 - In the third example, 20 is divisible by 5, so he can take the bus.
'''

#NOTE: Please do not copy and paste, kindly try to understand and apply on your own.

#Solution

#use try and except as without them you might get EOF (End of file) error
try:
    #storing input in n as an integer
    n = int(input())

    #determine whether the bus number is divisible by 5 or by 6
    #if condition satisfies then print YES
    if(n%5==0 or n%6==0):
        print("YES")
    #else print NO
    else:
        print("NO")
except:
    pass

