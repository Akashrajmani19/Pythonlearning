import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s: %(message)s")

file_handler = logging.FileHandler("logging2.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def add(x,y): # defining fucntion
    return x + y

def subtract(x,y): # defining fucntion
    return x - y

def multiply(x,y):  # defining fucntion
    return x * y

def divide(x,y):  # defining fucntion
    return x/y

x=45
y=78
add_result = add(x,y)
logger.debug(f"addition :  {x} + {y} = {add_result} ")

subtract_result = subtract(x,y)
logger.debug(f"subtract :  {x} - {y} = {subtract_result} ")

divide_result = divide(x,y)
logger.debug(f"divide :  {x} / {y} = {divide_result} ")

multiply_result = multiply(x,y)
logger.debug(f"multiply :  {x} * {y} = {multiply_result} ")