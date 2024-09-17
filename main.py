#Importing modules from another file
'''
Here, in this file we are going to achieve calculator function &
run choice at the o/p , but we have created display menu,
user choice & get 2 numbers in our arithmetic.py file.

so to incorporate those in this file , we are using concept called
modules concept-> which will import another file to another file or
many as per programmer needs.
here we have used user defined modules-> means we are importing
modules which we created in our airthmetic.py file
'''
from arithmetic import display_menu, get_choice, get_numbers

#Created Class name "Calculator" to perform mathimatical operation
'''
Here to perfom arithmetic operation we have created fuction &
incorporated in class which an oops(object oriented programing system)

syntax : to create class
class classname:
    properties
    
also we have incorporated constructor at start of class, which will
initialize & get called automatically.

synatx: to call constructor
__init__()

here self is compulosory while using class or it will throw an
error.

also incorporated exception with try- except- finally method.

also we have incoroprated destructor- which will release the
memory once operation ends
syntax:
__del__()
'''
class Calculator:
    def __init__(self):
        print("Program started!!")
    
    def add(self,n1,n2):
        res=n1+n2
        return res

    def subtract(self,n1,n2):
        res=n1-n2
        return res

    def multiply(self,n1,n2):
        res=n1*n2
        return res

    def divide(self,n1,n2):
        try:
            res=n1/n2
            return res
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    def power(self,n1,n2):
        res=n1**n2
        return res

    def truequo(self,n1,n2):
        try:
            res=n1//n2
            return res
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    def remain(self,n1,n2):
        try:
            res=n1%n2
            return res
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    def __del__(self):
        print("Program Ended!!")
        

# Excecution as per choice between 1 to 8:
'''
here we have craeted "domath()" class, which will get recalled
when user select appropriate choice input between 1 to 8

above class step we have created class "Calculator()", which we
are calling here means we have created object for that class which
also called as "Instantiation"

with while loop & by bool True condition=1, we are calling functions
which we made in previous file & also imported which is:
display_menu() & get_choice()

once we recevied choice from user, we called get_numbers() to accept
n1,n2.
'''
def domath():
    calc = Calculator()  # Created an ojbect/instance of the Calculator class
    
    while True:
        display_menu()  # Display the menu
        choice = get_choice()  # Get the user's choice

        if choice == 8:
            print("Exit.")
            break  # Exit the loop if the user chooses to exit

        a, b = get_numbers()  # Get the two numbers from the user

        if choice == 1:
            #print(f"Result: {a} + {b} = {calc.add(a, b)}")
            print("Addition =",calc.add(a,b))
        elif choice == 2:
            #print(f"Result: {a} - {b} = {calc.subtract(a, b)}")
            print("Subtraction =",calc.subtract(a,b))
        elif choice == 3:
            #print(f"Result: {a} * {b} = {calc.multiply(a, b)}")
            print("Multiplication =",calc.multiply(a,b))
        elif choice == 4:
            #print(f"Result: {a} / {b} = {calc.divide(a, b)}")
            print("Division =",calc.divide(a,b))
        elif choice == 5:
            #print(f"Result: {a} ** {b} = {calc.power(a, b)}")
            print("Power of =",calc.power(a,b))
        elif choice == 6:
            #print(f"Result: {a} // {b} = {calc.truequo(a, b)}")
            print("True Quotient =",calc.truequo(a,b))
        elif choice == 7:
            #print(f"Result: {a} % {b} = {calc.remain(a, b)}")
            print("Remainder =",calc.remain(a,b))
        

        input("Press Enter to continue...")

# to run calculator function, we need to call function "domatch()"
domath() # calling function to run choice menu
