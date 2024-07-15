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

class my_class_5:
    def __init__(self,name,age,stu_id,mark_e,mark_h,mark_s,mark_m,mark_art):
        self.name= name
        self.age= age
        self.stu_id= stu_id
        self.mark_e= mark_e
        self.mark_h= mark_h
        self.mark_s= mark_s
        self.mark_m= mark_m
        self.mark_art= mark_art
        
        avg= (mark_e+mark_h+mark_s+mark_m+mark_art)/5
        print(f'This is {self.name} and his ID is {self.stu_id}.'
             f'He has obtained these folliwing marks:\n'
             f'English: {self.mark_e}\n'
             f'History: {self.mark_h}\n'
             f'Science: {self.mark_s}\n'
             f'Math: {self.mark_m}\n'
             f'Art: {self.mark_art}\n'
             f'His average mark in this semester is: {avg}\n'
             f'He\'s grades are:\n'
             f'English: {self.grade(self.mark_e)}\n'
             f'History: {self.grade(self.mark_h)}\n'
             f'Science: {self.grade(self.mark_s)}\n'
             f'Math: {self.grade(self.mark_m)}\n'
             f'Art: {self.grade(self.mark_art)}')
        
    def grade(self,marks):
        if marks>90:
            print("A+")
        elif marks>80:
            print("A")
        elif marks>70:
            print("A-")
        elif marks>60:
            print("B")
        elif marks>50:
            print("C")
        else:
            print("F")
            
name= input("Enter name:")
age= input("Enter age")
stu_id= int(input("Enter Student ID:"))
mark_e= int(input("Marks in English:"))   
mark_h= int(input("Marks in History:"))
mark_s= int(input("Marks in Science:")) 
mark_m= int(input("Marks in Math:")) 
mark_art= int(input("Marks in Art:")) 

student= my_class_5(name,age,stu_id,mark_e,mark_h,mark_s,mark_m,mark_art)



'''
Enter name: rr
Enter age 5
Enter Student ID: 5
Marks in English: 5
Marks in History: 5
Marks in Science: 5
Marks in Math: 5
Marks in Art: 5
F
F
F
F
F
This is rr and his ID is 5.He has obtained these folliwing marks:
English: 5
History: 5
Science: 5
Math: 5
Art: 5
His average mark in this semester is: 5.0
He's grades are:
English: None
History: None
Science: None
Math: None
Art: None
'''
