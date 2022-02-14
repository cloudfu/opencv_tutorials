# 打开摄像头并灰度化显示
import cv2

capture = cv2.VideoCapture(0)

# 有时，cap可能尚未初始化捕获。在这种情况下，此代码显示错误。
# 你可以通过**cap.isOpened**()方法检查它是否已初始化。
# 如果是True，那么确定。否则，使用**cap.open**()打开它。
if not capture.isOpened():
    print("Cannot open camera")
    exit()

# 获取捕获的分辨率
# propId可以直接写数字，也可以用OpenCV的符号表示
width, height = capture.get(3), capture.get(4)
print(width, height)

# 以原分辨率的一倍来捕获
capture.set(cv2.CAP_PROP_FRAME_WIDTH, width * 2)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height * 2)

while(True):
    # 获取一帧
    # capture.read()函数返回的
    # 第1个参数ret(return value缩写)是一个布尔值，表示当前这一帧是否获取正确。
    ret, frame = capture.read()

    if ret:

        # 0：上下翻转
        # 1：左右翻转
        frame = cv2.flip(frame, 1)

        # 将这帧转换为灰度图
        # cv2.cvtColor()用来转换颜色，这里将彩色图转成灰度图。
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
