class Employee():
    def __init__(self):
        print("Employee is called")
    def __del__(self):
        print("Destructor")

def create_obj():
    print("Create object function")
    obj = Employee()
    print("Function ended")

print("Program started")
create_obj()
print("The program has ended")