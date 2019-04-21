#Developer: Dat Nguyen
#04/10/2019

import sys
from sys import argv



def recur (bucket, target, count):
	bucket = listsimplifier(bucket)
	#if there is no bucket initially
	if len(bucket) == 0:
		if target[0] == 0: return True
		else: return False
	#if recursion depth exceed 100 then return false
	if count > 100: return False
	#if there is only one bucket
	if len (bucket) == 1:
		for i in target:
			if i % bucket[0] != 0 or i * bucket[0] <= 0: return False 
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
	while 0 in mylist: mylist.remove(0)
	#exclude any same-sign multiple of all elements
	if len(mylist) != 0:
		i = 0
		while i < len(mylist)-1:
			j = i + 1
			while j <= len (mylist)-1:
				if (mylist[j] % mylist [i] == 0 and mylist[j] * mylist[i] > 0): 
					del mylist [j]
				else: j = j + 1
			i = i +1
	return mylist


#main 
script =  argv[0]
target = list(map(int, argv[1:2]))
bucket = list(map(int,argv[2:]))
if target[0] < 0:
	target = [-x for x in target]
	bucket = [-x for x in bucket]
print (recur (bucket, target, 0))