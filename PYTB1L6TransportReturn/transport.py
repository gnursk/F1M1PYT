while True:

    import time
    import os

    os.system("cls")
    thislist = ("Factory\nDistrubution\nShop")
    print (thislist)
    thislist2 = ("Factory[car]\nDistrubution[]\nShop[]")
    time.sleep(1)
    os.system("cls")
    print (thislist2)
    thislist3 = ("Factory[]\nDistrubution[car]\nShop[]")
    time.sleep(1)
    os.system("cls")
    print (thislist3)
    thislist4 = ("Factory[]\nDistrubution[]\nShop[car]")
    time.sleep(1)
    os.system("cls")
    print (thislist4)

    if (input("Restart?Y/N") == "Y" or "y"):
        os.system('cls')
        continue
    else:
     break


input()


