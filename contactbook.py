import sys
dict_contact={}
def save():
    try:
        file_write=open("contactsBook.txt",'a')
        name=input("Enter the Name: ")
        number=int(input("Enter the Number: "))
        relation=input("ENter the relation: ")
        dict_contact["name"]=name
        dict_contact["number"]=number
        dict_contact["realtion"]=relation
        for key,value in dict_contact.items():
            file_write.write(f"{key}:{value}+"  "")
        file_write.write("\n")
    finally:
        file_write.close()
        print("\n Contact got saved successfullyy........")
def delete():
    try:
        file_del=open("contactsBook.txt",'r+')
        content=file_del.readlines()
        ele=int(input("Enter the index "))
        del content[ele-1]
        file_del.seek(ele)
        file_del.writelines(content)
        file_del.truncate()
    finally:
        file_del.close()
        print("\nContact deleted successfulyyy.....\n")
def display():
    print("\nThe contacts areee...\n")
    try:
        file_read=open("contactsBook.txt",'r')
        content=file_read.readlines()
        #print(content)
        for index,i in enumerate(content):
            contact=i.split("+")
            print(f"\n{index+1} {contact[0]}    {contact[1]}    {contact[2]}  ")        
    finally:
        file_read.close()
def search():
    try:
        file_read=open("contactsBook.txt",'r')
        content=file_read.readlines()
        index=int(input("Enter the Contact Index "))
        s_contact=content[index-1].split("+")
        print(f"\n{s_contact[0]}    {s_contact[1]}     {s_contact[2]}  ")
    finally:
        file_read.close()
while True:
    op_num=int(input("\n1.Save Contact\n2.Delete Contact\n3.Display Contact\n4.Search Contact\n5.Exit from contact book\nEnter your choice "))
    match op_num:
        case 1:save()
        case 2:delete()
        case 3:display()
        case 4:search()
        case 5:sys.exit()