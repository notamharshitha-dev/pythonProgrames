file_write=open("example.txt","w")
try:
    file_write.write("Hello bro welcome to the concept of filehandling in python and from here the game starts")
finally:
    file_write.close()
file_read=open("example.txt","r")
try:
    print(file_read.read())
finally:
    file_read.close()