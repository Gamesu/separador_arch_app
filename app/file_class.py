from icecream import ic
from colorama import Fore, Back, init
#ic.disable()

class File:
    def __init__(self, name, path, positions):
        # Variable recibidas por el usuario
        self._name = name
        self._path = path
        self._positions = positions
        self._FILE_NAME_PARSED = f'Archivo Procesado: {self._name.replace('.txt', '')}.csv'
        # Variables propias del programa
        self._parsed_data = []
   
    def parse_line(self, line):
        fields = []
        start_position = 0
        for lenght in self._positions:
            fields.append(line[start_position: start_position + lenght].strip())
            start_position += lenght
        return fields

    def parse_file(self):
        import os
        ic(os.getcwd()) # Muestra la ruta donde debe estar el archivo plano

        with open(self._path, 'r') as file:
            for line in file:
                self._parsed_data.append(self.parse_line(line))
            
            ic(self._parsed_data) # Muestra la lista de valores separados
        
    def export_csv(self):
        ic(self._FILE_NAME_PARSED)
        import csv
        with open(self._FILE_NAME_PARSED, mode='w', newline='', encoding='utf-8') as file:
            file_writer = csv.writer(file, delimiter=';')
            file_writer.writerows(self._parsed_data)
            ic(f'Creando archivo {self._FILE_NAME_PARSED}')
            print(f'{Fore.GREEN}Creando archivo {Fore.CYAN}{self._FILE_NAME_PARSED}')

