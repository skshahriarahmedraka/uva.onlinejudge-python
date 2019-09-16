
n=int(input())
ans=[]
ans2=[]

def gcd(a,b):
    if b==0:
        return a
    else:
       return gcd(b,a%b)

for i in range(n):
    li=list(map(int,input().split(" ")))
    b=1
    for j in range(len(li)):
        if j>0:
            b*=li[j]
    a1=1
    x=li[0]
    del li[0]
    b1=0
    for j in range(x):
        a1*=li[j]
        b1+=int(b/li[j])
    
    x2=gcd(a1*x,b1)
    
    a=int(a1*x/x2)
    b=int(b1/x2)
    print(f"Case {i+1}: {a}/{b}")
    
            
