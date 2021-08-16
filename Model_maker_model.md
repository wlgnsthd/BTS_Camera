# Make workspace directory and subsidiary
C:\TensorFlow\workspace <br>
C:\TensorFlow\workspace\training_demo <br>
C:\TensorFlow\workspace\training_demo\images\train <br>
C:\TensorFlow\workspace\training_demo\images\test <br>
C:\TensorFlow\workspace\training_demo\annotations <br>
C:\TensorFlow\workspace\training_demo\pre-trained-models <br>
C:\TensorFlow\workspace\training_demo\models <br>
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

# Reuse Pre-trained models (can get all other models)
## Download Pre-trained model (.tar.gz)
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md <br>
unzip into C:\TensorFlow\workspace\training_demo\pre-trained-models <br>
Copy pipeline.config file into C:\TensorFlow\workspace\training_demo\models\my_ssd_resnet50_v1_fpn <br>

## Revise pipeline.config file in models folder
~~~
  3    num_classes: 1 # Set this to the number of different label classes
131  batch_size: 8 # Increase/Decrease this value depending on the available memory (Higher values require more memory and vice-versa)
161  fine_tune_checkpoint: "pre-trained-models/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8/checkpoint/ckpt-0" # Path to checkpoint of pre-trained model
167  fine_tune_checkpoint_type: "detection" # Set this to "detection" since we want to be training the full detection model
168  use_bfloat16: false # Set this to false if you are not training on a TPU
172  label_map_path: "annotations/label_map.pbtxt" # Path to label map file
174    input_path: "annotations/train.record" # Path to training TFRecord file
178  metrics_set: "coco_detection_metrics" #optional
179  use_moving_averages: false #optional
182  label_map_path: "annotations/label_map.pbtxt" # Path to label map file
186    input_path: "annotations/test.record" # Path to testing TFRecord
~~~
# Training the Model
Copy C:\TensorFlow\models\research\object_detection\model_main_tf2.py and paste it training_demo folder <br>
~~~
cd C:\TensorFlow\workspace\training_demo
python model_main_tf2.py --model_dir=models/my_ssd_resnet50_v1_fpn --pipeline_config_path=models/my_ssd_resnet50_v1_fpn/pipeline.config
~~~
It will look like frozen, but it logs every 100steps (depends GPU, batchsize) <br>
Lower Totalloss is better , but very low value = overfitting
~~~
#To monitor
cd C:\TensorFlow\workspace\training_demo
tensorboard --logdir=models/my_ssd_resnet50_v1_fpn
~~~
# Exporting a Trained Model
Copy C:\TensorFlow\models\research\object_detection\exporter_main_v2.py and paste it into training_demo folder
~~~
cd C:\TensorFlow\workspace\training_demo
python .\exporter_main_v2.py --input_type image_tensor --pipeline_config_path .\models\my_efficientdet_d1\pipeline.config --trained_checkpoint_dir .\models\my_efficientdet_d1\ --output_directory .\exported-models\my_model
~~~
New folder "*\training_demo\exported-models\my_model"
