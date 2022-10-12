# Create an object-oriented program that allows you to enter data for customers and employees.
# Problem Details
# Create a Person class that provides attributes for first name, last name, and emailaddress. This class should provide a property or method that returns the person’s fullname.
# Create a Customer class that inherits the Person class. This class should add anattribute for a customer number.
#  Create an Employee class that inherits the Person class. This class should add anattribute for a PAN number.
# The program should create a Customer or Employee object from the data entered bythe user, and it should use this object to display the data to the user. To do that, theprogram can use the isinstance() function to check whether an object is a Customer orEmployee object.
#


class Person:
    def __init__(self, fn, ln, email):
        self.fname = fn
        self.lname = ln
        self.email = email

    def disp(self):
        print("\n", self.fname, self.lname, self.email)


class Customer(Person):
    def __init__(self, fn, ln, email, cust_no):
        # super().__init__( fn, ln, email)
        Person.__init__(self, fn, ln, email)
        self.cust_no = cust_no

    def disp(self):
        Person.disp(self)
        print("Customer no=: ", self.cust_no)


class Employee(Person):
    def __init__(self, fn, ln, email, PAN):
        Person.__init__(self, fn, ln, email)
        self.PAN = PAN

    def disp(self):
        Person.disp(self)
        print("PAN=: ", self.PAN)


def main():
    choice='y'
    while choice=='y':
        fn,ln,email=input("Enter First Name Last Name and email: ").split()
        print("1:Customer 2:Employee  3:Person ")
        opt=int(input("Enter your option: "))
        if opt==1:
            cust_no=int(input("Enter customer number: "))
            c = Customer(fn, ln, email, cust_no)
            show(c)
        elif opt==2:
            pan=input("Enter employee PAN: ")
            e=Employee(fn, ln, email, pan)
            show(e)
        elif opt==3:
            p=Person(fn, ln, email)
            show(p)
        else:
            print("Invalid input")
            break

        choice=input('Enter "y" to continue and "n" to Terminate ')

    # p = Person("Shivam", "Karmudi", "jdaskj@gmail.com")
    # p.disp()
    #
    #
    # c.disp()
    #
    # e = Employee("Shivam", "Karmudi", "jdaskj@gmail.com", 400)
    # e.disp()


def show(ob):
    if isinstance(ob, Customer):
        print("Customer")
        ob.disp()
    elif isinstance(ob, Employee):
        print("Employee")
        ob.disp()
    elif isinstance(ob, Person):
        print("Person")
        ob.disp()


if __name__ == "__main__":
    main()

