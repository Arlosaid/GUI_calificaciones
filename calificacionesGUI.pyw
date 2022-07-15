import tkinter as tk
from tkinter import messagebox


class Interface(tk.Frame):
    
    def __init__(self,window): 
        self.window = window
        self.inicio_sesion()
    
       
    def inicio_sesion(self):    
        self.miFrame = tk.Frame(self.window,bg="#002E2C")
        self.miFrame.pack()
        
        self.usuario = tk.Entry(self.miFrame)
        self.usuario.grid(row=1,column=1,padx=5,pady=20)
        self.usuario1 = tk.Label(self.miFrame,text="Usuario",bg="#002E2C",fg="#EFF1C5")
        self.usuario1.grid(row=1,column=0,padx=5,pady=20)

        self.passw = tk.Entry(self.miFrame,show="*")
        self.passw.grid(row=2,column=1,padx=5)
        self.pass1 = tk.Label(self.miFrame,text="Contraseña",bg="#002E2C",fg="#EFF1C5")
        self.pass1.grid(row=2,column=0,padx=5)

        self.boton = tk.Button(self.window,text="Enter",width=10,bg="#035E7B",fg="#EFF1C5",command=self.sesion_iniciada)
        self.boton.pack(pady=20)

    def menu(self):
        menu_principal = tk.Toplevel(root)
        menu_principal.title("Menu Principal")
        menu_principal.geometry("500x300+700+300")
        tk.Label(menu_principal, text="Menu Principal",
        font=("Agency FB", 14)).place(x=50, y=50) 
        root.withdraw()


    def sesion_iniciada(self):
        if self.usuario.get() == "admin" and self.passw.get() == "12345":
            self.menu()
        else:
            messagebox.showwarning("Error de inicio de sesión","Usuario o contraseña incorrectos") 


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Iniciar sesión")
    root.iconbitmap("C:\\Users\\adroa\\Desktop\\programa_calificaciones\\img\\calif.ico")
    root.geometry("300x180+800+300")
    root.config(bg="#002E2C")
    frame = Interface(root)
    root.mainloop()

