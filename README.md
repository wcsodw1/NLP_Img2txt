# NLP_Img2txt
The practical apply in NLP image turn to text

## 1.PyPDF2 & PDFMiner: 
- $pip install PyPDF2 (pip install PyPDF2[crypto] : For crypto)
- $pip install pdfminer

## 2.PDF to text 
- Program : 
    - [PyPDF2 CV PDF](./PyPDF2_PDF2txt.py)
    - [PyPDF2 Alibaba PDF](./PyPDF2_PDF2txt.py)
    - [PDFMiner CV PDF ](./PDFMiner_PDF2txt.py)
    - [PyPDF2 CV PDF attachment](./PyPDF2_attachment.txt)

- Result : 
    - [PDFMiner CV PDF txt](./data/Wizpresso/output/PDFMiner_20221129CV.txt)
    - [PyPDF2 CV PDF txt](./data/Wizpresso/output/PyPDF2_20221129CV.txt)
    - [PyPDF2 Alibaba PDF txt](./data/Wizpresso/output/PyPDF2_file.txt)
    - [PyPDF2 CV PDF attachment](./data/Wizpresso/output/PyPDF2_attachment.txt)



## 3.Encrypt/Decrypte PDF with customize Password
- Program : 
    - [PyPDF2 encrypt PDF](./PyPDF2_encryptPDF.py)
    - [PyPDF2 Decrypt PDF](./PyPDF2_DecryptPDF.py)

- Result : 
    - [PyPDF2 encrypt PDF Result](./data/Wizpresso/output/Encrypt_David_CV.pdf) #Password : 820224
    - [PyPDF2 encrypt PDF Result](./data/Wizpresso/output/Decrypt_David_CV.pdf) #Password : 820224

### 4.Devide Paragraph : 
    - [PyPDF2 Devide_Paragrph](./Devide_Paragraph.py)

### Reference
- [PyPDF2 Document](https://pypdf2.readthedocs.io/en/latest/) <br>
- [PyPDF2 Apply](https://nanonets.com/blog/pypdf2-library-working-with-pdf-files-in-python) <br>
- [PyPDF2 PDF Annotations](https://pypdf2.readthedocs.io/en/latest/user/reading-pdf-annotations.html) <br>
- [Devide Paragraph by Python re](https://docs.python.org/zh-tw/3.8/library/re.html)
- [PDFMiner Document](https://pdfminer-docs.readthedocs.io/programming.html#performing-layout-analysis) <br>
