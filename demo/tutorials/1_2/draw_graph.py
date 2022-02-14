import cv2
import numpy as np



def draw_line(img,start_point,end_point,color,thickness):
    """
    绘制连线
    """
    cv2.line(img,start_point,end_point,color,thickness)


def draw_rectangle(img,start_point,end_point,color,thickness):
    cv2.rectangle(img,start_point,end_point,color,thickness)


def draw_circle(img,center_point,radius,color,fill):
    """
    fill:-1为填充
    """
    cv2.circle(img,center_point, radius, color, fill)

def draw_polylines(img,points,closed,color,thickness):
    """
    closed:是否闭合
    """
    cv2.polylines(img,[points],closed,color,thickness)

def draw_text(img,text,points,font_size,color,thickness):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'OpenCV',(10,500), font, font_size,color,thickness,cv2.LINE_AA)

# 创建黑色的图像
img = np.zeros((512,512,3), np.uint8)

# 绘制连线
draw_line(img,(0,0),(511,511),(255,0,0),5)
# 绘制矩形
draw_rectangle(img,(384,0),(510,128),(0,255,0),3)
# 绘制圆形
draw_circle(img,(447,63), 63, (0,0,255),-1)
# 画多边形
points = np.array([[10,5],[20,30],[70,20],[50,10]])
draw_polylines(img,points,False,(0,255,255),2)
# 绘制文字
draw_text(img,'OpenCV',(10,500),  1,(255,0,255),2)



cv2.imshow("demo",img)
cv2.waitKey(0)

