def main():
    try:
        while True:
            s1={int(i) for i in input().split()}
            s2={int(i) for i in input().split()}
           
            if s1==s2:
                print("A equals B")
            elif s2.issubset(s1):
                print("B is a proper subset of A")
            elif s1.issubset(s2):
                print("A is a proper subset of B")
            elif s1.isdisjoint(s2):
                print("A and B are disjoint")
            else:
                print("I'm confused!")
    except EOFError:
        pass

if __name__=="__main__":
    main()