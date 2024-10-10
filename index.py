#import(s)
import random
import re

#variable(s) global(s)
dico = {}
candidat_mot_suivant = {}

def charge_corpus(corpus_file):
    '''
        On prend un fichier txt contenant des phrases et trie chaques mots pour les mettre dans la variable dico
    '''
    with open(corpus_file, encoding='utf-8') as file:
        for line in file:
            phrase = re.sub(r'[^\w\s]', '', line).split()
            for indice in range(0, len(phrase)-1):

                if phrase[indice] in dico:
                    dico[phrase[indice]] += [[phrase[indice +1]]]
                else:
                    dico[phrase[indice]] = [[phrase[indice +1]]]

def candidat(mot):
    '''
        On utilise la variable dico pour chercher qu'elle mot on été dit après le mot donné en argument pour les mettre dans la variable candidat_mot_suivant
    '''
    global candidat_mot_suivant
    candidat_mot_suivant = {} #remet la variable a 0raboule un mot
    for element in dico[mot]:
        if element[0] in candidat_mot_suivant:
            candidat_mot_suivant[element[0]] += 1
        else:
            candidat_mot_suivant[element[0]] = 1

def choix_mot():
    '''
        On Choisis le(s) mot(s) en utilisant Les chaînes de Markov et le(s) return
    '''
    mots = list(candidat_mot_suivant.keys())
    poids = list(candidat_mot_suivant.values())
    mot_choisi = random.choices(mots, weights=poids)[0]# Choisi un mot au hasard en utilisant le poid pour faire une pondération


    return mot_choisi

#charge_corpus("fra_news_2023_1M-sentences.txt")

def main(mot, nb_mot):
    '''
        Permet d'appeller une seule fonction pour appeller toutes les autres
    '''
    phrase = mot
    dernier_mot = mot

    #Charger le corpus
    for _ in range(0, nb_mot-1):
        candidat(dernier_mot)
        dernier_mot = choix_mot()
        phrase += " " + dernier_mot
    return phrase


print(int(4 / str('4')))


