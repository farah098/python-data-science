# to represent binaries in python 
# we use 0b
# why we use 0b
# so that computer reads one one one zero zero one zer zero one
# instead of reading 1 hundred and one
# because one zero one is equals to RM5 not RM101

givenbinary = 0b101
filepermission = 0b111101001
print(f"Auto conversion binary to decimal: {filepermission}") #auto convert binary to decimal and print it
print(f"Output binary: {bin(filepermission)}")
number = 97409
print(f"Decimal to binary: {bin(number)}")

# filepermission holds a binary number and i am interested
# only in some bits not all
# for example i am interested only in permission belongs to the group
# which means i am interested in 4,5 and 6 bits only
# Feature Engineering
mask = 0b000111000
# original  111101001  &
# mask      000111000
# result    000101000
# the & operator is used for extracting the bits we are
# interested
# let us shift to left 3 times (000101000 -> 000000101)
# result            000000101  >> 3

print(f"Extract: {bin((filepermission & mask) >> 3)}")

# i want to set 3,5,6 bits to 1
# the other bits remain as it is then we use or operator
# original  111010101  |
# mask      000111000
# result    111111101

filepermission = 0b111101001
mask = 0b000111000
print(f"Setting: {bin(filepermission | mask)}")
# using or operator you cannot set the bits to 0

# xor operator

content = 0b10101010
key = 0b00111100
# i am going to encrypty J using s
# To decrypt you must know s
encryptedcontent = content ^ key
print(f"encryptedcontent: {bin(encryptedcontent)}")
decryptedcontent = encryptedcontent ^ key
print(f"decryptedcontent: {bin(decryptedcontent)}")

#1st complement = flip the bits from 1 to 0 or 0 to 1
givennumber = 5 #101
print(bin(~givennumber)) # 1  10 -6
print(~givennumber)
# get the 1s compliment and add 1
print(bin(~givennumber +1 ))
print(~givennumber+1)

print(-givennumber) # unary negative
print(+givennumber) # unary positive


#0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, A, B, C, D, E, F, 10, 11, 12, 13, 
#0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

hexadecimalnumber = 0xF
print(hexadecimalnumber)
print(hex(hexadecimalnumber))

#0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20 
#0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16

octalnumber = 0o10
print(octalnumber)
print(oct(octalnumber))

