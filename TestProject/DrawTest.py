import numpy as np
import cv2
#import MotorTest as mt

from matplotlib import pyplot as plt
count = 0
maxCol = 0
maxRow = 0
maxVal = 0
temp = 0
quickRow = 0

import serial
import time
import struct
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
ser.open()
time.sleep(2)
ser.write('9\r\n')

string = ''
delay = 0.5

def left(steps, speed):
    global string
    string = string + '2'
    print 'left'
def right(steps, speed):
    global string
    string = string + '3'
    print 'right'
def down(steps, speed):
    global string
    string = string + '1'
    print 'down'
def up(steps, speed):
    global string
    string = string + '0'
    print 'up'
def upLeft(steps1, speed):
    global string
    string = string + '7'
    print 'upleft'
def upRight(steps1, speed):
    global string
    string = string + '4'
    print 'upright'
def downLeft(steps1, speed):
    global string
    string = string + '5'
    print 'downleft'
def downRight(steps1, speed):
    global string
    string = string + '6'
    print 'downright'





speed = 1
step = 1
im = cv2.imread('messi60.png')
kernel = np.ones((5, 5), np.float32)/25
blur = cv2.pyrDown(im)
blur2 = cv2.pyrUp(blur)
dst = cv2.filter2D(blur2, -1, kernel)
drawArray = cv2.Canny(dst, 30, 70)
#drawArray = np.ones((1000,1000),np.float32)*255    #used for recursion depth test
colLength = len(drawArray[0, ...])
rowLength = len(drawArray[..., 0])
colZeroes = np.zeros((1, colLength), np.float32)
rowZeroes = np.zeros((rowLength, 1), np.float32)

#change to 100 if connectPoints problems occur
for i in range(0, int(colLength/25)):
    drawArray[...,i*25] = rowZeroes[...,0]
for i in range(0, int(rowLength/25)):
    drawArray[i*25,...] = colZeroes[0,...]

#Used to count white pixels around current pixel
def countIntersect(connected,row,col):
    count = 0
    if row - 1 >= 0 and col -1 >=0 and connected[row-1,col-1] == 255:
        count += 1
    if row - 1 >= 0  and connected[row-1,col] == 255:
        count += 1
    if row - 1 >= 0 and col +1 < colLength and connected[row-1,col+1] == 255:
        count += 1
    if col -1 >=0 and connected[row,col-1] == 255:
        count += 1
    if col +1 < colLength and connected[row,col+1] == 255:
        count += 1
    if row + 1 < rowLength and col -1 >=0 and connected[row+1,col-1] == 255:
        count += 1
    if row + 1 < rowLength and connected[row+1,col] == 255:
        count += 1
    if row + 1 < rowLength and col +1 < colLength and connected[row+1,col+1] == 255:
        count += 1
    return count

#Removes lone pixels, and picks starting point from spot that has the highest number of nearby pixels
for i in range(0, colLength):
    for j in range(0, rowLength):
        if drawArray[j, i] == 255:
            check = countIntersect(drawArray,j,i)
            if check < 1:
                drawArray[j,i] = 0
            else:
                count += 1
                if j-1 >= 0 and i-1 >= 0 and j+1 < rowLength and i+1 < colLength:
                    #Checks a  3X3 square around the pixel
                    if check > maxVal:
                        maxVal = check
                        maxRow = j
                        maxCol = i

edges = np.zeros((rowLength,colLength), np.float32) #Used to keep track of spots already drawn (has to be cleared for this to work

