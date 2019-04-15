**Bucket Problem**
Intbucket.py
	A problem-solving program written in Python which determines if the buckets in a given array can reach a given target value
------------
HOW TO RUN THE PROGRAM
On your terminal enter the command: 
python intbucket.py [target value] [buckets]
For example: target value = 14, buckets = [10, 2] 
python intbucket.py 14 10 2
The result for this case should be returned as True
------------
PSEUDOCODE
Step 1: Passing an array of target values (which has initial length of 1) and an array of buckets to a recursion function 
Step 2: Simplify the bucket by excluding any multiple any other elements in the array
Step 3: If there is only one bucket, check if any of the target values is divisible by the bucket. Return False and exit the program if it is not
Step 4: For each target value, see if it is divisible by each bucket. If any, return True and exit the program.
Step 5: When your program reaches this step, we acknowledge that there is more than one bucket value.  Return true if any of them are indivisible to any of the target values 
	We create an array (list) of new target which is the difference of each target to each bucket. We exclude any duplicate and negative value in the array.
Step 6: if there is no new target, return False and exit the program, else go to step 1 with a new array of target.
-----------------
WHY DOES THIS SOLUTION WORK?
The size of the bucket array was undefined initially. Therefore, this problem must be solve using some form of loop or recursion. First we exclude all the multiples of all other elements in the bucket list since those values can be constructed with existed buckets. 
Example: Target = [12], Bucketlist = [3, 6]. We can exclude number 6 since they can be expressed as 3+3. For 12 = 3 + 3 + 6 = 3 + 3 + (3 + 3).
With a simplified array of bucket, if there is only one bucket, we can jump straight to the conclusion by examing if any target value is divisible by the bucket.
For example: Target = [12], bucketlist = [5] then return False. Otherwise, forward to the next step
 When there are multiple buckets, conduct a new array of target which are the difference of each previous target values and each bucket. We exclude all duplicate or negative value in the list.
This the values in the list will get smaller until they become negative and be excluded from the list, which will eventually make the list smaller in size as well. Therefore this loop is finite. 
