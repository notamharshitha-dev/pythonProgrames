import sys
def add():
    todo=input("Enter the todo ")
    file_write=open("todos.txt",'a')
    try:
        file_write.write(todo+"\n")
    finally:
        file_write.close()
    print("Todo added succesfully")
def delete():
    ele=int(input("Enter the todo index "))
    try:
        file_del=open("todos.txt","r+")
        content=file_del.readlines()
        del content[ele]
        file_del.seek(ele)
        file_del.writelines(content)
        file_del.truncate()
    finally:
        file_del.close()
        

    print("Todo deleted successfully")
def display():
    print("The todoss areee")
    
    try:
        file_read=open("todos.txt",'r')
        #print(file_read.read())
        content=file_read.read()
        #todos=content.splitlines()
        #print(todos)
        todos=list(content.splitlines())
        #print(todos)
        for index,i in enumerate(todos):
            #print("Hello in for")
            print(index,i)
    finally:
        file_read.close()
while True:
    op_num=int(input("\n1.Add Todo\n2.Delete Todo\n3.Display\n4.Exit\nEnter your choice "))
    match op_num:
        case 1:add()
        case 2:delete()
        case 3:display()
        case 4:sys.exit()