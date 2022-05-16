#해당 확장자 파일 확인
import os
#데이터셋 디렉토리
Dir = r'C:/Users/Jihun Song/Desktop/export/'
#파일확장자
fileEx = r'.jpg'
jpg_list = [file for file in os.listdir(Dir) if file.endswith(fileEx)]
jpg_list
#파일 옮기기 실행
import shutil
#옮기는 대상 디렉토리
Dest = 'C:/Users/Jihun Song/Desktop/JPEGImages'
for f in jpg_list:
    shutil.move(Dir+f,dest)
#확장자를 제외한 파일명 생성
import os
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