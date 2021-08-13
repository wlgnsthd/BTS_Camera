# Anaconda, CUDA, C:\tensorflow1
## Run Anaconda
conda create -n tensorflow1 pip python=3.5
activate tensorflow1
python -m pip install --upgrade pip
pip install --ignore-installed --upgrade tensorflow-gpu

conda install -c anaconda protobuf
pip install pillow
pip install lxml
pip install Cython
pip install contextlib2
pip install jupyter
pip install matplotlib
pip install pandas
pip install opencv-python

set PYTHONPATH=C:\tensorflow1

##LabelIMG->xml->20%test 80%train
cd C:\tensorflow1
python xml_to_csv.py

##Revise generate_tfrecord.py ->replace labelmap
##Generate TFRecord file
python generate_tfrecord.py --csv_input=images\train_labels.csv --image_dir=images\train --output_path=train.record
python generate_tfrecord.py --csv_input=images\test_labels.csv --image_dir=images\test --output_path=test.record

##Revise pbtxt from txt
##Move config file to training folder and Revise #9,#106,#123,#125,#135,#137

##Train
python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config

##TensorBoard
tensorboard --logdir=training

##ckpt->pb file
python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph

