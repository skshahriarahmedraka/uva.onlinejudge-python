def main():
    t=int(input())
    for i in range(t):
        n=int(input())
        result=0
        for j in range(n):
            a,b,c=[int(i) for i in input().split()]
            result+=(a*c)
        print(result)

if __name__=="__main__":
    main()