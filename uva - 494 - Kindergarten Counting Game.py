def r1(s):
    for i in range(len(s)):
        if not ((s[i]>='a' and s[i]<='z') or (s[i]>='A' and s[i]<="Z")):
            s=s[0:i]+" "+s[i+1:]
    return s
def func(s):
    
    for i in range(len(s)):
        if (s[i] >='a' and s[i]<='z') or (s[i]>='A' and s[i]<='Z') :
            return True
    return False
try:
    while True:
        s=input()
        s=r1(s)
        li=s.split(" ")
        r=0
        for i in range(len(li)):
            if func(li[i]):
                r+=1
        print(r)
    
except EOFError:
    pass