from icecream import ic
from tkinter import filedialog, messagebox as mb
from app.file_class import File
import tkinter as tk
import re, os
ic.disable()

class user_interface:
    
    def __init__(self):
        # Variables del programa
        self._file_path = ''
        self._positions = []
        self._name_file = ''

        # Crear la ventana principal
        self.window = tk.Tk()
        self.window.title("Separador de archivos")  # Título de la ventana
        self.window.geometry("500x400")  # Tamaño de la ventana (ancho x alto)
        
        # Primer Frame (sección de archivo a procesar)
        self.frame1 = tk.Frame(self.window, relief="solid", bd=2, highlightcolor="#d3d3d3")
        self.frame1.pack(padx=10, pady=10, fill="both", expand=True)
           
        self.lbl_file_plane = tk.Label(self.frame1, text="Archivo plano a procesar: ")
        self.lbl_file_plane.place(x=5, y=5)
        self.lbl_file_path = tk.Label(self.frame1, text="Archivo escogido: ")
        self.lbl_file_path.place(x=5, y=40)                         
        self.btn_file_plane = tk.Button(self.frame1, text='Seleccionar..', command=self.choose_path_file)
        self.btn_file_plane.place(x=200, y=5)
        
        # Segundo Frame (sección de posiciones del archivo plano)
        self.frame2 = tk.Frame(self.window, relief="solid", bd=2)
        self.frame2.pack(padx=10, pady=10, fill="both", expand=True)
        
        self.lbl_positions = tk.Label(self.frame2, text='Ingrese las posiciones del archivo estas deben estar separados por espacio')
        self.lbl_positions.place(x=5, y=5)
        self.etr_positions = tk.StringVar()
        self.data_entry =  tk.Entry(self.frame2, width=10, textvariable=self.etr_positions)
        self.data_entry.place(x=5, y=30, relwidth=0.95, relheight=0.3)
        self.data_entry.config(state="disabled")

        self.btn_validate_positions = tk.Button(self.frame2, text='Validar datos ingresados', 
                                                command=self.capture_data)
        self.btn_validate_positions.place(x=5, y=70)

        # Tercer Frame (sección de botòn ejecutar y mensaje emergente)
        self.frame3 = tk.Frame(self.window, relief="solid", bd=2)
        self.frame3.pack(padx=10, pady=10, fill="both", expand=True)
        
        # self.lbl_name_file = tk.Label(self.frame3, text=f'Archivo Resultado:')
        # self.lbl_name_file.place(x=5, y=5)
        self.lbl_position_vector = tk.Label(self.frame3, text=f'Longitudes de cada campo: ')
        self.lbl_position_vector.place(x=5, y=5)

        self.btn_start_process = tk.Button(self.frame3, text='Procesar archivo', command=self.start_process)
        self.btn_start_process.place(x=5, y=30)
        self.btn_start_process.config(state="disabled")

    # Captura ruta de archivo
    def choose_path_file(self):
        # Abre el cuadro de diálogo para seleccionar un archivo
        file_path = filedialog.askopenfilename(title="Selecciona un archivo", 
                                      filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
        if file_path:
            ic(file_path)
            self._file_path = file_path
            self.lbl_file_path.config(text=f"Archivo escogido: {os.path.basename(file_path)}", fg='green')
            self.data_entry.config(state="normal")
        else:
            ic(file_path)
            self.lbl_file_path.config(text="No se selecciono ningun archivo para procesar", fg="red")
            self.data_entry.config(state="disabled")

    # Captura valor de posiciones y depura letras y espacios para crear el vector de posiciones
    def capture_data(self):
        # Valida que el campo de posiciones no este vacio
        data = self.etr_positions.get()
        if not data:
            mb.showerror('Campo vacio', 'El campo de posiciones esta vacio')
        else:
            filtered_data = re.findall(r'\d+', data)
            if filtered_data:
                fields = list(map(int, filtered_data))
                self._positions = fields
                ic(fields)
                self.lbl_position_vector.config(text=f'Longitudes de cada campo: {fields}')
                mb.showinfo('Confirmación', f'Posiciones del archivo plano: {fields}')
                self.btn_start_process.config(state="normal")
            else:
                mb.showerror('Datos incorrectos', 'No se permite ingresar letras u otros carácteres')

    def start_process(self):
        # Captura datos para procesar
        self._name_file = os.path.basename(self._file_path)
        ic(self._name_file, self._file_path, self._positions)
        csv_file = File(self._name_file, self._file_path, self._positions)
        csv_file.parse_file()
        csv_file.export_csv()
        mb.showinfo('Procesado terminado', f'Archivo procesado con exito')

    # # Iniciar el bucle de la interfaz gráfica
    def start_app(self):
        arte = '''
        ##################################
        #  -----                         #
        # | | | |  Separador de archivos #
        # | ___ |  - Version: 0.0.6      #
        #  -----                         #
        ##################################
            '''
        print(arte)
        self.window.mainloop()
