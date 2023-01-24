'''
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
'''

def cigar_party(cigars, is_weekend):
	# TODO: Complete during class
	if is_weekend:
		if cigars >= 40:
			return True
		else:
			return False
	else: # elif not is_weekend: 
		# elif !is_weekend <<< you cannot do this!
		if cigars > 60 or cigars < 40:
			return False
		# elif cigars < 40:
		# 	return False
		else: # between 40 and 60
			return True

def main():
	# TODO: complete during class
	# How many tests do we need to do
	# to ensure that our function
	# is correct?
	# 70, True ==> True
	# 55, True ==> True
	# 60, False ==> True
	result = cigar_party(70, True)	
	print(f"c`igar_party(70, True) results in {result}") # expect True

	cigars = int(input("How many cigars? "))
	is_weekend = bool(input("Is it the weekend? "))
	result = cigar_party(cigars, is_weekend)	
	print(f"cigar_party({cigars}, {is_weekend}) results in {result}") 


main()



