import random

import cv2
import os
from PIL import Image, ImageEnhance
import numpy as np


# 通过在 hsv 色彩空间中，对 h、s、v三个通道增加扰动，来进行色调增强变换
def augment_hsv(imageDir, image_name, hgain=0.2, sgain=0.7, vgain=0.4):
    """
    HSV color-space augmentation
    :param image:       待增强的图片
    :param hgain:       HSV 中的 h 扰动系数，yolov5：0.015
    :param sgain:       HSV 中的 s 扰动系数，yolov5：0.7
    :param vgain:       HSV 中的 v 扰动系数，yolov5：0.4
    :return:
    """
    #image = Image.open(os.path.join(imageDir, image_name))
    image=cv2.imread(os.path.join(imageDir, image_name))
    if hgain or sgain or vgain:
        # 随机取-1到1三个实数，乘以 hsv 三通道扰动系数
        # r:[1-gain,1+gain]
        r = np.random.uniform(-1, 1, 3) * [hgain, sgain, vgain] + 1  # random gains
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # cv2.split：通道拆分
        # h:[0~180], s:[0~255], v:[0~255]
        hue, sat, val = cv2.split(image_hsv)
        dtype = image.dtype  # uint8

        x = np.arange(0, 256, dtype=r.dtype)
        lut_hue = ((x * r[0]) % 180).astype(dtype)
        lut_sat = np.clip(x * r[1], 0, 255).astype(dtype)
        lut_val = np.clip(x * r[2], 0, 255).astype(dtype)

        # cv2.LUT：dst(I) = lut(src(I) + d)，d为常数0 / 128
        hue = cv2.LUT(hue, lut_hue)
        sat = cv2.LUT(sat, lut_sat)
        val = cv2.LUT(val, lut_val)

        # 通道合并
        image_hsv = cv2.merge((hue, sat, val)).astype(dtype)

        # 将hsv格式转为RGB格式
        image_dst = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
        #image = Image.formarry(cv2.cvtColor(image_dst, cv2.COLOR_BGR2RGB))
        image = cv2.cvtColor(image_dst, cv2.COLOR_BGR2RGB)
        return image
    else:
        return image

if __name__ == '__main__':
    img_path = 'D:/ycl/Ordinary-Image/Dataset/Project-Dataset/Crack-Dataset/Medical/Crack-Augmentation/VOC2007/train/JPEGImages'  # 图片文件夹路径
    label_path = 'D:/ycl/Ordinary-Image/Dataset/Project-Dataset/Crack-Dataset/Medical/Crack-Augmentation/VOC2007/train/SegmentationClass'  # xml标注文件夹路径
    img_write_path = 'D:/ycl/Ordinary-Image/Dataset/Project-Dataset/Crack-Dataset/Medical/Crack-Augmentation/VOC2007/train/JPEGImages-hsv'  # 翻转后的图片保存路径
    label_write_path = 'D:/ycl/Ordinary-Image/Dataset/Project-Dataset/Crack-Dataset/Medical/Crack-Augmentation/VOC2007/train/SegmentationClass-hsv'  # 修改后的xml标注保存路径
    if not os.path.exists(img_write_path):
        os.makedirs(img_write_path)
    if not os.path.exists(label_write_path):
        os.makedirs(label_write_path)


    for filename in os.listdir(img_path):
        #x = np.random.randint(-320, 320)
        #y = np.random.randint(-320, 320)
        #path=img_path+'/'+filename
        #image=Image.open(path)
        #image=cv2.imread(path)
        img=augment_hsv(img_path,filename)
        #print(type(img))
        cv2.imwrite(img_write_path+'/'+filename.split('.')[0]+'.jpg',img)

        label = Image.open(os.path.join(label_path, filename.split('.')[0] + '.png'))
        label.save(label_write_path + '/' + filename.split('.')[0] + '.png')