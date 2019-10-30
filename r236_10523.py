def main():
    try:
        while True:
            a,b=list(map(int,input().split(" ")))
            sum=0
            for i in range(1,a+1):
                sum+=i*pow(b,i)
            print(sum)
    except EOFError:
        pass
if __name__=="__main__":
    main()
