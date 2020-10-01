def maxdiff_pair(l,n,tar):
    if(n<2):
        return -1
    i=0
    j=1
    while(i<len(l) and j<len(l)):
        if(abs(l[i]-l[j])<tar):
            j+=1
        elif(abs(l[i]-l[j])>tar):
            i+=1
        else:
            return 1
    return -1

for _ in range(int(input())):
    n,tar=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    f=maxdiff_pair(l,n,tar)
    print(f)
