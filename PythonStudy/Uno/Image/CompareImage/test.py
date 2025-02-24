import cv2
import os
import numpy as np

image_path = 'D:/공부/블로그/JS.png'
with open(image_path, 'rb') as file:
    image = np.frombuffer(file.read(), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

if image is None:
    print("이미지를 불러올 수 없습니다. 경로를 확인해 주세요.")
else:
    cv2.imshow('test', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
