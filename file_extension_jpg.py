import os
# 폴더명 수정 
Dest = 'C:/Users/JHS_WIN/Desktop/Ladder_truck'
fileEx = r'.jpg'
jpg_list = [file for file in os.listdir(Dest) if file.endswith(fileEx)]

for i in range(len(jpg_list)):
#    print(jpg_list[i])
    jpg_list[i]=jpg_list[i][:-4]
jpg_list

#csv로 저장후 엑셀복사해서 txt로 저장
ATfile = open("traincsv.csv","w")
for i in range(len(jpg_list)):
    ATfile.write(jpg_list[i]+'\n')
ATfile.close()
