from imutils import paths
import argparse
import requests
import cv2
import os

for outdir in ['hatch', 'f1', 'hummer']:
    total = 0
    for imagePath in paths.list_images(outdir):
        p = os.path.sep.join([f'cars/{outdir}', "{}.jpg".format(str(total).zfill(3))])
        total += 1
        image = cv2.imread(imagePath)
        image = cv2.resize(image, (224, 224)) 
        cv2.imwrite(p, image)