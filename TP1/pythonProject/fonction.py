import cv2
import numpy as np

#Créer une méthode ‘display_image’
def display_image(img, name='Image'):
    if img is not None:
        cv2.imshow(name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error image")

def image_euclidean_distance(img1, img2):
    # On s'assure que les deux images ont les mêmes dimensions
    if img1.shape != img2.shape:
        raise ValueError("Error dimensions not equal")

    # Conversion des images en un tableau 1D pour calculer la distance
    img1_flat = img1.flatten()
    img2_flat = img2.flatten()

    # Calcul de la distance euclidienne
    distance = np.linalg.norm(img1_flat - img2_flat)
    return distance