

# It's spent a couple hour on how to install Poppler for me on windows : 

and  solution is : my

step1.Download the (0.68.0_x86 version) in the path of program file
https://blog.alivate.com.au/poppler-windows/
step2. unzip the file(.7z)
step3. Set the "bin" path on enviroment-variable(ex:C:\Program Files\poppler-0.68.0\bin)
step4. Program mention about the path of "bin"
from pdf2image import convert_from_path
images = convert_from_path("../data/testing/input/foo.pdf",
                           500, poppler_path=r'C:\Program Files\poppler-0.68.0\bin') 

step5.And it works!