
import string
import random

available = list(string.digits)
def createPassword():
    
    length = input("Please enter the length of your new password: ")
    random.shuffle(available)
    password = []
    for i in range(int(length)):
        password.append(random.choice(available))
    random.shuffle(password)
    np = "".join(password)
    label = input("For what the password?: ")
    dic = {}
    f = open("/home/appers/Desktop/p.txt", 'a')
    dic[label] = np
    print("This is your generated password")
    print(dic)
    print("\n would you like to add it to the passwords file?\n")
    choice = input("please type y for yes or n for no: ")
    if choice == 'y':
        cxs = (label + "   =>   "+ np+"\n")
        f.write(cxs)
    elif choice != 'y':
        print("\nOk")
    thChoice = input("\n Would you like see what inside the file? : ")
    f.close()
    xx=[]
    if thChoice == 'y':
        cc= open("/home/appers/Desktop/p.txt", 'r')
        lines = cc.readlines();
        for line in lines:
            data = line.split("\n")
            xx.append(data)
            print(str(xx))
        cc.close()
    elif thChoice != 'y':
        pass
    
       
    secChoice = input("\n Would you like to create a new password? : ")
    
    if secChoice == 'y':
        createPassword()
    elif secChoice != 'y':
        pass
createPassword()