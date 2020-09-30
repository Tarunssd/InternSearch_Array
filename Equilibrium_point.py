def equilibrium(l,n):
    if(n==1):
        return 1
    sum1=l[0]
    sum2=l[-1]
    i=0
    j=n-1
    while(i<j-1):
        if(sum1==sum2 and j-i==2):
            return i+2
        if(sum1>sum2):
            j-=1
            sum2+=l[j]
        else:
            i+=1
            sum1+=l[i]
    return -1

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    e=equilibrium(l,n)
    print(e)
