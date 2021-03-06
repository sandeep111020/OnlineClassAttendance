import cv2
import numpy as np
import os
import pyautogui
import tkinter as tk
import pandas as pd
from datetime import date

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

def rec():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    df = pd.read_csv("result.csv")
    b = date.today()
    #pd.date_range('2020-08-14', periods=1, freq='12H')
    df[b] = "absent"


    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 0

    names = ['none', 'satish', 'surendra', 'lohitha', 'anu']

    while True:

        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'screenshotf1.jpg')
        img = cv2.imread('screenshotf1.jpg')
        #img = cv2.flip(img, 1)  # Flip vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,

        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # If confidence is less them 100 ==> "0" : perfect match
            if (confidence < 100):
                #if id == 1 or id == 2:
                print(id)
                df.at[id - 1, b] = "present"
                # else:
                # df.at[id, b] = "present"

                df.to_csv('result.csv', index=False)



                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))




            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))


            cv2.putText(
                img,
                str(id),
                (x + 5, y - 5),
                font,
                1,
                (255, 255, 255),
                2
            )
            cv2.putText(
                img,
                str(confidence),
                (x + 5, y + h - 5),
                font,
                1,
                (255, 255, 0),
                1
            )


        cv2.imwrite('screenshotf2.jpg',img)





        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break


    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cv2.destroyAllWindows()


def endProgam():
    # top.quit()
    root.destroy()


myButton = tk.Button(text='Take Attendance', command=rec, bg='green', fg='white', font=10)
B = tk.Button( text = "Terminate", command = endProgam)
canvas1.create_window(150, 150, window=myButton)
canvas1.create_window(250, 250, window=B)

root.mainloop()