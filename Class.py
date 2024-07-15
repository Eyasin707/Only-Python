#Let's create a class:
class my_class:
    name = "Ali"
print(my_class.name)

#Let's make it harder:
class my_class_1:
    name = "Ali"
    age  = 23
    loc  = "NYC"
print(my_class_1.name,my_class_1.age,my_class_1.loc)

#Let's optimize it:
class my_class_2:
    def __init__(self, name, age, loc):
       self.name = name
       self.age  = age
       self.loc  = loc
p1= my_class_2("ali", 23, "NYC")

#Let's make it a bit more complex:
class my_class_3:
    def __init__(self,name,age,loc,work):
        self.name  = name
        self.age   = age
        print(f'This is {self.name}. He is {self.age} years old')
p2= my_class_3("Ali", 23, "NYC" , "Google")

#Let's incorporate the users choice:
class my_class_4:
    def __init__(self,name,age):
        self.name  = name
        self.age   = age
        print(f'This is {self.name} and he is {self.age} years old')
name= input("Enter your name:")
age = input("Enter your age:")
p3= my_class_4(name, age)

#Now we mix all it up and write our final code.
#this time we will try to make it complex.

class my_class:
    def __init__(self,name,age,stu_id,m_e,m_h,m_s,m_m,m_art):
        self.name= name
        self.age= age
        self.stu_id= stu_id
        self.m_e= m_e
        self.m_h= m_h
        self.m_s= m_s
        self.m_m= m_m
        self.m_art= m_art
        
        avg= (m_e+m_h+m_s+m_m+m_art)/5
        
        self.grade_e= self.grade(self.m_e)
        self.grade_h= self.grade(self.m_h)
        self.grade_s= self.grade(self.m_s)
        self.grade_m= self.grade(self.m_m)
        self.grade_art= self.grade(self.m_art)
        
        
        print(f'This is {self.name}, ID: {self.stu_id} and he is\n'
              f'{self.age} years old. He\'s marks in this semester\n'
              f'are:\n'
              f'English= {self.m_e}\n'
              f'History= {self.m_h}\n'
              f'Science= {self.m_s}\n'
              f'Math= {self.m_m}\n'
              f'Art= {self.m_art}\n'
              f'Hi\'s average maark is {avg}\n'
              f'He\'s grade distribution:'
              f'English: {self.grade_e}\n'
              f'History: {self.grade_h}\n'
              f'Science: {self.grade_s}\n'
              f'Math: {self.grade_m}\n'
              f'Art: {self.grade_art}')
        
        
    def grade(self,marks):
        if marks>90:
            return "A+"
        elif marks>80:
            return "A"
        elif marks>70:
            return "B"
        elif marks>60:
            return "C"
        else:
            return "F"
            
name = input("Enter Name: ").strip()  # Ensure no extra whitespace affects input
while True:
    try:
        age = int(input("Enter Age: "))
        break  # Exit the loop if conversion to int is successful
    except ValueError:
        print("Please enter a valid integer for Age.")

while True:
    try:
        stu_id = int(input("Enter student ID: "))
        break  # Exit the loop if conversion to int is successful
    except ValueError:
        print("Please enter a valid integer for Student ID.")

while True:
    try:
        m_e = int(input("Enter English Marks: "))
        break  # Exit the loop if conversion to int is successful
    except ValueError:
        print("Please enter a valid integer for English Marks.")

while True:
    try:
        m_h = int(input("Enter History Marks: "))
        break  # Exit the loop if conversion to int is successful
    except ValueError:
        print("Please enter a valid integer for History Marks.")

while True:
    try:
        m_s = int(input("Enter Science Marks: "))
        break  # Exit the loop if conversion to int is successful
    except ValueError:
        print("Please enter a valid integer for Science Marks.")

while True:
    try:
        m_m = int(input("Enter Math Marks: "))
        break  # Exit the loop if conversion to int is successful
    except ValueError:
        print("Please enter a valid integer for Math Marks.")

while True:
    try:
        m_art = int(input("Enter Art Marks: "))
        break  # Exit the loop if conversion to int is successful
    except ValueError:
        print("Please enter a valid integer for Art Marks.")

student= my_class(name,age,stu_id,m_e,m_h,m_s,m_m,m_art)
