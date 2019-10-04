def main():
    while True:
        x1,y1,x2,y2=list(map(int,input().split(" ")))
        if x1==0 and x2==0 and y1==0 and y2==0:
            break
        if x1==x2 and y2==y1:
            print("0")
        elif x1==x2 or y1==y2 or(abs(x1-x2)==abs(y1-y2)):
            print("1")
        else:
            print("2")
if __name__=="__main__":
    main()
