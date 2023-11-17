#python program to create bankaccount class
#with both a deposit() and a winthdraw() function
class bank_account:
    def __init__(self):
       self.balance=0
       print("hello!!! welcome to the deposit & withdrawal machine")

    def deposit(self):
       amount=float(input("enter amount to be deposited: "))
       self.balance += amount
       print("\n Amount deposited:" ,amount)
    def withdraw(self):
       amount = float(input("Enter amount to be withdrawn: "))
       if self.balance>=amount:
           self.balance_=amount
           print("\n you withdraw:", amount)
       else:
           print("\n insufficient balance  ")
    def display(self):
        print("\n net available balance=",self.balance)
#driver code


#creating an object of class
s= bank_account()

#calling function with that class
s.deposit()
s.withdraw()
s.display()
