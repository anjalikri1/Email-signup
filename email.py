print("sign up your mail here :")
fname=input("Enter your first name here :")
lname=input("Enter your last name here :")
if fname>="A" and fname<="Z" or fname>="a" and fname<="z":
    print("Your first name is: ",fname)
    if lname>="A" and lname<="Z" or lname>="a" and lname<="z":
        print("Your last name is: ",lname)
        print("click next")
        mob=int(input("enter the mobile number:"))
        if mob>=1000000000 and mob<=9999999999:
            print("your mob  number is :",mob)
            print("click next")
            OTP=int(input("enter the 6 digit OTP"))
            if OTP>=100000 and OTP<=999999:
                print("click next")
                print("please choose yoyr date of birth :")
                month=int(input("enter the month"))
                if month>=1 and month<=12:
                    print("Month is :",month)
                    day=int(input("enter the day"))
                    if day>=1 and day<=31:
                        print("date is ",day)
                        year=int(input("enter the year"))
                        if year>=1000 and year<=9999:
                            print("year is",year)
                            print("your date of birth is",day,"/",month,"/",year)
                            print("please enter your gender :")
                            gender=input("enter the gender M/F")
                            if gender=="M" or gender =="F" or gender =="f" or gender =="m":
                                print("your gender is ",gender)
                                print("prpceed to next")
                                print("you are successfully generated your email id")
                            else:
                                print("please select your valid identity")
                        else:
                            print("incorrect year ")
                    else:
                        print("incorrect date")
                else:
                    print("incorrect month")
            else:
                print("enter your valid OTP")
        else:
            print("please enter your 10 digit mobile number")
    else:
        print("make sure your name contain only alphabet letter")
else:
    print("make sure your name contain only alphabet letter")
    


    

