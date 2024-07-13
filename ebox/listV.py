# Basic in list
l = [1,2,3,[123,45,678],"hi","farah",[12.3,144,34,"jk",[13,244]]]

print(l[4])# hi
print(l[3][2]) #678
#########################################################3

# .insert()
# .append()
# .extend()
l = [1,2,3,4]
l.insert(2,4.5)
print(l) # [1, 2, 4.5, 3, 4]

l = [1,2,3,4]
l.append([7,8,9])
print(l) # [1, 2, 3, 4, [7, 8, 9]]

l = [1,2,3,4]
l.extend([7,8,9])
print(l) # [1, 2, 3, 4, 7, 8, 9]

l = [1,2,3,4]
for i in l:
    print(i) #  1 2 3 4 all in different line
print(23 in l) # False
print(23 not in l) # True

###################################################################
l1 = [1,2,3]
l2 = [3,4,5]
l2 = l1.copy() # copy l1 and store in variable l2
l = l1 + l2 # tambah all value put in one list
print(l) 
print(id(l1))
print(id(l2))

l1[1] = 'two' # change the value in that particular index
print(l1)
print(l2)

############################################################
# print that value in a list for 100 times
l = []
for i in range(100):
    l.append(0)
print(l)

l = [0] * 100

######################################################
#slicing
l = [1,2,3,4,5,6,7,8,9,10]

print(l[2:6]) # [3, 4, 5, 6]

print(l[::2]) # [1, 3, 5, 7, 9]

print(l[0:10:2]) # [1, 3, 5, 7, 9]


print(l[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(l[-1]) # 10
print(l[-5]) # 6
print(l[-1:-7:-1])
print(l[0:100]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


