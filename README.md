# Horse-Sword
  
## 新人第一次尝试，如有不妥，还请见谅。别喷，喷就是你对

## 如有疑问，可联系

        微信(Wechat)：Horse-Sword
        QQ：3071910019
        Email：3071910019@qq.com

## 欢迎大家一起来交流

---

### 所有说明中提到源码的行数，是进行了相关修改、说明过后的，其中yolov5-5.0说明中提到的行数与官方文件中的不一致，所有说明以本文件为准

#### 本项目中涉及到相关编码格式，统一为UTF-8格式，GBK格式在我电脑上出了点问题。如果你遇到编码格式问题，请参考每个文件夹下的readme文件中的内容，在对应位置进行修改

    下列出所有的编码格式所在
    文件 success.py ( 3dataset_processing\success.py ): 42, 43, 110, 111, 114, 115
    文件 another.py (3dataset_processing\another.py ): 20, 105
    文件 detect.py ( 4train\yolov5-5.0\detect.py ): 109
    文件 train.py ( 4train\yolov5-5.0\train.py ): 55, 57, 64, 369, 537, 561
    文件 test.py ( 4train/yolov5-5.0/test.py ): 73
    文件 yolo.py ( 4train\yolov5-5.0\models\yolo.py ): 74
    文件 autoanchor.py ( 4train\yolov5-5.0\utils\autoanchor.py ): 104
    文件 datasets.py ( 4train\yolov5-5.0\utils\datasets.py ): 268, 369, 473, 1026, 1064
    文件 general.py (4train\yolov5-5.0\utils\general.py): 103, 540, 549
    文件 google_utils.py ( 4train\yolov5-5.0\utils\google_utils.py ): 91
    文件 plots.py ( 4train\yolov5-5.0\utils\plots.py ): 323
    文件 resume.py ( 4train\yolov5-5.0\utils\aws\resume.py ): 21
    文件 log_dataset.py ( 4train\yolov5-5.0\utils\wandb_logging\log_dataset.py ): 11
    文件 wandb_utils.py ( 4train\yolov5-5.0\utils\wandb_logging\wandb_utils.py ): 57, 75, 194, 208

##### 在检查过程中，仍发现读取和写入文件时，路径会出现问题。项目中相关采用相对路径，目前在pycharm上可以完整运行。如果你遇到路径错误问题，请检查工作目录与相对路径，并在对应位置修改。若仍存在错误，无法修改，请使用绝对路径

    下列出可能出错的路径所在
    文件 start.py ( 1Image_preprocessing/code/start.py ):
    文件 all.py ( 1Image_preprocessing/code/all.py ):
    文件 success.py ( 3dataset_processing/success.py ): 43, 44, 及后面较多的与路径有关的语句

### yolov5 GitHub地址：<https://github.com/ultralytics/yolov5/tree/v5.0>

* 下为第一次使用yolo测试训练中的部分记录、截图
  ![4train/yolov5-5.0/runs/train/exp9/test_batch0_labels.jpg](4train/yolov5-5.0/runs/train/exp9/test_batch0_labels.jpg)
  ![4train/yolov5-5.0/runs/train/exp9/train_batch0.jpg](4train/yolov5-5.0/runs/train/exp9/train_batch0.jpg)
  ![img_test](4train/yolov5-5.0/runs/train/exp9/results.png)
  ![4train/yolov5-5.0/runs/train/exp9/train_batch1.jpg](4train/yolov5-5.0/runs/train/exp9/train_batch1.jpg)

---

