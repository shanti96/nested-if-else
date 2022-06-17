year=int(input("enter the year"))
if year%4==0:
    if year%400==0 and year%100==0:
        print("leap year and century year")
    elif year%100!=0:
        print("leap year")
else:
    print("not")            