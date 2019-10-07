d1={
"HELLO":"ENGLISH" ,
"HOLA":"SPANISH" ,"HALLO":"GERMAN","BONJOUR" :"FRENCH","CIAO": "ITALIAN","ZDRAVSTVUJTE" :"RUSSIAN"

}
i=1
while True:
    s=input()
    if s=="#":
        break
    elif s in d1.keys():
        print(f"Case {i}: {d1[s]}")
    else:
        print(f"Case {i}: UNKNOWN")
    i+=1
