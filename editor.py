from tkinter import *
from tkinter import filedialog
from io import open

ruta = ""  # La utilizaremos para almacenar la ruta de un fichero


def nuevo():
    # las varibles de aqui de adminstran internamente por tkinter asi que debemos ponerle como global
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, END)
    root.title(ruta + " - Mi editor")


def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = filedialog.askopenfilename(initialdir=".",
                                      filetype=(("Fichero de texto", "*.txt"),),
                                      title="Abrir un fichero de texto")
    if ruta != "":
        fichero = open(ruta, "r")
        contenido = fichero.read()
        texto.delete(1.0, END)
        texto.insert("insert", contenido)
        fichero.close()
        root.title(ruta + " - Mi editor")


def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El fichero se ha guardado correctamente")
    else:
        guardar_como()


def guardar_como():
    global ruta
    mensaje.set("Gudardo como")
    fichero = filedialog.asksaveasfilename(title="Guardar fichero",

                                           defaultextension=".txt")
    if fichero is not None:
        ruta = str(fichero)
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El fichero se ha guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""

# configurar la raiz
root = Tk()
root.title("editor")

# menu superior
menubar = Menu(root)
# Tearoff desactiva el peuqeño menu por defecto.
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

# Caja de texto central

texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

# Monitor inferior
mensaje = StringVar()

mensaje.set("Bienvenido a tu editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

root.config(menu=menubar)
# Finalmente ejecutamos el bucle
root.mainloop()
