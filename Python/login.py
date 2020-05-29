import sys
import time

#get the username from an argument
username = sys.argv[1] + ' ' + sys.argv[2]
#list of allowed users
user1 = "Ami Zaga"
user2 = "Eliran Zaga"
users_list = [user1, user2]

#control that the user belongs to the list of allowed users
print("Check the access..")
time.sleep(3)
if username in users_list:
    print("Access grented.")
    print("")
    print("Hello", username)
    print("Have a nice shift")
else:
    print("Access denied")
