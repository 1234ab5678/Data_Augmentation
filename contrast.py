import cv2
import os
from PIL import Image, ImageEnhance
import numpy as np

def contrastEnhancement(root_path, img_name, contrast):  # 对比度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_con = ImageEnhance.Contrast(image)
    #contrast = contrast
    image_contrasted = enh_con.enhance(contrast)
    return image_contrasted


if __name__ == '__main__':
    img_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/imgs/'  # 图片文件夹路径
    label_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/labels/'  # xml标注文件夹路径
    img_write_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/imgs6/'  # 翻转后的图片保存路径
    label_write_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/labels6/'  # 修改后的xml标注保存路径
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
        img=contrastEnhancement(img_path,filename,x)
        #print(type(img))
        img.save(img_write_path+'/'+filename.split('.')[0]+'contrast.jpg')

        #labelpath=label_path+'/'+filename.split('.')[0]+'.png'
        #label = contrastEnhancement(label_path,filename.split('.')[0]+'.png')
        label=Image.open(os.path.join(label_path, filename.split('.')[0]+'.png'))
        label.save(label_write_path + '/' + filename.split('.')[0] + 'contrast.png')
        label = cv2.imread(label_write_path + '/' + filename.split('.')[0] + 'contrast.png', 0)
        cv2.imwrite(label_write_path + '/' + filename.split('.')[0] + 'contrast.png', label)
        #cv2.imwrite(img_write_path+filename.split('.')[0]+'.png',img)