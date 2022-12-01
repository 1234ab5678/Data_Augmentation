import random

import cv2
import os
from PIL import Image, ImageEnhance
import numpy as np


# 图像的缩放
from numpy.random import rand

def scale(image, ih, iw):
   #ih, iw    = target_size
   s = image.shape
   h=s[0]
   w=s[1]

   scale = min(iw/w, ih/h)
   nw, nh  = int(scale * w), int(scale * h)
   image_resized = cv2.resize(image, (nw, nh))

   image_paded = np.full(shape=[ih, iw, 3], fill_value=0, dtype=np.uint8)
   dw, dh = (iw - nw) // 2, (ih-nh) // 2
   image_paded[dh:nh+dh, dw:nw+dw, :] = image_resized
   # image_paded = image_paded / 255.
   return image_paded

def scale2(image, ih, iw):
   #ih, iw    = target_size
   h,  w, _  = image.shape

   scale = min(iw/w, ih/h)
   nw, nh  = int(scale * w), int(scale * h)
   image_resized = cv2.resize(image, (iw, ih))

   #image_paded = np.full(shape=[ih, iw, 3], fill_value=0, dtype=np.uint8)
   #dw, dh = (iw - nw) // 2, (ih-nh) // 2
   #image_paded[dh:nh+dh, dw:nw+dw, :] = image_resized
   # image_paded = image_paded / 255.
   return image_resized

if __name__ == '__main__':
    img_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/imgs/'  # 图片文件夹路径
    label_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/labels/'  # xml标注文件夹路径
    img_write_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/imgs9/'  # 翻转后的图片保存路径
    label_write_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/labels9/'  # 修改后的xml标注保存路径
    if not os.path.exists(img_write_path):
        os.makedirs(img_write_path)
    if not os.path.exists(label_write_path):
        os.makedirs(label_write_path)


    for filename in os.listdir(img_path):
        i = random.randint(50,200)
        j = random.randint(50, 200)
        #i=100
        #j=100
        i=int((i/100)*448)
        j=int((j/100)*448)
        #x = np.random.randint(-320, 320)
        #y = np.random.randint(-320, 320)
        path=img_path+'/'+filename
        #image=Image.open(path)
        image=cv2.imread(path)
        img=scale(image,i,j)
        #print(type(img))
        cv2.imwrite(img_write_path+'/'+filename.split('.')[0]+'fs.jpg',img)

        labelpath=label_path+'/'+filename.split('.')[0]+'.png'
        label=cv2.imread(labelpath)
        label = scale(label,i,j)
        #label=Image.open(os.path.join(label_path, filename.split('.')[0]+'.png'))
        #label.save(label_write_path + '/' + filename.split('.')[0] + '.png')
        cv2.imwrite(label_write_path+'/'+filename.split('.')[0]+'fs.png',label)
        label = cv2.imread(label_write_path + '/' + filename.split('.')[0] + 'fs.png', 0)
        cv2.imwrite(label_write_path + '/' + filename.split('.')[0] + 'fs.png', label)