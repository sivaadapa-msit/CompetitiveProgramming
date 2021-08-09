# dicetoorderedhand(a, b, c) [5pts]
# Write the function dicetoorderedhand(a, b, c) that takes 3 dice and
# returns them in a hand, which is a 3-digit integer. However, even if the
# dice are unordered, the resulting hand must be ordered so that the largest
# die is on the left and smallest die is on the right. For example:
# assert(dicetoorderedhand(1,2,3) == 321)
# assert(dicetoorderedhand(6,5,4) == 654)
# assert(dicetoorderedhand(1,4,2) == 421)
# assert(dicetoorderedhand(6,5,6) == 665)
# assert(dicetoorderedhand(2,2,2) == 222)


def dicetoorderedhand(a, b, c):
    largest= max(a,b,c)
    smallest= min(a,b,c)
    middle= (a+b+c)-largest-smallest
    return largest*100+middle*10+smallest
	# your code goes here
 
# def dicetoorderedhand(a, b, c): 
# 	s=sorted((a,b,c),reverse=True)
# 	return s[0]*100+s[1]*10+s[2]
