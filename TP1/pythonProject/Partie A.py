import numpy as np
import matplotlib.pyplot as plt
import cv2
from fonction import display_image

#Fixer l’aléa (seed)
np.random.seed(1412)

#Créer une array numpy, X, de 1000 points avec valeur aléatoire dans l’intervalle [0, 3]
X = np.random.uniform(0, 3, 1000)
print("\nX : ",X[:10])

#Calculer la moyenne, l’écart type et la médiane de cette liste.
#Arrondir dans le code les valeurs au centième. Noter les valeurs
moyenne = np.mean(X)
ecart_type = np.std(X)
mediane = np.median(X)

print("Moyenne X :", round(moyenne, 2))
print("Écart type X :", round(ecart_type, 2))
print("Médiane X :", round(mediane, 2))

#Créer une array numpy, X_bis, de 1000 points avec valeur aléatoire dans l’intervalle [0, 3]
X_bis = np.random.uniform(0, 3, 1000)
print("\nX_bis : ",X_bis[:10])
moyenne = np.mean(X_bis)
ecart_type = np.std(X_bis)
mediane = np.median(X_bis)

print("Moyenne X_bis :", round(moyenne, 2))
print("Écart type X_bis :", round(ecart_type, 2))
print("Médiane X_bis :", round(mediane, 2))

#Créer une liste, y, de 1000 points ayant la valeur de sin(X) auquel on
# ajoute un bruit gaussien aléatoire ayant une amplitude de 10% (0.1).
sin_X = np.sin(X)
bruit = np.random.normal(0, 0.1, 1000)
y = sin_X + bruit
print("\nsin(X) : ",y[:10])


#Visualiser y en fonction de X sous forme de graph ‘scatter’
plt.figure(figsize=(10, 10))
plt.scatter(X, y)
plt.title('Graphique y en fonction de X')
plt.xlabel('X')
plt.ylabel('y')
plt.grid(True)
plt.show()

#Visualiser le bruit gaussien, noise, sous forme d’histogramme. Le nombre de bins est fixé à 50.
plt.figure(figsize=(10, 10))
plt.hist(bruit, bins=50)
plt.title('Histogramme du bruit gaussien')
plt.xlabel('Valeur du bruit')
plt.ylabel('Fréquence')
plt.grid(True)
plt.show()

#Je visualise l’image dans le bon espace couleur. Afficher l’image en noir et blanc
img = cv2.imread('image_1.jpg')
if img is None:
    print("Error image")
else:
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Image', img)
    cv2.imshow('Image Noir&Blanc', img_gray)

    # Importer et appeler la méthode ‘display_image’ précédemment créée pour
    # afficher l’image ‘image_1.jpg’.
    display_image(img, name='Image_fonction')

    cv2.waitKey(0)
    cv2.destroyAllWindows()