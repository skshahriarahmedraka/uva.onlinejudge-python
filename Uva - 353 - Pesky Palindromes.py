def pal(s2):
    s2len=len(s2)
    j=(s2len//2)-1
    if s2len==1:
        return True
    if s2len%2==0:
        x=s2[j+1:]
        x=x[::-1]
        if s2[:j+1]==x:
            return True
    else:
        x=s2[j+2:]
        x=x[::-1]
        if s2[:j+1]==x:
            return True
    return False
def main():
    try:
        while True:
            s=input()
            if len(s)==0:
                print(f"The string '{s}' contains {0} palindromes.")
                continue
            li=[]
            slen=len(s)
            for i in range(slen):
                for j in range(i,slen):
                    s1=s[i:j+1]
                    #print(s1)
                    if len(s1)!=0 and (not(s1 in li) ):
                        if pal(s1)  :
                            li.append(s1)
                        
                    
                    
            # print(li)   
            print(f"The string '{s}' contains {len(li)} palindromes.")
            
    except EOFError:
        pass
if __name__=="__main__":
    main()
