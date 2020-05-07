# Use tensorflow 2.x
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Layer

class inside_conv_block(Layer):
    def __int__(self):
        super(inside_conv_block,self).__init__(output_D,pool_size,name='')
        self.conv2d = tf.keras.layers.Conv2D(filters=output_D,kernel_size=3,padding='same',)
        self.batchnorm = tf.keras.layers.BatchNormalization()
        self.pool = tf.keras.layers.MaxPool2D(pool_size=pool_size)
        self.relu = tf.keras.layers.ReLU()

    def call(self,x):
        x = self.conv2d(x)
        x = self.batchnorm(x)
        x = self.pool(x)
        x = self.relu(x)

        return x

class inside_dense_block(Layer):
    def __int__(self):
        super(inside_dense_block, self).__int__(output_d,out=False,name='')
        self.dense = tf.keras.layers.Dense(units=output_d)
        self.dropout = tf.keras.layers.Dropout(rate=0.2,) #可以做实验参数 dropoutrate
        self.softmax = tf.keras.layers.Softmax()
        self.out = self.out

    def call(self,x):
        x = self.dense(x)
        if not self.out:
            x = self.dropout(x)
            return x
        else:
            x = self.softmax(x)
            return x
"""
网络结构借鉴 https://github.com/nickliqian/cnn_captcha 
1.输入层
2.隐藏层：
    2.1 卷积+pool+relu
    2.2 卷积+pool+relu
    2.3 卷积+pool+relu
    2.4 全连接 + dropout（rate）
    2.5 全连接 + softmax
3.输出层(beta0.1版本4个数字和字符的组合)
""" 

class Capcha_Model(Model):
    def __int__(self):
        super(Capcha_Model,self).__init__()
        self.input = tf.keras.layers.Input()
        self.hidden1_1 = inside_conv_block(output_D=16,pool_size=2,name='hidden1_1')
        self.hidden1_2 = inside_conv_block(output_D=32, pool_size=2, name='hidden1_2')
        self.hidden1_3 = inside_conv_block(output_D=64, pool_size=2, name='hidden1_3')
        self.inside_dense_block_1 = inside_dense_block(output_d=128,name='inside_dense_block_1')
        self.inside_dense_block_2 = inside_dense_block(output_d=10+26,out=True,name='inside_dense_block_1')

    def call(self,x):
        x = self.hidden1_1(x)
        x = self.hidden1_2(x)
        x = self.hidden1_3(x)
        x = self.inside_dense_block_1(x)
        x = self.inside_dense_block_2(x)

        return x
        
