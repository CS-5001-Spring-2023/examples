
# Conditions -- rock/paper/scissors

def main():
	# ask the user for a number between 1 and 10
	# if the number is larger than 10 tell the user too high
	# if the number is smaller than 1 tell the user too low

	number = int(input("Enter a number between 1 and 10: "))

	if(number >= 1 and number <= 10):
		print("Your number is in range.")
	else:
		print("Your number is out of range.")



	# if(number > 10):
	# 	print("Your number is too high.")
	# 	if(number > 100):
	# 		print("Whoa!")			
	# elif(number < 1):
	# 	print("Your number is too low.")
	# elif(number == 5):
	# 	print("Your number is 5.")
	# else:
	# 	print("Your number is just right...")

	# print("Done!")



main()