import time
import dlib
import cv2
# Đọc ảnh đầu vào
image = cv2.imread('/Users/DEVN/Downloads/okie.jpg')

# Khai bao su dung ham detect cua dlib
face_detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Detect cac khuon mat trong anh
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_detect.detectMultiScale(gray, 1.3, 5)

# Ve hinh chu nhat quanh mat nhan duoc
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("OK", image)
cv2.waitKey(0)