#### 所有可能用到过的库（未经筛选，显示我装的所有库）

    C:\Users\剑阁9021>conda list

    # packages in environment at D:\Anaconda:
    
    # 
    
    # Name                    Version                   Build  Channel
    
    _ipyw_jlab_nb_ext_conf    0.1.0                    py38_0    defaults
    absl-py                   0.14.1                   pypi_0    pypi
    alabaster                 0.7.12                     py_0    defaults
    altgraph                  0.17               pyhd3eb1b0_0    defaults
    anaconda                  2020.11                  py38_0    defaults
    anaconda-client           1.7.2                    py38_0    defaults
    anaconda-navigator        1.10.0                   py38_0    defaults
    anaconda-project          0.8.4                      py_0    defaults
    argh                      0.26.2                   py38_0    defaults
    argon2-cffi               20.1.0           py38he774522_1    defaults
    asn1crypto                1.4.0                      py_0    defaults
    astor                     0.8.1                    pypi_0    pypi
    astroid                   2.4.2                    py38_0    defaults
    astropy                   4.0.2            py38he774522_0    defaults
    async_generator           1.10                       py_0    defaults
    atomicwrites              1.4.0                      py_0    defaults
    attrs                     20.3.0             pyhd3eb1b0_0    defaults
    autopep8                  1.5.4                      py_0    defaults
    babel                     2.8.1              pyhd3eb1b0_0    defaults
    backcall                  0.2.0                      py_0    defaults
    backports                 1.0                        py_2    defaults
    backports.functools_lru_cache 1.6.4              pyhd3eb1b0_0    defaults
    backports.shutil_get_terminal_size 1.0.0                    py38_2    defaults
    backports.tempfile        1.0                pyhd3eb1b0_1    defaults
    backports.weakref         1.0.post1                  py_1    defaults
    bcrypt                    3.2.0            py38he774522_0    defaults
    beautifulsoup4            4.9.3              pyhb0f4dca_0    defaults
    bitarray                  1.6.1            py38h2bbff1b_0    defaults
    bkcharts                  0.2                      py38_0    defaults
    blas                      1.0                         mkl    defaults
    bleach                    3.2.1                      py_0    defaults
    blosc                     1.20.1               h7bd577a_0    defaults
    bokeh                     2.2.3                    py38_0    defaults
    boto                      2.49.0                   py38_0    defaults
    bottleneck                1.3.2            py38h2a96729_1    defaults
    brotlipy                  0.7.0           py38he774522_1000    defaults
    bzip2                     1.0.8                he774522_0    defaults
    ca-certificates           2020.10.14                    0    defaults
    cachetools                4.2.4                    pypi_0    pypi
    certifi                   2020.6.20          pyhd3eb1b0_3    defaults
    cffi                      1.14.3           py38h7a1dbc1_0    defaults
    chardet                   3.0.4                 py38_1003    defaults
    click                     7.1.2                      py_0    defaults
    cloudpickle               1.6.0                      py_0    defaults
    clyent                    1.2.2                    py38_1    defaults
    cmake                     3.19.6               h9ad04ae_0    defaults
    colorama                  0.4.4                      py_0    defaults
    commonmark                0.9.1                    pypi_0    pypi
    comtypes                  1.1.7                 py38_1001    defaults
    conda                     4.10.3           py38haa95532_0    defaults
    conda-build               3.20.5                   py38_1    defaults
    conda-env                 2.6.0                         1    defaults
    conda-package-handling    1.7.3            py38h8cc25b3_1    defaults
    conda-verify              3.4.2                      py_1    defaults
    console_shortcut          0.1.1                         4    defaults
    contextlib2               0.6.0.post1                py_0    defaults
    cryptography              3.1.1            py38h7a1dbc1_0    defaults
    cudatoolkit               10.2.89              h74a9793_1    defaults
    curl                      7.71.1               h2a8f88b_1    defaults
    cycler                    0.10.0                   py38_0    defaults
    cython                    0.29.21          py38ha925a31_0    defaults
    cytoolz                   0.11.0           py38he774522_0    defaults
    dask                      2.30.0                     py_0    defaults
    dask-core                 2.30.0                     py_0    defaults
    decorator                 4.4.2                      py_0    defaults
    defusedxml                0.6.0                      py_0    defaults
    diff-match-patch          20200713                   py_0    defaults
    distributed               2.30.1           py38haa95532_0    defaults
    docutils                  0.16                     py38_1    defaults
    entrypoints               0.3                      py38_0    defaults
    et_xmlfile                1.0.1                   py_1001    defaults
    fastcache                 1.1.0            py38he774522_0    defaults
    filelock                  3.0.12                     py_0    defaults
    flake8                    3.8.4                      py_0    defaults
    flask                     1.1.2                      py_0    defaults
    freetype                  2.10.4               hd328e21_0    defaults
    fsspec                    0.8.3                      py_0    defaults
    future                    0.18.2                   py38_1    defaults
    gast                      0.3.3                    pypi_0    pypi
    get_terminal_size         1.0.0                h38e98db_0    defaults
    gevent                    20.9.0           py38he774522_0    defaults
    glob2                     0.7                        py_0    defaults
    google-auth               1.35.0                   pypi_0    pypi
    google-auth-oauthlib      0.4.6                    pypi_0    pypi
    greenlet                  0.4.17           py38he774522_0    defaults
    grpcio                    1.41.0                   pypi_0    pypi
    h5py                      2.10.0           py38h5e291fa_0    defaults
    hdf5                      1.10.4               h7ebc959_0    defaults
    heapdict                  1.0.1                      py_0    defaults
    html5lib                  1.1                        py_0    defaults
    icc_rt                    2019.0.0             h0cc432a_1    defaults
    icu                       58.2                 ha925a31_3    defaults
    idna                      2.10                       py_0    defaults
    imageio                   2.9.0                      py_0    defaults
    imagesize                 1.2.0                      py_0    defaults
    importlib-metadata        2.0.0                      py_1    defaults
    importlib_metadata        2.0.0                         1    defaults
    iniconfig                 1.1.1                      py_0    defaults
    intel-openmp              2020.2                      254    defaults
    intervaltree              3.1.0                      py_0    defaults
    ipykernel                 5.3.4            py38h5ca1d4c_0    defaults
    ipython                   7.19.0           py38hd4e2768_0    defaults
    ipython_genutils          0.2.0                    py38_0    defaults
    ipywidgets                7.5.1                      py_1    defaults
    isort                     5.6.4                      py_0    defaults
    itsdangerous              1.1.0                      py_0    defaults
    jdcal                     1.4.1                      py_0    defaults
    jedi                      0.17.1                   py38_0    defaults
    jieba                     0.42.1                   pypi_0    pypi
    jinja2                    2.11.2                     py_0    defaults
    joblib                    0.17.0                     py_0    defaults
    jpeg                      9b                   hb83a4c4_2    defaults
    json5                     0.9.5                      py_0    defaults
    jsonschema                3.2.0                      py_2    defaults
    jupyter                   1.0.0                    py38_7    defaults
    jupyter_client            6.1.7                      py_0    defaults
    jupyter_console           6.2.0                      py_0    defaults
    jupyter_core              4.6.3                    py38_0    defaults
    jupyterlab                2.2.6                      py_0    defaults
    jupyterlab_pygments       0.1.2                      py_0    defaults
    jupyterlab_server         1.2.0                      py_0    defaults
    keyring                   21.4.0                   py38_1    defaults
    kiwisolver                1.3.0            py38hd77b12b_0    defaults
    krb5                      1.18.2               hc04afaa_0    defaults
    labelimg                  1.8.5                    pypi_0    pypi
    lazy-object-proxy         1.4.3            py38he774522_0    defaults
    libarchive                3.4.2                h5e25573_0    defaults
    libcurl                   7.71.1               h2a8f88b_1    defaults
    libiconv                  1.15                 h1df5818_7    defaults
    liblief                   0.10.1               ha925a31_0    defaults
    libopencv                 4.0.1                hbb9e17c_0    defaults
    libpng                    1.6.37               h2a8f88b_0    defaults
    libsodium                 1.0.18               h62dcd97_0    defaults
    libspatialindex           1.9.3                h33f27b4_0    defaults
    libssh2                   1.9.0                h7a1dbc1_1    defaults
    libtiff                   4.1.0                h56a325e_1    defaults
    libuv                     1.40.0               he774522_0    defaults
    libxml2                   2.9.10               hb89e7f3_3    defaults
    libxslt                   1.1.34               he774522_0    defaults
    llvmlite                  0.34.0           py38h1a82afc_4    defaults
    locket                    0.2.0                    py38_1    defaults
    lxml                      4.6.1            py38h1350720_0    defaults
    lz4-c                     1.9.2                hf4a77e7_3    defaults
    lzo                       2.10                 he774522_2    defaults
    m2w64-gcc-libgfortran     5.3.0                         6    defaults
    m2w64-gcc-libs            5.3.0                         7    defaults
    m2w64-gcc-libs-core       5.3.0                         7    defaults
    m2w64-gmp                 6.1.0                         2    defaults
    m2w64-libwinpthread-git   5.0.0.4634.697f757               2    defaults
    macholib                  1.14               pyhd3eb1b0_1    defaults
    markdown                  3.3.4                    pypi_0    pypi
    markupsafe                1.1.1            py38he774522_0    defaults
    matplotlib                3.3.2                         0    defaults
    matplotlib-base           3.3.2            py38hba9282a_0    defaults
    mccabe                    0.6.1                    py38_1    defaults
    menuinst                  1.4.16           py38he774522_1    defaults
    mistune                   0.8.4           py38he774522_1000    defaults
    mkl                       2020.2                      256    defaults
    mkl-service               2.3.0            py38hb782905_0    defaults
    mkl_fft                   1.2.0            py38h45dec08_0    defaults
    mkl_random                1.1.1            py38h47e9c7a_0    defaults
    mock                      4.0.2                      py_0    defaults
    more-itertools            8.6.0              pyhd3eb1b0_0    defaults
    mpmath                    1.1.0                    py38_0    defaults
    msgpack-python            1.0.0            py38h74a9793_1    defaults
    msys2-conda-epoch         20160418                      1    defaults
    multipledispatch          0.6.0                    py38_0    defaults
    navigator-updater         0.2.1                    py38_0    defaults
    nbclient                  0.5.1                      py_0    defaults
    nbconvert                 6.0.7                    py38_0    defaults
    nbformat                  5.0.8                      py_0    defaults
    nest-asyncio              1.4.2              pyhd3eb1b0_0    defaults
    networkx                  2.5                        py_0    defaults
    ninja                     1.10.2               h6d14046_1    defaults
    nltk                      3.5                        py_0    defaults
    nose                      1.3.7                    py38_2    defaults
    notebook                  6.1.4                    py38_0    defaults
    numba                     0.51.2           py38hf9181ef_1    defaults
    numexpr                   2.7.1            py38h25d0782_0    defaults
    numpy                     1.19.2           py38hadc3359_0    defaults
    numpy-base                1.19.2           py38ha3acd2a_0    defaults
    numpydoc                  1.1.0              pyhd3eb1b0_1    defaults
    oauthlib                  3.1.1                    pypi_0    pypi
    olefile                   0.46                       py_0    defaults
    opencv                    4.0.1            py38h2a7c758_0    defaults
    opencv-python             4.5.3.56                 pypi_0    pypi
    openpyxl                  3.0.5                      py_0    defaults
    openssl                   1.1.1h               he774522_0    defaults
    packaging                 20.4                       py_0    defaults
    paddlepaddle-gpu          2.1.3.post112            pypi_0    pypi
    pandas                    1.1.3            py38ha925a31_0    defaults
    pandoc                    2.11                 h9490d1a_0    defaults
    pandocfilters             1.4.3            py38haa95532_1    defaults
    paramiko                  2.7.2                      py_0    defaults
    parso                     0.7.0                      py_0    defaults
    partd                     1.1.0                      py_0    defaults
    path                      15.0.0                   py38_0    defaults
    path.py                   12.5.0                        0    defaults
    pathlib2                  2.3.5                    py38_0    defaults
    pathtools                 0.1.2                      py_1    defaults
    patsy                     0.5.1                    py38_0    defaults
    pefile                    2019.4.18                  py_0    defaults
    pep8                      1.7.1                    py38_0    defaults
    pexpect                   4.8.0                    py38_0    defaults
    pickleshare               0.7.5                 py38_1000    defaults
    pillow                    8.0.1            py38h4fa10fc_0    defaults
    pip                       20.2.4           py38haa95532_0    defaults
    pkginfo                   1.6.1            py38haa95532_0    defaults
    pluggy                    0.13.1                   py38_0    defaults
    ply                       3.11                     py38_0    defaults
    powershell_shortcut       0.0.1                         3    defaults
    prometheus_client         0.8.0                      py_0    defaults
    prompt-toolkit            3.0.8                      py_0    defaults
    prompt_toolkit            3.0.8                         0    defaults
    protobuf                  3.18.1                   pypi_0    pypi
    psutil                    5.7.2            py38he774522_0    defaults
    py                        1.9.0                      py_0    defaults
    py-lief                   0.10.1           py38ha925a31_0    defaults
    py-opencv                 4.0.1            py38he44ac1e_0    defaults
    pyasn1                    0.4.8                    pypi_0    pypi
    pyasn1-modules            0.2.8                    pypi_0    pypi
    pycocotools               2.0.2                    pypi_0    pypi
    pycodestyle               2.6.0                      py_0    defaults
    pycosat                   0.6.3            py38he774522_0    defaults
    pycparser                 2.20                       py_2    defaults
    pycryptodome              3.10.1           py38h2bbff1b_0    defaults
    pycurl                    7.43.0.6         py38h7a1dbc1_0    defaults
    pydocstyle                5.1.1                      py_0    defaults
    pyflakes                  2.2.0                      py_0    defaults
    pygments                  2.7.2              pyhd3eb1b0_0    defaults
    pyinstaller               3.6              py38h8cc25b3_6    defaults
    pylint                    2.6.0                    py38_0    defaults
    pynacl                    1.4.0            py38h62dcd97_1    defaults
    pyodbc                    4.0.30           py38ha925a31_0    defaults
    pyopenssl                 19.1.0                     py_1    defaults
    pyparsing                 2.4.7                      py_0    defaults
    pyqt                      5.9.2            py38ha925a31_4    defaults
    pyqt5                     5.15.4                   pypi_0    pypi
    pyqt5-qt5                 5.15.2                   pypi_0    pypi
    pyqt5-sip                 12.9.0                   pypi_0    pypi
    pyreadline                2.1                      py38_1    defaults
    pyrsistent                0.17.3           py38he774522_0    defaults
    pysocks                   1.7.1                    py38_0    defaults
    pytables                  3.6.1            py38ha5be198_0    defaults
    pytest                    6.1.1                    py38_0    defaults
    python                    3.8.5                h5fd99cc_1    defaults
    python-dateutil           2.8.1                      py_0    defaults
    python-jsonrpc-server     0.4.0                      py_0    defaults
    python-language-server    0.35.1                     py_0    defaults
    python-libarchive-c       2.9                        py_0    defaults
    pytorch                   1.8.0           py3.8_cuda10.2_cudnn7_0    pytorch
    pytz                      2020.1                     py_0    defaults
    pywavelets                1.1.1            py38he774522_2    defaults
    pywin32                   227              py38he774522_1    defaults
    pywin32-ctypes            0.2.0                 py38_1000    defaults
    pywinpty                  0.5.7                    py38_0    defaults
    pyyaml                    5.3.1            py38he774522_1    defaults
    pyzmq                     19.0.2           py38ha925a31_1    defaults
    qdarkstyle                2.8.1                      py_0    defaults
    qt                        5.9.7            vc14h73c81de_0    defaults
    qtawesome                 1.0.1                      py_0    defaults
    qtconsole                 4.7.7                      py_0    defaults
    qtpy                      1.9.0                      py_0    defaults
    regex                     2020.10.15       py38he774522_0    defaults
    requests                  2.24.0                     py_0    defaults
    requests-oauthlib         1.3.0                    pypi_0    pypi
    rich                      9.13.0                   pypi_0    pypi
    rope                      0.18.0                     py_0    defaults
    rsa                       4.7.2                    pypi_0    pypi
    rtree                     0.9.4            py38h21ff451_1    defaults
    ruamel_yaml               0.15.87          py38he774522_1    defaults
    scikit-image              0.17.2           py38h1e1f486_0    defaults
    scikit-learn              0.23.2           py38h47e9c7a_0    defaults
    scipy                     1.5.2            py38h14eb087_0    defaults
    seaborn                   0.11.0                     py_0    defaults
    send2trash                1.5.0                    py38_0    defaults
    setuptools                50.3.1           py38haa95532_1    defaults
    simplegeneric             0.8.1                    py38_2    defaults
    singledispatch            3.4.0.3                 py_1001    defaults
    sip                       4.19.13          py38ha925a31_0    defaults
    six                       1.15.0           py38haa95532_0    defaults
    snowballstemmer           2.0.0                      py_0    defaults
    sortedcollections         1.2.1                      py_0    defaults
    sortedcontainers          2.2.2                      py_0    defaults
    soupsieve                 2.0.1                      py_0    defaults
    sphinx                    3.2.1                      py_0    defaults
    sphinxcontrib             1.0                      py38_1    defaults
    sphinxcontrib-applehelp   1.0.2                      py_0    defaults
    sphinxcontrib-devhelp     1.0.2                      py_0    defaults
    sphinxcontrib-htmlhelp    1.0.3                      py_0    defaults
    sphinxcontrib-jsmath      1.0.1                      py_0    defaults
    sphinxcontrib-qthelp      1.0.3                      py_0    defaults
    sphinxcontrib-serializinghtml 1.1.4                      py_0    defaults
    sphinxcontrib-websupport  1.2.4                      py_0    defaults
    spyder                    4.1.5                    py38_0    defaults
    spyder-kernels            1.9.4                    py38_0    defaults
    sqlalchemy                1.3.20           py38h2bbff1b_0    defaults
    sqlite                    3.33.0               h2a8f88b_0    defaults
    statsmodels               0.12.0           py38he774522_0    defaults
    sympy                     1.6.2            py38haa95532_1    defaults
    tblib                     1.7.0                      py_0    defaults
    tensorboard               2.6.0                    pypi_0    pypi
    tensorboard-data-server   0.6.1                    pypi_0    pypi
    tensorboard-plugin-wit    1.8.0                    pypi_0    pypi
    terminado                 0.9.1                    py38_0    defaults
    testpath                  0.4.4                      py_0    defaults
    thop                      0.0.31-2005241907          pypi_0    pypi
    threadpoolctl             2.1.0              pyh5ca1d4c_0    defaults
    tifffile                  2020.10.1        py38h8c2d366_2    defaults
    tk                        8.6.10               he774522_0    defaults
    toml                      0.10.1                     py_0    defaults
    toolz                     0.11.1                     py_0    defaults
    torchaudio                0.8.0                      py38    pytorch
    torchvision               0.9.0                py38_cu102    pytorch
    tornado                   6.0.4            py38he774522_1    defaults
    tqdm                      4.50.2                     py_0    defaults
    traitlets                 5.0.5                      py_0    defaults
    typing_extensions         3.7.4.3                    py_0    defaults
    ujson                     4.0.1            py38ha925a31_0    defaults
    unicodecsv                0.14.1                   py38_0    defaults
    urllib3                   1.25.11                    py_0    defaults
    vboxapi                   1.0                      pypi_0    pypi
    vc                        14.1                 h0510ff6_4    defaults
    vs2015_runtime            14.16.27012          hf0eaf9b_3    defaults
    watchdog                  0.10.3                   py38_0    defaults
    wcwidth                   0.2.5                      py_0    defaults
    webencodings              0.5.1                    py38_1    defaults
    werkzeug                  1.0.1                      py_0    defaults
    wheel                     0.35.1                     py_0    defaults
    widgetsnbextension        3.5.1                    py38_0    defaults
    win_inet_pton             1.1.0                    py38_0    defaults
    win_unicode_console       0.5                      py38_0    defaults
    wincertstore              0.2                      py38_0    defaults
    winpty                    0.4.3                         4    defaults
    wordcloud                 1.8.1                    pypi_0    pypi
    wrapt                     1.11.2           py38he774522_0    defaults
    xlrd                      1.2.0                      py_0    defaults
    xlsxwriter                1.3.7                      py_0    defaults
    xlwings                   0.20.8                   py38_0    defaults
    xlwt                      1.3.0                    py38_0    defaults
    xmltodict                 0.12.0                     py_0    defaults
    xz                        5.2.5                h62dcd97_0    defaults
    yaml                      0.2.5                he774522_0    defaults
    yapf                      0.30.0                     py_0    defaults
    zeromq                    4.3.2                ha925a31_3    defaults
    zict                      2.0.0                      py_0    defaults
    zipp                      3.4.0              pyhd3eb1b0_0    defaults
    zlib                      1.2.11               h62dcd97_4    defaults
    zope                      1.0                      py38_1    defaults
    zope.event                4.5.0                    py38_0    defaults
    zope.interface            5.1.2            py38he774522_0    defaults
    zstd                      1.4.5                h04227a9_0    defaults

---

## 如果运行发现问题后，现统一回复

* 1、请阅读文档；
* 2、还有问题：请仔细阅读文档；
* 3、确实有问题：熟读并背诵文档。
* 4、如果真的有问题，那么重启可以解决80%的问题，。还有20%咋办，还有20%不用解决啊，这世上哪有能100%解决的问题，是吧！

## 问题文件

* 可能暂时有点问题，也可能没问题，……过了几天，我好像已经忘了为什么要列出来这些文件了。。。
* 4训练\yolov5-5.0\hubconf.py
* 4训练\yolov5-5.0\test.py
* 4训练\yolov5-5.0\utils\general.py
* 4训练\yolov5-5.0\utils\google_utils.py
  * 不用理这几个文件
---
