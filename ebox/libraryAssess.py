#Q1
'''
Date Decoder I

Madhumitha was working as an Accountant in BINNI mills Pvt Ltd, Coimbatore. She was in charge of crediting salary for all the employees, summarising the current financial status by collecting information, preparing balance sheet, profit, and loss statement, and other reports.

That particular day she was assigned to generate a report that contains the Date of Joining of employees between years 1980 - 2015 in the format (yyyy, MMM,dd). But the date of joining which is available in the present datasheet is in the format DD-MMM-YY. Help her to convert the date of joining of all the employees to (DD, MMM, yyyy) format by writing a program.

Note :
Create a dictionary suitable for decoding month names to numbers.
Months in a dictionary should be in the following format: JAN for January, FEB for February, MAR for March and so on..

Create a  function named date_decoder( ) that takes a date in the "dd-MMM-yy" format as its argument. Translate the month, correct the year to include all of the digits and respond with the format of (yyyy,MMM,dd).

Input format:
Input is a string that contains the date in the format DD-MMM-YY format.

Output format :
The output is the translated form of the input date string in the format (yyyy, MMM, dd) as a tuple.
and display whether the year is a leap year or not

Note: Refer to sample input and output for further formatting specifications.

Sample Input 1 :
85-MAR-19

Sample Output 1 :
 (19, 03, 1985) is not a leap year


Sample Input 2 :
04-DEC-12

Sample Output 2 :
(12, 12, 2004) is a leap year'''

def date_decoder(date_):

   month_dict = {
   "JAN" : "01",  "FEB" : "02",  "MAR" : "03", "APR" : "04",
   "MAY" : "05",  "JUN" : "06",  "JUL" : "07", "AUG" : "08",
   "SEP" : "09",  "OCT" : "10",  "NOV" : "11", "DEC" : "12"
}
   
   year, month_, day = date_.split("-")

   month = month_dict[month_]

   if int(year) >= 0 and int(year) <= 29:
      full_year = 2000 + int(year)
   elif int(year) >= 30 and int(year) <= 99:
      full_year = 1900 + int(year)

   if(full_year % 4 == 0 and full_year % 100 != 0 or full_year % 400 == 0):
      leap_status = "is a leap year"
   else:
      leap_status ="is not a leap year"


   return f"({day}, {month}, {full_year}) {leap_status}"

date_ = input().strip()

print(date_decoder(date_))



#Q2
'''
Different Sum Operations

Suresh playing a numbers game. The game description is  Suresh picks random numbers and calculate the sum of all numbers, and the problem is some times the sum of the numbers will be float value and he wants to modify that sum by using Floor(), Ceil(), Round() functions and finally, he wants to calculate the difference of these 3 functions.
(Gambar kat sini)

Input Format specifications:

Input consists of a list of values separated by space.
Output Format Specifications:

The first line of output should be the difference between floor()sum - ceil()sum.
Secondly of output should be the difference between the ceil()sum - round()sum.
The third line of output should be the difference between floor()sum - round()sum.
Constraints:

Use only floor() and ceil() round() function Python


Sample Input 1:
23.34 12 25

Sample Output 1:
-1.0
1.0
0.0

Sample Input 2:
-21.23 -18.23 -12

Sample Output 2:
-1.0
0.0
-1.0

'''
import math 

def Floor(total):
   return math.floor(total)

def Ceil(total):
   return math.ceil(total)

def Round(total):
   return round(total)

n = input().strip().split()

numbers = []
for number in n:
   numbers.append(float(number))

total = sum(numbers)

floor_n = Floor(total)
ceil_n = Ceil(total)
round_n = Round(total)

print(f"{(floor_n - ceil_n):.1f}")
print(f"{(ceil_n - round_n):.1f}")
print(f"{(floor_n - round_n):.1f}")
