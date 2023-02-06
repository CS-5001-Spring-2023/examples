"""
Write a program that will prompt a user for a password and verify that it matches a pre-set secret password. As long as the password entered is incorrect prompt the user to re-enter the password.

Modify your solution so that the user can only try to enter the correct password a maximum of three times.
"""
ACTUAL_PASSWORD = "5001ROCKs"
MAX_TRIES = 3


def login():
	
	num_tries = 1

	user_password = input("password: ")
	
	while ACTUAL_PASSWORD != user_password and num_tries < MAX_TRIES:	
		
		print("Invalid password.")
		num_tries += 1		
		user_password = input("password: ")

def main():
	login()

main()






















