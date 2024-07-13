# from os.path import exists


# f = open("sample.txt", "w+")

# rl = ["100\n","20\n","45\n","30\n"]
# f.writelines(rl)


# x = f.readlines()
# print(x)

# with open("sample.txt","r+") as f:
#     rl = ["100\n","20\n","45\n","30\n"]
#     f.writelines(rl)

with open("sample.txt") as f:
    x = f.readlines()
    print(x)
# ['100\n', '20\n', '45\n', '30\n', '019539000']

    # x = f.read()
    # print(x)
# 100
# 20
# 45
# 30
# 01953900

    sum = 0
    
    for line in f:
        y = int(line)
        sum += y
    print("sum =",sum)

with open("sample.txt","a+") as f:
    sum = str(sum)
    f.write(sum)
