~~~
python3 --version
pip3 --version

sudo apt update
sudo apt install python3-dev python3-pip python3-venv

python3 -m venv --system-site-packages ./venv
source ./venv/bin/activate  

pip install --upgrade pip

deactivate  # don't exit until you're done using TensorFlow
~~~
