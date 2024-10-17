#import(s)
import random
import re
import argparse

#variable(s) global(s)
dico = {}
candidat_mot_suivant = {}
taille_corpus = 1

def charge_corpus(corpus_file, n):
    '''
    On prend un fichier txt contenant des phrases et trie chaque groupe de n mots pour les mettre dans la variable dico.
    '''    
    global taille_corpus
    taille_corpus = n
    with open(corpus_file, encoding='utf-8') as file:
        for line in file:
            phrase = re.sub(r'[^\w\s]', '', line).split()
            for indice in range(0, len(phrase) - n):
                # Prendre les n mots consécutifs
                key = " ".join(phrase[indice:indice + n])
                next_word = phrase[indice + n]
                
                # Ajouter le n-gramme au dictionnaire
                if key in dico:
                    dico[key].append(next_word)
                else:
                    dico[key] = [next_word]

def candidat(mot):
    '''
        On utilise la variable dico pour chercher qu'elle mot on été dit après le mot donné en argument pour les mettre dans la variable candidat_mot_suivant
    '''
    global candidat_mot_suivant
    candidat_mot_suivant = {} #remet la variable a 0 un mot

    try :
        for element in dico[mot]:
            if element in candidat_mot_suivant:
                candidat_mot_suivant[element] += 1
            else:
                candidat_mot_suivant[element] = 1
    except:
        charge_corpus("phrase.txt", taille_corpus-1)
        candidat(mot)

def choix_mot():
    '''
        On Choisis le(s) mot(s) en utilisant Les chaînes de Markov et le(s) return
    '''
    mots = list(candidat_mot_suivant.keys())
    poids = list(candidat_mot_suivant.values())
    mot_choisi = random.choices(mots, weights=poids)[0]# Choisi un mot au hasard en utilisant le poid pour faire une pondération

    return mot_choisi


def main():
    '''
        Permet d'appeller une seule fonction pour appeller toutes les autres
    '''
    mot = ""
    nb_mot = 2

    parser = argparse.ArgumentParser(
        description="Afficheur d'image",
        epilog="Exemple d'utilisation: python main.py --image image.ppm --filigrane 'ne pas copier'"
    )

    parser.add_argument('--texte', type=str, help="Portion initiale de texte utilisée pour la génération")
    parser.add_argument('--nbchoix', type=int, help="Nombre de choix de mots proposés à l'utilisateur ")
    parser.add_argument('--auto', type=str, help="")

    args = parser.parse_args()

    if args.texte:
        mot = args.texte
    if args.nbchoix:
        nb_mot = args.nbchoix


    #Charger le corpus
    charge_corpus("phrase.txt", 1)

    phrase = mot
    dernier_mot = mot

    for _ in range(0, nb_mot-1):
        candidat(dernier_mot) 
        dernier_mot = choix_mot()
        phrase += " " + dernier_mot

    #print(phrase)

if __name__ == "__main__":
    main()
 
