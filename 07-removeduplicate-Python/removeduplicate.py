# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
    s=[]
    for ch in text:
        if ch not in s:
            s.append(ch)
        
    x=''.join(s)
    return x
    
    
	# Your code goes here
	