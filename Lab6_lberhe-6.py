"""
Program Name:  User Login System
Author: Lewam Berhe
Purpose: Lab 6 programming assignment for CSCI-1511
Starter Code: None
Date: feburary 24, 2026
"""
users = {
  "mhaile": "summer2026",
  "sberhe": "samdan$",
  "Ktedros": "Kiya2020",
  "guest": "guest"
}

attempt = 3

while attempt > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        if username == "guest":
            security_level = "Guest"
        else:
            security_level = "Security Level 1"
        
        print(f"Welcome, {username}!")
        print(f"Your security level is: {security_level}")
        break  
    else:
        attempt -= 1
        print("Invalid")
        
if attempt == 0:
    print("Too many failed attempts. Account locked")






