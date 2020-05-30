import os
import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
from PIL import Image

mp = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'a':10,
    'b':11,
    'c':12,
    'd':13,
    'e':14,
    'f':15,
    'g':16,
    'h':17,
    'i':18,
    'j':19,
    'k':20,
    'l':21,
    'm':22,
    'n':23,
    'o':24,
    'p':25,
    'q':26,
    'r':27,
    's':28,
    't':29,
    'u':30,
    'v':31,
    'w':32,
    'x':33,
    'y':34,
    'z':35,
}

def make_label(filename):
    test_label = [0 for _ in range(4*36)]
    tag = filename[:-4]
    real_label = []
    for i in range(4):
      test_label[i*36+mp[tag[i]]] = 1
      real_label+=test_label[i*36:(i+1)*36]
    real_label = np.asarray(real_label,dtype=np.float32)
    return real_label

def pre_pocess_imgs(imgs_dir):
    """
    参数：imgs_dir 图片所在文件夹
    返回: imagedataset和label
    """
    data_set = []
    label_set = []
    try :
        imgs = os.listdir(imgs_dir)
    except Exception as e:
        raise e
        print(f'读取文件夹{imgs_dir}出错')
        return None
    for img in imgs:
        captcha = Image.open(imgs_dir+img)
        np_grey_capt = np.asarray(captcha.convert('1'))
        captcha_np = np.expand_dims(np_grey_capt)
        data_set.append(captcha_np)
        label = make_label(img)
        label_set.append(label)
    data_set = np.asarray(data_set)
    label_set = np.asarray(label_set)
    return data_set,label_set

def generate_dataset(train_imgs_dir,test_imgs_dir):
    train_dataset,train_labels = pre_pocess_imgs(train_imgs_dir)
    test_dataset,test_labels = pre_pocess_imgs(test_imgs_dir)
    train_dataset = tf.data.Dataset.from_tensor_slices((train_dataset,train_labels))
    test_dataset = tf.data.Dataset.from_tensor_slices((test_dataset,test_labels))
    return train_dataset,test_dataset

if __name__ == '__main__':
    pass