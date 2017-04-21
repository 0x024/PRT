# -*- coding: utf-8 -*-

import cv2
import sys
import numpy as np

img=cv2.imread('./raw/6.jpg')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("test",img_gray)
# cv2.waitKey(0)
gaussian=cv2.GaussianBlur(img_gray,(3,3),0,0,cv2.BORDER_DEFAULT)
# cv2.imshow("gaussian",gaussian)
# cv2.waitKey(0)
median=cv2.medianBlur(gaussian,3)
# cv2.imshow('median',median)
# cv2.waitKey(0)
sobel = cv2.convertScaleAbs(cv2.Sobel(gaussian, cv2.CV_16S, 1, 0, ksize=3))
# cv2.imshow('sobel',sobel)
# cv2.waitKey(0)
ret,binary = cv2.threshold(sobel,200,255,cv2.THRESH_BINARY)
cv2.namedWindow("binary",cv2.WINDOW_NORMAL)
cv2.imshow('binary',binary)
cv2.waitKey(0)
element=cv2.getStructuringElement(cv2.MORPH_RECT,(20,10))
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, element)
# cv2.imshow('closed',closed)
# cv2.waitKey(0)
erosion=cv2.erode(closed,None,iterations=5)
# cv2.imshow('erosion',erosion)
# cv2.waitKey(0)
dilation =cv2.dilate(erosion,None,iterations=18)
cv2.namedWindow("dilation",cv2.WINDOW_NORMAL)
cv2.imshow('dilation',dilation)
cv2.waitKey(0)
img1,contours,hierarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
region=[]
for i in range(len(contours)):
	cnt = contours[i]
	area=cv2.contourArea(cnt)
	if area < 2000:
		continue
	rect = cv2.minAreaRect(cnt)
	box=np.int32(cv2.boxPoints(rect))
	height = abs(box[0][1]-box[2][1])
	width = abs(box[0][0]-box[2][0])
	ratio=float(width)/float(height)
	if ratio> 5 or ratio<2:
		continue
	region.append(box)
for box in region:
	cv2.drawContours(img,[box],0,(0,2255,255),3)
	cv2.namedWindow("image",cv2.WINDOW_NORMAL)
	cv2.imshow('image',img)
	cv2.waitKey(0)
