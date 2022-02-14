import os
import  cv2
import numpy as np

file_path = os.path.abspath(os.path.dirname(__file__))
img = os.path.join(file_path, "./images/img2.png")


img1 = cv2.imread(img)
start_time = cv2.getTickCount()
print(start_time)
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)

end_time = cv2.getTickCount()
print(end_time)
t = (end_time - start_time)/cv2.getTickFrequency()
print(t)
