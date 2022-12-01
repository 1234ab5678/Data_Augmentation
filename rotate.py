#!/usr/bin/env python
import random
import cv2
import math
import numpy as np
import os
import pdb
import xml.etree.ElementTree as ET


class ImgAugemention():
    def __init__(self):
        self.angle = 90


    # rotate_img
    def rotate_image(self, src, angle, scale=1.):
        w = src.shape[1]
        h = src.shape[0]
        # convet angle into rad
        rangle = np.deg2rad(angle)  # angle in radians
        # calculate new image width and height
        nw = (abs(np.sin(rangle)*h) + abs(np.cos(rangle)*w))*scale
        nh = (abs(np.cos(rangle)*h) + abs(np.sin(rangle)*w))*scale
        # ask OpenCV for the rotation matrix
        rot_mat = cv2.getRotationMatrix2D((nw*0.5, nh*0.5), angle, scale)
        # calculate the move from the old center to the new center combined
        # with the rotation
        rot_move = np.dot(rot_mat, np.array([(nw-w)*0.5, (nh-h)*0.5, 0]))
        # the move only affects the translation, so update the translation
        # part of the transform
        rot_mat[0, 2] += rot_move[0]
        rot_mat[1, 2] += rot_move[1]
        # map
        return cv2.warpAffine(
            src, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))),
            flags=cv2.INTER_LANCZOS4)

    def process_img(self, imgs_path, labels_path, img_save_path, label_save_path, angle_list):
        # assign the rot angles

        for img_name in os.listdir(imgs_path):
            # split filename and suffix
            n, s = os.path.splitext(img_name)
            # for the sake of use yolo model, only process '.jpg'
            if s == ".jpg":
                img_path = os.path.join(imgs_path, img_name)
                img = cv2.imread(img_path)
                length = len(angle_list)
                index = random.randint(1, length)
                # for angle in angle_list:
                angle = angle_list[index - 1]
                rotated_img = self.rotate_image(img, angle)
                save_name = n + "_" + str(angle) + "d.jpg"
                # 写入图像
                cv2.imwrite(img_save_path + save_name, rotated_img)

                img = cv2.imread(img_save_path + save_name)
                size = img.shape
                img=img[int(size[0]/2)-320:int(size[0]/2)+320,int(size[1]/2)-320:int(size[1]/2)+320,:]
                cv2.imwrite(img_save_path + save_name, img)

                label_path = os.path.join(labels_path, img_name.split('.')[0]+'.png')
                label = cv2.imread(label_path,0)
                rotated_label = self.rotate_image(label, angle)
                save_name = n + "_" + str(angle) + "d.png"
                # 写入图像
                cv2.imwrite(label_save_path + save_name, rotated_label)

                label = cv2.imread(label_save_path + save_name,0)
                size = label.shape
                label = label[int(size[0] / 2) - 224:int(size[0] / 2) + 224, int(size[1] / 2) - 224:int(size[1] / 2) + 224]
                cv2.imwrite(label_save_path + save_name, label)

            print("[%s] %s is processed." % (angle, img_name))


if __name__ == '__main__':
    img_aug = ImgAugemention()
    img_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/imgs/'  # 图片文件夹路径
    label_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/labels/'  # xml标注文件夹路径
    img_write_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/imgs3/'  # 翻转后的图片保存路径
    label_write_path = 'F:/MyRearsch/Dataset/Project-Dataset/Crack-Dataset/Tensorflow-Dataset/Medical/labels3/'  # 修改后的xml标注保存路径
    if not os.path.exists(img_write_path):
        os.makedirs(img_write_path)
    if not os.path.exists(label_write_path):
        os.makedirs(label_write_path)
    #angle_list = [90,270]
    angle_list=[]
    for i in range(360):
        angle_list.append(i)
    angle_list=np.array(angle_list)
    img_aug.process_img(img_path, label_path, img_write_path, label_write_path, angle_list)
