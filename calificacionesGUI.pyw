import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Interface(tk.Frame):
    
   
 #-------------------------------------Interface inicio de sesion------------------------------------- 
    def __init__(self,window): 
        self.window = window
        self.inicio_sesion()
       
    def inicio_sesion(self):    
        self.miFrame = tk.Frame(self.window)
        self.miFrame.pack()
        self.miFrame.config(bg="#002E2C")

        style = ttk.Style()
        style.configure("BW.TLabel", foreground="white", background="#002E2C")
        
        self.usuario = ttk.Entry(self.miFrame)
        self.usuario.grid(row=1,column=1,padx=5,pady=20)
        self.usuario1 = ttk.Label(self.miFrame,text="Usuario",style="BW.TLabel")
        self.usuario1.grid(row=1,column=0,padx=5,pady=20,)
        

        self.passw = ttk.Entry(self.miFrame,show="*")
        self.passw.grid(row=2,column=1,padx=5)
        self.pass1 = ttk.Label(self.miFrame,text="Contraseña",style="BW.TLabel")
        self.pass1.grid(row=2,column=0,padx=5)

        self.boton = ttk.Button(self.window,text="Enter",width=10,cursor ="hand2",command=self.sesion_iniciada)
        self.boton.pack(pady=20)

    
 #-------------------------------------Interface menu-------------------------------------
    def menu(self):
        root.withdraw()
        menu_principal = tk.Toplevel(self.miFrame)
        menu_principal.title("Menu Principal")
        menu_principal.geometry("500x350+700+300")
        menu_principal.iconbitmap("C:\\Users\\adroa\\Desktop\\programa_calificaciones\\img\\calif.ico")
        menu_principal.config(bg="#002E2C")
        menu_principal.resizable(False,False)
        
        self.registro = ttk.Button(menu_principal,text="Registro alumnos",width=30,cursor ="hand2",
        command=self.registrar).place(x=150, y=50)
       
        self.listar = ttk.Button(menu_principal,text="Registro alumnos",width=30,cursor ="hand2",
        command=self.registrar).place(x=150, y=100)
        
        self.asignar_materias = ttk.Button(menu_principal,text="Registro alumnos",width=30,cursor ="hand2",
        command=self.registrar).place(x=150, y=150)
        
        self.asignar_calificaciones = ttk.Button(menu_principal,text="Registro alumnos",width=30,cursor ="hand2",
        command=self.registrar).place(x=150, y=200)

        self.calif_final = ttk.Button(menu_principal,text="Registro alumnos",width=30,cursor ="hand2",
        command=self.registrar).place(x=150, y=250)

#-------------------------------------Interface registro alumnos-------------------------------------            
    def registrar(self):
        
        registro = tk.Toplevel(self.miFrame)
        registro.title("Menu Principal")
        registro.geometry("500x300+700+300")
        registro.iconbitmap("C:\\Users\\adroa\\Desktop\\programa_calificaciones\\img\\calif.ico")
        registro.config(bg="#002E2C")

 #-------------------------------------Inicio de sesion-------------------------------------                 
    def sesion_iniciada(self):
        if self.usuario.get() == "admin" and self.passw.get() == "12345":
            self.menu()
        else:
            messagebox.showwarning("Error de inicio de sesión","Usuario o contraseña incorrectos.") 

#-------------------------------------Interface root-------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Iniciar sesión")
    root.iconbitmap("C:\\Users\\adroa\\Desktop\\programa_calificaciones\\img\\calif.ico")
    root.geometry("300x150+800+300")
    root.config(bg="#002E2C")
    frame = Interface(root)
    root.mainloop()

