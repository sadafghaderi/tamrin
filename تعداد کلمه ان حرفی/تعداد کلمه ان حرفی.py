#تعداد کلمه ان حرفی
#صدف قادري بافتي
#يکشنبه ها از 7:45 تا 10

a=0

def word_count(str,n):
    a=0
    counts = dict()
    words = str.split()
    

    for word in words:
        if len(word)==n:
           a += 1
       

    return a


sadaf=input("enter sentence : ")
n=int(input("enter number : "))


print( word_count(sadaf,n))
