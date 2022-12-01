import cv2
import os
import numpy as np
import random
#添加高斯噪声
def gaussian_noise(img,mean,sigma):
    '''
    此函数将产生高斯噪声加到图片上
    :param img:原图
    :param mean:均值
    :param sigma:标准差
    :return:噪声处理后的图片
    '''

    img = img/255  #图片灰度标准化

    noise = np.random.normal(mean, sigma, img.shape) #产生高斯噪声
    # 将噪声和图片叠加
    gaussian_out = img + noise
    # 将超过 1 的置 1，低于 0 的置 0
    gaussian_out = np.clip(gaussian_out, 0, 1)
    # 将图片灰度范围的恢复为 0-255
    gaussian_out = np.uint8(gaussian_out*255)
    # 将噪声范围搞为 0-255
    # noise = np.uint8(noise*255)
    return gaussian_out# 这里也会返回噪声，注意返回值



def convert(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        path = input_dir + "/" + filename # 获取文件路径
        print("doing... ", path)
        noise_img = cv2.imread(path)#读取图片
        img_noise = gaussian_noise(noise_img, 0, 0.12) # 高斯噪声
        # img_noise = sp_noise(noise_img,0.025)# 椒盐噪声
        #img_noise  = random_noise(noise_img,500)# 随机噪声
        cv2.imwrite(output_dir+'/'+filename,img_noise )

if __name__ == '__main__':
    img_path = 'F:/MyRearsch/Competition/iflytek/Cerebrovascular/2d-data/VOC2007/train/JPEGImages/'  # 图片文件夹路径
    label_path = 'F:/MyRearsch/Competition/iflytek/Cerebrovascular/2d-data/VOC2007/train/SegmentationClass/'  # xml标注文件夹路径
    img_write_path = 'F:/MyRearsch/Competition/iflytek/Cerebrovascular/2d-data/VOC2007/train/JPEGImages4/'  # 翻转后的图片保存路径
    label_write_path = 'F:/MyRearsch/Competition/iflytek/Cerebrovascular/2d-data/VOC2007/train/SegmentationClass4/'  # 修改后的xml标注保存路径
    if not os.path.exists(img_write_path):
        os.makedirs(img_write_path)
    if not os.path.exists(label_write_path):
        os.makedirs(label_write_path)
    convert(img_path, img_write_path)
    #convert(label_dir, label_write_dir)