##Could probably be improved
#This algorithm recursively draws and removes points connected to it, this only works if a shape doesn't contain 25X25 pixels
def RemovePoint(row, col):
    global count
    if drawArray[row, col] != 0:
        drawArray[row, col] = 0
        edges[row,col] = 255
        count -= 1  #Used to keep track of pixels left to draw
    if row-1 >= 0 and col-1 >= 0 and drawArray[row-1, col-1] == 255:
        upLeft(step,speed)
        RemovePoint(row - 1, col - 1)
        downRight(step,speed)
    if row+1 < rowLength and col+1 < colLength and drawArray[row+1, col+1] == 255:
        downRight(step,speed)
        RemovePoint(row + 1, col + 1)
        upLeft(step,speed)
    if row-1 >= 0 and drawArray[row-1, col] == 255:
        up(step,speed)
        RemovePoint(row - 1, col)
        down(step,speed)
    if col-1 >= 0 and drawArray[row, col-1] == 255:
        left(step,speed)
        RemovePoint(row, col - 1)
        right(step,speed)
    if row+1 < rowLength and col-1 >= 0 and drawArray[row+1, col-1] == 255:
        downLeft(step,speed)
        RemovePoint(row + 1, col - 1)
        upRight(step,speed)
    if row-1 >= 0 and col+1 < colLength and drawArray[row-1, col+1] == 255:
        upRight(step,speed)
        RemovePoint(row - 1, col + 1)
        downLeft(step,speed)
    if col+1 < colLength and drawArray[row, col+1] == 255:
        right(step,speed)
        RemovePoint(row, col + 1)
        left(step,speed)
    if row+1 < rowLength and drawArray[row+1, col] == 255:
        down(step,speed)
        RemovePoint(row + 1, col)
        up(step,speed)
    point = [row, col]
    #plt.imshow(edges, cmap='gray')
    #plt.show()
    return point



#This algorithm attempts to move to a closer point on the same shape
'''
def moveToClosestPoint(row,col,finalRow,finalCol):
    global edges
    count = 0
    for i in range(0,2):
        if abs(finalRow-row) < abs(finalCol-col):
            if finalRow-row > 0:    #Point is down
                while count < 10:
                    if row+1 < rowLength and edges[row+1,col] == 255:
                        down(step,speed)
                        row = row+1
                        count = 0
                    elif row+1 < rowLength and col-1 >= 0 and edges[row+1,col-1] == 255:
                        downLeft(step,speed)
                        row = row+1
                        col = col-1
                        count = 0
                    elif row+1 < rowLength and col+1 < colLength and edges[row+1,col+1] == 255:
                        downRight(step,speed)
                        row = row+1
                        col = col+1
                        count = 0
                    elif col-1 >= 0 and edges[row,col-1] == 255:
                        left(step,speed)
                        col = col-1
                        count += 1
                    else:
                        count += 1
            else:
                while count < 10: #Point is up
                    if row-1 >= 0 and edges[row-1,col] == 255:
                        up(step,speed)
                        row = row-1
                        count = 0
                    elif row-1 >= 0 and col-1 >= 0 and edges[row-1,col-1] == 255:
                        upLeft(step,speed)
                        row = row-1
                        col = col-1
                        count = 0
                    elif row-1 >= 0 and col+1 < colLength and edges[row-1,col+1] == 255:
                        upRight(step,speed)
                        row = row-1
                        col = col+1
                        count = 0
                    elif col-1 >= 0 and edges[row,col-1] == 255:
                        left(step,speed)
                        col = col-1
                        count += 1
                    else:
                        count += 1
        else:
            if finalCol-col > 0:    #Point is right
                while count < 10:
                    if col+1 < colLength and edges[row,col+1] == 255:
                        right(step,speed)
                        col = col+1
                        count = 0
                    elif col+1 < colLength and row+1 < rowLength and edges[row+1,col+1] == 255:
                        downRight(step,speed)
                        row = row-1
                        col = col+1
                        count = 0
                    elif col+1 < colLength and row-1 >= 0 and edges[row-1,col+1] == 255:
                        upRight(step,speed)
                        row = row-1
                        col = col+1
                        count = 0
                    elif row-1 >= 0 and edges[row-1,col] == 255:
                        up(step,speed)
                        row = row-1
                        count += 1
                    else:
                        count += 1
            else:
                while count < 10:   #Point is left
                    if col-1 >= 0 and edges[row,col-1] == 255:
                        left(step,speed)
                        col = col-1
                        count = 0
                    elif col-1 >= 0 and row+1 < rowLength and edges[row+1,col-1] == 255:
                        downLeft(step,speed)
                        row = row+1
                        col = col-1
                        count = 0
                    elif col-1>= 0 and row-1 >= 0 and edges[row-1,col-1] == 255:
                        upLeft(step,speed)
                        row = row-1
                        col = col-1
                        count = 0
                    elif row-1 >= 0 and edges[row-1,col] == 255:
                        up(step,speed)
                        row = row-1
                        count += 1
                    else:
                        count += 1
'''

