#range concept 
#loops- for loop, while loop, do-while loop

#if-else decision making also constitute flow control
#Flow is particularly necesary in fetching data from containers

print('-------Range() concept-------------')
print(range(10))
rangeOutput = list(range(10))
#take note of range indexing - 0, detault , 10 exclusive
print(rangeOutput)

#Not the list at indx0(lowerRangeLimit[0])
lowerRangeLimit = list(range(2,10))
print(lowerRangeLimit)
print('----------Slicing lists-------')
print(rangeOutput[:])      # takes all elements in the list 
print(rangeOutput[4:])	# Picks elements from index 4 (inclusive) to the last element
print(rangeOutput[:4])  #Picks all elements before index 4 (exclusive)
print(rangeOutput[2:7])# Picks all elements between index 2(inclusive) and index 7 (exclusive) 
#Non-Issue #note the [5,5]- range is meant to sustain indexing 
print([(7-2),len(rangeOutput[2:7])])
#Non-Issue#
print('END------------- range concept----------------')
print('START --------------- for loops-------------')
outPut=[] #let's create an empty list
counter=0 #then a counter- we'll be monitoring the number of times the loop excecutes
for i in range(10): # for loop construct i.e for every element in a list of 10 items,
	outPut.append(i) #taken the empty list and append the element 'in mind' 
	counter+=1 # and for every round, add 1 to counter
	print([outPut,counter]) # for every cycle, print the results in a list 

#The last value is equal to the length of the elements list
print(len(outPut)==len(list(range(10))))
print(counter==len(outPut)==len(list(range(10))))


print('__________for loops with data__________')
mylist=['string',10,True,None,4.566,3.4e7,complex(4,7)] # This is a list of the most common data types
print(list)
# LOOPs in upacking lists 
unPackedList = []
for dataType in mylist:
	unPackedList.append(dataType)
print(unPackedList)
print(mylist==unPackedList) # The original mylist is similar to unpackedList 

print('-------- processing within for loop --------')
#  for loop with data processing
newProcessedList=list() # let's create an empty list #couls also use []
for datatype in mylist:#then pick the next element from myList
	typeOfElement = type(datatype)# lets determine the type of the data or element in list under excecution 
	newProcessedList.append(typeOfElement)## append the results to the newProcessedList
print(newProcessedList) # expect a list of the respective types of the datatypes
print('END --------------- for loops-------------')
print('START------------- while loop----------------')
# also present the use of Break and Continue in flow control
counter=0# we monitor cycles of excecution
while(True):
	print("This only excecutes once because we break instantly")
	counter+=1
	break
print('counter: '+ str(counter)) # counter is 1 becuase we loop only once

#more of the while loops
sampleSpace = [1,2,3,4,5,6,7]
loopOutput =[]
while(True):
	for i in sampleSpace:
		if i==3:
			print("Got 3" + str(i))
			break
		else:
			loopOutput.append(i)
	break 
print('loopOutput- for break test: = '+ str(loopOutput))
while(True):
	for i in sampleSpace:
		if i==3:
			print("Got 3")
			loopOutput.append(i)
			continue
		else:
			loopOutput.append(i)
	break 
print('loopOutput-for Continue test: = '+ str(loopOutput))
print('END------------- while loop----------------')

