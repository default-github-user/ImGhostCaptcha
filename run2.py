import cv2
import numpy as np
from matplotlib import pyplot as plotter
import pyautogui as pag
import time




loc_ = []
print("[!] Locating coordinates of reCaptcha....")

screen_ = pag.screenshot()
screen_.save("screenshot.jpg")

img_rgb_ = cv2.imread("screenshot.jpg")
img_rgb_gray_ = cv2.cvtColor(img_rgb_,cv2.COLOR_BAYER_BG2GRAY)

find_template_ = cv2.imread("find2.jpg",0)
w, h = find_template_.shape[::-1]
