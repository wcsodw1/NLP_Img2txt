
# python app.py -img_c2_path "../data/img/test.PNG"
# python app.py -img_c_path "../data/img/chinese.PNG" -img_e "../data/img/image2word.PNG"
# 其他語言包要另外下載 網址 : https://github.com/tesseract-ocr/tessdata
# 中文包要另外下載(chi_tra.traineddata)
# 路徑放入 : C:\Program Files\Tesseract-OCR\tessdata


import cv2
import argparse
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

ap = argparse.ArgumentParser()
ap.add_argument("-img_c_path", "--image_tradition_chinese",
                required=False, help="The Path to image")
ap.add_argument("-img_c2_path", "--image_simplify_chinese",
                required=True, help="The Path to image")
ap.add_argument("-img_e", "--image_english",
                required=False, help="The Path to image")
#ap.add_argument("-chi_out","--image_chinese_output", required = True, help = "The Path image to word output")

args = vars(ap.parse_args())
image_chi_tra = cv2.imread(args["image_tradition_chinese"])
image_chi_sim = cv2.imread(args["image_simplify_chinese"])


#========= 1.Chinese Tradition Image convert to Word =========#
# print("#========= 1.Chinese Image convert to Word =========#" )
# text = pytesseract.image_to_string(image_chi_tra, lang='chi_tra')
# print(type(text))
# print(text)
# with open("../data/img/chinese_tra.txt", "w", encoding='UTF-8') as text_file:
#     text_file.write(text)
# print("")

#========= 2.Chinese Simplify Image convert to Word =========#
print("#========= 2.Chinese Image convert to Word =========#")
text2 = pytesseract.image_to_string(image_chi_sim, lang='chi_sim')
print(type(text2))
print(text2)
with open("../data/img/chinese_sim.txt", "w", encoding='UTF-8') as text_file:
    text_file.write(text2)
print("")


