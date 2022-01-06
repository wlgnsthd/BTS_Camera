import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("csi://1")      # '/dev/video0' for V4L2 # csi://0
display = jetson.utils.videoOutput() # 'my_video.mp4' for file # "display://0"
#display.IsStreaming()
while True: 
	img = camera.Capture()
	detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
