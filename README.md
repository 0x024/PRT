- 定义蓝色车牌的hsv范围
lower_blue = np.array([100, 50, 50])
higher_blue = np.array([140, 255, 255])
- 读取图片，
cv2.imread()
-  将图片转化为hsv模式
cv2.cvtColo()
- 找到所有符合蓝色区间的像素点，并转化为二值图像
cv2.inRange()
- 形态学变换处理
	- 闭操作
	cv2.getStructuringElement()
	cv2.morphologyEx()
	- 开操作
		- 侵蚀
		cv2.erode()
		- 膨胀
		cv2.dilate()
-  查找车牌区域
	- 查找外部轮廓
	cv2.findContours()
	- 计算轮廓面积
	cv2.contourArea()
	- 面积小的忽略
	if area<2000
	- 转换成对应的矩形
	cv2.minAreaRect()
	- 根据矩形转化为box类型
	box=np.int32(cv2.boxPoints())
	- 计算高和宽
	height=abs()
	width=abd()
	- 筛选长比高在2.7-5之间的车牌区域
	ratio = float(width)/float(height)
	if ratio >5 or ratio <2
	- 符合的加入轮廓集合
	region.append(box)
- 标记出车牌区域
cv2.drawContours()
- 展示标记出区域的图片
cv2.imshow()






























