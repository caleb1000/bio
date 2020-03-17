
import sys

print('number of args: ', len(sys.argv), 'arguments')
print('Argument list', str(sys.argv))
import random
n =int(sys.argv[1])
a =int(sys.argv[2])
c =int(sys.argv[3])
g =int(sys.argv[4])
t =int(sys.argv[5])
k =int(sys.argv[6])
p =float(sys.argv[7])
s =int(a+g+c+t)

aprob = float(a/s)
gprob = float(g/s)
cprob = float(c/s)
tprob = float(t/s)

fname =sys.argv[8]

fname=fname+".txt"

f=open(fname, 'w')

#start of loop
seq = str(random.choices(
            population=['A', 'G', 'C','T'],
               weights=[aprob, gprob, cprob, tprob],
               k=n
               ))

seq=(seq.replace("[",''))
seq=(seq.replace(" ",''))
seq=(seq.replace("'",''))
seq=(seq.replace(",",''))
seq=(seq.replace("]",''))


index = 1
f.write(str(">Sequence ") + str(index) + "\n")
f.write(str(seq)+"\n")
listSeq = list(seq)

while index < k:
    index= index+1
    f.write(str(">Sequence ") + str(index)+ "\n")
    x = int(0)
    listTemp = list(listSeq)
    while x < len(listTemp):
            mutate = 'T' if random.random() < p else 'F'
            if mutate == 'T':
                mutation = random.randint(1, 5)
                if mutation == 1:
                    listTemp[x]= ''

                if mutation == 2:
                    listTemp[x] = 'A'

                if mutation == 3:
                    listTemp[x] = 'T'

                if mutation == 4:
                    listTemp[x] = 'G'

                if mutation == 5:
                    listTemp[x] = 'C'
            x = x + 1
    str1 = ''.join(listTemp)
    f.write(str(str1) + "\n")

f.close()