words = [
			['circle', 'Juan', 'tooth', 'tree', 'floor', 'pen', 'stick', 'Steven', 'date', 'knight'], 
			["isn't", 'is', 'do', 'try', 'for', 'fight', 'seeked', 'evened', 'ate', 'lined'], 
			['empty', 'lonely', 'paired', 'free', 'flase', 'fine', 'sick', 'even', 'late', 'denied']]

try:
	val = int(input ("please enter a sequence of number: "))
except ValueError: 
	print ("input format error!")
	exit()

number = list(map(int,str (val)))
count = 0
print ('-'*12)
print ("Hope the 'sentence' below helps: ")
for i in number:
	print (words[count % 3][i], end = " ")
	count = count + 1
	if count == len (number)-1 and count % 3 == 2: count = count + 1
