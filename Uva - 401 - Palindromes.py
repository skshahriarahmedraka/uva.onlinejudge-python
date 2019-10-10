def main():
    dic={
        "A":"A","B":"","C":"","D":"","E":"3","F":"","G":"","H":"H","I":"I","J":"L"
        ,"K":"","L":"J","M":"M","N":"","O":"O","P":"","Q":"","R":"","S":"2","T":"T",
        "U":"U","V":"V","X":"X","W":"W","Y":"Y","Z":"5","1":"1","2":"S","3":"E","4":'',"5":"Z","6":"","7":"","8":"8","9":''
    }
    try:
        while True:
            s=input()
            slen=len(s)

            pal=True
            mir=True
            if slen==0:
                return
        
            for i in range(slen//2 +1):
                if s[i]!=s[slen-i-1]:
                    pal=False
                    break
            
            for i in range(slen//2 +1):
                if dic[s[i]]!=s[slen-i-1]:
                    mir=False
                    break
            if pal and mir:
                print(f"{s} -- is a mirrored palindrome.")
                print("")
            elif not pal and mir:
                print(f"{s} -- is a mirrored string.")
                print("")
            elif pal and not mir:
                print(f"{s} -- is a regular palindrome.")
                print("")
            elif not pal and not mir:
                print(f"{s} -- is not a palindrome.")
                print("")
    except EOFError:
        pass


if __name__=="__main__":
    main()
