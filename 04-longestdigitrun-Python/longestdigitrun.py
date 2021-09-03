# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestDigitRun(n):
    n=abs(n)
    longestRun=1
    longestRunDigit=n%10
    currentRun=1
    index=n
    counter=0
    while(index!=0):
        index//=10
        counter+=1
    if (counter==1):
        return 1
    for j in range(0,counter):
        temp1=n%10
        n=n//10
        temp2=n%10
        if (temp1==temp2):
            currentRun+=1
        elif(currentRun>longestRun):              
            longestRun=currentRun
            longestRunDigit=temp1
            currentRun=1
        elif(currentRun==longestRun and temp1<longestRunDigit):
            longestRunDigit=temp1
            currentRun=1
        else:
            currentRun=1;
    return longestRunDigit
print(longestDigitRun(int(input())))