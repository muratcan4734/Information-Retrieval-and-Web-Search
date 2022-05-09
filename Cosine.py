import sys
import os
import math

if(len(sys.argv) !=3):
    raise ValueError('Enter three arguments')

#defining folder paths   
input_folder_path=sys.argv[1]
output_folder_path=sys.argv[2]

#arrays to hold document values
doc1_freq=[]
doc2_freq=[]
doc3_freq=[]

#cosine similarity function
def Cos_Sim(v1,v2):
    dot_prod = sum(n1 * n2 for n1, n2 in zip(v1, v2))
    vector1 = math.sqrt(sum(n**2 for n in v1))
    vector2 = math.sqrt(sum(n**2 for n in v2))
    cross_prod = vector1*vector2
    return (dot_prod/cross_prod)

for filename in os.listdir(input_folder_path):
    #file read
    f=open(os.path.join(input_folder_path, filename),'r')
    content=f.read()
    
    #removal of junk chararcters
    single_array=content.splitlines(True)
    # print(single_array)
    new_array=[x[:-1] for x in single_array]
    # print(new_array)
    total_items=len(new_array)
    for i in range(total_items):
        items_array=new_array[i].split("\t")
        # print(items_array[1])
        doc1_freq.append(items_array[1])
        doc2_freq.append(items_array[2])
        doc3_freq.append(items_array[3])

#Converting string to float for frequencies
doc1_freq=[float(a) for a in doc1_freq]
doc2_freq=[float(a) for a in doc2_freq]
doc3_freq=[float(a) for a in doc3_freq]

#Cosine similarity between the documents
#cosine simlarity between doc1 and doc2
CoSim_d1_d2="The cosine similarity between doc1 and doc2: "+str(Cos_Sim(doc1_freq,doc2_freq))
print(CoSim_d1_d2)

#cosine simlarity between doc2 and doc3
CoSim_d2_d3="The cosine similarity between doc2 and doc3: "+str(Cos_Sim(doc2_freq,doc3_freq))
print(CoSim_d2_d3)

#cosine simlarity between doc1 and doc3
CoSim_d1_d3="The cosine similarity between doc1 and doc3: "+str(Cos_Sim(doc1_freq,doc3_freq))
print(CoSim_d1_d3)

#Path to output
f=open(os.path.join(output_folder_path,'Cosine_similarity_results.txt'),'w+')

# #file write
f.write("%s\n%s\n%s\n" % (CoSim_d1_d2, CoSim_d2_d3, CoSim_d1_d3))  
f.close()









