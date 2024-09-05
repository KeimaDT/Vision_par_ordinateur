import cv2
from fonction import display_image

img = cv2.imread('image_1.jpg')

# # # #
# Seuillage manuel
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Définition des seuils minimum et maximum pour le seuillage manuel
seuil_min = 100
seuil_max = 255

# Application du seuillage binaire manuel
_, img_seuillage = cv2.threshold(img_gray, seuil_min, seuil_max, cv2.THRESH_BINARY)

display_image(img_seuillage, name='Seuillage manuel') # Affichage
cv2.imwrite('screen/seuillage_manuel.jpg', img_seuillage) # Sauvegarde

# # # #
# OTSU
# Conversion de l'image en espace de couleur HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Division de l'image HSV en trois canaux
channels = cv2.split(hsv_img)

# Liste pour stocker les résultats de chaque canal
thresholds = []

# Boucle pour appliquer le seuillage d'Otsu à chaque canal
for i, channel in enumerate(channels):
    _, otsu_channel = cv2.threshold(channel, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    thresholds.append(otsu_channel)

# Combinaison des résultats de seuillage Otsu des trois canaux
combined_otsu = cv2.bitwise_or(thresholds[0], thresholds[1])
combined_otsu = cv2.bitwise_or(combined_otsu, thresholds[2])
cv2.imwrite('screen/threshold_otsu_combined.jpg', combined_otsu) # Sauvegarde
threshold_otsu_combined = cv2.imread('screen/threshold_otsu_combined.jpg') # Chargement
display_image(threshold_otsu_combined, name='Otsu') # Affichage