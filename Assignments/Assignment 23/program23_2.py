# 2: Write a Python program to implement a class named BankAccount with the following requirements:

# The class should contain two instance variables:
# Name (Account holder name)
# Amount (Account balance)

# The class should contain one class variable:
# ROI (Rate of Interest), initialized to 10.5

# Define a constructor (init) that accepts Name and initial Amount.

# Implement the following instance methods:
# Display()-displays account holder name and current balance
# Deposit()accepts an amount from the user and adds it to balance

# Withdraw() accepts an amount from the user and subtracts it from balance 
# (Ensure withdrawal is allowed only if sufficient balance exists)

# CalculateInterest() calculates and returns interest using formula:
# Interest =  (Amount * ROI) / 100

# Create multiple objects and demonstrate all methods.

class BankAccount:
    ROI = 10.5

    def __init__(self, A, B):
        self.Name = A
        self.Amount = B

    def Display(self):
        print("Account Holder : ", self.Name)
        print("Account Balance : ", self.Amount)

    def Deposit(self):
        self.Add = int(input("Enter Amount You Want To Deposit : "))

        self.Amount = self.Amount + self.Add

    def Withdraw(self):
        self.Debit = int(input("Enter Amount You Want To Withdraw : "))

        if self.Amount < self.Debit:
            print("Unable to WithDraw as Insufficient Balance")
        else:
            print("Amount Withdrawed successfully")
            self.Amount = self.Amount - self.Debit

        print("Remaining Amount is : ", self.Amount)

    def CalculateInterest(self):
        self.Interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest is : ", self.Interest)

def main():
    obj = BankAccount("Krishna", 1000)

    obj.Display()

    obj.Deposit()

    obj.Withdraw()

    obj.CalculateInterest()

if __name__ == "__main__":
    main()