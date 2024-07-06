import random

NOMBRE_MIN=1
NOMBRE_MAX=10
NOMBRE_MAGIQUE=random.randint(NOMBRE_MIN,NOMBRE_MAX)
vies=4


def demander_nombre(nb_min,nb_max):
    a=0 
    while a==0  :
        nombre_str=input(f"Quel est le nombre magique(entre {nb_min} et{nb_max}) ? :")
        try:
            nombre_int=int(nombre_str)
        except:
            print("Erreur: veuillez entrer un nombre svp")
        else:
            a=1
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f'Respecter la limite !! le nombre doit etre entre {nb_min} et {nb_max}')
                a=0
    return nombre_int


def comparaison(nb,nb_magique,vie):
    if nb > nb_magique:
        print('le nombre magique est plus petit')
        print(f'il vous reste {vie} vies')
        
    elif nb < nb_magique:
        print('le nombre magique est plus grand ')
        print(f'il vous reste {vie} vies')
        
    else :
        print('Bravo vous avez trouvé le nombre magique !!!')


nombre=demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
comparaison(nombre,NOMBRE_MAGIQUE,vies)

while nombre != NOMBRE_MAGIQUE and vies != 0 :
    nombre=demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
    vies-=1
    comparaison(nombre,NOMBRE_MAGIQUE,vies)
    if vies == 0:
        print(f'vous avez perdu !!! il vous reste {vies} vies')
        print(f'le nombre magique etait {NOMBRE_MAGIQUE}')
    