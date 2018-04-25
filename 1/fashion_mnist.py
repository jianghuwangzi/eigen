import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten
from keras.layers.convolutional import Conv2D,MaxPooling2D
from tensorflow.examples.tutorials.mnist import input_data # for data
mnist = input_data.read_data_sets('MNIST_data', one_hot=False)

(X_train,y_train)=mnist.train.next_batch(60000)
(X_test,y_test)=mnist.test.next_batch(10000)
# (X_train,y_train),(X_test,y_test)=load_fashiondata()
print(X_train)
print(y_train)
print(X_train.shape)
print(y_train[0])
X_train=X_train.reshape(X_train.shape[0],28,28,1).astype('float32')
X_test=X_test.reshape(X_test.shape[0],28,28,1).astype('float')
X_train/=255
X_test/=255
#把标签用one-hot 从新编码
def tran_y(y):
    y_ohe=np.zeros(10)
    y_ohe[y]=1
    return y_ohe
y_train_ohe=np.array([tran_y(y_train[i])for i in range(len(y_train))])
y_test_ohe=np.array([tran_y(y_test[i])for i in range(len(y_test))])

#搭建卷积神经网络
model=Sequential()
model.add(Conv2D(filters=64,kernel_size=(5,5),strides=(1,1),padding='same',input_shape=(28,28,1),activation='relu'))
#添加MaxPooling2D，在2X2的格子中取最大值
model.add(MaxPooling2D(pool_size=(2,2)))
#设立Dropout层，常用的值为0.2,0.3,0.5
# model.add(Dropout(0.5))
model.add(Dropout(0.02))
#重复构造，搭建深度网络
model.add(Conv2D(128,kernel_size=(3,3),strides=(1,1),padding='same',activation='relu'))
# model.add(Conv2D(128,kernel_size=(5,5),strides=(1,1),padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
# model.add(Dropout(0.5))
model.add(Dropout(0.02))
model.add(Conv2D(256,kernel_size=(3,3),strides=(1,1),padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
# model.add(Dropout(0.5))
model.add(Dropout(0.02))
#把当前节点铺平
model.add(Flatten())
#构建全连接层
model.add(Dense(128,activation='relu'))
model.add(Dense(64,activation='relu'))
# model.add(Dense(32,activation='relu'))
model.add(Dense(10,activation='softmax'))
#定义损失函数，一般分类问题的损失函数选择Cross Entropy
model.compile(loss='categorical_crossentropy',optimizer='adagrad',metrics=['acc','mae'])
# model.fit(X_train,y_train_ohe,validation_data=(X_test,y_test_ohe),epochs=l30,batch_size=128)

model.fit(X_train,y_train_ohe,validation_data=(X_test,y_test_ohe),epochs=100,batch_size=64)
#评估

scores=model.evaluate(X_test,y_test_ohe,verbose=0)

