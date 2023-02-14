import sys

def search_replace(search, replace, infilename, outfilename):
	"""
	Write a function that will replace all instances of a search
	term in a given file with a replace term. The result will be 
	saved to a new file.
	
	Parameters:
	search : str
		the string to replace
	replace : str
		the replacement string
	infilename : str
		the name of the original file
	outfilename : str
		the name of the file where the result will be saved
	"""
	inputfile = open(infilename, "r")
	outputfile = open(outfilename, "w")
	for line in inputfile:		
		output_line = line.replace(search, replace)
		outputfile.write(output_line)
		# outputfile.write(line.replace(search, replace))
	inputfile.close()
	outputfile.close()

search_replace("a", "b", "c", "d")

def main():
	# The search term, replace term, input file name, and output file name
	# will be passed as command line parameters.
	if len(sys.argv) != 5:
		print("usage: python3 file_io.py <search> <replace> <infilename> <outfilename>")
		exit()

	search_replace(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


main()
