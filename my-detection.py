import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")      # '/dev/video0' or 'csi://0'
display = jetson.utils.videoOutput("display://0")     # 'my_video.mp4' for file


object_count = 0

while display.IsStreaming():
    img = camera.Capture()
    detections = net.Detect(img) # ,overlay='none' : no detection image

    for detection in detections:
        print(detection.Left, detection.Top, detection.Right, detection.Bottom)

    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
