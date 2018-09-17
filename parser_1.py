##opening initial input data for reading
data = open("mxm_dataset_train.txt", 'r')
#opening line.txt for writing breaking input by commas and writing in lines
fo = open("Line.txt",'w')
#the entire corpuse is broken into lines with delimeter as ,
class Parser:
    for aline in data:
        line = data.readline()
        line = line.strip()
        strlist = aline.split(',')
        l = len(strlist)

        for j in range(l):
            fo.write(strlist[j]+"\n")

    data.close()
    fo.close()
