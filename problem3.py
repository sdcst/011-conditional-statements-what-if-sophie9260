#! python3

"""
 Have the user enter a username 
 If the username is not "admin" then tell them it is an "invalid user", 
 but if it is, then ask them for a password 
 If they get the password correct (password is 12345password) 
 then display the message "Access granted"
 1 marks

 Example:
 Enter username: admin
 Enter password: 12345password
 Access granted

 Enter username: notadmin
 invalid user

 Enter username: admin
 Enter password: password
 Access denied
"""
username = input("Enter an username => ")

if username == "admin":
    password = input("Enter the password => ")
    if password == "12345password":
        print("Access granted")
    else:
        print("Access denied")
else:
    print("Invalid username")