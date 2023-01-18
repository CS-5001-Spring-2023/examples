# To generate a random number we will use
# an existing module. Specify that module
# at the top of the program
from random import randint

# Here is how you use the randint function from 
# the random module to generate a random integer
# between 1 and 10.
value = randint(1, 10)
print(value)