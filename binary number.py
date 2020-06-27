'''The binary representation of 5 is 101, so the maximum number of consecutive 1's is .

Sample Case 2:
The binary representation of13  is 1101, so the maximum number of consecutive 2's is .'''


if __name__ == '__main__':
    n = int(input())
    highest=0
    onescounter=0
while n>0:
    if n%2==1:
        onescounter+=1
        if onescounter>highest:
            highest=onescounter
    else:
        onescounter=0
    n=n//2
print(highest)        

 
