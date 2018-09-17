import pickle
#json
#import pprint

file = open("Line.txt", 'r')
file2 = open("mxm_dataset_train.txt", 'r')

class Array:
    arr = []
    for lin in file2:
        strline = lin.split(",")
        length = len(strline) - 2
        arr.append(length)
    #print(arr)

    dict = {}
    doc = ""
    a = 0.0
    pkl_file = open('wcode.pkl', 'rb')
    wordcode = pickle.load(pkl_file)
    i = 0
    for line in file:
        if(line == "\n"):
            i+=1
            doc = file.readline()
            weird = file.readline()
        if(':' in line):
            code = line.split(":")
            #taking care of any extra words in the docs?
            if(wordcode[code[0]] not in dict):
                dict[wordcode[code[0]]] = []
            a = (float((code[1])))/arr[i]
            dict[wordcode[code[0]]].append([doc,a])
            
    #print(dict['road'][0][1])

    output = open("inverted_index.pkl", 'wb')

    pickle.dump(dict, output)

    output.close()

    file.close()


