import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logging3.log")
formatter = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s : %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class employee:
    def __init__(self,first,last):
        self.name=first
        self.last=last

        logger.info(f"Created Employee : {self.fullname} - {self.email}")
    
    @property 
    def fullname(self):
        return f"{self.name} {self.last}"

    @property
    def email(self):
        return f"{self.name}.{self.last}@mail.com"


person1 = employee("Akash","Vaishnav")