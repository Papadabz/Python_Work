# class User:
#     def __init__(self, first_name, last_name, age):
#         """Store user information"""
#         self.fname = first_name
#         self.lname = last_name
#         self.age = age
#         self.login_attempts = 0

#     def describe_user(self):
#         """Describe user information"""
#         print(f"\nFirst: {self.fname.title()}, Last: {self.lname.title()}, Age: {self.age}")

#     def greet_user(self):
#         """Greet each user"""
#         print(f"Hello, {self.fname.title()} {self.lname.title()}")

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0

# danny = User('Daniel', 'Roybal', 30)
# zaira = User('Zaira', 'Roybal', 10)
# zelda = User('zelda', 'roybal', 6)

# danny.describe_user()
# danny.greet_user()
# print(f"{danny.login_attempts}")
# danny.increment_login_attempts()
# print(f"{danny.login_attempts}")
# danny.reset_login_attempts()
# print(f"{danny.login_attempts}")

# zaira.describe_user()
# zaira.greet_user()

# zelda.describe_user()
# zelda.greet_user()

from user import User

class Priveleges:
    """Simple priveleges class"""

    def __init__(self, priveleges):
            self.priveleges = priveleges

    def show_priveleges(self):
         """Display priveleges"""
         for privelege in self.priveleges:
              print(f"- {privelege}")

class Admin(User):
    """Simple admin class"""

    def __init__(self, first_name, last_name, age, priveleges):
        """Initialize admin class and attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.priveleges = Priveleges(priveleges)

    

admin_1 = Admin('Adam', 'Admin', 28, ['can add post', 'can delete post', 'can ban user'])
admin_1.priveleges.show_priveleges()