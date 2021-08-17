# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	n=abs(n)
	prev = -1
	while(n>0):
		one=n%10
		n = n//10
		if(prev == one):
			return True
		prev = one
	return False
	# your code goes here
 