
from tkinter import *
from ctypes import windll
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import encode
import decode

# Defining global variables to track if two child windows -
# for encoding, decoding and help window are in opened or closed state
encode_opened = False
decode_opened = False
# Defining a variable to track if the program is running on Windows OS or not
windows = True
# Defining an variable file_path to store the path of the selected image
file_path = ""


##########################################################
# ENCODE WINDOW COMPONENTS
##########################################################
# function to open a new window for encoding functionality
def open_encode_window():
    # referencing global variable to reflect modification globally
    global encode_opened
    # checking if the window is already open
    if not encode_opened:
        encode_window = Toplevel(window)
        encode_window.title("ImgStego - Encode")
        encode_window.geometry('800x500')
        encode_window.resizable(False, False)
        encode_window.transient(window)
        if windows:
            windll.shcore.SetProcessDpiAwareness(1)

        # Label to display image after the image is selected from the file window
        raw_image_label = Label(encode_window, text="Select Raw Image", height=20, width=50, relief="solid",
                                bg="#FFFFFF")
        raw_image_label.place(x=20, y=20)

        # Label to indicate text area to enter the text to be encoded
        text_to_encode_label = Label(encode_window, text="Text to Encode")
        text_to_encode_label.config(font=("Open Sans", 12))
        text_to_encode_label.place(x=400, y=20)

        # Textarea to enter the text to be encoded
        text_to_encode = Text(encode_window, height=7, width=34)
        text_to_encode.config(relief="solid", font=("Open Sans", 15))
        text_to_encode.place(x=400, y=51)

        # Label to indicate the text field to enter the password for encoding
        pass_to_encode_label = Label(encode_window, text="Password")
        pass_to_encode_label.config(font=("Open Sans", 12))
        pass_to_encode_label.place(x=400, y=262)

        # Text field to enter the password for encoding
        pass_to_encode = Entry(encode_window, width=34)
        pass_to_encode.config(relief="solid", font=("Open Sans", 15), show="*")
        pass_to_encode.place(x=400, y=293)

        # Button to browse for raw image to encode the text inside it
        # Calls a function browse_image() with the label to display the image as argument
        browse_image_btn = Button(encode_window, text="Browse Raw Image", width=29, cursor="hand2",
                                  command=lambda: browse_image(raw_image_label))
        browse_image_btn.config(font=("Open Sans", 15), bg="#015952", fg="white", borderwidth=0)
        browse_image_btn.place(x=20, y=350)

        # Button to encode the text inside the image and validate password field
        # Calls a function on separate encode class
        encode_image_btn = Button(encode_window, text="Encode", width=15, cursor="hand2",
                                  command=lambda: encode_image(file_path, pass_to_encode.get(),
                                                               text_to_encode.get("1.0", END)))
        encode_image_btn.config(font=("Open Sans", 15), bg="#db3504", fg="white", borderwidth=0)
        encode_image_btn.place(x=592, y=420)

        # setting the value of global tracking variable to true
        encode_opened = True
        # assigning a handler to define the actions when the window is tried to close
        encode_window.protocol("WM_DELETE_WINDOW", lambda: close_encode_window(encode_window))


# method to save the encoded image file on a chosen destination
def save_image(stego_image):
    # getting the path of the destination to save
    save_path = filedialog.asksaveasfile(initialfile="ImgStego.png", mode="wb", defaultextension=".png",
                                         filetypes=(("Image File", "*.png"), ("All Files", "*.*")))
    # saving the image
    stego_image.save(save_path)


# Function to call encode class to handle encoding
# takes path of the raw image, password and text to be encoded as arguments
def encode_image(image_path, password, text_to_encode):
    # calling Encode class constructor
    encode_action = encode.Encode(image_path, password, text_to_encode)
    # calling method inside Encode class to check if all the values are valid
    msg = encode_action.are_values_valid()

    if not msg[1]:
        messagebox.showerror("Error Encoding", msg[0])
    else:
        stego_image = encode_action.encode_into_image()
        # checking the returned status message from the function above
        if stego_image[1]:
            # calling save_image() function to show the save image dialog and save the output image
            if save_image(stego_image[0]) is None:
                messagebox.showinfo("Image Saved", "Encode operation was successful.")
        else:
            # Showing error if any error occurs while encoding the image
            messagebox.showerror("Error Encoding", stego_image[0])


