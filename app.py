from statistics import mode
import tkinter as tk
from turtle import title
import subprocess
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename


root =tk.Tk()

canvas = tk.Canvas(root,width=600,height=300)
canvas.grid(columnspan=3, rowspan=3)


logo= Image.open('Finallogo.png')
logo = logo.resize((300,200),Image.ANTIALIAS)
logo= ImageTk.PhotoImage(logo)
logo_label =tk.Label(image=logo)
logo_label.image= logo
logo_label.grid(column=1,row=0,  pady=55)


instructions = tk.Label(root, text="Check our PDF programs from the folder named Programs to view their content in the browser.", font='Raleway',pady=25)
instructions.grid(columnspan=3, column=0, row=1)

def openFile():
  browse_text.set('Loading...')
  file_location= askopenfilename(initialdir="/Programs",parent=root,  title='Choose a file',filetype=[('Pdf file', '*.pdf')])
  file = open(file_location,'r')
  if file_location:
    path='file'
    subprocess.Popen([file_location],shell=True)
    
     
browse_text= tk.StringVar()
browse_btn=tk.Button(root,textvariable=browse_text, command=lambda:openFile(), font='Raleway', bg='#05DBF2',fg='#0788D9',height=2, width=15, )
browse_text.set('Browse')
browse_btn.grid(column=1, )




canvas = tk.Canvas(root,width=600,height=50)
canvas.grid(columnspan=3)


root.mainloop()


