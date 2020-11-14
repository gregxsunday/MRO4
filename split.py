from imutils import paths
import random
import shutil

outdir = 'hummer400'

total = 0
for imagePath in paths.list_images(outdir):
    path = imagePath.replace('400/', '/')
    if random.uniform(0, 1) >= 0.7:
        path = 'validation/' + path
    else:
        path = 'training/' + path
    shutil.copyfile(imagePath, path)