# 打开摄像头并灰度化显示
import os
import cv2

# 播放本地视频

# 使用相对路径加载图片路径
my_path = os.path.abspath(os.path.dirname(__file__))
video_path = os.path.join(my_path, "../03-Open-Camera/demo_video.mp4")

capture = cv2.VideoCapture(video_path)

while(capture.isOpened()):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(30) == ord('q'):
        break
