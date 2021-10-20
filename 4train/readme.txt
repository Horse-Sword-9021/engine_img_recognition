
利用文件requirements.txt安装所依赖库：pip install -r requirements.txt

预训练权重来源：https://github.com/ultralytics/yolov5/releases      默认使用权重文件yolov5s.pt

复制文件 voc.yaml ( 4rain\yolov5-5.0\data\voc.yaml ),粘贴到同一位置，修改文件名。修改复制后的文件，第10行，将 'download: bash data/scripts/get_voc.sh'语句（为下载权重文件语句，此处不需要）注释掉。
    13，14，17，20行，分别对应训练集，测试集，标签类别总数，标签

复制文件 yolov5s.yaml ( 4train\yolov5-5.0\models\yolov5s.yaml ) ,粘贴到同一位置，修改文件名。修改复制后的文件，第2行，换为标签类别总数

修改train.py参数中的配置，第486，487，488，490，491行，具体内容详见源码文件。
    修改文件 detect.py ( 4train\yolov5-5.0\detect.py )

train.py文件中的第54，56，63，368，536，560行，为编码格式问题，本项目中所使用统一为UTF-8格式。GBK的格式在我电脑上出了点问题，如果你遇到编码格式问题，请在对应位置调整。
    detect.py第108行，编码格式
修改文件datasets.py( 4train\yolov5-5.0\utils\datasets.py )
    第81行，num_workers=0。
    第280行，将url转换为字符串格式


启用tensorbord查看训练过程
    训练中查看训练过程tensorboard --logdir=runs/train
    训练结束后查看训练过程tensorboard --logdir=runs

文件best.pt ( 4train\yolov5-5.0\runs\train\exp\weights\best.pt ) 为训练结束后生成的最好的权重文件，文件last.pt ( 4train\yolov5-5.0\runs\train\exp\weights\last.pt )为训练结束后生成的最后一轮权重文件。
    此处的文件路径可能有些许变化，不一定是exp下的，有可能会在某个exp[i]文件夹下。
    添加刚训练好的权重文件，替换原来的预训练权重文件 （第168行）
