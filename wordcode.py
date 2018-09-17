###this code collects all the words of the corpus and puts it into a dictionary format in wcode.pkl file
##It also assigns them a id

import pickle

f = open("Line.txt", 'r')

i=1
wordcode = {}

for line in f:
    if(line == '\n'):
        break;
    line = line.strip()
    wordcode[str(i)] = line
    i+=1
    
print(wordcode)
f.close()

output = open("wcode.pkl", 'wb')

pickle.dump(wordcode, output)

output.close()
