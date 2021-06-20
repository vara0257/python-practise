def my_function(value):
    print(value)

my_function(input("Enter a value:"))

==========================================

def my_function(fname, lname):
    print ("Full name is", fname, lname)

a, b = input("Enter firstname and lastname:").split()
my_function(a,b)

==========================================

def my_function(*students):
    print("Students names are: " + students[0], students[1])

my_function("1. Vara", "2. Mahesh", "3. Krishna")

==========================================

def my_function(**students):
    print("His last name is " + kid["fname"])

my_function(fname = "Vara", lname = "prasad")



