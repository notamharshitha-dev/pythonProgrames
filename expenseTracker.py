#expense trackerrr
import sys
dict_expense={}
def addExpense():
    while True:
        key=input("Enter the category (Type quit at the stop) ")
        if key.lower()=='quit':
                    print("Quit")
                    break
        value=int(input("Enter the Expense "))
        
        dict_expense[key]=value
        print(dict_expense)
    print("\nExpense added successfullyy\n")
def display():
    print("\nThe expensess areee...\n")
def deleteExpense():
    print("\nExpense got deleted successfullyy\n")
def TotalExpense():
    print("\nThe Total value iss\n")
while(True):
    op_num=int(input("\n1.Add expense \n2.Delete Expense \n3.Display the expensesn\n4.Total Expense\n5.Exit\nEnter your choice "))
    match op_num:
        case 1:addExpense()
        case 2:deleteExpense()
        case 3:display()
        case 4:TotalExpense()
        case 5:sys.exit()