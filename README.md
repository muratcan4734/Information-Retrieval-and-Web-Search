This document gives a short brief about the files, scripts and commands to be used to run the scripts.

System requirements:
Operating system - Windows OS(Win 7 to 11)
2GB RAM (4GB preferable)
256Gb HDD/SSD

Language and versions used:
Language: Python
Version: 3.10
IDE: Windows CMD

List of scripts in the folder:
1. Preprocessing.py 
2. InvertedIndex.py
3. TF-IDF.py
4. Cosine.py  
5. IR_Sys.py
6. ProbFuse.py

Libray file:
1. PorterStemmer.py  
2. StopWords.txt

#Instructions to run Preprocessing(Preprocessing.py) of documents:-
1. Add 3 text documents in the input folder. Note that the documents must be in .txt format. 
1. Open CMD and direct to the folder where the script files are stored (eg: cd "D:\IRWS\")
2. To run the script you need to enter 3 arguments: python Preprocessing.py <infolder> <outfolder> <stopword_list>
eg: python preprocessing.py "D:\IRWS\Input_files" "D:\IRWS\Preprocessed_files" StopWords.txt
3. To add any additional list of stop words, open file "StopWords.txt" and add the words
4. The preprocessed output will be stored in the specified folder

Sample Input
Doc1: This is a sample document, to check if the file read feature works well! -"Test Author"
Doc2: This is another sample document, to test the Stemming Algorithm. Sample document.
Doc3: Yesterday, rain-fog; today, frost-mist. But how fascinating each words in the documents are!

Output
Doc1: sample document check file read feature work test author
Doc2: anoth sample document test stem algorithm sample document
Doc3: yesterdai rainfog todai frostmist fascin word document


#Instructions to run InvertedIndex.py:-
1. Enter the folder path of processed files and the output folder as arguments: python InvertedIndex.py <infolder> <outfolder>
eg: python InvertedIndex.py "D:\IRWS\Preprocessed_files" "D:\IRWS\Invert_indexed_files"
Sample input
Doc1: sample document check file read feature work test author
Doc2: anoth sample document test stem algorithm sample document
Doc3: yesterdai rainfog todai frostmist fascin word document

Output
yesterdai	D1[0]	D2[0]	D3[1]
author	D1[1]	D2[0]	D3[0]
feature	D1[1]	D2[0]	D3[0]
sample	D1[1]	D2[2]	D3[0]
todai	D1[0]	D2[0]	D3[1]
word	D1[0]	D2[0]	D3[1]
document	D1[1]	D2[2]	D3[1]


#Instructions to run TF-IDF.py:-
1. Enter the folder path of invert-indexed files and a separate output folder as arguments: python TF-IDF.py <infolder> <outfolder>
eg: python TF-IDF.py "D:\IRWS\Invert_indexed_files" "D:\IRWS\TF_IDF_files"
Sample input
yesterdai	D1[0]	D2[0]	D3[1]
author	D1[1]	D2[0]	D3[0]
feature	D1[1]	D2[0]	D3[0]
sample	D1[1]	D2[2]	D3[0]
todai	D1[0]	D2[0]	D3[1]
word	D1[0]	D2[0]	D3[1]
document	D1[1]	D2[2]	D3[1]

Output:
yesterdai	0.0	0.0	0.477
author	0.477	0.0	0.0
feature	0.477	0.0	0.0
sample	0.176	0.176	0.0
todai	0.0	0.0	0.477
word	0.0	0.0	0.477
document	0.0	0.0	0.0

#Instructions to run cosine similarity script Cosine.py:-
1. Enter the folder path of invert-indexed files and a separate output folder as arguments: python Cosine.py <infolder> <outfolder>
eg: python Cosine.py "D:\IRWS\TF_IDF_files" "D:\IRWS\Cosine_Similarity_files"
Sample input
yesterdai	0.0	0.0	0.477
author	0.477	0.0	0.0
feature	0.477	0.0	0.0
sample	0.176	0.176	0.0
todai	0.0	0.0	0.477
word	0.0	0.0	0.477
document	0.0	0.0	0.0

Output:
The cosine similarity between doc1 and doc2: 0.08485745064821397
The cosine similarity between doc2 and doc3: 0.0
The cosine similarity between doc1 and doc3: 0.0

#Instructions to run IR system script IR_Sys.py:-
1. Enter the folder path of input file, a separate output folder, stopwords list file and, the query words within double inverted commas as arguments: python IR_Sys.py <infolder> <outfolder> <stopwords-list> "Query words"
eg: python IR_Sys.py "D:\IRWS\Input_files" "D:\IRWS\IR_results" "StopWords.txt" "Sample, Document!"

Sample Input
Doc1: This is a sample document, to check if the file read feature works well! -"Test Author"
Doc2: This is another sample document, to test the Stemming Algorithm. Sample document.
Doc3: Yesterday, rain-fog; today, frost-mist. But how fascinating each words in the documents are!

Output:
The similarity for query words in document 1: 0.14732671611824286
The similarity for query words in document 2: 0.1919938055229311
The similarity for query words in document 3: 0.0

#Instructions to run Fusion script i.e., Probfuse.py:-
1. Enter the command "python Probfuse.py"
2. Make sure the historic data and live data file are saved in the same folder.
3. Enter the correct input for questions asked (ensure correct formatting is followed)
4. The final output will be stored in the file: Fusion_results.txt