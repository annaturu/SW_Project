import os
import glob
import cv2
from PIL import Image

path = glob.glob("F:/image_convert/bmp2jpg2png_good/*.png")
save_path = "F:/image_convert/bmp2jpg2png2jpg_good/"
save_file_extend = ".jpg"

cv_img = []
cnt = 0
for img in path:

    full_file_name = os.path.basename(img)
    file_name = os.path.splitext(full_file_name)
    save_file_name = save_path+file_name[0]+save_file_extend
    
    #print("full_file_name",full_file_name)
    #print("file_name",file_name[0])
    #print("save_file_name",save_file_name)
    
    image = cv2.imread(img, cv2.IMREAD_COLOR)
    #img=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    img_b, img_g, img_r = cv2.split(image)

    merge_rgb = cv2.merge((img_r,img_g,img_b))
    
        
    #cv2.imshow("Original image",image)
    #cv2.imshow("img_b",img_b)
    #cv2.imshow("img_g",img_g)
    #cv2.imshow("img_r",img_r)
    #cv2.imshow("merge_rgb",merge_rgb)

    cv2.imwrite(save_file_name,merge_rgb)
    
    
    cnt =cnt +1
    print("cnt : ",cnt)

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

"""
save_path = "F:/image_convert/bmp2jpg2png_bad/"
save_file_extend = ".png"
path = glob.glob("F:/image_convert/bmp2jpg_bad/*.jpg")
cv_img = []
cnt = 0
for img in path:

    full_file_name = os.path.basename(img)
    file_name = os.path.splitext(full_file_name)
    save_file_name = save_path+file_name[0]+save_file_extend
    
    print("full_file_name",full_file_name)
    print("file_name",file_name[0])
    print("save_file_name",save_file_name)
    
    image = cv2.imread(img, cv2.IMREAD_COLOR)
    #img=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    img_b, img_g, img_r = cv2.split(image)

    merge_rgb = cv2.merge((img_r,img_g,img_b))
    
        
    cv2.imshow("Original image",image)
    #cv2.imshow("img_b",img_b)
    #cv2.imshow("img_g",img_g)
    #cv2.imshow("img_r",img_r)
    cv2.imshow("merge_rgb",merge_rgb)

    cv2.imwrite(save_file_name,merge_rgb)
    
    
    cnt =cnt +1

    if cnt > 3:
        break

    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""

