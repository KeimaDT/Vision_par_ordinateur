import cv2

#Créer une méthode ‘display_image’
def display_image(img, name='Image'):
    if img is not None:
        cv2.imshow(name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error image")