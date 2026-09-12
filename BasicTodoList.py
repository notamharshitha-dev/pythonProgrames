import sys
todos=[]
def add():
    todo=input("Enter the todo ")
    todos.append(todo)
    print(todos)
    print("\nTodo added successfullyy\n")
def delete():
    index=int(input("Enter the index number "))
    todos.pop(index)
    print("\nTodo deleted successfullyy\n")
def display():
    print("The todos areee")
    for index,i in enumerate(todos):
          print(index,i)
while True:
    op_num=int(input("\n1.Add Todo\n2.Delete Todo \n3.display Todo\n4.Exit\nEnter your choice "))
    match(op_num):
        case 1:add()
        case 2:delete()
        case 3:display()
        case 4:sys.exit()   