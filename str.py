class iostring():
    def __init__(self):
        self.str1 = " "
    def input_string(self):
        self.str1 = input("Enter your string to convert: ")
    def output_string(self):
        print("The result is: " , self.str1.upper())

obj1 = iostring()
obj1.input_string()
obj1.output_string()