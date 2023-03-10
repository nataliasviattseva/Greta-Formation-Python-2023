# ****************** #
## Lundi 30/01/2023 ##
# ****************** #

variable = 15


def portée_variable():
    print(variable)


def portée_variable2():
    global variable
    variable = 5


portée_variable2()

print(variable)
#
a = 3
print(f"a = 3, type(a): {type(a)}")

b = 5.3
print(f"b = 5.3, type(b): {type(b)}")

c = "Bonjour"
print(f'c = "Bonjour", type(c): {type(c)}')

d = (a > b)
print(f"d = (a > b), type(d): {type(d)}")

e = 6 / 3
print(f"e = 6 / 3, type(e): {type(e)}")

f = 6 // 3
print(f"f = 6 // 3, type(f): {type(f)}")

g = a + b
print(f"g = a + b , type(a): {type(a)}, type(b): {type(b)}, type(g): {type(g)}")

h = a + f       ## a = 3 (type: int), b = 5.3 (type: int)
print(f"h = a + f  , type(a): {type(a)}, type(f): {type(f)}, type(h): {type(h)}")

i = "3.14"
print(f'i = "3.14"  , type(i): {type(i)}')

j = float(i)
print(f'j = float(i) , type(j): {type(j)}')

# k = i + j # TypeError: can only concatenate str (not "float") to str
# print(type(j))

l = str(a)

m = str(f)

print(a, l, f, m, sep="***")
print("a + f =", a + f, "et l + m = ", l + m)

texte = "Salut \n tu vas bien ?"
print(texte)
print(texte, "texte")

prenom = input("Tapez votre prénom : ")
print("Vous vous appelez : ", prenom)

n = input("Donnez un nombre : ")
n = int(input("Donnez un nombre : "))
p = n + 7

q = float(input("Donnez un entier : "))
print(q)

r = int(input("Donnez un entier : "))
print(r)

s = int(3.14)
print(s)
print(type(s))

t = 8
print("t = 8")

u = "Truc"
print('u = "Truc"')

P = (t <= 10)
print("P = (t <= 10)")

Q = (u == "truc")
print('Q = (u == "truc")')

R = (u < "truc")
print('R = (u < "truc")')

print("P:", P)

print("Q:", Q)

print("R:", R)

print("P and Q:", P and Q)

print("P or Q:", P or Q)

print("P or R:", P or R)

print("not R:", not R)

print("P or (not R):", P or (not R))

print("P and (not R):", P and (not R))

print("(not P) and Q:", (not P) and Q)

print("not(P and Q):", not(P and Q))

# ********************* #
#  Marcredi 01/02/2023  #
# ********************* #
v = 37

w = 7

quotient = v // w
reste = v % w

print(v, "=", w, "x", quotient, "+", reste)

from math import *

x = 2.718
print(round(x, 2))
print(round(x**3.1))
print(abs(1 - x))
print(floor(x))
print(floor(1 - x))
print(floor(abs(1-x)))

print(round(exp(2), 3))
print(round(log(2), 2))
print(round(sqrt(2), 3))

print("Le", ord(chr(75)), "dans le ASCII équivalent à:", chr(75))
print("ASCCII code pour", chr(ord("È")), "est :", ord("È"))

texte = "Voici Henri"

# float(texte) # Error de formats
print("len(texte) :", len(texte))
print("texte.upper() :", texte.upper())
print("texte.lower() :", texte.lower())
print("texte[6] :", texte[6])
print("texte[7:8] :", texte[7:8])
print("texte[4:] :", texte[4:])
print("texte[:3] :", texte[:3])
print("texte[-3:] :", texte[-3:])
print("texte.find('i') :", texte.find('i')) # .find() trouve le premiere chaine dans le texte
print("texte.find('i', 5) :", texte.find('i', 5))
print("texte.find('i', 5, 9) :", texte.find('i', 5, 9))
print(type(texte.find('e', 5, 9)))

