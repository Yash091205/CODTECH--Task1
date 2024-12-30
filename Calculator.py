# Creating class for Calculator
class calci:
    def __init__ (self,fno,sno):
        self.fno=fno
        self.sno=sno
    # Function for addition
    def add(self):
        print(f"{self.fno} + {self.sno} = ", self.fno+self.sno)
    # Function for substraction
    def sub(self):
        print(f"{self.fno} - {self.sno} = ", self.fno-self.sno)
    # Function for multiplication
    def multi(self):
        print(f"{self.fno} * {self.sno} = ", self.fno*self.sno)
    # Function for division
    def div(self):
        if self.sno == 0:
            print("Invalid input!!\nSecond number is zero")
            main()
        else:
            print(f"{self.fno} / {self.sno} = ", self.fno/self.sno)

# Function to take input
def inp():
    global a,b,o1
    a = int(input("Enter First Number :- "))
    b = int(input("Enter Second Number :- "))
    o1 = calci(a,b) # Creating object of class calculator
    
# Function to select Choice
def main():
    print("---Which operation would you like to perform---")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    flag =1
    while flag ==1:
        choice = int(input("Enter your Choice = "))
        if choice == 1:
            print("Your choosen operation is Addition :- ")
            inp()
            o1.add()
        elif choice == 2:
            print("Your choosen operation is Substraction :- ")
            inp()
            o1.sub()
        elif choice == 3:
            print("Your choosen operation is Multiplication :- ")
            inp()
            o1.multi()
        elif choice == 4:
            print("Your choosen operation is Division :- ")
            inp()
            o1.div()
        elif choice == 5:
            print("Thank You!!")
            exit() # Exits from total function
        else:
            print("Enter a Valid Choice.")
            main()

# Calling functions
main()