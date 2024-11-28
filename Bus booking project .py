h=0
h1=0
h2=0
busplace=["Buses From Bangalore To Chennai, Hyderabad, Coimbatore, Mumbai, Goa","Buses From Chennai To Bangalore, Coimbatore, Madurai, Hyderabad, Trichy","Buses From Hyderabad To Bangalore, Chennai, Mumbai, Pune, Vijayawada","Buses From Pune To Goa, Bangalore, Nagpur, Hyderabad, Mumbai","Buses From Delhi To Lucknow, Dehradun, Manali, Kanpur, Jaipur","Buses From Mumbai To Bangalore, Goa, Pune, Indore, Ahmedabad","Buses From Coimbatore To Chennai, Bangalore, Madurai, Pondicherry, Nagercoil","Buses From Kolkata To Durgapur, Asansol, Siliguri, Bhubaneshwar, Bardhaman"]
nn=[]
n1=[]
n2=[]
# def ACbusbill(m):
#     m=m-5
#     print("name      :",nn[m])
#     m=m+1
#     print("mobile no :",nn[m])
#     m=m+1
#     print("address   :",nn[m])
#     m=m+1
#     print("Place     :",nn[m])
#     m=m+1
#     print("no of seat:",nn[m])
#     m=m+1
#     print("payment   :",nn[m])
#     print(" ")

# def normalbusbill(m):
#     m=m-5
#     print("normal bus")
#     print("name      :",n1[m])
#     m=m+1
#     print("mobile no :",n1[m])
#     m=m+1
#     print("address   :",n1[m])
#     m=m+1
#     print("place     :",n1[m])
#     m=m+1
#     print("no of seat:",n1[m])
#     m=m+1
#     print("payment   :",n1[m])
#     print(" ")
# def touristbusbill(m):
#     m=m-4
#     print("name      :",n2[m])
#     m=m+1
#     print("mobile no :",n2[m])
#     m=m+1
#     print("address   :",n2[m])
#     m=m+1
#     print("place     :",n2[m])
#     m=m+1
#     print("bus count :",n2[m])
#     print(" ")
#     print(" ")
def ACbus():
    l1=len(nn)
    if(0<l1):
        try:    
            for m in range(0,l1,6):
                print("name      :",nn[m])
                m=m+1
                print("mobile no :",nn[m])
                m=m+1
                print("address   :",nn[m])
                m=m+1
                print("Place     :",nn[m])
                m=m+1
                print("no of seat:",nn[m])
                m=m+1
                print("payment   :",nn[m])
                print(" ")
                if(l1==m):
                    break
        except:
            print(" ")
def normalbus():
    l1=len(n1)
    if(0<l1):
        try:   
            for m in range(0,l1,6):
                print("normal bus")
                print("name      :",n1[m])
                m=m+1
                print("mobile no :",n1[m])
                m=m+1
                print("address   :",n1[m])
                m=m+1
                print("place     :",n1[m])
                m=m+1
                print("no of seat:",n1[m])
                m=m+1
                print("payment   :",n1[m])
                print(" ")
                if(l1!=m):
                     break
        except:
            print("good")
def touristbus():
    l1=len(n2)
    if(0<l1):
        for m in range(0,l1,5):
            print("name      :",n2[m])
            m=m+1
            print("mobile no :",n2[m])
            m=m+1
            print("address   :",n2[m])
            m=m+1
            print("place     :",n2[m])
            m=m+1
            print("bus count :",n2[m])
            print(" ")
            print(" ")
            if(l1==m):
                break
