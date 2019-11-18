def main():
    try:
        while True:
            n,b,h,w=list(map(int,input().split(" ")))
            b1=False
            ans=0
            for i in range(h):
                p=int(input())
                li=list(map(int,input().split(" ")))
                if p*n<=b:
                    li.sort(reverse=True)
                    if li[0]>=n:
                        b1=True
                        if ans==0:
                            ans=p*n
                        elif p*n<ans:
                            ans=p*n
                    
            if b1 :
                print(ans)
            else:
                print("stay home")       


    except EOFError:
        pass

if __name__=="__main__":
    main()
