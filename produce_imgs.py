import sys
import os
import random
import shutil
from captcha.image import ImageCaptcha

#48,97
CHAR_SET = []
for i in range(10):
    CHAR_SET.append(chr(ord('0')+i))

for i in range(26):
    CHAR_SET.append(chr(ord('a')+i))

CAPTCHA_LEN = 4

CAPTCHA_IMG_PATH = 'images/'
TEST_PATH = 'test/'

NUMS = 100
TEST_NUMS = 20

try:
    os.listdir(CAPTCHA_IMG_PATH)
except FileNotFoundError as e:
    print(f'不存在{CAPTCHA_IMG_PATH}文件夹')
    os.mkdir(CAPTCHA_IMG_PATH)

try:
    os.listdir(TEST_PATH)
except FileNotFoundError as e:
    print(f'不存在{TEST_PATH}文件夹')
    os.mkdir(TEST_PATH)

def generate_capt_imgs(char_Set=CHAR_SET,char_Len=CAPTCHA_LEN,img_Path=CAPTCHA_IMG_PATH):
    
    for i in range(NUMS):
        context = ""
        for i in range(4):
            context += random.choice(CHAR_SET)
        image = ImageCaptcha()
        image.write(context,CAPTCHA_IMG_PATH+context+'png')
        print(f"{int((i+1)/TEST_NUMS*100)}%",end='\r')

def seperate_test_imgs(test_path=TEST_PATH):
    try:
        imgs = os.listdir(CAPTCHA_IMG_PATH)
    except Exception as e:
        raise e
        print('读取图片文件出错')
    random.shuffle(imgs)
    test_imgs = imgs[:TEST_NUMS]
    for i,img in enumerate(test_imgs):
        try:
            shutil.move(CAPTCHA_IMG_PATH+img,TEST_PATH+img)
        except Exception as e:
            print(f'移动图片{img}失败')
        print(f"{int((i+1)/TEST_NUMS*100)}%",end='\r')


if __name__ == '__main__':
    seperate_test_imgs()
