#چاپ مثلث
#صدف قادري بافتي
#يکشنبه ها از 7:45 تا 10

number = int(input("enter your number : "))
a = 0
for i in range (number):
    print(a * "*")
    a+=1
for i in range(number):
    print(a * "*")
    a-=1
