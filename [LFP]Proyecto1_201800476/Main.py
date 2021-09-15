from Analizador import Analizador
from imageGen import imageGen
from tokenReport import tokenReport
from failsReport import failsReport
from tkinter import *
import tkinter as t
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import webbrowser

tokens = []
images = []
List_images = []
total_rows = 0
total_columns = 0
gCont = 0

class Table:
    def __init__(self, tab2):
        self.tab2 = tab2
        self.cont = 220
        self.recorrer()

    def recorrer(self):
        global images
        for image in images:
            imageName0 = str(image.titulo)
            imageName1 = imageName0.replace("\"", "")
            name = imageName1.lower()
            v = StringVar(self.tab2, value=str(name))
            Entry(self.tab2, textvariable = v, width=20, fg='black',font=('Arial',10,'bold')).place(x=20, y=self.cont)
            self.cont += 20

def menu():
    print("*********************************")
    print("*         Menú Principal        *")
    print("*********************************")
    print("* 1) Cargar archivo             *")
    print("* 2) Generar imagenes en HTML   *")
    print("* 3) Generar reporte de Tokens  *")
    print("* 4) Generar reporte de Errores *")
    print("* 5) Salir                      *")
    print("*********************************")

def graphicBrowser():
    win = Tk()
    win.geometry("1x1")
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select a File", filetypes=(("Pxla files", "*.pxla*"), ("All files", "*.*")))
    win.destroy()
    return filename

def read(path):
    try:
        with open(path, 'r') as f:
            format = path.find(".pxla")
            if format:
                alltext = f.readlines()
                print("\n")
                print("Carga de datos realizada correctamente")
                print("\n")
                return alltext

            else:
                print("\n")
                print("Formato de carga no coincide con .pxla, intentalo de nuevo")
                print("\n")
    except:
        print("\n")
        print("Ha ocurrido un error, intentalo de nuevo")
        print("\n")

def returnValue():
    path = graphicBrowser()
    returned = read(path)
    analized = Analizador(returned)
    global images
    images = analized.getImages()
    global total_rows
    total_rows = len(images)
    global total_columns
    total_columns = 1
    Table(tab2)
    imageGen(images)
    global tokens
    tokens = analized.getTokens()
    messagebox.showinfo("Información","Carga realizada correctamente")

def reportTokens():
    global tokens
    tokenReport(tokens)
    messagebox.showinfo("Información","Reporte generado")
    new = 1
    url = "C:/Users/alexi/Downloads/ALEXI/Cursos/17 Lenguajes Formales/Laboratorio/Proyectos/Proyecto 1/Proyecto_01/template/reportes/reporte_Tokens.html"
    webbrowser.open(url,new=new)

def reportError():
    global tokens
    failsReport(tokens)
    messagebox.showinfo("Información","Reporte generado")
    new = 1
    url = "C:/Users/alexi/Downloads/ALEXI/Cursos/17 Lenguajes Formales/Laboratorio/Proyectos/Proyecto 1/Proyecto_01/template/reportes/reporte_Errores.html"
    webbrowser.open(url,new=new)

def nextImage():
    global images
    global gCont
    imageName0 =  str(images[gCont].titulo)
    imageName1 = imageName0.replace("\"", "")
    name = imageName1.lower()
    global antImage
    global sigImage
    global List_images
    List_images = []
    try:
        image_no_1 = ImageTk.PhotoImage(Image.open("template/images/png/" + str(name) + "_normal.jpg"))
        List_images.append(image_no_1)
    except:
        pass
    try:
        image_no_2 = ImageTk.PhotoImage(Image.open("template/images/png/" + str(name) + "_mirrorx.jpg"))
        List_images.append(image_no_2)
    except:
        pass
    try:
        image_no_3 = ImageTk.PhotoImage(Image.open("template/images/png/" + str(name) + "_mirrory.jpg"))
        List_images.append(image_no_3)
    except:
        pass
    try:
        image_no_4 = ImageTk.PhotoImage(Image.open("template/images/png/" + str(name) + "_doublemirror.jpg"))
        List_images.append(image_no_4)
    except:
        pass

    antImage = Button(tab2, text=" ↑ ", command=anteImage).place(x=400, y=440)

    if gCont == len(images) - 1:
	    sigImage = Button(tab2, text=" ↓ ", state=DISABLED).place(x=400, y=480)

    gCont += 1

def anteImage():
    global images
    global gCont
    gCont -= 1
    imageName0 =  str(images[gCont].titulo)
    imageName1 = imageName0.replace("\"", "")
    name = imageName1.lower()
    global sigImage
    global antImage
    global List_images
    List_images = []
    try:
        image_no_1 = ImageTk.PhotoImage(Image.open("template/images/png/" + str(name) + "_normal.jpg"))
        List_images.append(image_no_1)
    except:
        pass
    try:
        image_no_2 = ImageTk.PhotoImage(Image.open("template/images/png/" + str(name) + "_mirrorx.jpg"))
        List_images.append(image_no_2)
    except:
        pass
    try:
        image_no_3 = ImageTk.PhotoImage(Image.open("template/images/png/" + str(name) + "_mirrory.jpg"))
        List_images.append(image_no_3)
    except:
        pass
    try:
        image_no_4 = ImageTk.PhotoImage(Image.open("template/images/png/" + str(name) + "_doublemirror.jpg"))
        List_images.append(image_no_4)
    except:
        pass

    sigImage = Button(tab2, text=" ↓ ", command=nextImage).place(x=400, y=480)

    if gCont == 0:
	    antImage = Button(tab2, text=" ↑ ", state=DISABLED).place(x=400, y=440)

