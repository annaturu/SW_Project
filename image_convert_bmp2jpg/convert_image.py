
import glob
import cv2
save_path = "/image_convert/"
path = glob.glob("/image_convert/*.jpg")
cv_img = []
cnt = 0
for img in path:
    n = cv2.imread(img)
    img=cv2.cvtColor(n,cv2.COLOR_BGR2GRAY)
    print(path)
    cv2.imshow("Input image",img)
    #cv2.imwrite('G004.jpg',img)
    cnt =cnt +1
    
    
    

"""
for imagepath in path.glob("*.jpg"):
        img=cv2.imread(str(imagepath))
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        print("imagepath",imagepath)

"""
    
"""
img = cv2.imread('good4.jpg', cv2.IMREAD_COLOR)

print("Image Size : ",img.size) # (475 x 600 x 3) ==> 855Kb
print("Image Shape : ",img.shape) # (height, width, channel)
print("Image Data Type : ", img.dtype) # unsigned integer 8 bi


b,g,r = cv2.split(img)

merge_result = cv2.merge((b,g,r))

cv2.imshow("BGR",img)

cv2.imshow("merge_result",merge_result)

cv2.imwrite('G004.jpg',merge_result)
"""
cv2.waitKey(0)

cv2.destroyAllWindows()


