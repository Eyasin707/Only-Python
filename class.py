''' this is a very Basic class example which over the time will be improved and end up being a very inclusive example for class in python '''

class person():
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def __str__(self):
        return f"The name of this person is: {self.name} and his age is: {self.age}"
person1=person("Jhon", 23)
print(person1)
