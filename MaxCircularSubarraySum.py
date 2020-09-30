import math
def max_sub_sum(l,n):
    c=0
    for i in range(n):
        if(l[i]<0):
            c+=1
    if(c==n):
        return max(l)
    max_s_s=-math.inf
    t_max_s=0
    arr_s=0
    min_s_s=math.inf
    t_min_s=0
    for i in range(len(l)):
        arr_s+=l[i]
        t_max_s+=l[i]
        if(t_max_s<0):
            t_max_s=0
        if(max_s_s<t_max_s):
            max_s_s=max(max_s_s,t_max_s)
        t_min_s+=l[i]
        if(t_min_s>0):
            t_min_s=0
        if(min_s_s>t_min_s):
            min_s_s=min(min_s_s,t_min_s)
    if(arr_s==min_s_s):
        return max_s_s
    else:
        return max(max_s_s,arr_s-min_s_s)
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    print(max_sub_sum(l,n))