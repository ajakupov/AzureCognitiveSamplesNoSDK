import cv2
import numpy as np

import cv2
import numpy as np

def convert_to_sketch(image_path):
    img_rgb = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_gray_inv = 255 - img_gray
    img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(19, 19), sigmaX=0, sigmaY=0)

    img_blend = dodgeV2(img_gray, img_blur)
    cv2.imwrite('sketch.jpg', img_blend)

    sketch = cv2.imread('sketch.jpg')
    sketch[np.where((sketch != [255, 255, 255]).all(axis=2))] = [255, 255, 0]
    sketch[np.where((sketch == [255, 255, 255]).all(axis=2))] = [255, 0, 0]

    cv2.imshow('temp', img_blend)
    # key controller
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def dodgeV2(image, mask):
    return cv2.divide(image, 255-mask, scale=256)


def burnV2(image, mask):
    return 255 - cv2.divide(255-image, 255-mask, scale=256)


def draw_countours(image_path):
    # load image
    img = cv2.imread(image_path)

    lower = (80, 70, 30)
    upper = (220, 220, 180)

    # create the mask and use it to change the colors
    thresh = cv2.inRange(img, lower, upper)

    # apply morphology
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # invert
    morph = 255 - morph

    # find largest contour
    contours = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    big_contour = max(contours, key=cv2.contourArea)

    # draw white filled contour on black background as mask
    mask = np.zeros_like(thresh)
    cv2.drawContours(mask, [big_contour], 0, 255, -1)

    # apply mask to img
    result = img.copy()
    result[mask == 0] = (0, 0, 0)

    # write result to disk
    cv2.imwrite("beans_thresh2.png", thresh)
    cv2.imwrite("beans_morph2.png", morph)
    cv2.imwrite("beans_mask2.png", mask)
    cv2.imwrite("beans_result2.png", result)

    cv2.imwrite('thresh.jpg', thresh)

    # display it
    cv2.imshow("thresh", thresh)
    cv2.imshow("morph", morph)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
