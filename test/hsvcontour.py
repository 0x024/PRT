# -*- coding: utf-8 -*-

import cv2
import numpy as np
lower_blue = np.array([100, 50, 50])
higher_blue = np.array([140, 255, 255])
img = cv2.imread("./raw/6.jpg")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow('hsv_img',hsv_img)
# cv2.waitKey(0)
in_range_array = cv2.inRange(hsv_img, lower_blue, higher_blue)
cv2.namedWindow("in_range_array",cv2.WINDOW_NORMAL)
cv2.imshow('in_range_array',in_range_array)
cv2.waitKey(0)
element = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 3))
closed = cv2.morphologyEx(in_range_array, cv2.MORPH_CLOSE, element)
# cv2.imshow('closed',closed)
# cv2.waitKey(0)
eroded = cv2.erode(closed, None, iterations=2)
# cv2.namedWindow("eroded",cv2.WINDOW_NORMAL)
# cv2.imshow('eroded',eroded)
# cv2.waitKey(0)
dilation = cv2.dilate(eroded, None, iterations=2)
cv2.namedWindow("dilation",cv2.WINDOW_NORMAL)
cv2.imshow('dilation',dilation)
cv2.waitKey(0)
region = []
img1,contours,hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for i in range(len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    if area < 2000:
        continue
    rect = cv2.minAreaRect(cnt)

    box = np.int32(cv2.boxPoints(rect))
    height = abs(box[0][1] - box[2][1])
    width = abs(box[0][0] - box[2][0])
    ratio = float(width) / float(height)
    if ratio > 5 or ratio < 2:
        continue
    region.append(box)
for box in region:
    aaa=cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
    cv2.namedWindow("img",cv2.WINDOW_NORMAL)
    cv2.imshow("img", aaa)  
    cv2.waitKey(0)
