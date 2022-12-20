
# python PYPDF2.py

import pandas
import PyPDF2

#  create a reader object(f)
f = open('./data/Wizpresso/input/20221129CV.pdf', 'rb')
txt_path = './data/Wizpresso/output/PyPDF2_20221129CV.txt'
# pdfFileReader() reads the text  form the pdf
pdf_reader = PyPDF2.PdfFileReader(f)
page_num = pdf_reader.numPages

print(pdf_reader.isEncrypted)
# pdfReader.decrypt('rosebud')


# Print all the text from looping page :
for i in range(page_num):
    # read PDF page N information
    page_i = pdf_reader.getPage(i)
    # print(page_one)

    # extractText() extracts the the texts in a text format of page 1
    page_i_text = page_i.extractText()
    with open(txt_path, 'a', encoding='UTF-8') as f:
        f.write(page_i_text + "\n")
