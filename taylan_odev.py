dolarDun = 7.65
dolarBugun = 7.65

if dolarDun > dolarBugun:
    print("Artiş oku")
    print("Bitti")
    
elif dolarDun < dolarBugun:
    print("Azaliş oku")   
else:
    print("Eşittir oku")
    
print("Bitti")    
       
#if dolarDun < dolarDun:
    #print("Azalış oku")    
#if dolarDun == dolarBugun:
    #print("Eşittir oku")


#Bölüm Ödevi 1 #

# 2 adet sayısal değişken tanımlayınız. Bu sayılara istediğiniz değeri atayınız. Bu sayılardan hangisi büyükse, ekrana yazdırınız.

number1 = 32
number2 = 47

if number1 > number2 : 
    print("1.sayi, 2.sayidan büyüktür.")
elif number1 < number2 :
    print("2.sayi, 1.sayidan büyüktür.")
else:         
    print("iki sayi birbirine eşittir.")


#ödev2 

#3 adet sayısal değişken tanımlayınız. Bu sayılardan en büyük ve en küçük olanı ekrana ayrı ayrı yazdırınız. 

number1=3
number2=5
number3=7

if (number1 >= number2) and (number1 >= number3):
   buyuk = number1
   if number2 > number3:
     kucuk = number3
   else:
       kucuk = number2
elif (number2 >= number1) and (number2 >= number3):
   buyuk = number2
   if number1 > number3:
     kucuk = number3
   else:
       kucuk = number1   
else:
   buyuk = number3
   if number1 > number2:
     kucuk = number2
   else:
       kucuk = number1 

print("en küçük sayi : ",kucuk,"en büyük sayi : ",buyuk)