def busroute(t,placeadd):
    seat=["13","23","33","43","53","63","73"]
    for i in busplace:
        print(i)
    a=input("where are you going ?")
    placeadd=placeadd+1
    nn.insert(placeadd,a)
    for k in range(1,37):
        print(" ")
        if(t==1):
            print("per seat prize : 2000")
        elif(t==2):
            print("per seat prize : 1000")
        else:
            for i in busplace:
                print(i)
            where=input("where are you going :")
            placeadd=placeadd+1
            n2.insert(placeadd,where)    
            tourbuscount=int(input("How many bus you need ?"))
            print("contact this number : 9994654719")
            placeadd=placeadd+1
            n2.insert(placeadd,tourbuscount)
            return placeadd+1
            break
        print(" ")
        print("Select seats")
        print("booked seat",seat)
        for i in range(1,8):
            for j in range(1,8):
                if(1<=j<=2 or 4<=j<=8):
                    print("(",i,j,")",end=" ")
                else:
                    print(" ",end=" ")
            print("")
        s=input("seat no :")
        ss=0
        if(s in seat):
            print(" ")
            print("this seat already booked")
            print("give anther seat no? : ")
            ss=input()
            seat.insert(1,ss)
        if(s!=ss):
            seat.insert(1,s)
        print(" ")
        print(" ")
        print("Are you want to book anthor seat")
        print()
        a=int(input("1 YES 2 NO : "))
        if(a==1):
            print(" ")
            print(" ")
            print("thank you for anthor booking!")
            continue
        else:
            print(" ")
            return k
            break
print("*********************Welcome to KK travels******************")
print("    Difficult Roads Often Leads To Beautiful Destinations :)")
for i in range(0,50):
    print(" ")
    print("1.Bus booking ")
    print("2.private User")
    print("3.Exit")
    print(" ")
    a=int(input("what am i help you ?\n"))
    print(" ")
    if(a==1):
        a=0
        print(" ")
        print("what type of bus are you want ?")
        print("1 A/C bus")
        print("2 non A/C bus")
        print("3 tourist bus")
        print("4.Exit\n")
        print(" ")
        a=int(input())
        if(a==1):
            print(" ")
            name=input("Enter your name ? ")
            nn.insert(h,name)
            number=int(input("Enter mobile no :"))
            h=h+1
            nn.insert(h,number)
            place=input("Enter your place :")
            h=h+1
            nn.insert(h,place)
            pay1=busroute(1,h)
            h=h+2
            nn.insert(h,pay1)
            pay1=pay1*2000
            print("your bill : ",pay1)
            paid=int(input())
            pay1=pay1-paid
            if(pay1==0):
                print(" ")
                print("Arriving time:11.10PM AND Destination time:5.00AM ")
                print("you booked a  KK travels and your bus no is TN90KK0001 and contact no:7708645719 ")
                h=h+1
                nn.insert(h,"paid")
                print(" ")
            else:
                while(0!=pay1):
                    print("still your payment is pending \n1 pay \n2 exit\n",pay1)
                    yn=int(input())
                    if(yn==1):
                        while(0!=pay1):
                            print("still your bill pending :",pay1)
                            paid=int(input())
                            pay1=pay1-paid
                            if(pay1==0):
                                print("Arriving time:11.10PM AND Destination time:5.00AM ")
                                print("you booked a  KK travels and your bus no is TN90KK0001 and contact no 7708645719")
                                print(" ")
                                print("Thank you for choosing our KK travels")
                                h=h+1
                                nn.insert(h,"paid")
                            print(" ")
                    elif(yn==2):
                        h=h+1
                        nn.insert(h,"not paid")
                        print("thank you :)")
                        break
                    else:
                        print("give correct value")
  #          ACbusbill(h)
            #h=h+1
