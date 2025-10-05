
#qst1

def F1(n):
    print("Bonjour "*n) 

print(F1(6))

#qst2
def F2(a):
    if a%10==0:
        print(f"{a} est divisible par 10")
    else:
        print(f"{a} n'est pas divisible par 10")

print(F2(6))

#qst3
def F3(b):
     fact=1
     for i in range (1,b+1):
         fact=fact*i
     print(f"la valeur du factoriel est : {fact}")

print(F3(3))

#qst4
def F4(h):
    c = 0
    h=h.lower()
    voy=['a','e','i','o','u','y']
    for letter in h:
        if letter in voy:
            c=c+1
        else:
            continue
    print(f"le nombre des voyelles est : {c}")

h=input("donner la chaine : ")
print(F4(h))

#qst5
def F5(m):
        print(f"tableau de multiplication de {m}\n")
        for j in range (1,11):
            produit=m*j
            print(f"{m}x{j}= {produit}\n")

m=int(input("entrer le nombre "))
print(F5(m))

#qst6
def F6(ch):
    n=len(ch)
    print(f"la longeur du texte est: {n}")

ch=input("donner le texte : ")
print(F6(ch))

#qst7
def F7(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F7(n - 1) + F7(n - 2)


n=int(input("entrer le nombre: "))
print(F7(n))