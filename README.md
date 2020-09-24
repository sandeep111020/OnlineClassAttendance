# OnlineClassAttendance
INTRODUCTION:
     This is an attendance filling project in online clases.In this project we can note the attendance of the students who are appearing for the online classes by face recognization system.
It will recognize all the students faces in each class and note down their attendance in a csv file format.

WORKING:
In this project we have 3 parts of codes.
1.register part
2.train part  
3.recognize part
REGISTER PART:
In the register part we register the details of the students such as roll number with face samples.in this program intitally we enter the roll number of the student. 
After that it reads the screen of the system and find the face which is shown in the scrren and take the samples(pictures).Each and every sample is in RGB format we convert that into GRAY images.
Those GRAY images are saved in a particular folder which is mentioned in code.It will take 30 samples for each and every student.After taking those samples the program will terminate automatically.
Incase if anyone want to terminate in middle just click esc buttton.

TRAIN PART:
In the training part we take the sample images and train them using our  model.In this model we read the samples which are saved at the registeration time.Here  we take each and every image and convert the image in array format using numpy libraries.
Here every image pixcels.every pixcel contains one value in between 0,255.Because the image is converted into gary format. thats why pixcel values are between 0-255.
In this traiing model we save the sample images and ids in an array formatted lists with id value and pixcel values in lists.Those lists are trained by a model in a praticular mannner.
Finally,it saves the trained data in yml format.(yml is a particular file which can able to save the data like arrays,lists,dicts,etc).

RECOGNIZE PART:
In the recogniging model we recognize the faces which are displayed in  the screen.After recogniging the faces it will note down the attendance in a csv format.
IN the model we click  the button to take attendance.Then it reads the screen and find the faces which are appear in the screen.Those finded face will be converted into GRAY image.
Then the pixcel values of the converted image will be compared with the pixcels values which are saved in the yml file.Here we predict id which is matched to that recognized face.
When it is matched with a id then it gives a confidence value it is error rate.if confidence less than 100 then recognized face is matched to a particular face in the dataset.
After it matches with the id it will note down the attendance in csv format.So it gives present to that rollnumbered person.If it cannot recognize the face it do noting.
so the atttendance will be noted for the person who will appear on the screen if anybody will no on there camera in the online class it note there absent for the class.
Attendance will noted with rrespective date.
  
