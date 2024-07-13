name = "david "
batch = 101
fee= 13732.438831

#traditionally how we do this:
inputstring = "Hello" + name + "welcome to python class" + str(batch)


#special string called f string 
inputstring = f"Hello {name}, welcome to python class {batch}"
print(inputstring)

#
inputstring = f"Hello {name:40}, welcome to python class {batch}"
print(inputstring)

#align David to center 
inputstring = f"Hello {name:^40}, welcome to python class {batch}"
print(inputstring)

#align David to right
inputstring = f"Hello {name:>40}, welcome to python class {batch}"
print(inputstring)

#can also provide padding characters
inputstring = f"Hello {name:*>40}, welcome to python class {batch}"
print(inputstring)

#Trucate to 3 characters
inputstring = f"Hello {name:.3}, welcome to python class {batch}"
print(inputstring)

#Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:10d} in KL"
print(inputstring)

#Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:<10d} in KL"
print(inputstring)

#Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:<10d} in KL for RM{fee:10.2f}"
print(inputstring)

#Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:b} in KL for RM{fee:,}"
print(inputstring)

#Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:o} in KL for RM{fee:.2f}"
print(inputstring)

#Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:x} in KL for RM{fee:,}"
print(inputstring)