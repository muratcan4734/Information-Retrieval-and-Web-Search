import sys
import os
import math

if(len(sys.argv) !=3):
    raise ValueError('Enter three arguments')

#defining folder paths   
input_folder_path=sys.argv[1]
output_folder_path=sys.argv[2]

#Arrays to store values
freq_doc1=[]
freq_doc2=[]
freq_doc3=[]
TF_doc1=[]
TF_doc2=[]
TF_doc3=[]
Terms_list=[]


for filename in os.listdir(input_folder_path):
    #file read
    f=open(os.path.join(input_folder_path, filename),'r')
    content=f.read()

    chars_row=content.splitlines(True)
    newtest = [x[:-1] for x in chars_row]
    total_count=len(newtest)
    print("The total items in array newtest: "+str(total_count))

    for i in range(total_count):
        split_chars_row=newtest[i].split("\t")
        Terms_list.append(split_chars_row[0])
        # print(split_chars_row[1])
        # print(split_chars_row[2])
        # print(split_chars_row[3])
        freq_doc1.append((split_chars_row[1])[-2])
        freq_doc2.append((split_chars_row[2])[-2])
        freq_doc3.append((split_chars_row[3])[-2])

    print(Terms_list)
    

#Converting string to int
freq_doc1=[int(a) for a in freq_doc1]
freq_doc2=[int(a) for a in freq_doc2]
freq_doc3=[int(a) for a in freq_doc3]

#TF code here
for j in freq_doc1:
    TF_doc1.append(j/max(freq_doc1))
TF_doc1=[float(a) for a in TF_doc1]
print("Term frequency in Doc1: ")
print(TF_doc1)

for k in freq_doc2:
    TF_doc2.append(k/max(freq_doc2))
TF_doc2=[float(a) for a in TF_doc2]
print("Term frequency in Doc2: ")
print(TF_doc2)

for l in freq_doc3:
    TF_doc3.append(l/max(freq_doc3))
TF_doc3=[float(a) for a in TF_doc3]
print("Term frequency in Doc3: ")
print(TF_doc3)

#Path to output
f=open(os.path.join(output_folder_path,'TF_IDF_results.txt'),'w')

#IDF code here
for n in range(len(freq_doc1)):
    count=0
    if freq_doc1[n]>0:
        count+=1
    if freq_doc2[n]>0:
        count+=1
    if freq_doc3[n]>0:
        count+=1
    # print("Count of valid documents for term {number}: ".format(number=n+1) + str(count))
    no_of_docs =3

    # print("The IDF for term {number}: ".format(number=n+1) + str(math.log10(no_of_docs/count)))
    

    print(TF_doc1[n]*math.log10(no_of_docs/count))
    print(TF_doc2[n]*math.log10(no_of_docs/count))
    print(TF_doc3[n]*math.log10(no_of_docs/count))
    print(len(freq_doc1))

    #File writer code here      
    TF_IDF_Output=("{terms}\t{TFIDF_1}\t{TFIDF_2}\t{TFIDF_3}\n".format(terms=Terms_list[n], TFIDF_1=round(TF_doc1[n]*math.log10(no_of_docs/count),3), TFIDF_2=round(TF_doc2[n]*math.log10(no_of_docs/count),3), TFIDF_3=round(TF_doc3[n]*math.log10(no_of_docs/count),3)))
    
    #file write
    f.write(TF_IDF_Output)    
f.close()


    