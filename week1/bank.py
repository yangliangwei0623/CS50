while(True):
    s = input("Greeting\n")
    if(s.strip().lower().startswith("hello")):
        print("$0")
    elif(s.strip().lower().startswith("h")):
        print("$20")
    else:
        print("$100")