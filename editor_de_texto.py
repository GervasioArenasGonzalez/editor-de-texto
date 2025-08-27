import tkinter as tk
from tkinter import filedialog

#creo la ventana
ventana=tk.Tk()
ventana.geometry('1000x800+430+100')
ventana.title('Editor de texto')
ventana.config(background='#ddb892')

#creo el frame
cuadro=tk.Frame(ventana, bg='#a3b18a',relief='solid',height='30',borderwidth=0.3)
cuadro.pack(fill='x')

#creo el espacio de escritura
texto=tk.Text(ventana,bg='#e6ccb2',
              width=120,
              height=200,
              relief='solid',
              borderwidth=0.3
              )
texto.pack(pady=1,fill='x')

#creo la funcion para abrir un archivo
def abrir_archivo():
    archivo=filedialog.askopenfilename(title='Selecciona un archivo de texto')
    if archivo=='':
        return
    with open(archivo,'r')as file:
        contenido=file.read()
        texto.delete('1.0',tk.END)
        texto.insert('1.0',contenido)

#creo la funcion para guardar archivo
def guardar_archivo():
    archivo=filedialog.asksaveasfilename(title='Selecciona donde guardar',
                                         defaultextension='.txt',
                                         filetypes=[('Archivo de texto','*.txt'),('otro','*.*')])
    if archivo=='':
        return
    with open(archivo,'w')as file:
        contenido=texto.get('1.0','end-1c')
        file.write(contenido)

#creo los botones
abrir=tk.Button(cuadro,
                text='Abrir archivo'
                ,font=('Calibri',12,'normal')
                ,command=abrir_archivo,
                bg='#adb5bd',
                width=13,
                borderwidth=1)

abrir.grid(row=0,column=0)

guardar=tk.Button(cuadro,
                  text='Guardar archivo'
                  ,font=('Calibri',12,'normal')
                  ,command=guardar_archivo,
                  bg='#adb5bd',
                  width=13,
                  borderwidth=1)

guardar.grid(row=0,column=1)


ventana.mainloop()