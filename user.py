class User:
    def __init__(self, first_name, last_name, age):
        """Store user information"""
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Describe user information"""
        print(f"\nFirst: {self.fname.title()}, Last: {self.lname.title()}, Age: {self.age}")

    def greet_user(self):
        """Greet each user"""
        print(f"Hello, {self.fname.title()} {self.lname.title()}")