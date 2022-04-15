"""
author : Mehmet Baran Munar
"""

import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    
    def __init__(self):
        self.users = list()
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUsers()
    
    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding="utf-8") as f:
                users = json.load(f)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'] )
                    self.users.append(newUser)
            
        
    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("User Created.")
    
    def login(self, username, password):
        
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Login Successful!")
                break
    
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Logout Successful!")
    
    def identity(self):
        if self.isLoggedIn: 
            print(f"Username: {self.currentUser.username}")
        else:
            print("Not logged in!")
        
    def savetoFile(self):
        listt = list()

        for user in self.users:
            # user is class, we need to convert it to dict.
            listt.append(json.dumps(user.__dict__))

        with open("users.json", "w") as f:
            json.dump(listt, f)

repository = UserRepository()

while True:
    print("Menu".center(50, '*'))
    choice = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nYour choice:")
    
    if choice == '5':
        break 
    else:
        if choice == '1':
            # register
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")
            user = User(username=username, password=password, email=email)
            repository.register(user)

            #print(repository.users)
        elif choice == '2':
            # login
            if repository.isLoggedIn:
                print("You already logged in.")
            else:
                username = input("Username: ")
                password = input("Password: ") 
                repository.login(username, password)
        elif choice == '3':
            # logout
            repository.logout()
            
        elif choice == '4':
            # display username
            repository.identity()
        else:
            print('Incorrect Choice!')
