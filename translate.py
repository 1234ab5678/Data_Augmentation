import cv2
import os
from PIL import Image, ImageChops
import numpy as np

def shift(im,x,y):
    img = Image.open(im)
    img2 = ImageChops.offset(img,x,y)  # 水平位移：200，垂直位移：100
    #img = img.resize((224, 224), resample=Image.LANCZOS)
    return img2

if __name__ == '__main__':
    img_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/imgs/'  # 图片文件夹路径
    label_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/labels/'  # xml标注文件夹路径
    img_write_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/imgs4/'  # 翻转后的图片保存路径
    label_write_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/labels4/'  # 修改后的xml标注保存路径
    if not os.path.exists(img_write_path):
        os.makedirs(img_write_path)
    if not os.path.exists(label_write_path):
        os.makedirs(label_write_path)
    S = 224
    for filename in os.listdir(img_path):
        x = np.random.randint(-S, S)
        y = np.random.randint(-S, S)
        path=img_path+'/'+filename
        img=shift(path,x,y)
        #print(type(img))
        img.save(img_write_path+'/'+filename.split('.')[0]+'translate.jpg')

        labelpath=label_path+'/'+filename.split('.')[0]+'.png'
        label = shift(labelpath, x, y)
        label.save(label_write_path + '/' + filename.split('.')[0] + 'translate.png')
        label=cv2.imread(label_write_path + '/' + filename.split('.')[0] + 'translate.png',0)
        cv2.imwrite(label_write_path + '/' + filename.split('.')[0] + 'translate.png',label)
        #cv2.imwrite(img_write_path+filename.split('.')[0]+'.png',img)