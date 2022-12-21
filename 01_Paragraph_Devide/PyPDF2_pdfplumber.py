# python PyPDF2_pdfplumber.py

import re
import pdfplumber

file_path = "../data/testing/input/US_Declaration.pdf"
pdf = pdfplumber.open(file_path)


# for page in range(len(pdf.pages)):
p0 = pdf.pages[2]
text = p0.extract_text()

patterns = '.\n'  # 關鍵在text取出的資料 如何做切分 (ex : '.\n  ', '\n ')
paragraphs = text.split(patterns)
# print(text)

with open('../data/testing/output/01_DevideParagraph_US.txt', 'a', encoding='UTF-8') as f:

    for num, paragraph in enumerate(paragraphs):
        print('paragraph:', num)
        print('  ', paragraph.strip())
        f.write("paragraph : " + str(num))
        f.write(paragraph + "\n")
