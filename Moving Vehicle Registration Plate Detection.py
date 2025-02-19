import matplotlib.pyplot as plt
import keras_ocr
import mysql.connector
mydb = mysql.connector.connect(host="127.0.0.1",user="root",password="password",database="License")
mycursor = mydb.cursor(dictionary=True)
ocr_keras = keras_ocr.pipeline.Pipeline()
a=input("Enter image name (1 to 4):")
d = None
if a=="1":
    img_ocr = [keras_ocr.tools.read(img_ocr) for img_ocr in ['test4.jpg','test4.jpg',]]
elif a=="2":
    img_ocr = [keras_ocr.tools.read(img_ocr) for img_ocr in ['test3.jpg','test3.jpg',]]
elif a=="3":
    img_ocr = [keras_ocr.tools.read(img_ocr) for img_ocr in ['test2.jpg','test2.jpg',]]
elif a=="4":
    img_ocr = [keras_ocr.tools.read(img_ocr) for img_ocr in ['test5.jpg','test5.jpg',]]
predict = ocr_keras.recognize(img_ocr)
fig, axs = plt.subplots(nrows=len(img_ocr), figsize=(10, 20))
for ax, image, predictions in zip(axs, img_ocr, predict):
   		 keras_ocr.tools.drawAnnotations(image=image,predictions=predictions,ax=ax)							
img = predict [1]
for keras_text, box in img:
    x = keras_text.upper()
    if len(x)==10:
       d = x
b = "SELECT * FROM license.license WHERE License_Plate LIKE '%{}%'".format(d)
c = mycursor.execute(b)
mycursor.execute(c)
for c in mycursor:
    print(c)
