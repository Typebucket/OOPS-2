class sum():
    def __init__(self):
        print("Constructor")

    def sum2(self, numlist, target):
        lookup = { }
        for i, num in enumerate(numlist):
            if target-num in lookup:
                return(lookup[target-num], i)
            lookup[num]= i

Value = int(input("Enter the targeted sum value: "))
print("Index1 = %d, Index2 = %d"%sum().sum2((1,3,5,7,9,11,13),Value))