#This algorithm finds closest remaining point to current point, and moves towards that point
def ConnectPoints(row, col):
    pointRow = row
    pointCol = col
    val = 2
    global edges
    global quickRow
    global count
    #Finds a point that is either directly above, below, left, right, upLeft, upRight, downRight, or downLeft
    while val < rowLength and val < colLength:
        if row-val >= 0 and drawArray[row-val,col] == 255:
            pointRow = row-val
            for i in range(0, val+1):
                up(step,speed)
                edges[row-i,col] = 255
            break
        elif col-val >= 0 and drawArray[row,col-val] == 255:
            pointCol = col-val
            for i in range(0, val+1):
                left(step,speed)
                edges[row,col-i] = 255
            break
        elif col+val < colLength and drawArray[row,col+val] == 255:
            pointCol = col+val
            for i in range(0, val+1):
                right(step,speed)
                edges[row,col+i] = 255
            break
        elif row+val < rowLength and drawArray[row+val,col] == 255:
            pointRow = row+val
            for i in range(0, val+1):
                down(step,speed)
                edges[row+i,col] = 255
            break
        elif col-val >= 0 and row-val >= 0 and drawArray[row-val,col-val] == 255:
            pointCol = col-val
            pointRow = row-val
            for i in range(0, val+1):
                upLeft(step,speed)
                edges[row-i,col-i] = 255
            break
        elif col+val < colLength and row-val >= 0 and drawArray[row-val,col+val] == 255:
            pointCol = col+val
            pointRow = row-val
            for i in range(0, val+1):
                upRight(step,speed)
                edges[row-i,col+i] = 255
            break
        elif row+val < rowLength and col-val >= 0 and drawArray[row+val,col-val] == 255:
            pointCol = col-val
            pointRow = row+val
            for i in range(0, val+1):
                downLeft(step,speed)
                edges[row+i,col-i] = 255
            break
        elif row+val < rowLength and col+val < colLength and drawArray[row+val, col+val] == 255:
            pointCol = col+val
            pointRow = row+val
            for i in range(0, val+1):
                downRight(step,speed)
                edges[row+i,col+i] = 255
            break
        else:
            val += 1
    #This probably can be coded better to reduce lines
    if val >= rowLength or val >= colLength:
        for i in range(quickRow, rowLength):
            for j in range(0, colLength):
                if drawArray[i,j] == 255:
                    pointRow = i
                    pointCol = j
                    quickRow = i
                    point = [pointRow, pointCol]

                    if i > row:
                        for k in range(0, i-row):
                            down(step,speed)
                            edges[row+k,col] = 255
                    else:
                        for k in range(0, row-i):
                            up(step,speed)
                            edges[row-k,col] = 255
                    if j > col:
                        for k in range(0, j-col):
                            right(step,speed)
                            edges[row,col+k] = 255
                    else:
                        for k in range(0, col-j):
                            left(step,speed)
                            edges[row,col-k] = 255

                    #plt.imshow(edges, cmap='gray')
                    #()
                    return point
    # Moves to border if low number of points, doesn't work well yet
    '''
    if count <= -1:
        if rowLength-row < colLength-col and rowLength - row < row and rowLength-row < col:
            for k in range(0, rowLength-row):
                down(step,speed)
                edges[row+k,col] = 255
            for k in range(0, col):
                left(step,speed)
                edges[row, col-k] = 255
            for k in range(0, rowLength):
                up(step,speed)
                edges[rowLength-k-1,0] = 255
        elif colLength - col < rowLength - row and colLength-col < col and colLength-col < row:
            for k in range(0, colLength - col):
                right(step,speed)
                edges[row,col+k] = 255
            for k in range(0, row):
                up(step,speed)
                edges[row-k,colLength-1] = 255
            for k in range(0, colLength):
                left(step,speed)
                edges[0, colLength-k-1] = 255
        elif row < col:
            for k in range(0, row):
                up(step,speed)
                edges[row-k,col] = 255
            for k in range(0, col):
                left(step,speed)
                edges[row, col-k] = 255
        else:
            for k in range(0, col):
                left(step,speed)
                edges[row,col-k] = 255
            for k in range(0, row):
                up(step,speed)
                edges[row-k,0] = 255
        for i in range(quickRow, rowLength):
            for j in range(0, colLength):
                if drawArray[i,j] == 255:
                    pointRow = i
                    pointCol = j
                    quickRow = i
                    point = [pointRow, pointCol]
                    if rowLength - i < colLength-j and rowLength-i < i and rowLength-i < j:
                        for k in range(0, rowLength):
                            down(step,speed)
                            edges[k,0] = 255
                        for k in range(0,j):
                            right(step,speed)
                            edges[rowLength-1,k] = 255
                        for k in range(0,rowLength-i):
                            up(step,speed)
                            edges[rowLength-k-1,j] = 255
                    elif colLength - j < rowLength - i and colLength - j < j and colLength - j < i:
                        for k in range(0, colLength):
                            right(step,speed)
                            edges[0,k] = 255
                        for k in range(0, i):
                            down(step,speed)
                            edges[k,colLength-1] = 255
                        for k in range(0,colLength-j):
                            left(step,speed)
                            edges[i,colLength-k-1] = 255
                    elif i < j:
                        for k in range(0, j):
                            right(step,speed)
                            edges[0,k] = 255
                        for k in range (0, i):
                            down(step,speed)
                            edges[k,j] = 255
                    else:
                        for k in range (0, i):
                            down(step,speed)
                            edges[k,0] = 255
                        for k in range(0, j):
                            right(step,speed)
                            edges[i,k] = 255
                    return point
    '''
    #plt.imshow(edges, cmap='gray')
    #()
    point = [pointRow, pointCol]
    return point


