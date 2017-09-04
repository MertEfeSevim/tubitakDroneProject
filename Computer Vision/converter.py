import cv2
import numpy as np

green = np.uint8([[[255,255,255 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2RGB)
print(hsv_green)