import os
import time
from tpCelery1.work import ColorToWhite

if __name__ == '__main__':
    dossier_images = "cars"
    chemins_images = [os.path.join(dossier_images, fichier) for fichier in os.listdir(dossier_images) if fichier.endswith((".jpg", ".png", ".bmp"))]

    debut = time.time()
    for chemin_image in chemins_images:
        converted = ColorToWhite.delay(chemin_image)
    fin = time.time()

    temps_total = fin - debut
    print(f"Temps total écoulé pour le traitement de {len(chemins_images)} images : {temps_total} secondes.")