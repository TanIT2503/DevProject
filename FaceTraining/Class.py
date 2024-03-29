import os
from tkinter import * 
from tkinter import font
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1195x750+0+0")
        self.root.title("Face Recognitiom System")
        self.root.option_add("*tearOff", False)
        

        #Bg image
        img3 = Image.open(r"assets/img/bg_img.png")
        img3 = img3.resize((1195,765),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image = self.photoimg3)
        bg_img.place(x = 0,y = 0, width = 1195, height = 765)
        
        #student buttom
        img4 = Image.open(r"assets/img/student.png")
        img4 = img4.resize((180,180),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bt1 = ttk.Label( image = self.photoimg4, cursor= "hand2")
        bt1.place(x = 95, y = 200, width = 180, height = 180)

        b1_1 = ttk.Button( text = "Students details",command = self.student_details , style="ToggleButton", cursor= "hand2")
        b1_1.place(x = 95, y = 350, width = 180, height = 40)



        #Detect face buttom
        img5 = Image.open(r"assets/img/FaceDetect.png")
        img5 = img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        bt2 = ttk.Label(image = self.photoimg5, cursor= "hand2")
        bt2.place(x = 370, y = 200, width = 180, height = 180)

        b1_2 = ttk.Button(text = "Face Detector", command = self.face_data, style="ToggleButton", cursor= "hand2")
        b1_2.place(x = 370, y = 350, width = 180, height = 40)



        #Attendance face buttom
        img6 = Image.open(r"assets/img/attendance.png")
        img6 = img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        bt3 = ttk.Label(image = self.photoimg6, cursor= "hand2")
        bt3.place(x = 645, y = 200, width = 180, height = 180)

        b1_3 = ttk.Button(text = "Attendance", command = self.attendance_data, style="ToggleButton", cursor= "hand2")
        b1_3.place(x = 645, y = 350, width = 180, height = 40)


        #Subject buttom
        img7 = Image.open(r"assets/img/subjects.png")
        img7 = img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        bt4 = ttk.Label(image = self.photoimg7, cursor= "hand2")
        bt4.place(x = 920, y = 200, width = 180, height = 180)

        b1_4 = ttk.Button(text = "Subjects", style="ToggleButton", cursor= "hand2")
        b1_4.place(x = 920, y = 350, width = 180, height = 40)


        #Training buttom
        img8 = Image.open(r"assets/img/training.png")
        img8 = img8.resize((180,180),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        bt4 = ttk.Label(image = self.photoimg8, cursor= "hand2")
        bt4.place(x = 95, y = 450, width = 180, height = 180)

        b2_1 = ttk.Button(text = "Training",command = self.train_data, style="ToggleButton", cursor= "hand2")
        b2_1.place(x = 95, y = 600, width = 180, height = 40)

                #Photo buttom
        img9 = Image.open(r"assets/img/photo.png")
        img9 = img9.resize((180,180),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        bt4 = ttk.Label(image = self.photoimg9, cursor= "hand2")
        bt4.place(x = 370, y = 450, width = 180, height = 180)

        b2_2 = ttk.Button(text = "Photo", style="ToggleButton", cursor= "hand2", command = self.open_img)
        b2_2.place(x = 370, y = 600, width = 180, height = 40)

         #Lesson buttom
        img10 = Image.open(r"assets/img/subjects.png")
        img10 = img10.resize((180,180),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        bt4 = ttk.Label(image = self.photoimg10, cursor= "hand2")
        bt4.place(x = 645, y = 450, width = 180, height = 180)

        b2_3 = ttk.Button(text = "Subjects", style="ToggleButton", cursor= "hand2")
        b2_3.place(x = 645, y = 600, width = 180, height = 40)

                #Training buttom
        img11 = Image.open(r"assets/img/photo.png")
        img11 = img11.resize((180,180),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        bt4 = ttk.Label(image = self.photoimg11, cursor= "hand2")
        bt4.place(x = 920, y = 450, width = 180, height = 180)

        b2_4 = ttk.Button(text = "Photo", style="ToggleButton", cursor= "hand2")
        b2_4.place(x = 920, y = 600, width = 180, height = 40)

#================...========================
    def open_img(self):
        os.startfile("data")



    def student_details(self):
        self.new_windows = Toplevel(self.root)
        self.app = Student(self.new_windows)
    
    def train_data(self):
                self.new_windows = Toplevel(self.root)
                self.app = Train(self.new_windows)




    def face_data(self):
                self.new_windows = Toplevel(self.root)
                self.app = Face_Recognition(self.new_windows)

    def attendance_data(self):
                self.new_windows = Toplevel(self.root)
                self.app = Attendance(self.new_windows)


    




if __name__ == "__main__":
        root =Tk()
        root.option_add("*tearOff", False)

        # Make the app responsive
        root.columnconfigure(index=0, weight=1)
        root.columnconfigure(index=1, weight=1)
        root.columnconfigure(index=2, weight=1)
        root.rowconfigure(index=0, weight=1)
        root.rowconfigure(index=1, weight=1)
        root.rowconfigure(index=2, weight=1)

        # Create a style
        style = ttk.Style(root)



# Import the tcl file
        root.tk.call("source", "Azure-ttk-theme/azure-dark.tcl")

# Set the theme with the theme_use method
        style.theme_use("azure-dark")
        obj = Face_Recognition_System(root)
        root.mainloop()