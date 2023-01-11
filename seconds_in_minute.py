SECONDS_IN_A_MINUTE = 60

def main():
	# seconds = int(input("How many seconds? "))

	seconds_str = input("How many seconds? ")
	seconds = int(seconds_str)
	
	minutes = seconds // SECONDS_IN_A_MINUTE 
	left_over_seconds = seconds % SECONDS_IN_A_MINUTE
	
	print(f"{seconds} seconds is {minutes} minutes with {left_over_seconds} second remaining")

main()








