import cv2
from fonction import image_euclidean_distance

# Chargement des images en niveaux de gris
image_paths = {
    "Sobel": "screen/sobel_keyboard.jpg",
    "Canny": "screen/canny_keyboard.jpg"
}

# Lecture des images
img1 = cv2.imread(image_paths["Sobel"], cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(image_paths["Canny"], cv2.IMREAD_GRAYSCALE)

# Vérification de la bonne lecture des images
def check_images_loaded(*images):
    for idx, img in enumerate(images):
        if img is None:
            print(f"ERREUR : L'image {list(image_paths.keys())[idx]} n'a pas pu être chargée.")
            return False
    return True

if check_images_loaded(img1, img2):
    # Calcul et affichage de la distance euclidienne
    distance = image_euclidean_distance(img1, img2)
    print(f"Distance euclidienne entre les images Sobel et Canny : {distance}")
