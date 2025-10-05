L3=[1,2,3,4,5]
#qst1
for element in L3:
    print(element)

#qst2
s=0
for element in L3:
    s+=element
print("la somme des elements est : ",s)

#qst3
p=1
for element in range (L3[2],L3[4]):
    p=p*element
print("le produit des valeurs entre L3[2] et L3[4] est:",p)

#qst4
print("le maximum de la liste est : ",max(L3))
print("le minimum de la liste est : ",min(L3))

#qst5
c=0
for element in L3:
    if element%3==0:
        c=c+1
print("le nombre des multiples de 3 est : ",c)

#qst6:
L3.reverse()
print(L3)