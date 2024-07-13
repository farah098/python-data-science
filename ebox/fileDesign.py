inputfile = open("input.txt", "rt")
content = inputfile.readline()

outputfile = open("output.txt", "wt")
reversed_cont = content[::-1]
outcontent = outputfile.write(reversed_cont)

