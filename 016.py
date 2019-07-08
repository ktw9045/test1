fr = open('test.txt','r')
lines=fr.readlines()
for i in lines:
    print(i)
fr.close()

with open('test.txt','r') as fr:
    for line in fr:
        print(line.strip())
