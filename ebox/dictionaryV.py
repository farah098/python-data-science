'''
d = {}
d = dict()
'''

d = {
    'name' : 'JK',
    'age' : 25,
    'rollNo' : 12345,
    'weight' : 80.6,
    'subject': ['Maths','Science'],
    'address': {'DNo': 456,'sname':"12 across", 'city': 'cbe', 'Pincode':'72822'},
}
print(d) # print dictionary
print(d['name']) # JK
print(d['address']['city']) # cbe
print(d['subject'][1]) # Science

########################################
# new entry
d['height'] = '5.7'
print(d)

########################################
# delete
# pop() -randomly
del d['weight'] # delete weight from the dictionary
print(d) 
del d

##################################################

d = {
    1: 'int', 
    2.4: 'float',
    (12,32):'tuple',
    'name':'str',
    2+3j :'complex'}

print(d)

############################################
d = {12:'que',123:'ert',3214:'dsf'}
# print one by one 
for i in d:
    print(i,d[i],sep=('-'))

print("\nPrint Sorted")
# sort the value 
for i in sorted(d):
    print(i,d[i],sep=',')
print

# d.pop(12)
# print(d)
d[12] = [d[12]]
print(d)
d[12].append('abc')
print(d)

