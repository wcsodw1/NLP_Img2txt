
# python PyPDF2_attachment.py
import pandas as pd
from PyPDF2 import PdfReader

reader = PdfReader("../data/testing/input/20221129CV.pdf")

# save to .csv or .txt
txt_path = "../data/testing/output/02_attachment_PyPDF2_20221129CV.csv" 
# txt_path = "../data/testing/output/02_attachment_PyPDF2_20221129CV.txt"


list_ = []
for page in reader.pages:
    if "/Annots" in page:
        for annot in page["/Annots"]:
            obj = annot.get_object()
            annotation = {"subtype": obj["/Subtype"], "location": obj["/Rect"]}
            content = list(annotation.items())
            list_.append(content)

# Final : 開檔, 儲存
df = pd.DataFrame.from_dict(list_)
df.to_csv(txt_path, index=False)
