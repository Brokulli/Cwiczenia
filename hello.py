imie = "Patrycja"
nazwisko = "Respondek-Szpakowska"
pelne_imie = imie + " " + nazwisko
print"Hello world", pelne_imie

# Hello world Patrycja Respondek-Szpakowska

for liczba in range(10):
...     print liczba
...
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9

for x in range(1,21):
...     if x%2==0:
...         print "Bazyl parzysty"
...     elif x%2!=0:
...         print x-2
...     if x%7==0:
...         if x%2==0:
...             break
...
#-1
#Bazyl parzysty
#1
#Bazyl parzysty
#3
#Bazyl parzysty
#5
#Bazyl parzysty
#7
#Bazyl parzysty
#9
#Bazyl parzysty
#11
#Bazyl parzysty

x=0
>>> while x%7!=0:
...     if x%2==0:
...         print "Bazyl parzysty"
...     if x%2!=0:
...         print x-2
...     x=x+1
