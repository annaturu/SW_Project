import os
import cv2
from PIL import Image
import glob

"""
img = cv2.imread("F:/image_convert/bmp2jpg_bad/2.0_3_FX=420_LZ0=3.0(1000)_LZ1=4.0(2000)_LZ2=8.5(2000).jpg", cv2.IMREAD_COLOR)
print("image size: ",img.size)
print("image shape: ",img.shape) # heiht, width, channel
cv2.imshow("img",img)

"""

filepath = glob.glob("F:/image_convert/bmp2jpg_bad/*.jpg")

save_filepath = "F:/image_convert/bmp2jpg_bad/bmp2jpg2png_bad/"
file_extended = ".png"
cnt = 0
for files in filepath:
    print(files)
    img = cv2.imread(files, cv2.IMREAD_COLOR)
    #print("image size: ",img.size)
    #print("image shape: ",img.shape) # heiht, width, channel
    cv2.imshow(files,img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cnt =cnt + 1
    print("File cnt: ",cnt)
    
    #if files.endswith(".jpg"):
        #print(files)

        #img = cv2.imread(files, cv2.IMREAD_COLOR)
        #print("img",img)
        

        #print("image name",files)
        #print("image size: ",img.size)
        #print("image shape: ",img.shape) # heiht, width, channel
        #cvt_grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #s = os.path.splitext(files)
        #s = os.path.split(s[0])
        
        #cvt_filename = s[1]+file_extended
        #print("cvt_filename: ",cvt_filename)
        #cvt_filepath = save_filepath + cvt_filename
        #print("cvt_filepath: ",cvt_filepath)
        #cv2.imshow(files,img)
        #cv2.imshow("cvt_grayimg",cvt_grayimg)

        #cv2.imwrite(cvt_filepath,cvt_grayimg)
        
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        #cnt =cnt + 1
        #print("File cnt: ",cnt)
    
        

