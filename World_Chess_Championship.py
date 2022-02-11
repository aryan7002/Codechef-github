for _ in range(int(input())):
    n = int(input())
    s  = str(input())
    if s.count('1')%2==0 or s.count('0')%2==0: 
        print("YES")
    else:
        print("NO")
        