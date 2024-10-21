from fonction.charge_corpus import charge_corpus

candidat_mot_suivant = {}

def candidat(dico, mot, taille_corpus):
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
        candidat(dico, mot, taille_corpus)
    return candidat_mot_suivant