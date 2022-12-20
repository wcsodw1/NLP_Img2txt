
# python PYPDF2.py

import PyPDF2

#  create a reader object(f)
f = open('./data/Wizpresso/input/20221129CV.pdf', 'rb')

# pdfFileReader() reads the text  form the pdf
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)
print(pdf_reader.isEncrypted)
