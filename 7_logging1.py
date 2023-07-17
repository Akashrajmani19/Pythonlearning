import logging   # importing logging module

logging.basicConfig(filename = "logging1.log", level = logging.DEBUG , format = "%(asctime)s : %(name)s : %(levelname)s : %(message)s")
""" Saving log file name as logging.log and set level at DEBUG"""

def add(x,y): # defining fucntion
    return x + y

def subtract(x,y): # defining fucntion
    return x - y

def multiply(x,y):  # defining fucntion
    return x * y

def divide(x,y):  # defining fucntion
    return x/y

#x=int(input("number 1 : ")) # defining variable 
#y = int(input("number 2 : "))  # defining variable
x=45
y=78
add_result = add(x,y)
logging.debug(f"addition :  {x} + {y} = {add_result} ")

subtract_result = subtract(x,y)
logging.debug(f"subtract :  {x} - {y} = {subtract_result} ")

divide_result = divide(x,y)
logging.debug(f"divide :  {x} / {y} = {divide_result} ")

multiply_result = multiply(x,y)
logging.debug(f"multiply :  {x} * {y} = {multiply_result} ")


