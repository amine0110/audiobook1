from tkinter import *
from tkinter import filedialog
import pyttsx3
import PyPDF2 
from PIL import Image
from PIL import ImageTk

app = Tk()
app.geometry('300x400')
app.title('Audio Book')
app.configure(bg='#ffdab9')


def talk():
    my_path = path
    pageL = pagebox.get()
    if path and pageL:
        book = open(path, 'rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        speaker = pyttsx3.init()
        page = pdfreader.getPage(int(pageL))
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()

 

def click():
    global path
    path = None
    path = filedialog.askopenfilename()


image1 = Image.open("AudioBook.png")
image1 = image1.resize((70, 70), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)

label1 = Label(app, image=test, bg='#ffdab9')
label1.pack()

text = Label(app, text='Let listen to the book!', font='agencyFB 20',bg='#ffdab9')
text.pack()

page = Label(app, text='Please enter the page number', bg='#ffdab9')
page.pack(pady=(50,0))

pagebox = Entry(app, bg='#ffdab9')
pagebox.pack()

button = Button(app, text='Open', width=20,bg='#ffdab9', command=click)
button.pack(pady=(20,0))

button2 = Button(app, text='Talk', width=20,bg='#ffdab9', command=talk)
button2.pack(pady=(20,0))


app.mainloop()