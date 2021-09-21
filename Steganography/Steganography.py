from tkinter import *


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

    buttonSelect=Button(text="Select File")
    buttonSelect.place(relx=0.1,rely=0.3)

    buttonEncode=Button(text="Encode")
    buttonEncode.place(relx=0.5,rely=0.4)


def decode():
    main.destroy()
    dec=Tk()
    dec.title("Decode")
    dec.geometry("500x400+300+150")

    buttonSelect=Button(text="Select File")
    buttonSelect.place(relx=0.1,rely=0.3)

    buttonDecode=Button(text="Decode")
    buttonDecode.place(relx=0.5,rely=0.4)


main= Tk()
main.title("Image Steganography")
main.geometry("500x400+300+150")

encodeButton=Button(text="Encode", command=encode)
encodeButton.place(relx=0.3,rely=0.3,height=40, width=80)

decodeButton=Button(text="Decode",command=decode)
decodeButton.place(relx=0.5,rely=0.3,height=40, width=80)


main.mainloop()