from PIL import Image, ImageEnhance, ImageOps
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Chargement de l'image
image_path = 'image_1.jpg'
image = Image.open(image_path)

# Liste des transformations à appliquer
transformations = {
    'Original': image,
    'Color Jitter (Couleurs amplifiées)': ImageEnhance.Color(image).enhance(2.0),
    'Inversé (Négatif)': ImageOps.invert(image.convert("RGB")),
    'Noir et Blanc': image.convert('L'),
    'Plus Lumineux': ImageEnhance.Brightness(image).enhance(1.5),
    'Moins Lumineux': ImageEnhance.Brightness(image).enhance(0.5),
    'Contraste Augmenté': ImageEnhance.Contrast(image).enhance(2.0),
    'Contraste Réduit': ImageEnhance.Contrast(image).enhance(0.5)
}

# Création d'une figure pour afficher les transformations
plt.figure(figsize=(12, 8))

# Boucle pour appliquer les transformations et afficher les images
for index, (title, transformed_image) in enumerate(transformations.items()):
    plt.subplot(4, 2, index + 1)
    # Affichage en noir et blanc pour la 4ème transformation (Noir et Blanc)
    if title == 'Noir et Blanc':
        plt.imshow(transformed_image, cmap='gray')
    else:
        plt.imshow(transformed_image)
    plt.title(title)
    plt.axis('off')

# Enregistrement de la figure finale
plt.tight_layout()
plt.savefig('screen/result_transformations.png')
plt.show()


# # # #
# Chargement de l'image
image_path = 'image_1.jpg'
image = cv2.imread(image_path)
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

# Définition des transformations
transformations = {
    'Original': image,
    'Recadré': image[50:250, 50:250],  # Recadrage centré
    'Retourné Horizontalement': cv2.flip(image, 1),
    'Retourné Verticalement': cv2.flip(image, 0),
    'Roté (45°)': cv2.warpAffine(image, cv2.getRotationMatrix2D(center, 45, 1.0), (w, h)),
    'Déplacé': cv2.warpAffine(image, np.float32([[1, 0, 20], [0, 1, 50]]), (w, h)),
    'Perspective Modifiée': cv2.warpPerspective(image,
        cv2.getPerspectiveTransform(
            np.float32([[50, 50], [200, 50], [50, 200], [200, 200]]),
            np.float32([[10, 100], [200, 50], [100, 250], [200, 200]])
        ),
        (w, h)
    )
}

# Affichage des transformations
plt.figure(figsize=(12, 8))

for i, (title, transformed_img) in enumerate(transformations.items()):
    plt.subplot(4, 2, i + 1)
    plt.imshow(cv2.cvtColor(transformed_img, cv2.COLOR_BGR2RGB))  # Conversion en RGB
    plt.title(title)
    plt.axis('off')

# Ajustement de l'affichage et sauvegarde de l'image
plt.tight_layout()
plt.savefig('screen/transformations_position.png')
plt.show()
