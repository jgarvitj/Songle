import math as m
import operator
import pickle
from nltk.stem import PorterStemmer
ps = PorterStemmer()
#n is the N in formula idf=log(1+trf)*log(N/dfi), i.e. total number of documents
n=200000
pkl_file = open('inverted_index.pkl', 'rb')
TF={}
IDF={}
WordDict={}
Scores={}
class normalize:
    def TRF(query):
        query=query.strip()
        query=query.split()
        global TF
        global IDF
        global WordDict
        index=0
        output= pickle.load(pkl_file)    
        
        for word in query:
            word = ps.stem(word)
            
            docName=[]
            ctr=0
            trf=[]
            if word in WordDict:
                continue
            if word not in output:
                continue
            WordDict[word]=index
            index+=1
            for i in output[word]:
                for j in i:
                    ctr+=1
                    j=str(j).strip()
                    
                    if (ctr&1)==1:
                        docName.append(j)
                    if (ctr&1)==0:
                        trf.append(float(j))
            TF[word]=[]
            for (i,j) in zip(docName,trf):
                TF[word].append([j,i])
            temp= m.log10(n/len(docName)) 
            IDF[word]=(temp)
        
        return;
        #We now have TF and IDF of each document
        #Assign idf and tf to some global variable or list - cannot return 2 things.

    
    #k=number of results to return
    k=10

    def cosine(query):
        
        #global WordDict
        global TF
        global IDF
        global Scores
        query=query.strip()
        query=query.split(' ')
        
        tfq={}
        idfq={}
        Dq={}
        Dd={}
        for i in query:
            
            i = ps.stem(i)
            print(i)
            if i not in WordDict:#WordDict= Query words in our database
                continue
            if not i in tfq:
                tfq[i]=1
                idfq[i]=IDF[i]
            else:
                tfq[i]+=1
        for i in query:
            i = ps.stem(i)
            if i not in tfq:
                continue
            tfq[i]/=len(query)
        for i in query:
            i = ps.stem(i)
            ctr=0
            if i not in WordDict:
                continue
            for k,j in TF[i]:
                ctr2=0
                if j not in Scores:
                    Scores[j]=IDF[i]*IDF[i]*m.log10(1+k)*m.log10(1+tfq[i])
                    Dq[j]=(IDF[i]*m.log10(1+tfq[i]))**2
                    Dd[j]=(IDF[i]*m.log10(1+k))**2
                else:
                    Scores[j]+=IDF[i]*IDF[i]*m.log10(1+k)*m.log10(1+tfq[i])
                    Dq[j]+=(IDF[i]*m.log10(1+tfq[i]))**2
                    Dd[j]+=(IDF[i]*m.log10(1+k))**2
                ctr2+=1
            ctr+=1
        key=Scores.keys()
        for i in key:
            Scores[i]/=(Dq[i]*Dd[i])**0.5
        sorted_Scores = sorted(Scores.items(), key=operator.itemgetter(1),reverse=False)
        
        length=len(sorted_Scores)
        if length==0:
            print('No Results Found :(')
            return;
        for i in sorted_Scores:
            pass
            
        #Returns top k values in dict of {DocName:Value} sorted by cosine score 
        k=10
        
        sorted_Scores=sorted_Scores[max(0,length-int(k)):]

        return sorted_Scores   
"""
query=input()
TRF(query)
Ans=cosine(query)
Ans = reversed(Ans)
ctr=0;
j = 0
with open('out.txt','w') as file1:
    file1.write('\n'.join('%s %s' % x for x in Ans))
    

file1.close()

with 
"""
