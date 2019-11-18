def main():
    t=int(input())
    for i in range(t):
        li=list(map(int,input().split(" ")))
        li.sort(reverse=True)
        print(f"Case {i+1}: {li[0]}")









if __name__=="__main__":
    main()
