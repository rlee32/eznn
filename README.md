#eznn

Easy (ez) neural network (nn). Intended to be a quick tool to see if neural 
networks are right for you, by allowing you to easily try it on your dataset.  

## Introduction

This is a modified, hopefully easier-to-use version of the Python code that 
can be found on:  
https://github.com/mnielsen/neural-networks-and-deep-learning/blob/master/src  

The feature vectors are obtained from the .dat files in a specified folder, 
where each .dat file represents a single instance.

## Usage

The user-friendliness of the program is still being improved. Will be ready 
soon!

## Input Representation

The first row is the space-delimited input vector.
The second row is the space-delimited output vector.
All values must be in [0, 1].


You can store each feature vector and corresponding result in a single 
.dat file. For example, if the feature vector is [1, 2, 3] and the result is 
[0.1, 0.2], then the file will be:  
  
1  
2  
3  
0.1  
0.2  
  
You can have line breaks anywhere and use '#' for comments. For example, this 
is also valid:  
  
\# Some comment  
\# and description  
1  
2  
3  
  
0.1  
0.2  
  
If you store all files in a single folder, you can specify the folder path and 
eznn will read all .dat files in the folder.  

## Scaling

The feature data must be scaled first to [0,1]. The results must also be scaled 
to [0,1]. This is handled in the feature_scaling.dat and result_scaling.dat 
files. They both are specified as follows:

\<start_index\>, \<end_index\>, \<start_value\>, \<end_value\>

So the following specification:  

0, 4, -1, 1  
5, 10, -2, 5  

means starting from index 0 and ending at index 4, we expect values to be 
between -1 and 1. 
The program will scale appropriately so that [-1,1] becomes [0,1]. 
Then starting from index 5, we scale so that [-2, 5] becomes [0,1]. 
Hopefully this is clear. 
