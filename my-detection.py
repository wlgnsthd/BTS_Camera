import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")      # '/dev/video0' or 'csi://0'
display = jetson.utils.videoOutput("display://0")     # 'my_video.mp4' for file


object_count = 0

while display.IsStreaming():
    img = camera.Capture()
    detections = net.Detect(img)#overlay='none'

    for detection in detections:
        # allocate the output image, with the cropped size
        imgCropped = jetson.utils.cudaAllocMapped(width=detection.Width,
                                                  height=detection.Height,
                                                  format=img.format)

        # get the cropping ROI from the bounding box
        #crop_roi = (detection.Left, detection.Top, detection.Right, detection.Bottom)
        print(detection.Left, detection.Top, detection.Right, detection.Bottom)

        # crop the image
        #jetson.utils.cudaCrop(img, imgCropped, crop_roi)

        # save the image
        #jetson.utils.saveImage('object_{:d}.jpg'.format(object_count), imgCropped)
        #object_count += 1
        #del imgCropped

    display.Render(img)
    print("1")
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
