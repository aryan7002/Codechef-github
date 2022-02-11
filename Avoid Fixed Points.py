for _ in range(int(input())):
    n  = int(input())
    a  = list(map(int, input().split()))
    
    k = 0
    for i in range(n):
        v = 1+i+k
        if v  == a[i]:
            k+=1
    print(k)