t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2=['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre']
i=0
for element in t1:
    t2.insert(2*i+1,element)
    i=i+1
print(t2)