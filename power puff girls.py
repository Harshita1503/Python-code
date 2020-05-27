'''The first line of input consists of the number of ingredients, N
The second line of input consists of the N space-separated integers representing the quantity of each ingredient required to create a Powerpuff Girl.
The third line of input consists of the N space-separated integers representing the quantity of each ingredient present in the laboratory.
There are N ingredients required in a certain quantity to create a Powerpuff Girl.
Professor has all the N ingredients in his laboratory and knows the quantity of each available ingredient. 
He also knows the quantity of a particular ingredient required to create a Powerpuff Girl.
Professor is busy with the preparations and wants to start asap.'''




def main():
    n=int(input())
    q=list(map(int,input().split()))
    t=list(map(int,input().split()))
    l=[]
    for i in range(0,len(t)):
        data=t[i]//q[i]
        l.append(data)
    print(min(l))

main()
