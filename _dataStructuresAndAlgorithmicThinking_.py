
# Implements the Bag ADT container using a Python list.
# create this Class
class thisClass:
	def __init__(self):
		self._ourNames = list()

	#How many are we?
	def _counter_(self):
		return len(self._ourNames)

	#Is (one of us's name e.g Mercy) in this room?
	def __isIn__(self,_nameholder_):
		check = _nameholder_ in self._ourNames
		return check # check is a bool (True/Flase)
	
	#Add new name- new student?
	def __addName__(self,_nameholder_):
		self._ourNames.append(_nameholder_)
		newClassList = self._ourNames
		return newClassList # or return self._outNames

	# remove name- Someone is taking a break-
	def _remove_name(self,_nameholder_):
		# let's check if name exists
		try:
			assert _nameholder_ in self._ourNames
			# get index of the name
			index_of_name = self._ourNames.index(_nameholder_)
			#remove the name from class list
			newList = self._ourNames.pop(index_of_name)
		except Exception as e:
			raise 'Name not in class List'
	## get the class list printed
	def _printList_(self):
		# interate through the list
		ourList = []
		for element in self._ourNames:
			ourList.append(element)
		return ourList

############## Tests panel- methods ###########
######## Initialising Objects ########
print('START --------------- Handling Methods------------- output in lists')
bootcamp_2019 = thisClass()
ourList_empty=[bootcamp_2019._printList_(), bootcamp_2019._counter_()] 
print(ourList_empty)

print('START---------- adding new students in 2020 Bootcamp-----------')
# Expecting a jump to [[Mercy M],1]
bootcamp_2020 = thisClass()
bootcamp_2020.__addName__("Mercy M")
ourList = [bootcamp_2020._printList_(), bootcamp_2020._counter_()] 
print(ourList)

# Add one more student Denis D
bootcamp_2020.__addName__("Denis D")
ourList = [bootcamp_2020._printList_(), bootcamp_2020._counter_()] 
print(ourList)

# check if name exists
Check_isIn = bootcamp_2020.__isIn__("Mercy M")
print(Check_isIn)
Check_isIn_not = bootcamp_2020.__isIn__("Ann N")
print(Check_isIn_not)

#Remove a student 
bootcamp_2020._remove_name("Mercy M")
#displaying content
#expect [[Denis D],1]
print([bootcamp_2020._printList_(), bootcamp_2020._counter_()])


# Dealing with Arrays
print ("--------------------ARRAYS The Array Abstract Data Type-----------")

myArray = [[1,2],[3,4],[5,6]]
print(myArray)
print(myArray[0]) # getting the first element of Array = List [1,2]
print(len(myArray))
			##### Replacing value at index[i] where i=0
myArray[0]=["new_element"]
print(myArray)


print("------------------ ALGORITHMS----------------------")
print("------------------ Thought flow in Divide and conquer----------------------")

## Algorithms follow thought, it is a step by step procedure of "cooking" a concept
##Takes in information (Based on discussed DataTypes and uses them as parameters)
## More data can be manually inserted
## data structures help in data management-
'''
#Searching through a sorted numeric list is implemented with the following thought procces
#-function gets the list and element whose index we are to search as arguments
#-get the element at the center of the list then compare if it is the one we are looking for, now 
#1. if they are the same, that is likely the answer 
#2. if value at middle index is greater than search value, then
#the value is in the left, so the list is cut by half, the right is discarded
#2. if value at middle index is less than search value, then
#the value is in the right, so the list is cut by half, the left is discarded
#NB: This algorithm (O)= exponential-\
#To get middle number we take the average of max and min points of the list length
# Lets Find the middle most value
'''
def index_point_search(list, val):# function value search takes list and reqested value 
									# list and val are arguments in procedure index_point_search 
	list_size = len(list) - 1 # let's get the length of list then minus 1 (because
							#lists index start from 0 i.e 0,1,2,4...n-1)
							#list_sides exits as a value that can denote the last_element=list(list_size)
	idx0 = 0 # lets get the index for the first element first_element=list[0], so index0=0
	idxn = list_size #list_size  lets get the index for the last for last element last_element=list[inxn=list_size], so index0=list_size
#NB: Use of control in programming (looping concept - while loop)
	while idx0 <= idxn:
		midval = (idx0 + idxn)// 2  # Basic operation with operators (+(add ints or concatinate strings,-(negate),*(multiplication),//(div),%(modulus))
		if list[midval] == val:
			return midval
# Compare the value the middle most value
		if list[midval] == val: #Says if the value at the center list[midval] is the same as our search value, 		
			return midval  # return the index position as the anwer to our question, 
# Compare the value the middle most value
		if val > list[midval]: # But if our search value is greater than the value to the center of the list, 
			idx0 = midval + 1  # Take the index and add 1 (because)
		else:
			idxn = midval - 1
	if idx0 > idxn:
		return None
# Initialize the sorted list
list = [2,7,19,34,53,71,77,78,90,99,101] #Use of lists in data
# Print the search result
print(index_point_search(list,77))
print(index_point_search(list,53))