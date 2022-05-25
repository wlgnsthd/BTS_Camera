import os
import matplotlib.pyplot as plt
#대상폴더 수정
Dest = '/media/nvidia/nvidia_deep/models/Laddertruck/'
#대상 파일확장자 수정
fileEx = r'.pth'
file_list = [file for file in os.listdir(Dest) if file.endswith(fileEx)]

# mb1-ssd-Epoch-123-Loss-0.123456789.pth
# x = Epoch, y = Loss
r = 0
y = list()
for i in file_list:
    y.append(i.split('-')[5])
    r = r + 1

r = 0
for i in y:
    y[r] = y[r][:3]
    r = r + 1

x = list()
for i in range(len(file_list)):
    x.append(i+1)

plt.plot(x,y)
plt.show()