#         if(a==2):
#             print(" ")
#             name=input("Enter your name ? ")
#             nn.insert(h,name)
#             number=int(input("Enter mobile no :"))
#             h=h+1
#             nn.insert(h,number)
#             place=input("Enter your place :")
#             h=h+1
#             nn.insert(h,place)
#             pay1=busroute(1,h)
#             h=h+2
#             nn.insert(h,pay1)
#             pay1=pay1*2000
#             print("your bill : ",pay1)
#             paid=int(input())
#             pay1=pay1-paid
#             if(pay1==0):
#                 print(" ")
#                 print("Arriving time:11.10PM AND Destination time:5.00AM ")
#                 print("you booked a  KK travels and your bus no is TN90KK0001 and contact no:7708645719 ")
#                 h=h+1
#                 nn.insert(h,"paid")
#                 print(" ")
#             else:
#                 while(0!=pay1):
#                     print("still your payment is pending \n1 pay \n2 exit\n",pay1)
#                     yn=int(input())
#                     if(yn==1):
#                         while(0!=pay1):
#                             print("still your bill pending :",pay1)
#                             paid=int(input())
#                             pay1=pay1-paid
#                             if(pay1==0):
#                                 print("Arriving time:11.10PM AND Destination time:5.00AM ")
#                                 print("you booked a  KK travels and your bus no is TN90KK0001 and contact no 7708645719")
#                                 print(" ")
#                                 print("Thank you for choosing our KK travels")
#                                 h=h+1
#                                 nn.insert(h,"paid")
#                             print(" ")
#                     elif(yn==2):
#                         h=h+1
#                         nn.insert(h,"not paid")
#                         print("thank you :)")
#                         break
#                     else:
#                         print("give correct value")
#   #          ACbusbill(h)
#             h=h+1
        if(a==2):
            h1=0
            print(" ")
            name=input("Enter your name ? ")
            n1.insert(h1,name)
            number=int(input("Enter mobile no :"))
            h1=h1+1
            n1.insert(h1,number)
            place=input("Enter your place :")
            h1=h1+1
            n1.insert(h1,place)
            pay1=busroute(2,h1)
            h1=h1+2
            n1.insert(h1,pay1)
            pay1=pay1*1000
            print("your bill : ",pay1)
            paid=int(input())
            pay1=pay1-paid
            if(pay1==0):
                print(" ")
                print("Arriving time:11.10PM AND Destination time:5.00AM ")
                print("you booked a  KK travels and your bus no is TN90KK0001 and contact no:7708645719 ")
                h1=h1+1
                n1.insert(h1,"paid")
                print(" ")
            else:
                while(0!=pay1):
                    print("still your payment is pending \n1 pay \n2 exit\n",pay1)
                    yn=int(input())
                    if(yn==1):
                        while(0!=pay1):
                            print("still your bill pending :",pay1)
                            paid=int(input())
                            pay1=pay1-paid
                            if(pay1==0):
                                print("Arriving time:11.10PM AND Destination time:5.00AM ")
                                print("you booked a  KK travels and your bus no is TN90KK0001 and contact no 7708645719")
                                print(" ")
                                print("Thank you for choosing our KK travels")
                                h1=h1+1
                                n1.insert(h1,"paid")
                            print(" ")
                    elif(yn==2):
                        h1=h1+1
                        n1.insert(h1,"not paid")
                        print("thank you :)")
                        break
                    else:
                        print("give correct value")
  #     normalbusbill(h1)
        #h1=h1+1
        if(a==3):
            print(" ")
            name=input("Enter your name :")
            n2.insert(h,name)
            h2=h2+1
            print(" ")
            mobile=int(input("Enter your mobile no : "))
            h2=h2+1
            n2.insert(h2,mobile)
            ad=input("Enter your place : ")
            n2.insert(h2,ad)
            print(" ")
            pay1=busroute(3,h2)
            print("Thank you :)")
    #        touristbusbill(h2)
         #   h2=h2+1
            a=0
    elif(a==2):
        password=input("Enter password : ")
        if(password=="smke1234"):
            while(0<1):
                print("1.AC bus \n2.non A/C bus\n3.tourist bus\n4.Add any place\n5.Exit")
                print(" ")
                j=int(input())
                if(j==1):
                    ACbus()
                elif(j==2):
                    normalbus()
                elif(j==3):
                    touristbus()
                elif(j==4):
                    place=input("Add new place\"Start\" and \"End\" ")
                    busplace.insert(8,place)
                else:
                    break
        else:
            print("Worng password And Try again :(")
    if(a==3):
        break