a = 1
b = a
a += 1
b += a
a += 1
b += a
a += 1
b += a

print(a)
print(b)

a = 1
b = a + 1
a = b + 2
b = a + 2
a = b + 3
b = a + 3

print(a)
print(b)

# {} en: braces fr: accolade

a = "mais"
b = "Non"
c = "allo"
d = "quoi"

message = "%s %s %s, %s !" % (b, a, c, d)
print(message)

message_format = "{} {} {}, {} !".format(b, a, c, d)
print(message_format)

message_f_string = f"{b} {a} {c}, {d} !"
print(message_f_string)

# découpage
e = message[4:13]
print(e)

e = message_format[4:13]
print(e)

e = message_f_string[4:13]
print(e)

animaux = ["girafe", "tigre", "singe", "souris"]
print(animaux)

tailles = [5, 2.5, 1.75, 0.15]
print(tailles)

mixte = ["girafe", 5, "souris", 0.15]
print(mixte)

print(animaux[0])
print(animaux[1])
print(animaux[3])

print([type(i) for i in animaux])

animaux_liste = f"animaux[0] = {animaux[0]}"
print(animaux_liste)

liste_formate = f"la liste formatée est :  {animaux}, {tailles}, {mixte}"
print(liste_formate)

# concatenation

ani1 = ["girafe", "tigre"]
ani2 = ["singe", "souris"]

animaux_complet = ani1 + ani2

print(f"ani1 + ani2 : {animaux_complet}")
print(f"ani1 * 3 : {ani1 * 3}")

# indexes négatives

print(animaux[-4])
print(animaux[-2])
print(animaux[-1])

toto = f"animaux[-4] = {animaux[-4]}, animaux[-2] = {animaux[-2]}, animaux[-1] = {animaux[-1]}"
print(toto)

print(f"animaux[0:2] : {animaux[0:2]}")
print(f"animaux[0:3] : {animaux[0:3]}")
print(f"animaux[0:] : {animaux[0:]}")
print(f"animaux[:] : {animaux[:]}")
print(f"animaux[1:] : {animaux[1:]}")
print(f"animaux[1:-1] : {animaux[1:-1]}")
print(f"animaux[::-1] : {animaux[::-1]}")

enclos1 = ["girafe", 4]
enclos2 = ["tigre", 2]
enclos3 = ["singe", 5]

zoo = [enclos1, enclos2, enclos3]
print(f"zoo : {zoo}")

print(f"zoo[1] : {zoo[1]}")
print(f"zoo[0][0] : {zoo[0][0]}")
print(f"zoo[0][1] : {zoo[0][1]}")
print(f"zoo[1][0] : {zoo[1][0]}")
print(f"zoo[1][1] : {zoo[1][1]}")
print(f"zoo[2][0] : {zoo[2][0]}")
print(f"zoo[2][0] : {zoo[2][1]}")

# 1
"""Constituez une liste 'semaine' contenant les 7 jours de la semaine. À partir de cette liste,
comment récupérez-vous seulement les 5 premiers jours de la semaine d'une part, et ceux du week-end
d'autre part (utlizer pour cela l'indiçage) ? Cherchez un autre moyen pour arriver au même résultat
(en utulusant un autre indiçage)."""

semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

print(semaine[0:5])
print(semaine[:5])
print(semaine[:-2])

print(semaine[5:7])
print(semaine[5:])
print(semaine[-2:])

# 2
"""Trouvez deux manières pour accéder au dernier jour de la semaine."""

print(semaine[6])
print(semaine[-1])

# 3
"""Inversez les jours de la semaine en une commande."""

# semaine.reverse()
# print(semaine)
print(semaine[::-1])