##########################################################
# DECODE WINDOW COMPONENTS
##########################################################
# function to open a new window for decoding functionality
def open_decode_window():
    # referencing global variable to reflect modification globally
    global decode_opened
    # checking if the window is already open
    if not decode_opened:
        # Initializing new child window for decoding functions
        decode_window = Toplevel(window)
        decode_window.title("ImgStego - Decode")
        decode_window.geometry('800x500')
        decode_window.resizable(False, False)
        decode_window.transient(window)
        if windows:
            windll.shcore.SetProcessDpiAwareness(1)

        # Label to display image after the image is selected from the file window
        stego_image_label = Label(decode_window, text="Select Stego Image", height=20, width=50, relief="solid",
                                  bg="#FFFFFF")
        stego_image_label.place(x=20, y=20)

        # Label to indicate textarea to display decoded text
        text_to_decode_label = Label(decode_window, text="Decoded Text")
        text_to_decode_label.config(font=("Open Sans", 12))
        text_to_decode_label.place(x=400, y=20)

        # Textarea to display decoded text
        text_to_decode = Text(decode_window, height=7, width=34)
        text_to_decode.config(relief="solid", font=("Open Sans", 15), state=DISABLED)
        text_to_decode.place(x=400, y=51)

        # Label to indicate password field to decode the image
        pass_to_decode_label = Label(decode_window, text="Password")
        pass_to_decode_label.config(font=("Open Sans", 12))
        pass_to_decode_label.place(x=400, y=262)

        # Text field to enter password to decode the image
        pass_to_decode = Entry(decode_window, width=34)
        pass_to_decode.config(relief="solid", font=("Open Sans", 15), show="*")
        pass_to_decode.place(x=400, y=293)

        # Button to browse for encoded image or stego image to decode
        # Calls a function browse_image() with the label to display the image as argument
        browse_stego_btn = Button(decode_window, text="Browse Stego Image", width=29, cursor="hand2",
                                  command=lambda: browse_image(stego_image_label))
        browse_stego_btn.config(font=("Open Sans", 15), bg="#db3504", fg="white", borderwidth=0)
        browse_stego_btn.place(x=20, y=350)

        # Button to decode the image and validate password field
        # Calls a function on separate decode class
        decode_stego_btn = Button(decode_window, text="Decode", width=15, cursor="hand2",
                                  command=lambda: decode_image(file_path, pass_to_decode.get(), text_to_decode))
        decode_stego_btn.config(font=("Open Sans", 15), bg="#015952", fg="white", borderwidth=0)
        decode_stego_btn.place(x=592, y=420)

        # Setting the status of decode_window as true to denote that decode window is open
        decode_opened = True
        # assigning a handler to define the actions when the window is tried to close
        decode_window.protocol("WM_DELETE_WINDOW", lambda: close_decode_window(decode_window))


# Function to call decode class to handle decoding
# takes path of the stego image, password and text field to show decoded text as arguments
def decode_image(image_path, password, text_field):
    # calling Decode class constructor
    decode_action = decode.Decode(image_path, password)
    msg = decode_action.are_values_valid()

    if not msg[1]:
        messagebox.showerror("Error Decoding", msg[0])
    else:
        decoded_text = decode_action.decode_from_image()
        # checking status of the message and if message extraction is successful, displaying on the window
        if decoded_text[1]:
            # enabling the disabled text widget on the decode window
            text_field.config(state=NORMAL)
            # clearing the text field before inserting the decoded text
            text_field.delete(1.0, END)
            # inserting the decoded text
            text_field.insert(1.0, decoded_text[0])
            # re-disabling the widget to prevent accidental insertion
            text_field.config(state=DISABLED)
            # showing success message
            messagebox.showinfo("Text Decoded", "Decode operation was successful.")
        else:
            # showing error message if any error occurs during decoding process
            messagebox.showerror("Error Decoding", decoded_text[0])


