class GoogleUser:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.date_of_birth = ""
        self.gender = ""
        self.username = ""
        self.password = ""
        self.phone_number = ""
    def create_account(self):
        print("create your google account")
        self.first_name = input("what is your first name: ")
        self.last_name = input("what is your last name: ")
        self.date_of_birth = input("what is your date of birth, enter in x/x/x format: ")
        self.gender = input("what is your gender, male, female, or prefer not to say: ")
        self.username = input("what is your prefered username, this will be xxxxxxx@gmail.com: ")
        self.password = input("what is your password: ")
        self.phone_number = input("what is your phone number, enter in xxx-xxx-xxxx: ")

    def display_account(self):
        print("this is what your account will look like to others")
        print("name:",self.first_name, self.last_name)
        print("date of birth:",self.date_of_birth)
        print("gender:",self.gender)
        print("email adress:",self.username,"@gmail.com")

newaccount = GoogleUser()
newaccount.create_account()
newaccount.display_account()

