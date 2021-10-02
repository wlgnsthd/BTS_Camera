# BTS_Camera
#### https://drive.google.com/file/d/1iusDtPvxBYOtyzao3nvTVx4CaU_VTrK7/view?usp=sharing
## RPI Command Code
### Download and Update1 & Testing
~~~
sudo apt update
sudo apt full-upgrade

sudo apt-get update
sudo apt-get dist-upgrade

#Camera
sudo raspi-config 
raspistill -v -o test.jpg
raspivid -v -t 10000 -o testvid.h264

#Tensorflow Lite script download
git clone https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi.git
~~~

### Download and Update2
~~~
#Install OpenCV, TensorflowLite_files
sudo pip3 install opencv-python 

##Download and Install TPU files
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install libedgetpu1-max
~~~


### Virtual envrionment Run1
~~~
mv TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi tflite1

#Tensorflow Lite Virtual environment setting
cd tflite1
sudo pip3 install virtualenv
python3 -m venv tflite1-env
source tflite1-env/bin/activate

bash get_pi_requirements.sh

#Download Sample file(normal/edge TPU model)(once)
wget https://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip
unzip coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip -d Sample_TFLite_model
wget https://dl.google.com/coral/canned_models/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite
mv mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite Sample_TFLite_model/edgetpu.tflite

#For competition
##to communicate with arduino
# python3 -m pip install serial
# python3 -m pip install pyserial


~~~

### Run2(after putting tflite files into a folder) 
~~~
##Tensorflow Lite webcam code with TPU (revise resolution in .py file)
python3 TFLite_detection_webcam.py --modeldir=Sample_TFLite_model --edgetpu

#Tensorflow Lite webcam code without TPU
python3 TFLite_detection_webcam.py --modeldir=Sample_TFLite_model
~~~

# Change detect.py file
![IMG_7770](https://user-images.githubusercontent.com/88171531/135710082-72bd71c0-109a-42bb-9002-465c97e60f96.jpeg)
![IMG_8059](https://user-images.githubusercontent.com/88171531/135710089-28ee9cfb-fbf6-46c3-b47d-fa1ff43b1b1b.jpg)
![IMG_8060](https://user-images.githubusercontent.com/88171531/135710093-962216ea-292f-43b6-86d7-ce4bfd064174.jpeg)

