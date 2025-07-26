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
    
class ListNode:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def Train_Compartment(head):
    for i in range(1, 11):
        compartment = ListNode([[0]*10 for j in range(1,11)])
        # print(compartment.data)
        
        if i == 1:
            head = compartment
        else:
            current = head
            while current.next:
                current = current.next
            current.next = compartment
    return head

def list_compartments(head):
    current = head
    compartment_number = 1
    while current:
        for i in range(len(current.data)):
            for j in range(len(current.data[i])):
                print(current.data[i][j], end=' ')
            print()
        current = current.next
        print(f"---------------")
        compartment_number += 1
    

head = None
head = Train_Compartment(head)
list_compartments(head)

def main():
    
    while True:
        choice = input("Welcome to the User Management System"
        "\nPlease select an option:\n"
        "1. Register\n"
        "2. Login\n"
        "3. Exit\n"
        "Choose an option: ")

        if choice == '1':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user = Register(name, email, password)
            print(user.register())
            if user.register() == "Registration successful":
                print(f"Welcome {name}!")
            


      
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


