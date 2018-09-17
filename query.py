from user1 import normalize

query=input()
normalize.TRF(query)
Ans=normalize.cosine(query)
file2 = open("out.txt", 'w')
try:
    Ans = reversed(Ans)
    

    ctr=0;
    j = 0
    with open('outtmp.txt','w') as file1:
        file1.write('\n'.join('%s %s' % x for x in Ans))
        
    file1.close()

    strline = []
    file1 = open("outtmp.txt",'r')
    

    for line in file1:
        strline = line.split(' ')
        file2.write(str(strline[0]) + '\n')
        
     
except:
    file2.write("No result found")
    
file2.close()
