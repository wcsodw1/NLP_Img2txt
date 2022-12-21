
# python pdf2image.py

import pdf2image
doc = pdf2image.convert_from_path("../data/testing/input/foo.pdf")
len(doc)  # <-- check num pages
doc[0]  # <-- visualize a page
