def main():
    t=int(input())
    for i in range(t):
        n=int(input())
        di1={}
        ans=0.0
        for j in range(n):
            a,b=list(map(str,input().split(" ")))
            di1[a]=float(b)
        n2=int(input())
        for j in range(n2):
            s=input()
            for k in range(len(s)):
                if s[k] in di1:
                    ans+=di1[s[k]]
        ans=ans/100
        print(f"{ans:.2f}$")

if __name__=="__main__":
    main()