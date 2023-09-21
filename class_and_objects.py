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


