def main():
    try:
        while True:
            v,t=[int(i) for i in input().split()]
            a=0
            if t!=0:
                a=v/t
            ans=.5*(a)*t**2 + v*t+.5*(a)*t**2
            print(round(ans))
    except EOFError:
        pass
if __name__=="__main__":
    main()