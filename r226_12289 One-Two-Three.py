n=int(input())
# li1=["o","n","e"]
# li2=["t","w","o"]
#li3=["t","h","r","e","e"]
for i in range(n):
    s=input()
    if len(s)==5:
        print(3)
    elif len(s)==3:
        if s=="one":
            print(1)
        elif s=="two":
            print(2)
        
        
        elif s[0] == "o" and s[1] == "n" and s[2] != "e" :
            print(1)
        elif s[0] == "o" and s[1] != "n" and s[2] == "e" :
            print(1)
        elif s[0] != "o" and s[1] == "n" and s[2] == "e" :
            print(1)
        else:
            print(2)
    