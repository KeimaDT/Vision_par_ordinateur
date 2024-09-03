# Cours de Vision par ordinateur
septembre-novembre 2024, ESIEE-IT
## TP 1
### Partie A

#### 7.
##### Calculer la moyenne, l’écart type et la médiane de cette liste. Arrondir dans le code les valeurs au centième. Noter les valeurs
Moyenne X : 1.54
Écart type X : 0.84
Médiane X : 1.56

##### Créer une array numpy, X_bis, de 1000 points avec valeur aléatoire dans l’intervalle [0, 3]
Moyenne X_bis : 1.47
Écart type X_bis : 0.87
Médiane X_bis : 1.44

##### Comparer les résultats de moyenne, écart type et médiane des listes X et X_bis.
Dans mes résultats, la moyenne de X est supérieur à X_bis. Il y a donc des valeurs plus élevées dans mon array X que dans X_bis
Pour l'écart type, X_bis est supérieur à X. Ce qui indique que X_bis possède des valeurs plus varié que X.
Et concernant la médiane, X semble avoir une moitié des valeurs plus élevées que X_bis

##### A quoi sert le fait de fixer l’aléa (seed) ?
Cela permet d'avoir les mêmes résultats avec nos listes aléatoires. Plus précisment, nos valeurs aléatoires sont généré grâce à une seed. Si cette seed est fixe alors nos valeurs seront les mêmes à chaque itération. Cela permet d'avoir un jeu de données aléatoires tout en les gardant pour apporté des modifications ou les comparer.

#### 8.
##### Changer la taille de la figure. Quelle ligne de code permet de le faire ?
Cette ligne de code permet de changer la taille de la figure : "plt.figure(figsize=(10, 10))"

##### A quelle fonction la distribution de noise fait penser ?
Elle fait penser à une loi normale

### Partie B
####  Quelle couleur est représentée par le 0 ? Quelle couleur est représentée par le 255?
0 est représenté par le noir et 255 par le blanc

#### Je lis l’image ‘image_1.jpg’ et je la met dans la variable img. Quelle méthode est utilisée ?
On utilise la méthode imread et imshow de cv2

#### Afficher l’image en noir et blanc. Que faut-il ajouter à la ligne de code précédente ?
On rajoute une conversion des couleurs de notre image d'origine.
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)