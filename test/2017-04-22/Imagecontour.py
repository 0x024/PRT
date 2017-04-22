# -*- coding: utf-8 -*-

import cv2
import sys
import numpy as np

img=cv2.imread('./raw/3.jpg')
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
# cv2.namedWindow("binary",cv2.WINDOW_NORMAL)
# cv2.imshow('binary',binary)
# cv2.waitKey(0)
element=cv2.getStructuringElement(cv2.MORPH_RECT,(20,10))
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, element)
# cv2.imshow('closed',closed)
# cv2.waitKey(0)
erosion=cv2.erode(closed,None,iterations=5)
# cv2.imshow('erosion',erosion)
# cv2.waitKey(0)
dilation =cv2.dilate(erosion,None,iterations=18)
# cv2.namedWindow("dilation",cv2.WINDOW_NORMAL)
# cv2.imshow('dilation',dilation)
# cv2.waitKey(0)
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
	ys=[box[0,1],box[1,1],box[2,1],box[3,1]]
	xs=[box[0,0],box[1,0],box[2,0],box[3,0]]
	ys_sorted_index=np.argsort(ys)
	xs_sorted_index=np.argsort(xs)
	min_x = box[xs_sorted_index[0], 0]
	max_x = box[xs_sorted_index[3], 0]
	min_y = box[ys_sorted_index[0], 1]
	max_y = box[ys_sorted_index[3], 1]
	img_plate = img[(min_y-10):max_y+10, min_x-10:max_x+10]
	cv2.namedWindow("img",cv2.WINDOW_NORMAL)
	cv2.imshow("img", img_plate)  
	cv2.imwrite("img.jpg",img_plate)
	cv2.waitKey(0)
	img_gray=cv2.cvtColor(img_plate,cv2.COLOR_BGR2GRAY)
	# cv2.namedWindow("img_gray",cv2.WINDOW_NORMAL)
	# cv2.imshow("img_gray",img_gray)
	# cv2.waitKey(0)
	gaussian=cv2.GaussianBlur(img_gray,(3,3),0,0,cv2.BORDER_DEFAULT)
	# cv2.namedWindow("gaussian",cv2.WINDOW_NORMAL)
	# cv2.imshow("gaussian",gaussian)
	# cv2.waitKey(0)
	median=cv2.medianBlur(gaussian,1)
	# cv2.namedWindow("median",cv2.WINDOW_NORMAL)
	# cv2.imshow('median',median)
	# cv2.waitKey(0)
	# sobel8u = cv2.Sobel(median,cv2 .CV_8U,1,0,ksize=1)
	# cv2.namedWindow("sobel8u",cv2.WINDOW_NORMAL)
	# cv2.imshow('sobel8u',sobel8u)
	# cv2.waitKey(0)  
	edges = cv2.Canny(img_plate,100,200)
	cv2.imshow('edges',edges)
	cv2.waitKey(0)

	# ret,thresh = cv2.threshold(edges,127,255,0)
	# cv2.namedWindow("thresh",cv2.WINDOW_NORMAL)
	# cv2.imshow('thresh',thresh)
	# cv2.waitKey(0)

	img1,contours,hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	region=[]
	for i in range(len(contours)):
		cnt = contours[i]
		area=cv2.contourArea(cnt)
		if area < 300:
			continue
		rect = cv2.minAreaRect(cnt)
		box=np.int32(cv2.boxPoints(rect))
		height = abs(box[0][1]-box[2][1])
		width = abs(box[0][0]-box[2][0])
		ratio=float(width)/float(height)
		if ratio>1.5 or ratio<0.2:
			continue
		region.append(box)
	for box in region:
		cv2.drawContours(median,[box],0,(0,2255,255),3)
		cv2.namedWindow("image",cv2.WINDOW_NORMAL)
		cv2.imshow('image',median)
		cv2.waitKey(0)


