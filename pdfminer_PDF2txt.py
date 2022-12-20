# python pdfminer_PDF2txt.py

''' Purpose : Read Document(PDF) save to TXT(.txt file) '''

import sys
import time
import os.path
import argparse
import importlib

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

importlib.reload(sys)
time_start = time.time()


def ReadPDF2TXT(pdf_path, txt_path):

    # 1.Preprocessing :
    fp = open(pdf_path, 'rb')  # class -> _io.BufferedReader
    # 用文件檔案創建分析器(型態轉換 : class -> 'pdfminer.pdfparser.PDFParser')
    parser = PDFParser(fp)
    # 型態轉換 : class -> 'pdfminer.pdfdocument.PDFDocument'
    doc = PDFDocument(parser)
    parser.set_document(doc)     # 連接分析器與文檔

    # 2.鑒察是否能轉換為txt 不行就raise
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 開始撈(爬)內文資料 :
        # enumerate :　將一個Array(list, tuple, string)變為有包含index的序列Array
        for i, page in enumerate(PDFPage.create_pages(doc)):

            interpreter.process_page(page)
            layout = device.get_result()

            # 操作text属性取得特定類型資料
            for content in layout:
                print(content)
                if(isinstance(content, LTTextBoxHorizontal)):  # Boolean判斷 : 判断一个參數是否與另一個參數相同資料型態

                    # Final : 開檔, 儲存
                    with open(txt_path, 'a', encoding='UTF-8') as f:
                        results = content.get_text()
                        f.write(results + "\n")


if __name__ == '__main__':

    # Path and call funciton :
    pdf_path = "./data/Wizpresso/input/20221129CV.pdf"
    txt_path = './data/Wizpresso/output/20221129CV.txt'
    ReadPDF2TXT(pdf_path, txt_path)

    # Operation Time :
    time_end = time.time()
    print("Total operation Time(運算時間) :", time_end-time_start)
