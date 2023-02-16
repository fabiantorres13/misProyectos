import tkinter as tk
from tkinter import Canvas, ttk


ventana = tk.Tk()
ventana.config(width=700, height=600, bg='#F0EEED')
ventana.title("Chutter")
ventana.resizable(width=False, height=False)


labelAdios = ttk.Label(ventana, text="De FABIÁN con \U00002764 para tu", font= 'Terminal').place(x=180,y=550)


canvasLogo = Canvas(width=400, height=180, bg='black').place(x=150,y=50)




ventana.mainloop()