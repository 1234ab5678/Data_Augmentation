import os
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np

def random_crop(image,min_ratio,max_ratio):
    #min_ratio = 0.4
    #max_ratio = 0.7
    #scale=0
    w, h = image.size
    ratio = 0.5
    #print(ratio)
    scale = min_ratio + ratio * (max_ratio - min_ratio)
    new_h = int(h * scale)
    new_w = int(w * scale)
    y = np.random.randint(0, h - new_h)
    x = np.random.randint(0, w - new_w)
    image = image.crop((x, y, x + new_w, y + new_h))
    return image

def data_handle(image_path,save_path,min,max):
    image = Image.open(image_path)
    if image.mode is not 'RGB':
        image=image.convert('RGB')
    res = random_crop(image,min,max)
    res.save(save_path)  # 保存新图
    #return res

#data_handle('D:\PycharmProjects\Classification1\datasets/1.jpg','D:\PycharmProjects\Classification1\datasets/10.jpg')
#print((random.random()*10)//0.5)

if __name__ == '__main__':
    img_path = 'F:/MyRearsch/Competition/iflytek/Cerebrovascular/2d-data/VOC2007/train/JPEGImages/'  # 图片文件夹路径
    label_path = 'F:/MyRearsch/Competition/iflytek/Cerebrovascular/2d-data/VOC2007/train/SegmentationClass/'  # xml标注文件夹路径
    img_write_path = 'F:/MyRearsch/Competition/iflytek/Cerebrovascular/2d-data/VOC2007/train/JPEGImages6/'  # 翻转后的图片保存路径
    label_write_path = 'F:/MyRearsch/Competition/iflytek/Cerebrovascular/2d-data/VOC2007/train/SegmentationClass6/'  # 修改后的xml标注保存路径
    if not os.path.exists(img_write_path):
        os.makedirs(img_write_path)
    if not os.path.exists(label_write_path):
        os.makedirs(label_write_path)


    for filename in os.listdir(img_path):
        min = np.random.randint(80, 90)
        max = np.random.randint(90, 100)
        min=min/100
        max=max/100
        #print(x)
        img=data_handle(img_path+'/'+filename,img_write_path+'/crop'+filename,min,max)
        #print(type(img))
        #img.save(img_write_path+'/'+filename.split('.')[0]+'.jpg')

        #labelpath=label_path+'/'+filename.split('.')[0]+'.png'
        #label = contrastEnhancement(label_path,filename.split('.')[0]+'.png')
        #label=Image.open(os.path.join(label_path, filename.split('.')[0]+'.png'))
        label=data_handle(label_path+'/'+filename.split('.')[0]+'.png',label_write_path+'/crop'+filename.split('.')[0]+'.png',min,max)
        label = cv2.imread(label_write_path + '/crop' + filename.split('.')[0] + '.png', 0)
        cv2.imwrite(label_write_path + '/crop' + filename.split('.')[0] + '.png', label)
