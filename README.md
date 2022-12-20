# NLP_Img2txt
The practical apply in NLP image turn to text

## 1.PDFMiner & PyPDF2 : 
- $pip install pdfminer 
- $pip install PyPDF2 (pip install PyPDF2[crypto] : For crypto)

## 2.Turn to text 
- Program : 
    - [PDFMiner CV PDF](./PDFMiner_PDF2txt.py)
    - [PyPDF2 CV PDF](./PYPDF2_PDF2txt.py)
    - [PyPDF2 Alibaba PDF](./PYPDF2_PDF2txt.py)

- Result : 
    - [PDFMiner CV PDF Result](./data/Wizpresso/output/PDFMiner_20221129CV.txt)
    - [PyPDF2 CV PDF Result](./data/Wizpresso/output/PyPDF2_20221129CV.txt)
    - [PyPDF2 Alibaba PDF Result](./data/Wizpresso/output/PyPDF2_file.txt)

## 3.Encrypt PDF with customize Password
- Program : 
    - [PyPDF2 encrypt PDF](./PyPDF2_encryptPDF.py)

- Result : 
    - [PyPDF2 encrypt PDF Result](./data/Wizpresso/output/David_CV.pdf) #Password : 820224

### 4. Reference
- [PyPDF2 Apply](https://nanonets.com/blog/pypdf2-library-working-with-pdf-files-in-python) <br>
- [PDFMiner Document](https://pdfminer-docs.readthedocs.io/programming.html#performing-layout-analysis) <br>
- [PyPDF2 Extract Image](https://pypdf2.readthedocs.io/en/latest/user/extract-images.html)