import cv2
import os
import xml.etree.ElementTree as ET
import random

# 水平镜像翻转
def h_MirrorImg(img_path, img_write_path):
    img = cv2.imread(img_path)
    mirror_img = cv2.flip(img, 1)
    cv2.imwrite(img_write_path, mirror_img)

# 垂直翻转
def v_MirrorImg(img_path, img_write_path):
    img = cv2.imread(img_path)
    mirror_img = cv2.flip(img, 0)
    cv2.imwrite(img_write_path, mirror_img)

# 水平垂直翻转
def a_MirrorImg(img_path, img_write_path):
    img = cv2.imread(img_path)
    mirror_img = cv2.flip(img, -1)
    cv2.imwrite(img_write_path, mirror_img)

# 水平镜像翻转
def h_MirrorLabel(img_path, img_write_path):
    img = cv2.imread(img_path,0)
    mirror_img = cv2.flip(img, 1)
    cv2.imwrite(img_write_path, mirror_img)

# 垂直翻转
def v_MirrorLabel(img_path, img_write_path):
    img = cv2.imread(img_path,0)
    mirror_img = cv2.flip(img, 0)
    cv2.imwrite(img_write_path, mirror_img)

# 水平垂直翻转
def a_MirrorLabel(img_path, img_write_path):
    img = cv2.imread(img_path,0)
    mirror_img = cv2.flip(img, -1)
    cv2.imwrite(img_write_path, mirror_img)

def mirror(img_dir, label_dir, img_write_dir, label_write_dir):
    if not os.path.exists(img_write_dir):
        os.makedirs(img_write_dir)
    if not os.path.exists(label_write_dir):
        os.makedirs(label_write_dir)

    img_name = os.listdir(img_dir)
    for img in img_name:
        img_path = os.path.join(img_dir, img)
        label_path = os.path.join(label_dir, img.split('.')[0]+'.png')
        # 注意img[:-4]，如果后缀是jpeg则改成img[:-5]
        h_img_write_path = os.path.join(img_write_dir, img[:-4] + '_hflip' + '.jpg')
        h_label_write_path = os.path.join(label_write_dir, img[:-4] + '_hflip' + '.png')
        #
        v_img_write_path = os.path.join(img_write_dir, img[:-4] + '_vflip' + '.jpg')
        v_label_write_path = os.path.join(label_write_dir, img[:-4] + '_vflip' + '.png')
        #
        a_img_write_path = os.path.join(img_write_dir, img[:-4] + '_aflip' + '.jpg')
        a_label_write_path = os.path.join(label_write_dir, img[:-4] + '_aflip' + '.png')
        #
        index=random.randint(1, 3)
        #print(index)
        if(index==1):
            h_MirrorImg(img_path, h_img_write_path)
            h_MirrorLabel(label_path, h_label_write_path)
        elif(index==2):
            v_MirrorImg(img_path, v_img_write_path)
            v_MirrorLabel(label_path, v_label_write_path)
        elif(index==3):
            a_MirrorImg(img_path, a_img_write_path)
            a_MirrorLabel(label_path, a_label_write_path)


if __name__ == '__main__':
    img_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/imgs/'  # 图片文件夹路径
    label_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/labels/'  # xml标注文件夹路径
    img_write_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/imgs2/'  # 翻转后的图片保存路径
    label_write_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/labels2/'  # 修改后的xml标注保存路径
    mirror(img_path, label_path, img_write_path, label_write_path)
