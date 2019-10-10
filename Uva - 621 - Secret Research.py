n=int(input())
for i in range(n):
    s=input()
    slen=len(s)
    if s=="1" or s=="4" or s=="78":
        print("+")
    elif s[slen-2: ] =="35":
        print("-")
    elif s[0]=="9" and s[slen-1]=="4":
        print("*")
    elif s[0:3]=="190":
        print("?")
    else:
        print("?")
