import cv2
import numpy as np
from PIL import Image
import os
import tkinter as tk



root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

def train():
    path = 'dataset'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)
        return faceSamples, ids

    print("\n[INFO] training the faces.It will take few seconds....")

    faces, ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))

    recognizer.write('trainer/trainer.yml')

    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))




myButton = tk.Button(text='Update', command=train, bg='green', fg='white', font=10)
canvas1.create_window(150, 150, window=myButton)


root.mainloop()