
# python english2chinese.py -img_e "./img/ENGLISH.png"

# 其他語言包要另外下載 網址 : https://github.com/tesseract-ocr/tessdata
# 中文包要另外下載(chi_tra.traineddata)
# 路徑放入 : C:\Program Files\Tesseract-OCR\tessdata


#========= 1.Import Library =========#
import cv2
import argparse
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


#========= 2.Parse the argument =========#
ap = argparse.ArgumentParser()
ap.add_argument("-img_e", "--image_english",
                required=True, help="The Path to image")
args = vars(ap.parse_args())
image_eng = cv2.imread(args["image_english"])


#========= 3.English Image convert to Word =========#
print("#========= 3.English Image convert to Word =========#")
eng_text = pytesseract.image_to_string(image_eng, lang='eng')
print(eng_text)
with open("./output/english.txt", "w", encoding='UTF-8') as text_file:
    text_file.write(eng_text)
