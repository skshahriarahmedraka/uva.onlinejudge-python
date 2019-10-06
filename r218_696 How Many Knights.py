from math import ceil
def main():
    while True:
        r,c=list(map(int,input().split(" ")))
        if r+c==0:
            break
        elif r*c==0:
            print(f"{0} knights may be placed on a {r} row {c} column board.")
        elif r*c==4:
            print(f"{4} knights may be placed on a {r} row {c} column board.")
        elif r*c==3:
            print(f"{3} knights may be placed on a {r} row {c} column board.")
        elif r*c==2:
            print(f"{2} knights may be placed on a {r} row {c} column board.")
        elif r*c==1:
            print(f"{1} knights may be placed on a {r} row {c} column board.")
        elif min(r,c)==2:
            x=max(r,c)
            if x%4==0:
                z=(x/4)*4
            elif x%4==1:
                z=(x//4)*4+2
            elif x%4==2:
                z=(x//4)*4+4
            elif x%4==3:
                z=(x//4)*4+4
            print(f"{int(z)} knights may be placed on a {r} row {c} column board.")
        elif min(r,c)==1:
            x=max(r,c)
            print(f"{x} knights may be placed on a {r} row {c} column board.")
        elif r*c==6:
            print(f"{4} knights may be placed on a {r} row {c} column board.")
        elif r*c==5:
            print(f"{5} knights may be placed on a {r} row {c} column board.")
        
        elif r>=3 and c>=3:
            x1=r//2
            y1=ceil(r/2)
            x2=c//2
            y2=ceil(c/2)
            z=(x1*x2+y1*y2)
            print(f"{z} knights may be placed on a {r} row {c} column board.")
        
            


if __name__=="__main__":
    main()