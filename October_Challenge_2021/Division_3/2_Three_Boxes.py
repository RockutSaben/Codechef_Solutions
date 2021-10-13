#Question
'''Chef has 3 boxes of sizes A, B, and C respectively. He puts the boxes
in bags of size D (A≤B≤C≤D). Find the minimum number of bags Chef needs
so that he can put each box in a bag. A bag can contain more than one box
if the sum of sizes of boxes in the bag does not exceed the size of the bag.

INPUT:
 - The first line contains T denoting the number of test cases. 
   Then the test cases follow.
 - Each test case contains four integers A , B, C, and D on a single line
   denoting the sizes of the boxes and bags.

OUTPUT:
For each test case, output on a single line the minimum number of bags 
Chef needs.

Constraints:
 - 1 ≤ T ≤ 100
 - 1 ≤ A ≤ B ≤ C ≤ D ≤ 100

Subtasks:
Subtask 1 (100 points): Original constraints

Sample Input 1:
3
2 3 5 10
1 2 3 5
3 3 4 4

Sample Output 1:
1
2
3

Explanation:
 - Test case 1: The sum of sizes of boxes is 2+3+5=10 which is equal to the 
   size of a bag. Hence Chef can put all three boxes in a single bag.
 - Test case 2: Chef can put boxes of size 1 and 3 in one bag and box of 
   size 2 in another bag.
 - Test case 3: Chef puts all the boxes in separate bags as there is 
   no way to put more than one box in a single bag.
'''

#NOTE: Please do not copy and paste, kindly try to understand and apply on your own.

#Solution

#use try and except as without them you might get EOF (End of file) error
try:
    #using int(input()) to get the no of test cases and iterate that no of times
    for _ in range(int(input())):
        #using input().split() to split the total input string into a list of multiple strings containing the individual numbers
        # Applying map(int, input().split()) to convert every individual strings into integers
        # Realloting the integers into respective variables
        a, b, c, d = list(map(int, input().split()))
        
        #This problem is siilar to bin-packing problem
        #refer for more - https://www.geeksforgeeks.org/bin-packing-problem-minimize-number-of-used-bins/
        
        #We will be using best-fit as that requires least no of bins
        #creating a list of weights and bins as required
        weights = [a,b,c]
        bins = [d]

        for i in weights:
            minn = d
            min_index = -1
            for j in range(len(bins)):
                #finding the bin which fits the weight leaving the least empty space
                if(bins[j]-i>=0 and bins[j]-i<minn):
                    minn = bins[j]-i
                    min_index = j
            #if the weight does not fits in none of the available bins                   
            if(min_index)==-1:
                bins.append(d-i)
            #else, fitting the weight in the bin having least remaining space
            else:
                bins[min_index] -= i

        #printingghe total no of bins used                
        print(len(bins))
except:
    pass