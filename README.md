# face_recognition
#### 基于open cv和face_recognition的人脸识别
---
环境：&emsp;Win10  
&emsp;&emsp;&emsp;&emsp;python 3.7.3  
&emsp;&emsp;&emsp;&emsp;opencv 4.2.0.34  
&emsp;&emsp;&emsp;&emsp;dlib 19.20.0  
&emsp;&emsp;&emsp;&emsp;[face_recognition](https://github.com/ageitgey/face_recognition/blob/master/README_Simplified_Chinese.md) 1.3.0  
<br/>
<br/>
<p><strong>1.&ensp;<a href="https://github.com/fishvi/face_recognition/blob/master/load.py">load.py</a></strong> <br>

&emsp;&emsp;用于录入照片，根据提示输入姓名(支持中文)，然后拍照。随后加载照片，定位人脸，编码人脸。</p>

<blockquote>
  <p>注意： <br>
  &emsp;&emsp;"正在编码第1张照片..." <br>
  &emsp;&emsp;"*第1张照片已编码完成" <br>
  只有出现“第n张照片已编码完成",才算在第n张照片中找到人脸并编码
  否则请重新拍照，直至提示编码完成 <br>
  在face_recognition.face_locations()中加上参数model='cnn'会显著提高准确率，但需要开启GPU加速  </p>
</blockquote>
 <br/>
 <br/>
<p><strong>2.&ensp;<a href="https://github.com/fishvi/face_recognition/blob/master/face.py">face.py</a></strong> <br>

&emsp;&emsp;用于进行人脸识别，找到照片中的人脸并显示对应的姓名，姓名为录入时所输入的姓名，识别到未录入的人脸会显示“未识别”。</p>
&emsp;&emsp;同理，在face_recognition.face_locations()中加上参数model='cnn'会显著提高准确率，但需要开启GPU加速</p>
 <br/>
 <br/>
<p><strong>3.&ensp;images</strong></p>

<p>&emsp;&emsp;该文件夹用于存储照片，照片命名即为人脸名字。</p>
 <br/>
 <br/>
 <p><strong>4.&ensp;face_names.pkl</strong></p>
 
&emsp;&emsp;录入照片时生成的一个文件，用于存储人脸姓名。</p>
 <br/>
 <br/>
  <p><strong>5.&ensp;face_encodings.pkl</strong></p>
  
&emsp;&emsp;录入照片时生成的一个文件，用于存储人脸编码。</p>
