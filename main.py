#-------Modules-------
from fonction.charge_corpus import charge_corpus
from fonction.candidat import candidat
from fonction.choix_mot import choix_mot

#variable(s) global(s)
dico = {}
candidat_mot_suivant = {}
taille_corpus = 1

def main(mot, nb_mot):
    '''
        Permet d'appeller une seule fonction pour appeller toutes les autres
    '''
    phrase = mot
    dernier_mot = mot

    #Charger le corpus
    for _ in range(0, nb_mot-1):
        global candidat_mot_suivant
        candidat_mot_suivant = candidat(dico, "voiture", taille_corpus)#charger les candidats 
        dernier_mot = choix_mot(candidat_mot_suivant)
        phrase += " " + dernier_mot
    return phrase


dico, taille_corpus = charge_corpus("phrase.txt", 2) #charger un corpus
print(main("le", 5))

