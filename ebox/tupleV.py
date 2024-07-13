'''
t = tuple()
t = ()
'''

l = [1,2,3,4]
t = tuple(l)
print(t)
print(type(t)) # tuple class

t = (1,2,3,[123,45,678],"hi","farah",[12.3,144],34,"jk",(13,244,(123,44,2)))
print(len(t))
print(t[9][2][0]) # 123

l = [1,2,3,4]
t[2] = "three"
print(t)

t = (1,2,3,[123,45,678],(123,445))