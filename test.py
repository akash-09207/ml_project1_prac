with open('requirements.txt','r') as file:
    l=file.readlines()
    for i in l:
        print(type(i))