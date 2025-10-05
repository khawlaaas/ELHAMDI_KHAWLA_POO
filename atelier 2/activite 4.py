machines={
"m1":"192.168.0.1",
"m2":"192.168.0.2",
"m3":"192.168.0.3",
"m4":"192.168.0.4",
"m5":"192.168.0.5"
}
#qst1
print("l'adresse IP de la machine 2 est : ",machines["m2"])
#qst2
print("le nombre de machines est : ",len(machines))
#qst3
machines["m6"]="192.168.0.6"
print(machines)
#qst4
del machines["m4"]
print(machines)
#qst5
est_dans_dictionnaire="m5" in machines
print(est_dans_dictionnaire)
#qst6
m=input("entrer le nom de la machine: ")
if m in machines:
    print(f"l'adresse IP de la machine {m} est : {machines[m]}")
else:
    print("la machine ",m," n'est pas repertoriee")
