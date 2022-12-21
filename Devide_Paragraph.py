# python Devide_Paragrph.py

import re
import pdfplumber

file_path = "./data/US_Declaration.pdf"
pdf = pdfplumber.open(file_path)


# for page in range(len(pdf.pages)):
p0 = pdf.pages[2]
text = p0.extract_text()

patterns = '.\n'  # 關鍵在text取出的資料 如何做切分 (ex : '.\n  ', '\n ')
paragraphs = text.split(patterns)
# print(text)

with open('./data/Wizpresso/output/Devide_Paragraph_US.txt', 'a', encoding='UTF-8') as f:

    for num, paragraph in enumerate(paragraphs):
        print('paragraph:', num)
        print("")
        print('  ', paragraph.strip())
        f.write("paragraph : " + str(num))
        f.write(paragraph + "\n")
