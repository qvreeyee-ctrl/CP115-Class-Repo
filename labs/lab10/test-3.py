#Programmer Name : Vivi
#Program Description : This Program is to help PASU Telecommuniction Company to calculate and display the amount of the bill that people need to pay after receiving the discount. In this program , user will just enter their monthly usage then the program will handle the rest of them.

usage = float (input ("Enter your monthly usage :RM "))   #user will enter their monthly usage

if usage < 50 :
    discount = 0
elif usage <= 100 :
    discount = 0.05 * usage
else :
    discount = 0.2 * usage

monthly_bill = usage - discount  #calculate the bill user need to pay after discount
print ("Your monthly bill is : RM ", monthly_bill)  #display the monthly bill user need to pay after discount