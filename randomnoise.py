import cv2
import os
from PIL import Image, ImageEnhance
import numpy as np

#----随机噪声----
def random_noise(image,noise_num):
    '''
    添加随机噪点（实际上就是随机在图像上将像素点的灰度值变为255即白色）
    :param image: 需要加噪的图片
    :param noise_num: 添加的噪音点数目，一般是上千级别的
    :return: img_noise
    '''
    #
    # 参数image：，noise_num：
    img = cv2.imread(image)
    img_noise = img
    # cv2.imshow("src", img)
    #img = cv2.imread(path)
    rows, cols, chn = img_noise.shape[:3]
    # 加噪声
    for i in range(noise_num):
        x = np.random.randint(0, rows)#随机生成指定范围的整数
        y = np.random.randint(0, cols)
        img_noise[x, y, :] = 255
    return img_noise


if __name__ == '__main__':
    img_path = 'D:/ycl/Ordinary-Image/Dataset/Project-Dataset/Crack-Dataset/Medical/Crack-Augmentation/VOC2007/train/JPEGImages'  # 图片文件夹路径
    label_path = 'D:/ycl/Ordinary-Image/Dataset/Project-Dataset/Crack-Dataset/Medical/Crack-Augmentation/VOC2007/train/SegmentationClass'  # xml标注文件夹路径
    img_write_path = 'D:/ycl/Ordinary-Image/Dataset/Project-Dataset/Crack-Dataset/Medical/Crack-Augmentation/VOC2007/train/JPEGImages-randomnoise'  # 翻转后的图片保存路径
    label_write_path = 'D:/ycl/Ordinary-Image/Dataset/Project-Dataset/Crack-Dataset/Medical/Crack-Augmentation/VOC2007/train/SegmentationClass-randomnoise'  # 修改后的xml标注保存路径
    if not os.path.exists(img_write_path):
        os.makedirs(img_write_path)
    if not os.path.exists(label_write_path):
        os.makedirs(label_write_path)


    for filename in os.listdir(img_path):
        x = np.random.randint(0, 20)
        x = int((x / 100)*640*640)
        print(x)
        #x = np.random.randint(-320, 320)
        #y = np.random.randint(-320, 320)
        path=img_path+'/'+filename
        img=random_noise(path,x)
        #print(type(img))
        #img.save(img_write_path+'/'+filename.split('.')[0]+'.jpg')
        cv2.imwrite(img_write_path+'/'+filename.split('.')[0]+'.jpg',img)
        #labelpath=label_path+'/'+filename.split('.')[0]+'.png'
        #label = contrastEnhancement(label_path,filename.split('.')[0]+'.png')
        label=Image.open(os.path.join(label_path, filename.split('.')[0]+'.png'))
        label.save(label_write_path + '/' + filename.split('.')[0] + '.png')
        #cv2.imwrite(img_write_path+filename.split('.')[0]+'.png',img)