#Q1
a=int(input("Donner a\n"))
b=int(input("Donner b\n"))
print("la somme de a et b est :",a+b)
print("la multiplication de a et b est :",a*b)

#Q2

a=int(input("Donner a\n"))
b=int(input("Donner b\n"))

print("a=",b)
print("b=",a)

#Q2'
a=int(input("Donner a\n"))
b=int(input("Donner b\n"))
c=a
a=b
b=c
print("a=",a)
print("b=",b)
#Q2''
a,b=b,a

#Q3
a=int(input("Donner a\n"))
b=int(input("Donner b\n"))
c=int(input("Donner c\n"))
m=a
if b>m:
    if b>c:
        m=b
    else:m=c

print(m)

#Q4
d=int(input("Donner la distance\n"))
u=int(input("Donner l'unite : 1 pour kilometres et 2 pour milles\n"))
match u:
    case 1:
        print("La distance en milles est ",d*0.621371)
    case 2:
        print("La distance en kilometres est ",d*1.60934)
