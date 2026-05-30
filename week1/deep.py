while(True):
    ans = input("What is the answer to the Ultimate Question of Life, The Universe, and Everything? ")
    try:
        if int(ans) == 42:
            print("Yes")
            break
    except ValueError:
        pass
    if ans.lower() == "forty-two":
        print("Yes")
        break
    elif ans.lower() == "forty two":
        print("Yes")
        break
    else:
        print("No")