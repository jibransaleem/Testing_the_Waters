import re
class Auth:
    def __init__(self):
        self.SignUp()
    def UserName(self):
        self.flag1 = False
        self.username =  input("Enter you name : ")
        pattern = r"^[a-zA-z_ ]*$"
        try: 
            while re.match(pattern,self.username).group() != self.username:
                self.username = input("Enter you name : ")
            self.flag1 = True 
        except Exception as e:
            print(e)
    def Father(self) :
        self.flag2 = False
        self.father = input("Enter your father name : ")
        pattern = r"^[a-zA-z_ ]*$"
        try:
            while re.match(pattern,self.father).group() != self.father:
                self.father = input("Enter you name : ")
            self.flag2 = True
        except Exception as e:
            print(e)
    def Email(self):
        pattern  = r"^\w+@\w+\.[a-z]{3,}$"
        self.flag3 = False
        self.email = input("Enter your email : ")
        try:
            while re.match(pattern,self.email).group() != self.email:
                self.email = input("Enter you email : ")
            self.flag3 = True
        except Exception as e:
            print(e)
    def Password(self):
        self.password =  input("Enter your password  : ")
        self.flag4 = False
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$'
        try:
            while re.match(pattern , self.password).group(0)!= self.password:
                self.password = input("Enter your password  : ")
            self.flag4 = True
            
            self.Saver()
        except Exception as e:
            print(e)
    def Saver(self):
        try :
            if self.flag1 and self.flag2 and self.flag3 and self.flag4:
                data = [self.username,self.father,self.email,self.password]
                with open('data.txt','a+') as f:
                    f.write(str(data)+'\n')
        except Exception as e:
            print(e)
    def SignUp(self):
        confrom = input("Do you wanq to sign up (y/n) : ").lower()
        if confrom == 'y':
            self.UserName()
            self.Father()
            self.Email()
            self.Password()
            retrive_conformation = input("Do you want to retrive your data (y/n) : ").lower()
            if retrive_conformation == 'y':
                self.Retrive()
            else:
                print("Thank you for using our service!")
                return
        else:
            print("Thank you for using our service!")
    def Retrive(self):
        try :
            with open('data.txt','r') as f:
                data = f.read()
            data = eval(data)
            print("--------DETAILS--------")
            print(f"User Name : {data[0]}")
            print(f"Father Name : {data[1]}")
            print(f"Email : {data[2]}")
            print(f"Password : {data[3]}")
            
        except Exception as e:
            print(e)
    
a = Auth()
