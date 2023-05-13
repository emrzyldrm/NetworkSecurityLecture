from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import main

# Tkinter penceresi oluştur.
window = Tk()
window.title("Image Selector")

# Pencere boyutu
window.geometry("400x400")

# Yazı bölmesi
label = Label(window, text="Please select an image")
label.pack(pady=30)
labelOutput = Label(window, text="")

# Görsel seçmek için buton. Burada seçilen görsel bir dosya yolu seçicek ve main dosyasını çalıştıracak.
def select_image():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    path = pathConfig(file_path)
    img.thumbnail((40, 40))
    img_tk = ImageTk.PhotoImage(img)
    panel.configure(image=img_tk)
    panel.image = img_tk
    textOutput = main.main(path)
    labelOutput.config(text=textOutput)

def pathConfig(file_path):
    newPath = file_path.split('/')
    return newPath[-1]

button = Button(window, text="Select Image", command=select_image)
button.pack(pady=30)

labelOutput.pack(pady= 30)

# Add panel to display image
panel = Label(window)
panel.pack(pady=0)

window.mainloop()