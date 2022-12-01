import random

import cv2
import os
from PIL import Image, ImageEnhance
import numpy as np


def colorEnhancement(root_path,img_name,color):#颜色增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_col = ImageEnhance.Color(image)
    #color = 1.5
    image_colored = enh_col.enhance(color)
    return image_colored



if __name__ == '__main__':
    img_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/imgs/'  # 图片文件夹路径
    label_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/labels/'  # xml标注文件夹路径
    img_write_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/imgs7/'  # 翻转后的图片保存路径
    label_write_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/labels7/'  # 修改后的xml标注保存路径
    if not os.path.exists(img_write_path):
        os.makedirs(img_write_path)
    if not os.path.exists(label_write_path):
        os.makedirs(label_write_path)


    for filename in os.listdir(img_path):
        x = np.random.randint(50, 250)
        x = x / 100
        print(x)
        #x = np.random.randint(-320, 320)
        #y = np.random.randint(-320, 320)
        #path=img_path+'/'+filename
        img=colorEnhancement(img_path,filename,x)
        #print(type(img))
        img.save(img_write_path+'/'+filename.split('.')[0]+'color.jpg')

        #labelpath=label_path+'/'+filename.split('.')[0]+'.png'
        #label = colorEnhancement(label_path,filename.split('.')[0]+'.png',x)
        label=Image.open(os.path.join(label_path, filename.split('.')[0]+'.png'))
        label.save(label_write_path + '/' + filename.split('.')[0] + 'color.png')
        label = cv2.imread(label_write_path + '/' + filename.split('.')[0] + 'color.png', 0)
        cv2.imwrite(label_write_path + '/' + filename.split('.')[0] + 'color.png', label)
        #cv2.imwrite(img_write_path+filename.split('.')[0]+'.png',img)