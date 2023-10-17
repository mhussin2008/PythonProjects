print('hello world')
import operator
import numpy as np
import cv2

img_rgb = cv2.imread('original.png')
template = cv2.imread('small_template.png')
w, h = template.shape[:-1]


# font 
font = cv2.FONT_HERSHEY_SIMPLEX 
  
# org 
org = (50, 50) 
  
# fontScale 
fontScale = 1
   
# Blue color in BGR 
color = (255, 0, 0) 
  
# Line thickness of 2 px 
thickness = 2

print(w,h)
res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
threshold = .8
loc = np.where(res >= threshold)
i=0
for pt in zip(*loc[::-1]):# Switch columns and rows
     newpt = tuple(map(operator.sub, pt, (0,30)))
     cv2.rectangle(img_rgb, newpt, (pt[0] - 300, pt[1] + w+10), (0, 0, 255), 2)
     cv2.putText(img_rgb, str(i), newpt, font,  
                   fontScale, color, thickness, cv2.LINE_AA)
     i=i+1
     
          
     
#   cv2.rectangle(img_rgb, pt, (pt[0] - h, pt[1] + w), (0, 0, 255), 2)
# cv2.circle(img_rgb, pt,20,(0, 0, 255),2)
cv2.imwrite('result.png', img_rgb)