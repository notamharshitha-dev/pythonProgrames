#file read,write and delete operation operations
import sys
def read():
    print("The data in the file is........\n")
def write():
    print("Data Written Successfullyyy....")
def delete():
    print("The data deleted suceessfulyy.......\n")
while(True):
    op_num=int(input("1.Read\n2.Write\n3.Delete\n4.Exit\nEnter the operational value"))
    match op_num: 
        case 1:read()
        case 2:write()
        case 3:delete()
        case 4:sys.exit()