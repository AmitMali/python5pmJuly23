class persone:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact

    def info(self):
        print(f'name ={self.name}\nContact={self.contact} ')

    def updateName(self,name):
        self.name=name

person1=persone("amit mali",74343743748)
person2=persone("rahul ",32939893829)

person1.info()
person2.info()
person1.updateName("amit")
person1.info()