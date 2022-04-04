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
```
