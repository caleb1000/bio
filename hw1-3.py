import sys
print('number of args: ', len(sys.argv), 'arguments')
print('Argument list', str(sys.argv))
fname = str(sys.argv[1])
s = int(sys.argv[2])
r = int(sys.argv[3])
d = int(sys.argv[4])
f = open(fname+".txt")
counter = 0
line = f.readline()
split_strings = str()
#split_strings will contain all the subsequences on a new line
while line:

    if line[0] == ">":
        line = f.readline()
    temp = str(line)
    split_strings+=line
    line = f.readline()
sublist = split_strings.split()



#sublist holds the sub sequences in an easy to iterate list
print(split_strings)



