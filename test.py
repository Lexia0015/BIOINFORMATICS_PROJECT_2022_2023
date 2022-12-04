# importing the sys module
import sys

# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs

sys.setrecursionlimit(10**6)

# a simple recursive function
# to compute the factorial of a number
# it takes one parameter, the
# number whose factorial we
# want to compute and returns
# its factorial
def fact(n):

	if(n == 0):
		return 1

	return n * fact(n - 1)

if __name__ == '__main__':

	# taking input
	f = int(input('Enter the number: \n'))

	print(fact(f))
