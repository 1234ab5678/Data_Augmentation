import random

import cv2
import os
from PIL import Image, ImageEnhance
import numpy as np


# 遮挡
def paste(im,i,j,x):
    imgg = Image.open(im)
    # 生成一张白色图片
    img = Image.new('RGB', (imgg.size[0], imgg.size[1]), (0, 0, 0))

    #i = random.randint(0, 180)
    #j = random.randint(0, 180)

    # img2 = img.crop((0,0,80,180))  #裁剪原图中一部分作为覆盖图片 # 80 80 两个参数可以设置为裁剪大小
    img2 = img.crop((0, 0, i, j))  # 裁剪原图中一部分作为覆盖图片 # 80 80 两个参数可以设置为裁剪大小
    #print(imgg)

    #x = random.randint(0, 200)
    #print(x)
    imgg.paste(img2, (x, x, x + img2.size[0], x + img2.size[1]))  # 第二个参数是覆盖位置
    return imgg



if __name__ == '__main__':
    img_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/imgs/'  # 图片文件夹路径
    label_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/labels/'  # xml标注文件夹路径
    img_write_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/imgs5/'  # 翻转后的图片保存路径
    label_write_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/labels5/'  # 修改后的xml标注保存路径
    if not os.path.exists(img_write_path):
        os.makedirs(img_write_path)
    if not os.path.exists(label_write_path):
        os.makedirs(label_write_path)


    for filename in os.listdir(img_path):
        i = random.randint(50, 200)
        j = random.randint(50, 200)
        x = random.randint(0, 400)
        #x = np.random.randint(-320, 320)
        #y = np.random.randint(-320, 320)
        #path=img_path+'/'+filename
        img=paste(img_path+'/'+filename,i,j,x)
        #print(type(img))
        img.save(img_write_path+'/'+filename.split('.')[0]+'zd.jpg')

        #labelpath=label_path+'/'+filename.split('.')[0]+'.png'
        label = paste(label_path+'/'+filename.split('.')[0]+'.png',i,j,x)
        #label=Image.open(os.path.join(label_path, filename.split('.')[0]+'.png'))
        label.save(label_write_path + '/' + filename.split('.')[0] + 'zd.png')
        label = cv2.imread(label_write_path + '/' + filename.split('.')[0] + 'zd.png', 0)
        cv2.imwrite(label_write_path + '/' + filename.split('.')[0] + 'zd.png', label)
        #cv2.imwrite(img_write_path+filename.split('.')[0]+'.png',img)