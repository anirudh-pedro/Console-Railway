from collections import defaultdict
class Register:
    dic = defaultdict(list)
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
    def register(self):
        if not self.name or not self.email or not self.password:
            return "All fields are required"
        if '@' not in self.email or '.' not in self.email.split('@')[-1]:
            return "Invalid email format"
        if len(self.password) < 6:
            return "Password must be at least 6 characters long"
        if not self.name.isalpha():
            return "Name must contain only letters"
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
        if not self.email or not self.password:
            return "Email and password are required"
        if '@' not in self.email or '.' not in self.email.split('@')[-1]:
            return "Invalid email format"
        
        if self.email not in Register.dic:
            return "Email not registered"
        elif self.password != Register.dic[self.email][0][1]:
            return "Incorrect password"
        else:
            return "Login successful"
        

class BookSeat:
    def __init__(self,seats):
        self.seat = seats
    def display_compartments(self):
        # head = Train_Compartment(None)
        # list_compartments(head)
        # print(f"Total compartments: {self.seat}")
        # print("Seats available in each compartment:")
        # for i in range(1, self.seat + 1):
        #     print(f"Compartment {i}: 10 seats")
        pass
    
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
    c = 'A'
    while current:
        print(f"*********** Compartment {c} *************")
        for i in range(len(current.data)):
            print(" "*10,end = "")
            for j in range(len(current.data[i])):
                print(current.data[i][j], end=' ')
            print()
        c = chr(ord(c) + 1)

        current = current.next
        print(f"---------------")
        compartment_number += 1
    


# head = None
# head = Train_Compartment(head)
# list_compartments(head)

def main():
    head = None
    head = Train_Compartment(head)
    while True:
        print("*"*20)
        choice = input("Choose an option:\n1. Register\n2. Login\n3. Exit\nEnter your choice: ")
        print("*"*20)

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
            res = user.check_login()
            print(res)
            if res == "Login successful":

                print("*"*20)
                print("how many seats do you want to book?")
                num_seats = int(input("Enter the number of seats you want to book: "))
                print("*"*20)
                d = BookSeat(num_seats)
                break

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

    print("*"*20)
    print("Welcome to the Train Seat Booking System!")
    print("*"*20)
    
    list_compartments(head)
    print("how many seats do you want to book?")
    num_seats = int(input("Enter the number of seats you want to book: "))
    d = BookSeat(num_seats)
            
if __name__ == "__main__":
    main()


