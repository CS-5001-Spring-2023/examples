"""
Write a program that will prompt a user for a password and verify that it matches a pre-set secret password. As long as the password entered is incorrect prompt the user to re-enter the password.

Modify your solution so that the user can only try to enter the correct password a maximum of three times.
"""
ACTUAL_PASSWORD = "5001ROCKs"

def main():
	user_password = input("password: ")
	num_tries = 1

	while ACTUAL_PASSWORD != user_password:	
		print("Invalid password.")
		user_password = input("password: ")
		# response = input("password: ") 

	print("Successful login")


main()






















