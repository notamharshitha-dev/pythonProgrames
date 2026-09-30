#expense trackerrr
import sys
dict_expense={}
total=0
def addExpense():
    while True:
        key=input("Enter thssse category (Type quit at the stop) ")
        if key=='quit' or key.upper()=="QUIT":
                print("Quit")
                break
        value=input("Enter the Expense ")
        dict_expense[key]=value
        try:
            file_write=open("expense.txt",'a')
            for key,value in dict_expense.items():
                file_write.write(f"{key}:{value}\n")
        finally:
            file_write.close()             
        print("\n THe Expense Added Successfulyy.....")
        
def display():
    print("\nThe expensess areee...\n")
    try:
        file_read=open("expense.txt",'r')
        content=file_read.readlines()
        #print(content)
        for index,i in enumerate(content):
            print("\n",i)
    finally:
        file_read.close()
def deleteExpense():
    print("\nExpense got deleted successfullyy\n")
def TotalExpense():
    total=0
    try:
        file_read=open("expense.txt",'r')
        content=file_read.readlines()
        for i in content:
           # print(i.split(":"))
            one_item=i.split(":")
            '''cost=one_item[1]
            total+=int(cost)'''
            total+=int(one_item[1])
        print("\nThe expenses is : ",total)
    finally:
        file_read.close()
    
while(True):
    op_num=int(input("\n1.Add expense \n2.Delete Expense \n3.Display the expensesn\n4.Total Expense\n5.Exit\nEnter your choice "))
    match op_num:
        case 1:addExpense()
        case 2:deleteExpense()
        case 3:display()
        case 4:TotalExpense()
        case 5:sys.exit()