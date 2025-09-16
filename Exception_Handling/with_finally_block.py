try :
    file = open ('D:\Code_with_sagar\Exception_Handling\errors.txt','r')
    content = file.read()
    print(content)

except FileNotFoundError:
     print("file not Found")
finally:
     file.close()
     print('file operation completed')