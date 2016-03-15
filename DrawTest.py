import numpy as np
import cv2

from matplotlib import pyplot as plt
count = 0
maxCol = 0
maxRow = 0
maxVal = 0
temp = 0
quickRow = 0
quickCol = 0
im = cv2.imread('messi6.jpg')
kernel = np.ones((5, 5), np.float32)/25
blur = cv2.pyrDown(im)
blur2 = cv2.pyrUp(blur)
dst = cv2.filter2D(blur2, -1, kernel)
edges = cv2.Canny(dst, 30, 70)
colLength = len(edges[0, ...])
rowLength = len(edges[..., 0])
drawArray = edges.copy()
for i in range(0, colLength):
    for j in range(0, rowLength):
        if edges[j, i] == 255:
            count += 1
            if j-1 >= 0 and i-1 >= 0 and j+1 < rowLength and i+1 < colLength:
                temp = edges[j, i]/255 + edges[j-1, i]/255 + edges[j, i-1]/255 + edges[j+1, i]/255 + edges[j, i+1]/255 \
                       + edges[j+1, i+1]/255 + edges[j-1, i-1]/255 + edges[j-1, i+1]/255 + edges[j+1, i-1]/255
                if temp > maxVal:
                    maxVal = temp
                    maxRow = j
                    maxCol = i



def RemovePoint(row, col):
    global count
    if drawArray[row, col] != 0:
        drawArray[row, col] = 0
        count -= 1
    point = [row, col]
    if row-1 >= 0 and col-1 >= 0 and drawArray[row-1, col-1] == 255:
        point = RemovePoint(row - 1, col - 1)
    if row+1 < rowLength and col+1 < colLength and drawArray[row+1, col+1] == 255:
        point = RemovePoint(row + 1, col + 1)
    if row-1 >= 0 and drawArray[row-1, col] == 255:
        point = RemovePoint(row - 1, col)
    if col-1 >= 0 and drawArray[row, col-1] == 255:
        point = RemovePoint(row, col - 1)
    if row+1 < rowLength and col-1 >= 0 and drawArray[row+1, col-1] == 255:
        point = RemovePoint(row + 1, col - 1)
    if row-1 >= 0 and col+1 < colLength and drawArray[row-1, col+1] == 255:
        point = RemovePoint(row - 1, col + 1)
    if col+1 < colLength and drawArray[row, col+1] == 255:
        point = RemovePoint(row, col + 1)
    if row+1 < rowLength and drawArray[row+1, col] == 255:
        point = RemovePoint(row + 1, col)
    return point


def ConnectPoints(row, col):
    pointRow = row
    pointCol = col
    val = 2
    global quickRow
    global quickCol
    while val < rowLength and val < colLength:
        if row-val >= 0 and drawArray[row-val,col] == 255:
            pointRow = row-val
            break
        elif col-val >= 0 and drawArray[row,col-val] == 255:
            pointCol = col-val
            break
        elif col+val < colLength and drawArray[row,col+val] == 255:
            pointCol = col+val
            break
        elif row+val < rowLength and drawArray[row+val,col] == 255:
            pointRow = row+val
            break
        elif col-val >= 0 and row-val >= 0 and drawArray[row-val,col-val] == 255:
            pointCol = col-val
            pointRow = row-val
            break
        elif col+val < colLength and row-val >= 0 and drawArray[row-val,col+val] == 255:
            pointCol = col+val
            pointRow = row-val
            break
        elif row+val < rowLength and col-val >= 0 and drawArray[row+val,col-val] == 255:
            pointCol = col-val
            pointRow = row+val
            break
        elif row+val < rowLength and col+val < colLength and drawArray[row+val, col+val] == 255:
            pointCol = col+val
            pointRow = row+val
            break
        else:
            val += 1
    if val >= rowLength or val >= colLength:
        for i in range(quickRow, rowLength):
            for j in range(0, colLength):
                if drawArray[i,j] == 255:
                    pointRow = i
                    pointCol = j
                    quickRow = i
                    point = [pointRow, pointCol]
                    return point
    point = [pointRow, pointCol]
    return point

point = RemovePoint(maxRow, maxCol)

while count > 1:
    newPoint = ConnectPoints(point[0], point[1])
    RemovePoint(newPoint[0], newPoint[1])

print count
print maxVal
print point[0]
print point[1]
print maxRow
print maxCol

plt.subplot(121), plt.imshow(drawArray, cmap='gray')
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.show()
