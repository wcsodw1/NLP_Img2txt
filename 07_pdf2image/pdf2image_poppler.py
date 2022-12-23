
# python pdf2image_poppler.py -p "../data/testing/input/foo.pdf" -o "../data/testing/output/"

import argparse
from pdf2image import convert_from_path


# 1.parse the argument :
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--PDF_path", required=True,
                help="Path to the PDF file")
ap.add_argument("-o", "--output_image_path", required=True,
                help="Path to save the output image(name)")
args = vars(ap.parse_args())

# 2.Set the path
images = convert_from_path(args["PDF_path"],
                           500, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
path = args["output_image_path"]


# 3.Select the image from PDF-TRANSFORM-IMAGE
for i, image in enumerate(images):
    print(i)
    fname = path + 'image'+str(i)+'.png'
    print("Save image path is : ", fname)
    image.save(fname, "PNG")
