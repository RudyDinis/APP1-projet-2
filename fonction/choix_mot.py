import random

def choix_mot(candidat_mot_suivant):
    '''
        On Choisis le(s) mot(s) en utilisant Les chaînes de Markov et le(s) return
    '''
    mots = list(candidat_mot_suivant.keys())
    poids = list(candidat_mot_suivant.values())
    mot_choisi = random.choices(mots, weights=poids)[0]# Choisi un mot au hasard en utilisant le poid pour faire une pondération

    return mot_choisi