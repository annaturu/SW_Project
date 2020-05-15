import os
import glob
import cv2
from PIL import Image

#save_path = "G:\SW산학PJ_TSE\image_convert/bmp2jpg_good/"
save_path = "G:\SW산학PJ_TSE\image_convert/bmp2jpg_bad/"
save_file_extend = ".jpg"
#path = glob.glob("G:\SW산학PJ_TSE\Soldering_good/*.bmp")
path = glob.glob("G:\SW산학PJ_TSE\Soldering_bad/*.bmp")
cv_img = []
cnt = 0
for img in path:
    im = Image.open(img)
    #im.save("test.jpg","JPEG")
    file_name = os.path.basename(img)
    #print(file_name)
    only_file_name = os.path.splitext(file_name)
    #print(only_file_name[0])
    save_file_name = save_path+only_file_name[0]+save_file_extend
    print(save_file_name)
    im.save(save_file_name,"JPEG")
    cnt =cnt +1