def forward(img_no):
    global button_forward
    global button_back
    tab2.grid_forget()
    Label(tab2, image=List_images[img_no-1]).place(x=450, y=175)
    button_forward = Button(tab2, text="Siguiente", command=lambda: forward(img_no+1)).place(x=710, y=130)
    button_back = Button(tab2, text="Anterior", command=lambda: back(img_no-1)).place(x=650, y=130)
    if img_no ==4:
	    button_forward = Button(tab2, text="Siguiente", state=DISABLED).place(x=710, y=130)
    if img_no==1:
	    button_back = Button(tab2, text="Anterior", state=DISABLED).place(x=650, y=130)

def back(img_no):
    global button_forward
    global button_back
    tab2.grid_forget()
    Label(tab2, image=List_images[img_no-1]).place(x=450, y=175)
    button_forward = Button(tab2, text="Siguiente", command=lambda: forward(img_no+1)).place(x=710, y=130)
    button_back = Button(tab2, text="Anterior", command=lambda: back(img_no-1)).place(x=650, y=130)
    if img_no ==1:
	    button_back = Button(tab2, text="Anterior", state=DISABLED).place(x=650, y=130)

v = t.Tk()
v.geometry("800x600")
v.minsize(800, 600)
v.maxsize(800, 600)
v.title("Bitxelart")

tabControl = ttk.Notebook(v)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Cargar')
tabControl.add(tab2, text ='Analizar')
tabControl.add(tab3, text ='Reportes')
tabControl.pack(expand = 1, fill ="both")

#TAB1
t.Label(tab1, text="", width=200, height=36, bg = "#162742").place(x=0, y=0)
t.Label(tab1, text="BITXELART", fg="#fcba03", width=10, height=10, bg = "#162742", font = "Helvetica 32 bold italic").place(x=265, y=0)
t.Button(tab1, text="Cargar archivo", width=25, command = returnValue, font = "Arial 14").place(x=260, y=280)
t.Label(tab1, text = "", width=130, height=20, bg = "dark gray").place(x=0, y=550)
t.Label(tab1, text = "   201800476 - Proyecto 1 de Lenguajes formales y de programación", fg="black", bg = "dark gray").place(x=0, y=550)

#TAB2
t.Label(tab2, text="", width=200, height=36, bg = "#162742").place(x=0, y=0)
t.Label(tab2, text="Analizar", width=10, fg="#fcba03", bg = "#162742", font = "Helvetica 24 bold italic").place(x=600, y=30)
button_forward = Button(tab2, text="Siguiente", command=lambda: forward(1)).place(x=710, y=130)
button_back = Button(tab2, text="Anterior", command=lambda: back(1)).place(x=650, y=130)
sigImage = Button(tab2, text=" ↓ ", command=nextImage).place(x=400, y=480)
antImage = Button(tab2, text=" ↑ ", command=anteImage).place(x=400, y=440)
t.Label(tab2, text="Lista", width=10, fg="#fcba03", bg = "#162742", font = "Helvetica 12").place(x=-10, y=175)
t.Label(tab2, text="Filtros", width=10, fg="#fcba03", bg = "#162742", font = "Helvetica 12").place(x=660, y=100)
t.Label(tab2, text="Imágenes", width=10, fg="#fcba03", bg = "#162742", font = "Helvetica 12").place(x=290, y=460)
t.Label(tab2, text = "", width=20, height=19, bg = "white").place(x=20, y=220)
t.Label(tab2, text = "", width=130, height=20, bg = "dark gray").place(x=0, y=550)
t.Label(tab2, text = "   201800476 - Proyecto 1 de Lenguajes formales y de programación", fg="black", bg = "dark gray").place(x=0, y=550)

#TAB3
t.Label(tab3, text="", width=200, height=36, bg = "#162742").place(x=0, y=0)
t.Label(tab3, text="Reportes", width=10, fg="#fcba03", bg = "#162742", font = "Helvetica 24 bold italic").place(x=580, y=30)
t.Button(tab3, text="Tokens", width=15, command = reportTokens, font = "Arial 14").place(x=600, y=130)
t.Button(tab3, text="Errores", width=15, command = reportError, font = "Arial 14").place(x=600, y=180)
t.Label(tab3, text = "", width=130, height=20, bg = "dark gray").place(x=0, y=550)
t.Label(tab3, text = "   201800476 - Proyecto 1 de Lenguajes formales y de programación", fg="black", bg = "dark gray").place(x=0, y=550)

v.mainloop()

"""
Ejecucion = True
while Ejecucion:
    
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        name = graphicBrowser()
        returned = read(name)

    elif opcion == "2":
        analized = Analizador(returned)
        images = analized.getImages()
        imageGen(images)
        #imgkit.from_file('template/images/reporte_Pokeball.html', 'out.jpg')
        
    elif opcion == "3":
        tokens = analized.getTokens()
        tokenReport(tokens)
    
    elif opcion == "4":
        failsReport(tokens)

    elif opcion == "5":
        print("Has salido del programa")
        Ejecucion = False

    else:
        print("Intenta de nuevo")
"""
