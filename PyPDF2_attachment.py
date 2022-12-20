
# python PyPDF2_attachment.py
import pandas as pd
from PyPDF2 import PdfReader

reader = PdfReader("./data/Wizpresso/input/20221129CV.pdf")
txt_path = "./data/Wizpresso/output/PyPDF2_attachment.txt"

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
