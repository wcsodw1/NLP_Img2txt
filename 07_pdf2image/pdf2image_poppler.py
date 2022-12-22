
# python pdf2image_poppler.py

from pdf2image import convert_from_path
images = convert_from_path("../data/testing/input/foo.pdf",
                           500, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')

path = "../data/testing/output/"
for i, image in enumerate(images):
    fname = path + 'image'+str(i)+'.png'
    print("Save image path is : ", fname)
    image.save(fname, "PNG")
