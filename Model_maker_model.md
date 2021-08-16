# Make workspace directory and subsidiary
C:\TensorFlow\workspace <br>
C:\TensorFlow\workspace\training_demo <br>
C:\TensorFlow\workspace\training_demo\images\train <br>
C:\TensorFlow\workspace\training_demo\images\test <br>
C:\TensorFlow\workspace\training_demo\annotations <br>
C:\TensorFlow\scripts\preprocessing <br>

# Preparing the Dataset(labelImg)
~~~
pip install labelImg
labelImg C:\TensorFlow/workspace/training_demo/images
~~~
make .xml file

# Partition the Dataset
move images and xml file to 10% test folder 90% train folder

# Create Label Map
make label_map.pbtxt file and put it into annotations folder
~~~
item {
    id: 1
    name: 'cat'
}

item {
    id: 2
    name: 'dog'
}
~~~

# Creat Tensorflow records
https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/_downloads/da4babe668a8afb093cc7776d7e630f3/generate_tfrecord.py
 <br>
 
save it into preprocessing folder
~~~
conda install pandas
cd C:\TensorFlow\scripts\preprocessing
# Create train data:
python generate_tfrecord.py -x C:\TensorFlow\workspace\training_demo\images\train -l C:\TensorFlow\workspace\training_demo\annotations\label_map.pbtxt -o C:\TensorFlow\workspace\training_demo\annotaions\train.record
# Create test data:
python generate_tfrecord.py -x C:\TensorFlow\workspace\training_demo\images\test -l C:\TensorFlow\workspace\training_demo\annotations\label_map.pbtxt -o C:\TensorFlow\workspace\training_demo\annotaions\test.record
~~~
