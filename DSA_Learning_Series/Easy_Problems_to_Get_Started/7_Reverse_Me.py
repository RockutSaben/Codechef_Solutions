#Question
'''
You are given a list of N integers and you need to reverse it 
and print the reversed list in a new line.

INPUT:
 - First-line will contain the number N
 - Second line will contain N space-separated integers.

Output:
Print the reversed list in a single line.

Constraints:
1 ≤ N, Ai ≤ 10^5

Sample Input 1:
4
1 3 2 4

Sample Output 1:
4 2 3 1

Sample Input 2:
2
9 8

Sample Output 2:
8 9

Explanation:
 - In the first example, the reverse of the [1,3,2,4] is [4,2,3,1].
 - In the second example, the reverse of [9,8] is [8,9].
'''

#NOTE: Please do not copy and paste, kindly try to understand and apply on your own.

#Solution

#use try and except as without them you might get EOF (End of file) error
try:
    #storing no. of integers in n as an integer
    n = int(input())

    #using input().split() to split the total input string into a list of multiple strings containing the individual numbers
    #Applying map(int, input().split()) to convert every individual strings into integers
    #using list() to create a list containing the integers
    num = list(map(int, input().split()))

    #reverse the list permanently
    num.reverse()

    #printing the entire list as a single string by using join() function
    #This helps in reducing the usage of loops
    print(" ".join(list(map(str, num))))

    #We can also use loop instead of the above print statement in the following way
    '''
    for i in num:
        print(i, end=" ")
    '''
    
    #Instead of reversing the list permanently we can use slicing technique
    '''print(" ".join(list(map(str, num[::-1]))))''' #Here -1 represents negative step value 1
except:
    pass

