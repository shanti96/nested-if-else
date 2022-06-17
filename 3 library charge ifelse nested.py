x_date=int(input("enter expected date"))
x_month=int(input('enter expected month'))
x_year=int(input("enter expected year"))
re_date=int(input("enter return date"))
re_month=int(input("enter return month"))
re_year=int(input("enter return year"))
if x_month==re_month and x_year==re_year:
    if re_date<=x_date:
        print("no fine")
    else:
        print("total fine=",(re_date-x_date)*15) 
elif re_year==x_year and re_month>x_month:
    if x_month==1 or x_month==3 or x_month==5 or x_month==7 or x_month==8 or x_month==10 or x_month==12:
        a=(31-x_date)+re_date
        print("total fine=",a*500) 
    elif x_month==4 or x_month==6 or x_month==9 or x_month==11:
        a=(30-x_month)+re_date
        print("total fine=",a*500)
    elif x_month==2:
        a=(28-x_date)+re_date
        print("total fine=",a*500) 
else:
    print("one year late fine=10000")           