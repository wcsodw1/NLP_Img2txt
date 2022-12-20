
# python PyPDF2_encryptPDF.py -f './data/Wizpresso/input/20221129CV.pdf' -p "820224" -o './data/Wizpresso/output/Encrypt_David_CV.pdf'


import argparse
from PyPDF2 import PdfReader, PdfWriter


ap = argparse.ArgumentParser()

ap.add_argument("-f", "--file_PDF", required=True,
                help="Path to the source PDF file")
ap.add_argument("-p", "--Password", required=True,
                help="The PDF Password")
ap.add_argument("-o", "--output_txt", required=True,
                help="Path to save the output pdf name (file)")
args = vars(ap.parse_args())

reader = PdfReader(args["file_PDF"])
writer = PdfWriter()


# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Add a password to the new PDF
writer.encrypt(args["Password"])

# Save the new PDF to a file
with open(args["output_txt"], "wb") as f:
    writer.write(f)