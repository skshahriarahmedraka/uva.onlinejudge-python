
def main():
    try:
        while True:
            n,m=list(map(int,input().split(" ")))
            if(n==0 and m==0):
                break
            li=list(map(int,input().split(" ")))
            li2=[]
            for i in range(m-1):
                for j in range(i+1,m):
                    li2.append(abs(li[i]-li[j]))
            li3=[i for i in range(1,n+2)]
            b=True
            for i in range(n):
                if not(li3[i] in li2):
                    b=False
                    break
            # print(li)
            # print(li2)
            # print(li3)
            if b:
                print("Y")
            else:
                print("N")
    except EOFError:
        pass


if __name__=="__main__":
    main()