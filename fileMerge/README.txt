File Merger
filemerge.py
Given two files, each contains lines of information consist of an identifier (key) followed by a space-delimited field. This program creates an output file contain the merged lines of both field that has the same identifier in those two files
Example: 
File 1: 
ab1 Dat Nguyen
cgv John Smith 
ath Thomas Mays
File 2:
ath Morgan Johnsons
ab1 Jane Karia
erh Paul Ruths
Output:
ath Thomas Mays Morgan Johnsons
ab1 Dat Nguyen Jane Karia
------------------------
HOW TO RUN THE PROGRAM
In the terminal, enter the following command:
python filemerge.py [file1name].txt [file2name].txt [outputfilename].txt
Example: python filemerge.py file1.txt file2.txt output.txt
------------------------
PSEUDOCODE
Step 1: Retrieve information from file 1 and store them in the map data structure X where the keys are the identifiers and the values are the following string field after the key.
Step 2: Store all identifier of file 1 in a set A (or an array)
Step 3: Retrieve information from file 2 and store them in another map data structure Y where keys are the identifier  and the values are the following string field after the key
Step 4: For each identifier in file 2, if it exists in set A then write the identifier and their values in map X and Y to the output file.
Step 5: Close all files and exit the program
--------------------------
HOW EFFICIENT IS THIS PROGRAM?
We use a Python dynamic data structure called 'set' instead of an array to store all the identifiers in file 1 since checking if an identifier in file 2 exists in the set would yield an average time-complexity of O(1). In the case of an array, it would be O(n). 
Also, getting the values from the map using an existed key also take O(1). 
------------------------
PROS AND CONS
Pro: 
- Simple to code in Python since this language supports ‘x in set’ which check if an element x exists in a set with average time complexity of O(1).
Cons:
- Would confront scalability problems if implemented with other programing languages like C++ since iterating through an array to check for existence would take O(n).
- Might encounter exception if the field following the identifier is empty. 
-------------------------------
DIFFERENT APPROACH
Step 1: Identifier in both files will be stored in two arrays, A and B. Those arrays will be sorted base on alphabetical order. Store the fields in two files in two maps with keys as their identifiers.
Step 2: Initiate two indexes, a and b, each for every array.
Step 3: if a >= length (A) or b >= length(B) go to step 5
Step 4: Compare A[a] and B[b], if A[a] < B[b] then a++ and back to step 3. Else, if A[a] > B[b] then b++ and back to Step 3. Else, write A[a] and the fields in file 1 and 2, increase a and b then back to step 3.
Step 5: close the files and exit the program.
