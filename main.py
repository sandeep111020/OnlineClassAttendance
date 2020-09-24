
import cv2
import pyautogui
import tkinter as tk



root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

e1 = tk.Entry(root)
canvas1.create_window(150, 100, window=e1)



def read():
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    face_id = e1.get()
    #input('\n enter user id end press ==>  ')
    print("\n [INFO] Initializing face capture. Look the camera and wait ...")

    count = 0
    while True:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'screenshotf1.png')
        img = cv2.imread('screenshotf1.png')
        # img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1
            cv2.imwrite("dataset/UserNumber." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
            # cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff
        if k == 27:  # press 'ESC' to quit
            break
        elif count >= 20:
            break
    print("\n [INFO] Exiting Program and cleanup stuff")
    cv2.destroyAllWindows()


myButton = tk.Button(text='Show The Face', command=read, bg='green', fg='white', font=10)
canvas1.create_window(150, 150, window=myButton)


root.mainloop()

