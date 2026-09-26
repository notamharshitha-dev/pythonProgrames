"""try:

    file_write=open("example.txt","r+")
    file_write.write("This is the last of the of this file"+'\n')
    content=file_write.readlines()
    del content[2]
    file_write.seek(1)
    file_write.writelines(content)
    file_write.truncate()
finally:
    file_write.close()"""
'''try:
    file_read_write=open("example.txt","r+")    
    content=file_read_write.readlines()
    del content[0]
    file_read_write.seek(0)
    file_read_write.writelines(content)
    file_read_write.truncate()
finally:
    file_read_write.close()'''
'''try:
    file_del=open("example.txt","r+")
    content=file_del.readlines()
    del content[1]
    file_del.seek(0)
    file_del.writelines(content)
    file_del.truncate()
finally:
    file_del.close()'''
