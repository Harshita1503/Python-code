'''A player can win only when his/her beyblade power is strictly greater than the opponents beyblade power.
The first line of input consists of the number of test cases, T
The first line of each test case consists of the number of members each team can have, N.
The second line of each test case consists of N space-separated integers representing the power of beyblades of Team G-Revolution members.
The third line of each test case consists of N space-separated integers representing the power of beyblades of opponent team members.'''
def main():
    t=int(input())
    while t>0:
        count=0
        n=int(input())
        power_g=list(map(int,input().split()))
        power_o=list(map(int,input().split()))
        power_g.sort(reverse=True)
        power_o.sort(reverse=True)
        p=0
        for i in range(n):
            for j in range(p,n):
                if power_g[i]>power_o[j]:
                    p=j+1
                    count+=1
                    break
        print(count)
        t-=1


main()


