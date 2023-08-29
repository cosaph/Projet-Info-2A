# Projet-Info-2A

# Pour créer une nouvelle branche basée sur la branche actuelle :


```
git branch <nom_de_branche>
```

#Changement de branche

Pour passer à une autre branche :

```
git checkout <nom_de_branche>

```

# Fusion de branches

Pour fusionner une branche spécifique dans la branche actuelle :
bash

```
git merge <nom_de_branche>
```



# Vérification de l'état

Pour afficher l'état actuel de votre référentiel Git :

```
git status
```

# Ajout de fichiers modifiés

Pour ajouter les modifications de fichiers spécifiques à l'index :

```
git add <nom_fichier1> <nom_fichier2> ...
```

# Validation des modifications

Pour valider les modifications ajoutées à l'index :

```
git commit -m "Message de validation"
```

# Récupération des dernières modifications

Pour récupérer les dernières modifications du référentiel distant et les fusionner avec votre branche actuelle :
bash

```
git pull origin <nom_de_branche>
```

# Envoi des modifications locales


Pour envoyer vos modifications locales vers le référentiel distant :
bash

```
git push origin <nom_de_branche>
```
