from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk, Image
from stegano import exifHeader as stg
from tkinter import messagebox

def encode():
    main.destroy()
    enc=Tk()
    enc.title("Encode")
    enc.geometry("500x400+300+150")

    label1=Label(text="Secret message")
    label1.place(relx=0.1,rely=0.1,height=20,width=100)

    entry=Entry()
    entry.place(relx=0.4,rely=0.1)

    label2=Label(text="File")
    label2.place(relx=0.1,rely=0.2,height=20,width=100)

    entrySave=Entry()
    entrySave.place(relx=0.4,rely=0.2)

    def openFile():
        global fileOpen
        fileOpen= StringVar()
        fileOpen= askopenfilename(initialdir="/Desktop", title="select file", filetypes=(("jpeg files","*jpg"),("all files","*.*")))
        label3=Label(text=fileOpen)
        label3.place(relx=0.3,rely=0.3)

    def encodee():
        response= messagebox.askyesno("pop up","do you want to encode?")
        if response==1:
            stg.hide(fileOpen,entrySave.get()+'.jpg',entry.get())
            messagebox.showinfo("pop up", "message successfully encoded")

        else:
            messagebox.showwarning("pop up ", "Unsuccessful")


    buttonSelect=Button(text="Select File", command=openFile)
    buttonSelect.place(relx=0.1,rely=0.3)

    buttonEncode=Button(text="Encode", command=encodee)
    buttonEncode.place(relx=0.5,rely=0.4)


def decode():
    main.destroy()
    dec=Tk()
    dec.title("Decode")
    dec.geometry("500x400+300+150")

    
    def openFile():
        global fileOpen
        fileOpen= StringVar()
        fileOpen= askopenfilename(initialdir="/Desktop", title="select file", filetypes=(("jpeg files","*jpg"),("all files","*.*")))

    def decodee():
        message=stg.reveal(fileOpen)
        label4=Label(text=message)
        label4.place(relx=0.3, rely=0.3)

     
    buttonSelect=Button(text="Select File", command=openFile)
    buttonSelect.place(relx=0.1,rely=0.3)

    buttonDecode=Button(text="Decode", command=decodee)
    buttonDecode.place(relx=0.5,rely=0.4)


main= Tk()
main.title("Image Steganography")
main.geometry("500x400+300+150")

encodeButton=Button(text="Encode", command=encode)
encodeButton.place(relx=0.3,rely=0.3,height=40, width=80)

decodeButton=Button(text="Decode",command=decode)
decodeButton.place(relx=0.5,rely=0.3,height=40, width=80)


main.mainloop()