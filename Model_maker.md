# Install Tensorflow
## Install Anaconda
~~~
conda create -n tensorflow pip python=3.9
conda activate tensorflow
pip install --ignore-installed --upgrade tensorflow==2.5.0
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
~~~
## Install CUDA cuDNN(C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\) 
https://developer.nvidia.com/cuda-11.2.2-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exenetwork
https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.1.0.77/11.2_20210127/cudnn-11.2-windows-x64-v8.1.0.77.zip
### envrironment variables(system)
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\libnvvp
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\include
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\extras\CUPTI\lib64
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\cuda\bin
## Make TensorFlow directory (C:\TensorFlow)
https://github.com/tensorflow/models
## Install Protobuf(C:\Program Files\Google Protobuf)
https://github.com/google/protobuf/releases 
### envrionment variables(system)
C:\Program Files\Google Protobuf
### Compliation
~~~
cd C:\TensorFlow\models\research
protoc object_detection/protos/*.proto --python_out=.
~~~
## Install COCO API
Visual C++ 2015 must be installed
https://www.microsoft.com/ko-kr/download/details.aspx?id=48159
~~~
pip install cython
conda install git
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
~~~
## Install Object Detection API
~~~
cp object_detection/packages/tf2/setup.py .
python -m pip install --use-feature=2020-resolver .
~~~
## Test Installation
python object_detection/builders/model_builder_tf2_test.py
