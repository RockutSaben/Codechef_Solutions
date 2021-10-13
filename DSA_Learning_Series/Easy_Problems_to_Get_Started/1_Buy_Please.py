#Question
'''Chef went to a shop and buys 'a' pens and 'b' pencils. Each pen costs 'x' units and
each pencil costs 'y' units. Now find what is the total amount Chef will spend to buy
 'a' pens and 'b' pencils.

INPUT:
First-line will contain 4 space separated integers a, b, x and y respectively.

Output:
Print the answer in a new line.

Constraints:
1 ≤ a, b, x, y ≤ 10^3

Sample Input 1:
2 4 4 5

Sample Output 1:
28

Sample Input 2:
1 1 4 8

Sample Output 2:
12

Explanation:
 - In the first example, total cost is (2 * 4 + 4 * 5) = 28.
 - In the second example, total cost is (1 * 4 + 1 * 8) = 12.
'''

#NOTE: Please do not copy and paste, kindly try to understand and apply on your own.

#Solution

#use try and except as without them you might get EOF (End of file) error
try:
    #using input().split() to split the total input string into a list of multiple strings containing the individual numbers
    # Applying map(int, input().split()) to convert every individual strings into integers
    # Realloting the integers into respective variables
    no_of_pens, no_of_pencils, cost_per_pen, cost_per_pencil = list(map(int, input().split()))

    #calculating the total amount
    total_amount_spent = no_of_pens*cost_per_pen + no_of_pencils*cost_per_pencil

    #printing the desired output
    print(total_amount_spent)
except:
    pass

