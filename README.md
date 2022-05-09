# Information-Retrieval-and-Web-Search


In this project, I will give information about my learning. First of all, I started by drafting the project task. I investigated how the logic of Task 1 would work. For this, we did a research on our lecture notes and the internet. I have implemented 3 documents for which we prepared the Preprocessing steps in Task 1. In the beginning.I used ready-made libraries for stop word and stemming, but then we created a new class with the information I got from our classmates, I used the link for stemming in the project and I created this class stemming by Porter’s Algorithm. Thus, my document data was in a state of inverted indexing. 



For the Inverted index, I calculated how many times each unique term appeared in the document. I printed these values in a string format as output document e.g. 
term1  D1[x] D2[y]  Here we separated each value with TAB character to read later. After calculating the inverted index value of each term, I used these values for TF and IDF.



Term frequency (TF) means how often a term occurs in a document. Term frequency is divided by the total number of terms in the document then we used these values in cosine similarity.
Inverse Document Frequency (IDF) is calculated by dividing the number of documents by the number of documents in which the relevant word occurs. Then the IDF is found by taking the logarithm of this value.



Cosine Similarity is the relationship of two vectors with respect to each other is expressed by an angle. Two vectors that are exactly the same, the cosine value will be 1 ( cos(0) = 1 ) . For vectors that are completely unrelated, the cosine value will be 0 ( cos(90) = 0. The cosine similarity is described mathematically as the division between the dot product of vectors and the product of  magnitude each vector so we need two vectors, after that we calculated the ratio of the product of the two vectors (dot product) to the product of the lengths of the two vectors.



IR SYSTEM I calculated the weights of TF_IDF for each document, and to find cosine similarity betweena query and a document.
