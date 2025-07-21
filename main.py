from collections import defaultdict
class Register:
    dic = defaultdict(list)
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
    def register(self):
        if self.email in self.dic:
            return "Email already registered"
        else:
            self.dic[self.email].append([self.name,self.password])
            return "Registration successful"
class Login:
    def __init__(self,email,password):
        self.email = email
        self.password = password    
    def check_login(self):
        if self.email not in Register.dic:
            return "Email not registered"
        elif self.password != Register.dic[self.email][0][1]:
            return "Incorrect password"
        else:
            return "Login successful"
    

def main():
    while True:
        choice = input("Choose an option: 1. Register 2. Login 3. Exit: ")
        if choice == '1':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user = Register(name, email, password)
            print(user.register())
        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user = Login(email, password)
            print(user.check_login())
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

            
if __name__ == "__main__":
    main()


