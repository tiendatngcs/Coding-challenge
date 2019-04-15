#Developer: Dat Nguyen
#04/10/2019

import sys
from sys import argv



def recur (bucket, target, count):
	#if recursion depth exceed 100 then return false
	if count > 100: return False
	#if there is only one bucket
	bucket = listsimplifier(bucket)
	if len (bucket) == 1:
		for i in target:
			if i % bucket[0] != 0: return False 
	#for every element in bucket if any of them is divisible to target then return true
	for i in target:
		for j in bucket:
			if i % j == 0:
				return True
	#if nothing is returned, create new target
	newtarget = []
	for i in range (len(target)): #for each value in target
		#subtract it with each element of bucket
		for j in range (len(bucket)):
			diff = target[i]-bucket[j] 
			if diff not in newtarget and diff > 0: newtarget.append(diff)
	if len(newtarget) == 0: return False
	else: return recur (bucket, newtarget, count + 1)

def listsimplifier (mylist):
	mylist.sort()
	#exclude any multiple of all elements
	i = 0
	while i < len(mylist)-1:
		j = i + 1
		while j <= len (mylist)-1:
			if mylist[j] % mylist [i] == 0: 
				del mylist [j]
			else: j = j + 1
		i = i +1
	return mylist


#main 
script =  argv[0]
target = list(map(int, argv[1:2]))
bucket = list(map(int,argv[2:]))
#find smallest value in bucket
print (recur (bucket, target, 0))