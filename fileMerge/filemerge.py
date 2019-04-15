from sys import argv

script, file1, file2, file3 = argv

#retieive data from file 1
file =  open (file1)
text = file.read()
data1 = text.split("\n") #split text by end of line
dict1 = {} #python dictionary, works similar to map in other languages
key = set() #set of key

for i in data1: #for every line in file 1
	x = i.split (" ", 1) #split key (id) with the data by the first blankspace encountered
	if x[0] not in key: key.add(x[0]) #add the key to key set
	dict1[x[0]] = x[1] #add key and data to the dictionary
file.close()


file = open (file2)
output = open (file3, 'w+')
text = file.read()

data2 = text.split("\n")

dict2 = {}
for i in data2:
	x = i.split (" ", 1)
	dict2[x[0]] = x[1] #add key and data to the dictionary 
	#if this key exists in key list, print out the key and the corresponding data of both dictionary one and two
	if x[0] in key: output.write (x[0] + " " +  dict1[x[0]] + " " + dict2[x[0]] + '\n') 
file.close()
output.close()
