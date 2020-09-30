def subarray(l,n,tar):
    currsum=l[0]
    start=0
    i=1
    while(i<=n):
        while(currsum>tar and start<i-1):
            currsum-=l[start]
            start+=1
        if(currsum==tar):
            print(start+1,i)
            return 1
        if(i<n):
            currsum+=l[i]
        i+=1
    print(-1)
    return 0
t=int(input())
while(t):
    n,tar=map(int,input().split())
    l=list(map(int,input().split()))
    subarray(l,n,tar)
    t-=1   
