'''
##############################################################
####          Presentation BY Sugut Viscount          ########
Python scripting:
	- A thought flow into production in python
	- Designed to accelerate towards WEB APPs- DJango _framework , REST API, Django_BACKEND(ORM Databases)
	- Designed to offer basics necessary for a Journey into Data sciecne (we handles models and imports, and PIP (PyPI)) and ML (sklearn-classification), 
	- Later sections will synthesis FRONTEND and BACKEND [- BOOTSTRAP 4], and DATABASES -Object Relational Models (ORM)-a and SQLite 
'''
##############################################################
####          Presentation BY Sugut Viscount          ########
##################   1. DATA TYPES- ##########################
##       Campturing objects from the Physical world 		##
## (Int, float, string, Boolean,Complex Numbers				##
## Built-In Functions, Classes, Attributes, and Inheritance)##
## Introduction to using variables & Assignment 			##
## -x is created pointed to int 10 x=10						##
##############################################################
# int
# This is a comment
print("START-------------INT----------------")
print(10)
print(5+5)
x=5
z=5
print(x+z)
print(type(x))
	#converting to int
print("END-------------INT----------------")

print("START--------------FLOATS-----------")
print("----------CONVERTING TO INT FROM STRING----------------")
string = "4"
print(type(string))
string_to_int = int(string)
print(type(string_to_int))

# Floats
print(type(4.2))
print("END--------------FLOATS-----------")

	#representing exponential points

print('START------------exponential points----------')
ex = 1.79e308
print(ex)
print(type(ex))
print("---------Complex Numbers-------")
c_complex=complex(4)
d_complex=complex(4.5)
e_complex=complex(4.5,3)
# List of results 
print('----List of results ---- ')
print(['c_complex number = '+ c_complex.__str__(),'d_complex:= '+ d_complex.__str__(),'e_complex:= '+ e_complex.__str__()])
print([type(c_complex),type(d_complex),type(e_complex)])

# STRING DATA TYPE

print("START---------STRING-----------")
y="This is a sring"
print(y)
print(type(y))

# Indexing in strings
print('START------------Indexing & slicing in strings-------------')
#The first element of string y- expect [T, Thi]		
print([y[0], y[:3]])

print('END------------Indexing & slicing in strings-------------')
# \',\",\newline, \\

#error - print('This string contains a single quote (') character.'
# solution
print('This string contains a single quote (\') character.')
print('Breaking a string to new line using \\')
print('a\
... b\
... c')
 #Using tabs in Python \t
print('first_element \t second after Tab')

		#CONCATINATION IN STRINGs#
print('START-----------CONCATINATION IN STRINGs-----------#')
print('py''thon')
print('py'+'thon')
a='py'
b="thon: "
print(a+b)

print('-----------#CONCATINATION IN STRINGs- converting to string using str(int(x))#-----')

print('Converting to string')
intValue = 10
print(a+b+str(10))
print('END-----------CONCATINATION IN STRINGs-----------#')
print("END---------STRING-----------")

# DATA TYPES - Boolean
print("START---------DATA TYPES - BOOLEANS-------")
print(type(True))
print(type(False))

print("END---------DATA TYPES - BOOLEANS-------")


#Built-In Functions

print('START---------------BUILT_IN FUNCTIONS --------- Abstraction')
## we can write out own logic, capture it in a variable
## and call it as a primary datatype as int, string, float or Booleans
##We will alsobe calling our function pyCalc

## writing first function - Python as a calculator-
def pyCalc(a,b):
	results = a+b
	return results
results = pyCalc(1,2)
print('results from pyCalc: = '+ results.__str__())

## common built-in functions: sum(), pow(),min(),max(),sqr(),set(),round() etc 
##for more go to Link = https://data-flair.training/blogs/python-built-in-functions/

#classes
print('END---------------BUILT_IN FUNCTIONS --------- Abstraction')
print('START--------USING CLASS as PRIMARY NAMESPACE (OOP) & attributes of the class-----------')
#classes are also forms of abstraction in Object Oriented programming
#class implementation of simple class-Instance(object) construct.

class home:
	pass
instance_of_home=home()
print(['class home:= '+ str(type(home)),'type of instance:= ' + str(type(instance_of_home))])
print(type(instance_of_home))
print('END--------USING CLASS as PRIMARY NAMESPACE (OOP) & attributes of the class-----------')
#Other data types
print ('START------------ list,tuple,dicts,sets,----')
#list
print(type([]))
#tuple
print(type(()))
#dict
print(type({}))
#set
print(type(set()))

print ('END------------ list,tuple,dicts,sets,----')

