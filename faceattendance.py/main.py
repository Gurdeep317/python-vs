from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

    # 1st image
        img=Image.open(r"C:\Users\lenovo\OneDrive\attendanceproject pictures.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
    
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

    # 2nd image
        img1=Image.open(r"C:\Users\lenovo\OneDrive\attendanceproject pictures.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

    # 3rd image
        img2=Image.open(r"C:\Users\lenovo\OneDrive\attendanceproject pictures.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

    # background image
        img3=Image.open(r"C:\Users\lenovo\OneDrive\attendanceproject pictures.jpg")
        img3=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=1000,y=0,width=550,height=130)

    
    









if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()