# 4
"""Créez 4 listes 'hiver', 'printemps', 'été' et 'automne' contenant les nois correspondant à ces saisons.
Créez ensuite une liste 'saisons' contenant les sous-listes 'hiver', 'printemps', 'été' et 'automne'. 
Prévoyez ce que valent les variables suivantes, puis vérifiez-le dans l'interpéteur:
- saisons[2]
- saisons[1][0]
- saisons[1:2]
- saisons[:][1]
Comment expliquez-vouz ce dernier résultat ?"""

hiver = ["Décembre", "Janvier", "Février"]
printemps = ["Mars", "Avril", "May"]
ete = ["Juin", "Juillet", "Août"]
automne = ["Septembre", "Octobre", "Novembre"]

saisons = [hiver, printemps, ete, automne]

print(f"saisons[2] : {saisons[2]}")
print(f"saisons[1][0] : {saisons[1][0]}")
print(f"saisons[1:2] : {saisons[1:2]}")
print(f"saisons[:][1] : {saisons[:][1]}")

# 5
"""Affichez la table des 9 en une seule commande avec l'instructon range()"""

[print(f"{i} x 9 = {i * 9}") for i in range(1, 10)]

# 6
"""Avec Python, répondez à la question suivante en une seule commande. Combien y a-t-il de nombres
pairs dans l'intervale [2, 10000] inclus ?"""

# option 1 : utilizer le 'counter', condition '%2' et liste en compréhension
compteur1 = 0
print(f"option 1 : {sum([compteur1+1 for i in range(1, 10001) if i% 2 == 0])}")

# option 2 : utilizer le 'counter', condition '%2' et circle 'for'
compteur2 = 0
for i in range(2, 10001):
    if i % 2 == 0:
        compteur2 += 1
print(f"option 2 : {compteur2}")

# option 3 : modification de variante 2 - utiliser le 'step' de founction range()
compteur3 = 0
for i in range(2, 10001, 2):
    compteur3 += 1
print(f"option 3 : {compteur3}")

# option 4 (pas préferable) : utiliser les founctions len() et range()
print(f"option 4 : {len(range(2, 10001, 2))}")

# option 5 (pas le mien) :
## la boucle va créer une liste des reste des divisions par 2 de tous les éléments du range.
## Les nombres pairs auront un reste & 0, les impairs un reste à 1
## [0, 1, 0, 1, 0 ...]
## la méthode .count(0) va compter le nombre d'éléments 0 dans la liste (soit le nombre de nombres pairs)
print(f"option 5 : {([i % 2 for i in range(2, 10001)]).count(0)}")

# ********************* #
#   Jeudi 02/02/2023    #
# ********************* #
tuple_prenoms = ("Gustave", "Solange", "Alphonce")
liste_prenoms = list(tuple_prenoms)
print(tuple_prenoms)
print(liste_prenoms)

exemple_liste = [8, 6.9, "Kevin"]
print(exemple_liste)
print(len(exemple_liste))

exemple_liste.append("Loana")
print(exemple_liste)

print(len(exemple_liste))

element = exemple_liste[2]
print(element)

exemple_liste.insert(1, "Gabrielle")
print(exemple_liste)

jours1 = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
jours2 = ["Samedi", "Dimanche"]

jours1.extend(jours2)
print(jours1)

liste1 = [1, "", False, 4.6]
liste2 = [2, "", True, 5.6]

liste = liste1 + liste2
print(liste)

liste1.extend(liste2)
print(liste1)

jours = ["Lundi", "Mardi", "Jeudi"]
# je souhaite insérer "Mercredi"
jours[2:2] = ["Mercredi"]
print(jours)

unsorted_jours = ['Mercredi', 'Lundi', 'Mardi', 'Jeudi', 'Samedi', 'Dimanche', 'Vendredi']
# TypeError: can only concatenate list (not "str") to list
# sorted_jours = unsorted_jours[1:3] + unsorted_jours[0] + unsorted_jours[3] + unsorted_jours[4:6] + unsorted_jours[6]
# Il faut toujors utiliser le slicing
sorted_jours = unsorted_jours[1:3] + unsorted_jours[0:1] + unsorted_jours[3:4] + unsorted_jours[6:7] + unsorted_jours[4:6]
print(sorted_jours)

