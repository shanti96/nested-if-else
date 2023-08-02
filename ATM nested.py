atm_card=input("insert the atm card ")
if atm_card=="right side" or atm_card=="RIGHT SIDE":
    language=input("select language ")
    if language=="english" or language=="ENGLISH" or language=="hindi" or language=="HINDI":
        pin=int(input("enter the pin code "))
        if pin>=1000 and pin<=9999:
            type_option=input("select the transation option ")
            if type_option=="withdraw" or type_option=="WITHDRAW":
                account_type=input("select the account type ")
                if account_type=="savings" or account_type=="SAVINGS":    
                    withdraw=int(input("enter eithdraw money "))
                    if withdraw<=500 and withdraw<=20000:
                        press_key=input("pressing the keypad ok ")
                        amount=int(input("enter amount "))
                        if amount>=500 and amount<=2000 and amount%500==0:
                            a=withdraw//2000
                            b=withdraw%2000
                            c=b//500
                            print("total 2000 note=",a,"total 500 notes=",c)
                            end_session=input("withdrew compelet pressing the cancel")
                            if end_session=="cancel" or end_session=="cross button":
                                print("all transetion succesful")
                            else:
                                print("please cancel the transection session")    
                        else:
                            print("amount not are avelable")
                    else:
                        print("current balance not avelable")
                else:
                    print("please select account type") 
            elif type_option=="balance enquiry" or type_option=="BALANCE ENQUIRY":
                account_type=input("select account type ")
                if account_type=="current" or account_type=="saving":
                    account_no=int(input("enter account number "))
                    if account_no>=100000000000 and account_no<=999999999999:
                        press_key=input("press ok")
                        if press_key=="ok" or press_key=="OK":
                            session_end=input("enter cancel button ")
                            if session_end=="cancel" or session_end=="CANCEL":
                                print("balance chcking succesful")
                            else:
                                print("please cancel button press")
                        else:
                            print("please press ok button")
                    else:
                        print("account number not currect")        
                else:
                    print("selsect account type") 
            elif type_option=="deposit money" or type_option=="DEPOSIT MONEY":
                account_type=input("selsect account type ")
                if account_type=="current" or account_type=="saving" :
                    account_no=int(input("enter account number "))
                    if account_no>=10000000000 and account_no<=99999999999:
                        enter_money=int(input("enter the money "))
                        key_press=input("press the ok ")
                        if key_press=="ok" or key_press=="OK" :
                            print("deposit money transaction compelet")
                        else:
                            print("please press ok")
                    else:
                        print("worng account number")
                else:
                    print("please selsect the account type") 
            elif type_option=="billpay" or type_option=="billpay" :
                account_no=int(input("enter the account number "))
                if account_no>=10000000000 and account_no<=99999999999:
                    bill_id=int(input("enter the bill id number "))
                    if bill_id>=10000000000 and bill_id<=99999999999:
                        amount=int(input("enter the bill amount "))
                        press_key=input("press ok button ")
                        if press_key=="ok" or press_key=="OK" :
                            print("bill transaction compelet")
                        else:
                            print("please press ok button")
                    else:
                        print("wrong bill id number")
                else:
                    print("wrong account number")
            else:
                print("select right transaction option") 
        else:
            print("wrong pin number")
    else:
        print("please select language")
else:
    print("wrong side atm card insert")                                                                                                                                                 