##########################################################
# COMMON COMPONENTS
##########################################################
# function to open file window to browse image to encode and decode
def browse_image(image_frame):
    # Referencing global variable file_path to store the path of the file
    global file_path
    # Opening the file dialog to allow user to choose image files
    file_path = filedialog.askopenfilename(title="Choose an Image",
                                           filetypes=(("Image Files", "*.png"), ("All Files", "*.*")))
    # Getting the path of the selected image
    selected_image = Image.open(file_path)
    # Setting the maximum width of the image to display it on the window
    max_width = 350
    # Calculating the aspect ratio for proportional image resizing
    aspect_ratio = max_width / float(selected_image.size[0])
    # Calculating the proportional height for the defined width
    max_height = int((float(selected_image.size[1]) * float(aspect_ratio)))
    # Resizing the image with calculated height and width
    selected_image = selected_image.resize((max_width, max_height), Image.ANTIALIAS)
    # converting the selected image format to tkinter compatible image
    selected_image = ImageTk.PhotoImage(selected_image)
    # Setting the label configurations to display the image on the label
    image_frame.config(image=selected_image, height=304, width=354)
    image_frame.image = selected_image


##########################################################
# MAIN WINDOW COMPONENTS
##########################################################
# Function to define actions to be performed when encoding window is tried to closed
def close_encode_window(encode_window):
    # referencing global variable to reflect modification globally
    global encode_opened
    # Destroying the passed child encoding window
    encode_window.destroy()
    # Setting the value of global tracking variable to false to denote that window is closed
    encode_opened = False


# Function to define actions to be performed when decoding window is tried to closed
def close_decode_window(decode_window):
    # referencing global variable to reflect modification globally
    global decode_opened
    # Destroying the passed child encoding window
    decode_window.destroy()
    # Setting the value of global tracking variable to false to denote that window is closed
    decode_opened = False

# Function to define actions to be performed when main window is tried to closed
def close_window():
    window.destroy()

# Initializing tkinter window
window = Tk()
window.title("ImgStego")
window.geometry('800x500')
window.resizable(False, False)
if windows:
    windll.shcore.SetProcessDpiAwareness(1)

logo = Image.open("../Steganography/images/logo.png")
logo = logo.resize((180, 180), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
window.iconphoto(True, logo)

# Initializing label to display image on the window
image_label = Label(window, image=logo, height=180, width=180)
image_label.pack(pady=20)

# Initializing label to display title label on the window
title_label = Label(window, text="ImgStego")
title_label.pack()
title_label.config(font=("Open Sans", 32))

# Initializing button for encode action
encode_btn = Button(window, text="Encode", height=2, width=15, bg="#db3504", fg="white", cursor="hand2", borderwidth=0,
                    command=open_encode_window)
encode_btn.config(font=("Open Sans", 15, "bold"))
encode_btn.pack(side=LEFT, padx=50)

# Initializing button for the decode button
decode_btn = Button(window, text="Decode", height=2, width=15, bg="#015952", fg="white", cursor="hand2", borderwidth=0,
                    command=open_decode_window)
decode_btn.config(font=("Open Sans", 15, "bold"))
decode_btn.pack(side=RIGHT, padx=50)

# Initializing button for exit action
exit_btn = Button(window, text="Exit", height=2, width=15, bg="#000000", fg="white", cursor="hand2", borderwidth=0,
                  command=close_window)
# Setting font configurations for the button - font family, font size and font weight
exit_btn.config(font=("Open Sans", 15, "bold"))
# Packing the button on the window
exit_btn.pack(side=BOTTOM, pady=80)



window.mainloop()
