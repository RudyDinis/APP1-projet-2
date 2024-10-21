#import(s)
import re


#variable(s) global(s)
dico = {}
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
    return dico, taille_corpus