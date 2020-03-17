import sys
import random
print('number of args: ', len(sys.argv), 'arguments')
print('Argument list', str(sys.argv))

fname = str(sys.argv[1])
x = int(sys.argv[2])
y = int(sys.argv[3])
fout = str(sys.argv[4])

f = open(fname+".txt")
f2=open(fout+".txt", 'w')
line = f.readline()
split_strings = []
seqenceNum = 1
while line:

    if line[0] == ">":
        line = f.readline()
        #skip a line if it is a comment
        continue
    length = random.randint(x, y)
    for index in range (0, len(line),length):
        length = random.randint(x, y)
        if(length>=(len(line)-index)):
            continue
        split_strings += str(">Sequence ") + str(seqenceNum)+ "\n"
        split_strings.append(line[index:index+length]+"\n")
        seqenceNum= seqenceNum+1
        length = random.randint(x, y)

    line = f.readline()
str1 = ''.join(split_strings)
f2.write(str(str1))

f.close()