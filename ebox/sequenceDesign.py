# word = input()   
# word =  ''.join([char for char in word if char.isalpha()])
# # word = word.lower()
# # filtered_s = ''.join([char for char in s if char.isalpha()])
# # word = word.lower().replace(' ','').replace('!','')
# # first = word[0]
# # second = word[1]

# last = word[-1]
# sec_last = word[-2]

# first = word[::-1]
# word = word.replace(last,first)
# word = word.replace(sec_last,second)

# for i in word:
#     print(i,end="")

# word = list(instring)
# print(word)
# print(last)
# last= first.copy() # no copy() function for str 
# only have copy module  that need to import
# print(first)
# word[-1] = first #  string does not cannot have assignment 

#Q1

############################################
#Q9
def getsecond_highest(marks):
    unique_mark = list(set(marks))
    unique_mark.sort()

    if len(unique_mark) == 1:
        return unique_mark[0]
    else:
        return unique_mark[1]


num_std = int(input())

record = {}

for i in range(num_std):
    data = input().split() # user input split by space
    name = data[0]
    marks = list(map(float ,data[1:]))
    record[name]= marks

std_name = input().strip()

if std_name in record:
    marks = record[std_name]
    second_highest, all_same = getsecond_highest(marks)
    if all_same:
        print(f"{std_name} scored same marks in all subjects: {second_highest}")
    else:
        print(f"Second Highest mark of {std_name}: {second_highest}")
else:
    print("Student doesn't exist")

##################################################################################################3

# Q10

sentence = input()

sentence = sentence.lower()

words = sentence.split()

word_count = {}

for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

print(word_count)



    