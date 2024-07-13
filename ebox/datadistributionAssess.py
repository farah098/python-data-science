#Q1
'''
Finding Statistics

Ramesh, the businessman had a list of data containing the overall transactions in a year. He wanted to calculate the statistics of his transactions i.e. calculating mean, median, and variance of his transactions to keep the track of his business growth over the years.

Let's help Ramesh to calculate the mean, median and variance of the list of transactions given by writing code according to his requirements.

Input format:

Input consists of an array containing the overall transactions done in a year.

Output Format:

The output displays the mean, median and standard deviation of the transactions.


Refer the sample Input and Output for formatting specifications

Sample Input and Output:

Enter the transactions done in each month for last year

4545
232
5565
1232
4512
-7878
-9698
-7785
6624
-5757
7597
-774848

Mean : -64638.25
Median : 732.00
Standard Deviation : 214218.97

 '''
def calculate_mean(transactions):
    return sum(transactions) / len(transactions)

def calculate_median(transactions):
    transactions.sort()
    n = len(transactions)
    if n % 2 == 0:
        median = (transactions[n//2 - 1] + transactions[n//2]) / 2
    else:
        median = transactions[n//2]
    return median

def calculate_variance(transactions, mean):
    return sum((x - mean) ** 2 for x in transactions) / len(transactions)

def calculate_standard_deviation(variance):
    return variance ** 0.5

def calculation():
    print("Enter the transactions done in each month for last year")
    transactions = []
    for _ in range(12):
        transaction = float(input())
        transactions.append(transaction)

    if len(transactions) == 0:
        print("No transactions provided.")
        return

    mean = calculate_mean(transactions)
    median = calculate_median(transactions)
    variance = calculate_variance(transactions, mean)
    std_dev = calculate_standard_deviation(variance)

    print(f"Mean : {round(mean, 2):.2f}")
    print(f"Median : {round(median, 2):.2f}")
    print(f"Standard Deviation : {round(std_dev, 2):.2f}")

calculation()



#Q2
'''
Maximum and Minimum Turnovers
 
Ramesh is self-employed. it's been years after setting his business. With all the hardships he brought his business into the track. He got a thought to analyze his graph of progress from last year to the current year.  
He has a list of data containing the transactions done per month in a year, he wanted to calculate the turnovers of the month and which month had the Maximum turnover and which month had the minimum turnover.

But unaware of any software he had to do it manually which was tedious work.  He asks Suresh, a Software Engineer to help him in this. Fortunately, Suresh was working on data science and thought he could easily help him. 
Assume yourself to be in Suresh's position and had to help Ramesh in tracking his growth from last year to current year. Given the data set of calculate the turnovers of the month and which month had the Maximum turnover and which month had the minimum turnover.

Note: All positive values in the transactions are considered as the "Income" and All negative values are considered as "Investment".

Input Format:
Input consists of an array indicating the transactions done over the year.

Output Format:
The Output displays the months having the maximum turnover and the minimum turnover.

Refer sample input and output for formatting specifications.

Sample Input and Output: 

Enter the transaction done last year
10000
7898
7878
787878
787878
777
777878
77777
-5656556
45454
45455
4545454
Minimum Turnover : -5656556
Maximum Turnover : 4545454
Minimum Turnover Month : 8
Maximum Turnover Month : 11'''

print("Enter the transaction done last year")
transactions = []
for _ in range(12):
    transaction = float(input())
    transactions.append(transaction)
        
min_turnover = float('inf')
max_turnover = float('-inf')
min_turnover_month = 0
max_turnover_month = 0

for i in range(len(transactions)):
    if transactions[i] < min_turnover:
        min_turnover = transactions[i]
        min_turnover_month = i + 1
    if transactions[i] > max_turnover:
        max_turnover = transactions[i]
        max_turnover_month = i + 1

print("Minimum Turnover :", int(min_turnover))
print("Maximum Turnover :", int(max_turnover))
print("Minimum Turnover Month :", min_turnover_month - 1)
print("Maximum Turnover Month :", max_turnover_month - 1)