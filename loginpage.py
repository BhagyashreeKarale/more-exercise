name=[]    
password=[]    
diary=""    
x =""    
namee=""    
passwordd=""    

file = open("user.txt","a")    
print("welcome to world!")    
while x != "q":    
    print("1) Enter :1 sign in!")    
    print("2) Enter :2 create new soul?")   
    print("3) Enter :q exit!")    
    x = input("what do you want?\n")    
    if x == "1":    
        namee=input("Enter your name!")    
        passwordd=input("Enter your password!")    
        if namee in name:    
            if passwordd not in password or name.index(namee) != password.index(passwordd) :    
                print("wrong password")    
            else:    
                file.write("\n\n\n\n")    
                file.write(namee)    
                file.write("\n\n")    
                diary = input("write your diary\n")    
                file.write(diary)    

        else :    
            print("can't find your name here.\n please create new soul!.")    
    elif x =="2":    
        namee = input("enter you name!")    
        if namee in name:    
            print("user name taken")    
        else:    
            passwordd = input("enter your password")    
            name.append(namee)    
            password.append(passwordd)
    elif x=="q":    
        print("thank you for your time")    
    else :    
        print("please enter valid value!")    
print("thanks.!")    
print(name,password)    
file.close()