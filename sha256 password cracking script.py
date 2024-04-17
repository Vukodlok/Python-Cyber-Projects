
from pwn import *
import sys

if len(sys.argv) != 2:
    print("Invalid arguments!")
    print(">> {} <sha256sum>".format(sys.argv[0])))
    exit()

wanted_hash = sys.argv[1]
password_file = "rockyou.txt"
attempts = 0

with log.process("Attempting to back: {}!\n".format(wanted_hash)) as p:
    with open(password_file, "r", encoding='latin-1') as password_list:
        password = password.strip("\n").encode('latin-1')