import random
# Genération de la liste aléatoire
liste_aleatoire = [random.randint(-5, 40) for _ in range(102)]
print(liste_aleatoire)

# stoker toutes les values negatives
negative = [i for i in liste_aleatoire if i < 0]
print(negative)

# autre option de genérer de la liste aléatoire
liste_aleatoire1 = []
for i in range(102):
    liste_aleatoire1.append(random.randint(-5, 40))
print(liste_aleatoire1)

import random


def recup_petite_valeur(valeur):
    petite_valeur = valeur[0]
    for valeur in valeur:
        if valeur < petite_valeur:
            petite_valeur = valeur
    return petite_valeur


def recup_grande_valeur(valeur):
    grande_valeur = valeur[0]
    for valeur in valeur:
        if valeur > grande_valeur:
            grande_valeur = valeur
    return grande_valeur

# Genération de la liste aléatoire
liste_aleatoire = [random.randint(-5, 40) for _ in range(102)]
print(liste_aleatoire)


print(f"Recuperer la petite valeur: {recup_petite_valeur(liste_aleatoire)}")
print(f"Recuperer la grange valeur: {recup_grande_valeur(liste_aleatoire)}")


# stoker toutes les values negatives
negative = [i for i in liste_aleatoire if i < 0]
print(negative)

# Alerter si le nombre de nombres negatives superior de 5
if len(negative) > 5:
    print("ALERT !!! Le nombre de nombres negatives superior de 5")

# autre option de genérer de la liste aléatoire
liste_aleatoire1 = []
for i in range(102):
    liste_aleatoire1.append(random.randint(-5, 40))
print(liste_aleatoire1)

prenoms = ["Gabrielle", "Alphonce", "Kevin", "Loana"]
nombres = [8, 52, 0, 3.2, -5.6, 7, -23]

prenoms.sort(reverse=True)
nombres.sort()

print(prenoms)
print(nombres)

i_prenoms = prenoms.index("Gabrielle")
i_nombres = nombres.index(52)
i_nombres = nombres.index(53) # ValueError: 53 is not in list

print(i_prenoms)
print(i_nombres)

prenoms1 = ["Gabrielle", "Alphonce", "Kevin", "Loana", "Gabrielle"]

i_prenoms1 = prenoms.index("Gabrielle", 3)
print(i_prenoms)

prenoms3 = ["Gabrielle", "Alphonce", "Kevin", "Loana"]

popped1 = prenoms3.pop()
print(popped1, prenoms3)

popped2 = prenoms3.pop(1)
print(popped2, prenoms3)

prenoms4 = ["Gabrielle", "Alphonce", "Kevin", "Loana", "Kevin"]

prenoms4.remove("Kevin")
print(prenoms4)

prenoms5 = ["Gabrielle", "Alphonce", "Kevin", "Loana", "Kevin"]

n = prenoms5.count("Kevin")
print(n)

prenoms6 = ["Gabrielle", "Alphonce", "Kevin", "Loana", "Kevin"]

if "Kevin" in prenoms6:
    print("Le test d'appartenance est positif.")
else:
    print("Ce prénom est absent de la liste.")

# ********************* #
#  Vendredi 03/02/2023  #
# ********************* #

liste_initiale = list(range(0, 16))
print(liste_initiale)

liste_2 = []

for n in liste_initiale:
    liste_2.append(n*2)

print(liste_2)

liste_3 = [n*2 for n in liste_initiale]

liste_pair = [n for n in liste_initiale if n % 2 == 0]
print(liste_pair)

nouvelle_liste = [n*2 if n % 2 == 0 else n*3 for n in liste_initiale]
print(nouvelle_liste)

