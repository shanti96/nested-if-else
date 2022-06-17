age=int(input("enter age"))
sex=input("enter sex")
marital=input("enter status")
if marital=="yes"or marital=="no":
    if sex=="F":
        print("work in urban areas")
    elif sex=="M"and age>=20 and age<=40:
        print("work in anywhere")
    elif sex=="M"and age>=40 and age<=60:
        print("work in urban only") 
else:
    print("not")               