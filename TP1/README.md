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
Sa courbe fait penser à une loi normale

#### 9.
##### Je lis l’image ‘image_1.jpg’ et je la met dans la variable img. Quelle méthode est utilisée ?
On utilise la méthode imread et imshow de cv2.

##### Afficher l’image en noir et blanc. Que faut-il ajouter à la ligne de code précédente ?
On rajoute une conversion des couleurs de notre image d'origine.
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


### Partie B
####  Quelle couleur est représentée par le 0 ? Quelle couleur est représentée par le 255?
0 est représenté par le noir et 255 par le blanc

##### 1. Seuillage

###### Le seuillage manuel. Expliquer ce terme. 
Il s'agit d'une méthode de segmentation qui consiste à tester pour chaque pixel de l'image si sa valeur est supérieur ou inférieur à un certain seuil. Puis cela va produire une image qui différencie les résultats.

###### Quels sont les seuils min et max qui optimisent la segmentation ?
Les valeurs qui optimisent la segmentation sont un seuil min = 100 et un seuil max = 250
![seuillage_manuel.jpg](https://github.com/KeimaDT/Vision_par_ordinateur/blob/main/TP1/pythonProject/screen/seuillage_manuel.jpg)

###### Quelles sont les seuils optimaux trouvés par ce seuillage pour chacun des canaux hsv de l’images ?
Les seuils optimaux sont déterminés automatiquement grâce à la méthode d'Otsu, qui identifie le seuil idéal pour chaque canal de l'image.
![threshold_otsu_combined.jpg](https://github.com/KeimaDT/Vision_par_ordinateur/blob/main/TP1/pythonProject/screen/threshold_otsu_combined.jpg)

###### Comparer les deux techniques de seuillage utilisées
Seuillage manuel : Facile et rapide, mais requiert de définir manuellement les seuils optimaux, ce qui peut s'avérer difficile.
Seuillage d'Otsu : Automatique et détermine les seuils optimaux sans intervention humaine, mais peut être moins précis sur des images avec un éclairage complexe.

##### 2. Détection de contour

###### Expliquer à quoi serve chacun des paramètres et noter les valeurs optimales pour repérer le clavier
ddepth = cv2.CV_64F => Profondeur de l'image de sortie.
dx = 1, dy = 0" => horizontal
dx = 0, dy = 1" => vertical
ksize = 3 => Taille du noyau

###### Appliquer le filtre de Sobel pour détecter le contour du chat blanc. Noter les valeurs optimales des paramètres pour cela
ddepth = cv2.CV_64F
dx = 1, dy = 0"
dx = 0, dy = 1"
ksize = 5 => capture des contours plus doux du chat


######  Appliquer le filtre de Canny pour détecter les contours du clavier. Expliquer à quoi serve chacun des paramètres et noter les valeurs optimales pour repérer le clavier
Le filtre de Canny détecte les contours en utilisant un processus multi-étapes, incluant la détection de bords, le suivi des contours, et l'élimination des pixels non maximaux.
threshold1 : 50 => Seuil bas pour l'hystérésis.
threshold2 : 150 => Seuil haut pour l'hystérésis.
apertureSize : 3 => Taille du noyau Sobel utilisé pour la détection des gradients.

###### Appliquer le filtre de Canny pour détecter le contour du chat blanc. Noter les valeurs optimales des paramètres pour cela
threshold1 : 30
threshold2 : 100
apertureSize : 5 => capture des détails plus subtils du chat

###### Comparer les deux détections de contour dans le repérage du chat blanc
Sobel : Efficace mais sensible au bruit.
Canny : Plus précis et robuste, particulièrement adapté pour détecter les contours fins et détaillés, comme ceux du chat blanc.

##### 3. Transformation par point
![result_transformations.png](https://github.com/KeimaDT/Vision_par_ordinateur/blob/main/TP1/pythonProject/screen/result_transformations.png)

![transformations_position.png](https://github.com/KeimaDT/Vision_par_ordinateur/blob/main/TP1/pythonProject/screen/transformations_position.png)
