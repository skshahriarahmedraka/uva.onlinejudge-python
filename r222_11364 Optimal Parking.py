t=int(input())
for i in range(t):
    n=int(input())
    
    li=list(map(int,input().split(" ")))
    li.sort()
    print(2*(li[n-1]-li[0]))