liste_initiale = [[0, "a"], [2, "b"], [3, "c"]]
nouvelle_liste = [n*2 for i in liste_initiale for n in i]
print(nouvelle_liste)

liste_initiale = [[0, "a"], [2, "b"], [3, "c"]]
nouvelle_liste = [n*2 for i in liste_initiale for n in i]
print(nouvelle_liste)

liste_initiale = [[0, "a"], [2, "b"], [3, "c"]]
nouvelle_liste = [n*2 if (type(n) == int) else n*3 if type(n) == str else n for i in liste_initiale for n in i ]
print(nouvelle_liste)

# fizz_buzz_liste = ['fizzbuzz' if i % 3 == 0 and i % 5 == 0 else 'fizz' if i % 3 == 0 else 'buzz' if i % 5 == 0 else i for i in range(1, 101)]
# print(*fizz_buzz_liste, sep='\n')

prenom = "Gustave"
liste_lettres = [lettre for lettre in prenom]
print(liste_lettres)

print(*['Bonjour' for _ in range(int(input("Combien de fois ?\n")))], sep="\n")


def permis(somme, somme_permis, years):
    """Founction prends les 3 paramétrés: somme initiale, somme de permis et nombre des annees er retourne True si le
    à la fin depasse le permis et False en outre cas somme """
    for i in range(1, years + 1):
        somme += somme * 2.5 / 100
        print(f"Sum a la fin de {i} annee = {somme}")
    if somme >= somme_permis:
        return True
    else:
        return False


def combien_des_annes_pour_permis(somme, somme_permis, years):
    """Founction prends les 3 paramétrés: somme initiale, somme de permis et nombre des annees et retourne True si le
    à la fin depasse le permis et False en outre cas somme """
    compteur = 0
    while somme > somme_permis:
        somme += somme * 2.5 / 100
        compteur += 1
    return compteur


print("Non" if permis(710, 805, 3) == False else "Oui")

compteur = 1
years = 1


def combien_des_annees_pour_permis(somme, somme_permis):
    """Founction prends les 3 paramétrés: somme initiale, somme de permis et retourne nombre des annees suiffisant pour
    depasser le somme de permis"""
    global years
    global compteur
    for i in range(years):
        somme += somme * 2.5/100
        print(f"Sum a la fin de {compteur} annee = {somme}")
    if somme >= somme_permis:
        print(f"Le montant total après {compteur} ans est de {somme:.2f}")
    else:
        compteur += 1
        combien_des_annees_pour_permis(somme, somme_permis)


combien_des_annees_pour_permis(710, 805)


somme_initiale = 710
q = 0.025
n = 6
somme = somme_initiale * (1 + q)**n
print(somme)

bougies_tarte = 0

# premier option
for i in range(1, 100):
    # print(f"Dans {i} annee c'etais {bougies_tarte}") # c'est ligne pour suivre augementation de bougies
    if bougies_tarte >= 1999:
        print(f"L'Emir Hifik a {i} ans.")
        break
    bougies_tarte += i
    annee_manquant = bougies_tarte - 1999

print(f"Il mangue {annee_manquant}")  # ici on encore augumente 1999, dont 2016 = 1999 = 17 (l'annee manguant)

# deuxieme option (avec formule)
for i in range(1, 100):
    k = i * (i + 1)/2 # formule
    # print(f"Dans {i} annee c'etais {int(k)}") # c'est ligne pour suivre augementation de bougies
    if k >= 1999:
        print(f"L'Emir Hifik a {i} ans.")
        annee_manquant_1 = k - 1999  # ici on encore augumente 1999, dont 2016 = 1999 = 17 (l'annee manguant)
        break

print(f"Il mangue {int(annee_manquant_1)} ans.")

lettre = input("lettre ? ")
chaîne = input("chaîne ? ")
occurance = 0

for character in chaîne:
    if lettre == character:
        occurance += 1

print(f"occurance : {occurance}")
