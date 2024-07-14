''' this is a very Basic class example which over the time will be improved and end up being a very inclusive example for class in python '''

class person():
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def __str__(self):
        return f"The name of this person is: {self.name} and his age is: {self.age}"
person1=person("Jhon", 23)
print(person1)



#example:

class person:
    def __init__(self, name, age, loc):
        self.name= name
        self.age = age
        self.loc= loc
    def abc(self):
        print(f"Hello! My name is {self.name}, I'm only {self.age} years old and I live at {self.loc}")
p1= person("Jhon", 23, "NYC")
p1.abc()

