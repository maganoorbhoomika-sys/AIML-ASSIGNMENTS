'''Assignment for today - 7th Feb 2026

Create a strong code for password authentication using python. 

Keep the code ready. We will share the instructions to upload it'''


class PasswordAuth:
    
    def __init__(self, password):
        self.password = password
        self.attempts = 3
    
    def login(self):
        while self.attempts > 0:
            user_pass = input("Enter password: ")
            
            if user_pass == self.password:
                print("Access Granted")
                return
            else:
                self.attempts -= 1
                print("Wrong Password")
                print("Attempts left:", self.attempts)
        
        print("Account Locked")


# Create object
p1 = PasswordAuth("admin123")

# Call method
p1.login()