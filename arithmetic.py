# Display Menu-> for user
'''
Below created is function which user defined function.
here we are achieving a menu which user going to see when program
get started

here to define function -keyword -def to be used
& we defined to function display_menu()

synatx:
def function_name():
    function_body

indentation to write function_body to be taken care of, which
can be seen below.

i have created 7 selections which will do airthmetic operations
& last select to break/exit out of program.
'''
def display_menu():
    print("--- Welcome to the Simple Calculator ---")
    print("--> Select 1 for Addition")
    print("--> Select 2 for Subtraction")
    print("--> Select 3 for Multiplication")
    print("--> Select 4 for Division")
    print("--> Select 5 for Power")
    print("--> Select 6 for True Quotient")
    print("--> Select 7 for Remainder")
    print("--> Select 8 for Exit")

# User choice-> 
'''
to achieve this we have created function name "get_choice()" with while loop & with
boolean condition.
also we have handled exception which can occur while handling
user choice at the output end , if use enter invalid input such
as if user enter letter "one" instead of 1 digit then error will
occure & we wont be able process further.
so to handle this first we have to check which error comes when user
enter word.

# Testing for calculator project
choice = int(input("Enter your choice (1/2/3/4/5/6/7/8): "))

while choice>=1 and choice<=8:
    print("Correct choice")

hence to handle this logical error we have used exception method,
which is try-except-finally

also to select between 1 to 8 choice- we have used logical operator
here that is and operator, if both i/p's turn 1 or true it will
process further

here return is keyword which will hold the result but wont display
at the output, which can used later if we want.
'''

def get_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3/4/5/6/7/8): "))
            if choice>=1 and choice<=8: #Logical operator- and logic - it will see if both choice condition turn out be true then only it will process choice & hold value but wont display it due return statement written
                return choice
            else:
                print("Invalid choice, Please select a choice number between 1 to 8!!.")
        except ValueError:          #ValueError: Logical error-if exception error (logical error) has any spelling mistake in wont work,hence before putting test it
            print("Select choice in digit format only!")

# Get two numbers from user->
'''
here to achieve, getting 2 numbers from user we have created an
function with while loop & boolean true condition, which we mentioned
as a True which execute the try-except-finally exception loop.

where
try : is holding logic which will accept user 2 inputs n1,n2
and hold n1,n2

where
except followed by error names, here we have taken care of 2 errors.
will get handled if occur.

'''
def get_numbers():
    while True:
        try:
            n1 = float(input("Enter Number 1: "))
            n2 = float(input("Enter Number 2: "))
            return n1,n2
        except ZeroDivisionError:   # if exception error (logical error) has any spelling mistake in wont work,hence before putting test it
            print("Denominator can not be Zero!")
        except ValueError:          # if exception error (logical error) has any spelling mistake in wont work,hence before putting test it
            print("Enter number in digit format only!")

