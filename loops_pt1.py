
# A sample code fragment that prompts the user for 
# a word until it matches the computer's secret
# word

secret_word = "banana"

response = input("Try to guess my word: ")
while secret_word != response:
	print("No match")
	response = input("Try to guess my word (again): ")

print("winner winner!")


# A sample code fragment that prints all
# numbers from 1 to end (inclusive)
end = 10

current_index = 1 #control variable
while current_index <= end: #condition
	print(current_index)
	current_index += 1 #update control variable

# Two different ways of writing a code 
# fragment that prints all evens between
# 2 and end (inclusiv)

end = 100
current_index = 2
while current_index <= end:
	print(current_index)
	current_index += 2
	# current_index = current_index + 2


end = 100
current_index = 2
while current_index <= end:
	if current_index % 2 == 0:
		print(current_index)
	current_index += 1	


'''
Write a function called count_up that takes a 
positive integer as a parameter and then 
prints all of the numbers between 1 and 
that integer (both inclusive)
'''


'''
Write a function called print_evens that prints the even numbers from 2 to 100 (inclusive).
'''




