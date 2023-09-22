#what is class?
# class is a blueprint

class User:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact

    def info(self):
        print(f'Name : {self.name}\nContact:{self.contact}\n')


amit=User("amit",9595949452)
rahul=User("Rahul",94857684790)

amit.info()

class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model

    def info(self):
        print(f'Make of Car:{self.make}\nModel of car:{self.model}')

figo=Car("Ford","Figo Sports")
figo.info()

thar=Car("Mahindra","Thar 2022")
thar.info()