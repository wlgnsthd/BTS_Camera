```
sudo apt-get update
sudo apt-get install git cmake libpython3-dev python3-numpy
git clone --recursive https://github.com/dusty-nv/jetson-inference

cd jetson-inference
mkdir build
cd build
cmake ../
## download model
# cd jetson-inference/tools
# ./download-models.sh
## download pytorch
# cd jetson-inference/build
# ./install-pytorch.sh

make
sudo make install
sudo ldconfig
```
```
# 1) check CUDA version
dpkg -l | grep cuda 

# 2) check Camera directory
ls -ltrh /dev/video*
# csi://1

# 3) swap memory
sudo systemctl disable nvzramconfig
sudo fallocate -l 4G /mnt/4GB.swap
sudo mkswap /mnt/4GB.swap
sudo swapon /mnt/4GB.swap
/mnt/4GB.swap  none  swap  sw 0  0
swapon -s

# 4) check RAM GPU CPU
tegrastats
# top
# free

# 5) labelling
camera-capture csi://1
# /dev/video1

# 6) pth to onnx
python3 onnx_export.py --model-dir=models/*
```
