import jetson.inference
import jetson.utils

net = jetson.inference.detectNet('ssd-mobilenet-v2', argv=['--model=ssd-mobilenet.onnx','--labels=labels.txt','--input-blob=input_0','--output-cvg=scores','--output-bbox=boxes'],threshold = 0.5)
camera = jetson.utils.videoSource("/dev/video1")      # '/dev/video0' or 'csi://0'
display = jetson.utils.videoOutput("display://0")     # 'my_video.mp4' for file


while display.IsStreaming():
    img = camera.Capture()
    detections = net.Detect(img) # ,overlay='none' : no detection image
    node_to_ROS = []
    object_count = 0


    for detection in detections: 
        node_to_ROS = [object_count+1,
                       net.GetClassDesc(detection.ClassID),
                       detection.Left, detection.Top, detection.Right, detection.Bottom,
                       detection.Width,detection.Height]
        object_count = object_count + 1

    if node_to_ROS == []:
        print("No Detection")
    else:
        print(node_to_ROS)


    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

