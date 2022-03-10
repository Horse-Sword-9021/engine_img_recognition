Horse-Sword
######engine_img_recognition-main\1Image_preprocessing\code
初始使用opencv版本4.0.1，有些地方与opencv3不同，以下第一解答
https://stackoverflow.com/questions/54734538/opencv-assertion-failed-215assertion-failed-npoints-0-depth-cv-32
opencv官方文档https://github.com/opencv/opencv

初始相关库包版本：pip版本20.2.4，matplotlib版本3.3.2，numpy版本1.19.2，python版本3.8.5。

暂无模型迭代训练                                                   已加入，yolov5
图片批处理，代码优化之后出错,待修改。                                  已解决

外部参考案列https://www.mindspore.cn/news/newschildren?id=354
华为模型来源： https://www.mindspore.cn/resources/hub/             未使用

MiindSpore相关内容，anaconda版本2020.11，conda版本4.10.3，pip版本21.0.1，anaconda安装python版本3.8.5，为兼容华为相关产品，下设python虚拟环境3.7.5，mindspore暂用版本1.2.0，opencv-python版本4.5.1.48，matplotlib版本3.4.1，numpy版本1.17.5，
easydict版本1.9。
'''
>>>class Flower(EasyDict):
>>>     power = 1
>>>
>>> f = Flower({'height': 12})
>>> f.power
>>>1
>>> f['power']
>>>1
'''
> 
> 
> 
> hsf

#####以平滑处理/降噪函数为例，说明all.py和start.py文件中，可能存在的路径问题
    $ python all.py  # webcam
    wd = os.getcwd()                        #获取工作目录
    data_base_dir = os.path.join(wd, "../") #退回工作目录的上级目录    
    data_base_dir_1 = os.path.join(data_base_dir, "imgs/")
    if not os.path.isdir(data_base_dir):
        print('无初始数据集！')                #数据集存放在（1Image_preprocessing/imgs/imgs）下
    lower_base_dir = os.path.join(data_base_dir_1, "operate_imgs/")#文件夹覆盖
    if not os.path.isdir(lower_base_dir):
        os.mkdir(lower_base_dir)
    detail_operate_dir = os.path.join(lower_base_dir, "1smooth/")
    if not os.path.isdir(detail_operate_dir):
        os.mkdir(detail_operate_dir)

    cv2.imwrite(f'../imgs/operate_imgs/1smooth/{i}_median.png', median_)  # 写入（退回上级目录后写入）

* 将数据集放在imgs/imgs中的文件夹中，处理完毕后会自动生成operate_imgs及以后的文件夹。

操作：根据具体数据集选取更合理的操作
一、
1、首先设置roi
2、预处理:高斯平滑加二值化即可
3、查找最大轮廓
4、透视变换抠取检测对象
5、再次查找对象区域内的轮廓，筛选出缺陷点
6、缺陷映射回原图
当采用斜外接矩形获取检测对象时，映射回原图存在裂缝，这是应该斜外接矩形有角度，抠图和映射回去是产生了误差，需要手动修复
7、对图像拼接处进行修复

二、
预处理:高斯平滑加二值化即可
高斯平滑+腐蚀+边缘检测/梯度操作（会将反光部分识别为缺陷部位）+

三、
先对孔探图像进行灰度化、滤波降噪、锐化、阈值分割、边缘提取等系列的预处理，
再基于样条插值自动测量叶片缺口的尺寸，该方法的局限是与缺陷的边缘特征强关联，
仅对单一场景、边缘特征明显的叶片缺口图像有效。

先用边缘检测算法预处理损伤图像再进行小波分解，自适应检测算法，同样基于小波和边缘检测技术，
不同之处是利用边缘检测和小波滤波来降低噪点以增强图像质量，之后利用阈值分割技术来提取叶片裂纹的特征.

