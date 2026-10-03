import sys
import json
student=[]

def write():
    temp_dict={}
    name=input("Enter the Name: ")
    branch=input("Enter the Branch: ")
    year=int(input("Enter the Year: "))
    temp_dict["name"]=name
    temp_dict["branch"]=branch
    temp_dict["year"]=year
    #print(temp_dict)
   
    student.append(temp_dict)
    with open("example.json",'r') as file:
        content=json.load(file)
        print(content)
        if(content==[]):
            with open("example.json",'w') as file:
                json.dump(student,file,indent=4)
        else:
            with open("example.json",'w') as file:
                content.append(temp_dict)
                json.dump(content,file,indent=4)
    print("\nThe data Stored suceessfuullyyy......\n")
def display():
    print("\nThe data in the file iss.......\n")
    with open("example.json",'r') as file:
        content=json.load(file)
        #print(content)
        for index,i in enumerate(content):
            print(index,i)
def search():
    with open("example.json",'r') as file:
        ele=int(input("Enter the index: "))
        content=json.load(file)
        print(content[ele])
        
def delete():
    with open("example.json",'r') as file:
        content=json.load(file)
        #print(content)
        ele=int(input("Enter the index: "))
        content.pop(ele)
        with open("example.json",'w') as file:
            json.dump(content,file,indent=4)
    print("\nThe data Poped successsfuullyy....\n")
while True:
    op_num=int(input("1.Write\n2.Delete\n3.Display\n4.Search\n5.Exit\nEnter your Choice: "))
    match op_num:
        case 1:write()
        case 2:delete()
        case 3:display()
        case 4:search()
        case 5:sys.exit()