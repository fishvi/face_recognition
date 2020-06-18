import pickle
import numpy
import cv2
import face_recognition 
from PIL import Image, ImageDraw, ImageFont

def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype("font/simsun.ttc", textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)

def face(path):
    known_names=[] #存储知道人名列表
    known_encodings=[]#存储知道的特征值
    pkl_names = open('face_names.pkl','rb')
    known_names = pickle.load(pkl_names)
    pkl_encodings = open('face_encodings.pkl','rb')
    known_encodings = pickle.load(pkl_encodings)     

    video_capture = cv2.VideoCapture(0) #打开摄像头，0表示内置摄像头
    while(video_capture.isOpened()):
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_frame = small_frame[:, :, ::-1] #opencv的图像是BGR格式的，而我们需要是的RGB格式的，因此需要进行一个转换
        if ret:
            face_locations = face_recognition.face_locations(rgb_frame) #获得所有人脸位置 or model='cnn'
            face_encodings = face_recognition.face_encodings(rgb_frame) #获得人脸特征值
            face_names = [] #存储出现在画面中人脸的名字
            for face_encoding in face_encodings:         
                matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.48)
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_names[first_match_index]
                else:
                    name = "未识别"
                face_names.append(name)

        # 将捕捉到的人脸显示出来
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2) #画人脸矩形框
            frame = cv2ImgAddText(frame, name, left, top - 25, (0, 255, 0), 20) #显示名字        
        cv2.imshow('Face Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    face("./images/") #存放已知图像路径