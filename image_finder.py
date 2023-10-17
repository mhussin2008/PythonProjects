print('hello world')
import operator
import numpy as np
import cv2

img_rgb = cv2.imread('original.png')
template = cv2.imread('small_template.png')
w, h = template.shape[:-1]

print(w,h)
res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
threshold = .8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):# Switch columns and rows
     newpt = tuple(map(operator.sub, pt, (0,30)))
     cv2.rectangle(img_rgb, newpt, (pt[0] - 300, pt[1] + w+10), (0, 0, 255), 2)
#   cv2.rectangle(img_rgb, pt, (pt[0] - h, pt[1] + w), (0, 0, 255), 2)
# cv2.circle(img_rgb, pt,20,(0, 0, 255),2)
cv2.imwrite('result.png', img_rgb)