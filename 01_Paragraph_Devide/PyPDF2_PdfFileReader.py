
# python PyPDF2.py (fail) 

'''依照文檔狀況 有些檔案無法讀取到title'''

import os
from PyPDF2 import PdfFileReader
pdf = PdfFileReader('../data/testing/input/20221129CV.pdf')
bookmarks = pdf.getOutlines()
print(bookmarks)
page = []


def get_pagenum(page, lit):
    for i in range(len(lit)):
        if len(i) == 1:
            page.append([i['/Title'], pdf.getDestinationPageNumber(lit[i])])
        else:
            get_pagenum(page, i)
    return page


get_pagenum(page, bookmarks)
