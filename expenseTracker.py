#expense trackerrr
import sys
dict_expense={}
def addExpense():
    while True:
        key=input("Enter thssse category (Type quit at the stop) ")
        if key=='quit' or key.upper()=="QUIT":
                print("Quit")
                break
        value=input("Enter the Expense")
        dict_expense[key]=value
        '''try:
            file_write=open("expenses.txt",'a')
            value=int(input("Enter the Expense "))        
            dict_expense[key]=str(value)
            print(dict_expense)
            file_write.append(f"\n{key}:{value}\n")
            print("\nExpense added successfullyy\n")
        finally:
            file_write.close()'''
        try:
            file_write=open("expense.txt",'w')
            for key,value in dict_expense.items():
                file_write.write(f"{key}:{value}\n")
        finally:
            file_write.close()
             
        print("\n THe Expense Added Successfulyy.....")
        
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