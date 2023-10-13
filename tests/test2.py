

import hashlib


def chiffrer_mdp(mdp, email): 
        # comme sel nous allons prendre l'email de l'utilisateur.
        salt = email
        return hashlib.sha256((salt.encode() + mdp.encode('utf-8'))).hexdigest()

print(chiffrer_mdp("123456", "coralie@hotmail.f"))