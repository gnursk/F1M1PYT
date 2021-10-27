while True:
    print ("Hello you!, Nick")
    print ("Wie ben jij?")
    name = input ("Hello + name")
    print ("Hello" + name)

    import datetime
    import os

    x = datetime.datetime.now()
    print ("de tijd en datum zijn:")
    print (x)
    if (input("Wil je restarten?") == "Y"):
        os.system('cls')
        continue
    else:
     break

input()