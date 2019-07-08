with open('test.txt','r') as fr:
    with open('test1.txt','w') as fw:
        for i in fr:
            fw.write(i)
