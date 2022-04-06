import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
#net = jetson.inference.detectNet(network = "ssd-mobilenet-v2", model = "models/QR/ssd-mobilenet.onnx", labels = "models/QR/labels.txt", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")      # '/dev/video0' or 'csi://0'
display = jetson.utils.videoOutput("display://0")     # 'my_video.mp4' for file

while display.IsStreaming():
    img = camera.Capture()
    detections = net.Detect(img) # ,overlay='none' : no detection image

    node_to_ROS = []

    object_count = 0

    for detection in detections: 
        # print(detection.Left, detection.Top, detection.Right, detection.Bottom)
        node_to_ROS[0, object_count] = GetClassDesc(detection) # detected class
        node_to_ROS[1, object_count] = object_count + 1 # detected number
        node_to_ROS[2, object_count] = 0.5 * (detection.Left + detection.Right) # x try detection.Center[1]
        node_to_ROS[3, object_count] = 0.5 * (detection.Top + detection.Bottom) # y try detection.Center[2]
        node_to_ROS[4, object_count] = detection.Width
        node_to_ROS[5, object_count] = detection.Height
        object_count = object_count + 1
    
    print(node_to_ROS)

    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
