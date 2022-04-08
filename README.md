# UAM_UOU_ObjectDetection

https://github.com/dusty-nv/jetson-inference.git

## /home/nvidia/jetson-inference/python/training/detection/ssd/mine

# annotation example
```
<annotation>
    <filename>20220106-162319.jpg</filename>
    <folder>QR</folder>
    <source>
        <database>QR</database>
        <annotation>custom</annotation>
        <image>custom</image>
    </source>
    <size>
        <width>1280</width>
        <height>720</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
    <object>
        <name>QR1</name>
        <pose>unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>741</xmin>
            <ymin>334</ymin>
            <xmax>934</xmax>
            <ymax>528</ymax>
        </bndbox>
    </object>
    <object>
        <name>QR2</name>
        <pose>unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>923</xmin>
            <ymin>324</ymin>
            <xmax>1127</xmax>
            <ymax>519</ymax>
        </bndbox>
    </object>
</annotation>
```
# file tree
jetson-inference/python/training/detection/ssd / models/QR,mobilenet~.pth
                                               /data/QR/(Annotaions,ImageSets,JPEGImages),labels.txt
![20220408_104459](https://user-images.githubusercontent.com/88171531/162373747-3b52eb9e-dd9e-427e-bb38-61a5ee22a400.jpg)


https://user-images.githubusercontent.com/88171531/162373762-34355905-ec1e-463f-a4d9-3a51b1c50820.mp4

