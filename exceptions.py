result = input("Give me a float: ")

# if result is a float:
# 	result_float = float(result)
# else:
# 	print("error -- you didn't give me a float")

try:
	result_float = float(result)
	print(f"You entered {result_float}.")
except:
	print("error -- you didn't give me a float")	



"""
try:
  print(x)
except:
  print("An exception occurred")
 """