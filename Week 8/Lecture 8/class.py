class Student():

    def __init__(self, name, house):
        if not name:
            raise ValueError
        self.name = name
        self.house = house
    
    def __str__(self):
        return (f"name: {self.name}, house: {self.house}")


    #getter
    @property
    def name(self):
        return self._name
    
    #setter
    @name.setter
    def name(self, name):
        if name == 'Homie':
            raise ValueError ("That's actually not my real name!")
        self._name = name


    def call(self):
        #print(self.name, self.house)
        print (self)

def main():
    student = Student("Motun", "Shobande")
    student.name = 'Homie'
    student.call()
    #print (student)

main()