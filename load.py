import os
import os.path
import time
import pickle
import cv2
import face_recognition

name = input("请输入您的姓名：")
print("请按下's'键拍照录入")
cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret,frame = cap.read()
    if ret:
        cv2.imshow('Please Keep Smiling', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imencode('.jpg', frame)[1].tofile('./images/' + name + '.jpg')
            break
cap.release()
cv2.destroyAllWindows()

print("===============================")
print("开始预加载照片...") 
print("请稍等...")
time_start=time.time()
path = os.getcwd()+'/images'
os.chdir(path)
images_file = os.listdir('.')
know_names = []
know_paths = []
know_encodings = []
print("正在读取文件...")
for each in images_file:
    name = os.path.splitext(each)[0]
    know_names.append(name)
    image_path = path + '/' + each
    know_paths.append(image_path)
print("开始编码照片中的人脸...")
count = 1
for each_path in know_paths:
    img = face_recognition.load_image_file(each_path)
    print("正在编码第%d张照片..." % count)
    locations = face_recognition.face_locations(img) #or model='cnn'
    encoding0 = face_recognition.face_encodings(img, locations, num_jitters=10)
    if len(encoding0) > 0:
        encoding = encoding0[0]
        know_encodings.append(encoding)
        print("第%d张照片已编码完成" % count)
    count = count + 1

print("编码结束！写入文件中...")	
pickle_encoding_file = open('../face_encodings.pkl','wb')
pickle.dump(know_encodings, pickle_encoding_file)
pickle_encoding_file.close() 
pickle_name_file = open('../face_names.pkl','wb')
pickle.dump(know_names, pickle_name_file)
pickle_name_file.close()
time_end=time.time()
time_take = time_end - time_start
print("照片预加载完成！")
print("花费时间：%s 秒!" % time_take)
print("===============================")
