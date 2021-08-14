# Anaconda, CUDA, C:\tensorflow1
## Run Anaconda
~~~
conda create -n tensorflow1 pip python=3.5
activate tensorflow1
python -m pip install --upgrade pip
pip install --ignore-installed --upgrade tensorflow-gpu
~~~
~~~
conda install -c anaconda protobuf
pip install pillow
pip install lxml
pip install Cython
pip install contextlib2
pip install jupyter
pip install matplotlib
pip install pandas
pip install opencv-python

set PYTHONPATH=C:\tensorflow1\models;C:\tensorflow1\models\research;C:\tensorflow1\models\research\slim
echo %PYTHONPATH%

cd C:\tensorflow1\models\research
protoc --python_out=. .\object_detection\protos\anchor_generator.proto .\object_detection\protos\argmax_matcher.proto .\object_detection\protos\bipartite_matcher.proto .\object_detection\protos\box_coder.proto .\object_detection\protos\box_predictor.proto .\object_detection\protos\eval.proto .\object_detection\protos\faster_rcnn.proto .\object_detection\protos\faster_rcnn_box_coder.proto .\object_detection\protos\grid_anchor_generator.proto .\object_detection\protos\hyperparams.proto .\object_detection\protos\image_resizer.proto .\object_detection\protos\input_reader.proto .\object_detection\protos\losses.proto .\object_detection\protos\matcher.proto .\object_detection\protos\mean_stddev_box_coder.proto .\object_detection\protos\model.proto .\object_detection\protos\optimizer.proto .\object_detection\protos\pipeline.proto .\object_detection\protos\post_processing.proto .\object_detection\protos\preprocessor.proto .\object_detection\protos\region_similarity_calculator.proto .\object_detection\protos\square_box_coder.proto .\object_detection\protos\ssd.proto .\object_detection\protos\ssd_anchor_generator.proto .\object_detection\protos\string_int_label_map.proto .\object_detection\protos\train.proto .\object_detection\protos\keypoint_box_coder.proto .\object_detection\protos\multiscale_anchor_generator.proto .\object_detection\protos\graph_rewriter.proto .\object_detection\protos\calibration.proto .\object_detection\protos\flexible_grid_anchor_generator.proto

python setup.py build
python setup.py install
~~~
##Jupyter로 시험
~~~
cd C:\tensorflow1\models\research\object_detection
jupyter notebook object_detection_tutorial.ipynb

~~~

##LabelIMG->xml->20%test 80%train
~~~
python xml_to_csv.py
~~~

##Revise generate_tfrecord.py labelmap
##Generate TFRecord file
~~~
python generate_tfrecord.py --csv_input=images\train_labels.csv --image_dir=images\train --output_path=train.record
python generate_tfrecord.py --csv_input=images\test_labels.csv --image_dir=images\test --output_path=test.record

~~~

##Change .pbtxt from .txt
##Move config file to training folder and Revise #9,#106,#123,#125,#135,#137

##Train
~~~
python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config
~~~
##TensorBoard
~~~
tensorboard --logdir=training
~~~
##ckpt->pb file XXXX=highest number in training folder .ckpt
~~~
python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph
~~~
