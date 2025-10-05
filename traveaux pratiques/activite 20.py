adresses_ip=["192.168.0.1","10.0.0.1","172.16.0.1","200.100.50.1","169.254.0.1"]
dict={
"192.168.0.1":"classe C",
"10.0.0.1":"classe A",
"172.16.0.1":"classe B",
"200.100.50.1":"adresse IP publique",
"169.254.0.1":"adresse IP de lien vocal(APIPA)",
}
#qst1
print("la premiere adresse dans la liste est : ",adresses_ip[0])
#qst2
print("la derniere adresse dans la liste est : ",adresses_ip[4])
#qst3
print("la troisieme adresse dans la liste est : ",adresses_ip[2])
#qst4
adresses_ip.append("172.31.0.1")
print(adresses_ip)
#qst5
adresses_ip.remove("200.100.50.1")
print(adresses_ip)
#qst6
print("le nombre d'adresses restants est: ",len(adresses_ip))
#qst7
est_dans_la_liste ="192.168.0.1" in adresses_ip
print(est_dans_la_liste)
#qst8
print("la classe de l'adresse IP de 10.0.0.1 est : ",dict["10.0.0.1"])
#qst9
adresses_ip.sort()
print(adresses_ip)
#qst10
c=0
for cle, valeur in dict.items():
    if valeur == "classe C":
        c=c+1
if c == len(dict):
    print("Toutes les adresses IP appartiennent a la classe C")
else:
    print("Toutes les adresses IP n'appartiennent pas a la classe C")

#qst11
c=0
for cle, valeur in dict.items():
    if valeur == "adresse IP publique":
        c=c+1
print("le nombre d'adresses publiques est : ",c)