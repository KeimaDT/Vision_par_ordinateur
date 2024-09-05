import cv2
from fonction import display_image

# Chargement de l'image en couleur et en niveaux de gris
img = cv2.imread('image_1.jpg')  # Chargement de l'image en couleur
img_gray = cv2.imread('image_1.jpg', cv2.IMREAD_GRAYSCALE)  # Chargement de l'image en niveaux de gris

# # # #
# Filtre de Sobel pour détecter les contours horizontaux et verticaux (clavier)

sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)

# Combinaison des deux gradients (horizontal et vertical)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

cv2.imwrite('screen/sobel_keyboard.jpg', sobel_combined) # Sauvegarde
sobel_keyboard = cv2.imread('screen/sobel_keyboard.jpg') # Chargement
display_image(sobel_keyboard, 'Sobel') # Affichage de l'image

# # # #
# Filtre de Sobel pour détecter les contours du "chat blanc"
sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=5)

# Combinaison des deux gradients (horizontal et vertical)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)


cv2.imwrite('screen/sobel_cat.jpg', sobel_combined) # Sauvegarde
sobel_cat = cv2.imread('screen/sobel_cat.jpg') # Chargement
display_image(sobel_cat, 'sobel_cat') # Affichage de l'image

# # # #
# Application du filtre de Canny pour détecter les contours du clavier
# Le filtre Canny utilise deux seuils (50 et 150) pour la détection des bords
canny_edges = cv2.Canny(img_gray, 50, 150, apertureSize=3)

cv2.imwrite('screen/canny_keyboard.jpg', canny_edges) # Sauvegarde
canny_keyboard = cv2.imread('screen/canny_keyboard.jpg') # Chargement
display_image(canny_keyboard, 'canny_keyboard') # Affichage de l'image

# # # #
# Application du filtre de Canny pour détecter les contours du "chat blanc"
# Le filtre Canny utilise des seuils plus bas (30 et 100) et un noyau plus grand (apertureSize=5)
canny_edges = cv2.Canny(img, 30, 100, apertureSize=5)

cv2.imwrite('screen/canny_cat.jpg', canny_edges) # Sauvegarde
canny_cat = cv2.imread('screen/canny_cat.jpg') # Chargement
display_image(canny_cat, 'canny_cat')# Affichage de l'image
