#file read,write and delete operation operations
import sys
def write():
    try:
        file_write=open("example.txt",'w')
        while True:
            content=input("Enter the content (ENter stop to end) ")
            if content=="stop":
                break
            file_write.write(content+'\n')
            print("Data written succeessfulyyy......\n")
    finally:
        file_write.close()       
    
def read():
    print("\nThe Data in the file isss....\n")
    try:
        file_read=open("example.txt",'r')
        content=file_read.readlines()#returns a list 
        #print(content)
        for index,i in enumerate(content):
            print(index+1,i)
    finally:
        file_read.close()
def delete():
    try:
        file_del=open("example.txt",'r+')
        i=int(input("Enter the index"))
        content=file_del.readlines()
        del content[i-1]
        file_del.seek(i)
        file_del.writelines(content)
        file_del.truncate()
    finally:
        file_del.close()
    print("\nThe data deleted suceessfulyy.......\n")
while(True):
    op_num=int(input("1.Read\n2.Write\n3.Delete\n4.Exit\nEnter the operational value "))
    match op_num: 
        case 1:read()
        case 2:write()
        case 3:delete()
        case 4:sys.exit()