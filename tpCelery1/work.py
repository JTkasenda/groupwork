from celery import Celery
from PIL import Image
import os

app = Celery(
    'tpcelery1',
    broker='amqp://guest:guest@192.168.1.254/',
    backend='rpc://'
)

@app.task #By doing this Addition becomes  a task that can be executed concurrently and can be executed using celery
def ColorToWhite(chemin_image):
    image = Image.open(chemin_image)
    image_noir_blanc = image.convert("L")

    dossier_convert = "img_convert"
    if not os.path.exists(dossier_convert):
        os.makedirs(dossier_convert)

    nom_image = os.path.basename(chemin_image)
    chemin_image_noir_blanc = os.path.join(dossier_convert, nom_image.replace(".", "_noir_blanc."))
    image_noir_blanc.save(chemin_image_noir_blanc)