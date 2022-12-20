
# python PYPDF2.py -f './data/Wizpresso/input/20221129CV.pdf' -o './data/Wizpresso/output/PyPDF2_20221129CV.txt'
# python PYPDF2.py -f './data/Wizpresso/input/file.pdf' -o './data/Wizpresso/output/PyPDF2_file.txt'


# 1.preprocess : import necessary libray and parse the argument
import pandas
import PyPDF2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file_PDF", required=True,
                help="Path to the source PDF file")
ap.add_argument("-o", "--output_txt", required=True,
                help="Path to save the output txt file")
args = vars(ap.parse_args())


# 2.Change data structure :
f = open(args["file_PDF"], 'rb')  # create a reader object(f)
# pdfFileReader() reads the text form the pdf
pdf_reader = PyPDF2.PdfFileReader(f)
page_num = pdf_reader.numPages  # check the number of PDF page
# print(pdf_reader.isEncrypted) # check data Crypt or not(return true or false)
# pdfReader.decrypt('rosebud') # Decrypted

# 3.Print PDF content and Save :
# Print all the text from looping page :

pdf_writer = PyPDF2.PdfFileWriter()

for i in range(page_num):
    # a.read PDF page N information
    page_i = pdf_reader.getPage(i)

    # b.extractText() extracts the texts in a text format from each page
    page_i_text = page_i.extractText()

    # c.Save the PDF content to .txt
    with open(args["output_txt"], 'a', encoding='UTF-8') as f:
        f.write(page_i_text + "\n")

    # D.Add page
    # pdf_writer.addPage(page_i)
    # pdf_output = open("./data/Wizpresso/output/New.pdf", "wb")
    # pdf_writer.write(pdf_output)
