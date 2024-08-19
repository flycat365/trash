

import cv2
import numpy as np
kernel = np.ones((5, 5), np.uint8)
planets = cv2.imread('D:/fu/296592388201473793.jpg')
gray_img = cv2.cvtColor(planets, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(planets, cv2.COLOR_BGR2HSV)
opening = cv2.morphologyEx(gray_img, cv2.MORPH_OPEN, kernel)
bila = cv2.bilateralFilter(opening, 10, 100, 200)
edges = cv2.Canny(bila, 70, 100)

circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 50, param1=120, param2=5, minRadius=10, maxRadius=40)

circles = np.uint16(np.around(circles))
a=0
for i in circles[0, :]:
    a+=1
    cv2.circle(planets, (i[0], i[1]), i[2], (0, 255, 0), 2)


    cv2.circle(planets, (i[0], i[1]), 2, (0, 0, 255), 3)



cv2.imshow("HoughCirlces", planets)
cv2.waitKey()
cv2.destroyAllWindows()
print(a)