def ConnectPoints2(row, col):
    dist = rowLength*colLength
    pointRow = row
    pointCol = col
    for i in range(0, rowLength):
        for j in range(0, colLength):
            if drawArray[i,j] == 255:
                newDist = np.sqrt(abs(i-row)^2+abs(j-col)^2)
                if dist > newDist:
                    dist = newDist
                    pointRow = i
                    pointCol = j

    if i > row:
        for k in range(0, i-row):
            down(step,speed)
            edges[row+k,col] = 255
    else:
        for k in range(0, row-i):
            up(step,speed)
            edges[row-k,col] = 255
    if j > col:
        for k in range(0, j-col):
            right(step,speed)
            edges[row,col+k] = 255
    else:
        for k in range(0, col-j):
            left(step,speed)
            edges[row,col-k] = 255

    point = [pointRow,pointCol]
    return point





point = RemovePoint(maxRow, maxCol)


while count > 1:
    newPoint = ConnectPoints(point[0], point[1])
    point = RemovePoint(newPoint[0], newPoint[1])
plt.imshow(edges, cmap='gray')
plt.show()
count2 = 1
print len(string)
while len(string) > 50:
    if count2 > 58:
        ser.close()
        time.sleep(2);
        ser.open()
        time.sleep(2)
        ser.write('9\r\n')
        count2 = 0
    ser.write(string[0:50]+'\r\n')
    string = string[50:]
    print string
    time.sleep(3.8) #3.8 #12.7
    print count2
    count2 += 1
if len(string) > 0:
    ser.write(string + '\r\n')
    print count2
    count2 += 1
ser.close()
print string
print count
print maxVal
print maxRow
print maxCol
plt.imshow(edges, cmap='gray')

#plt.subplot(121), plt.imshow(drawArray, cmap='gray')







