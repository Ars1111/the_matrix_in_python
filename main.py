
#╭━━━┳━━━┳━━━╮╭╮
#┃╭━╮┃╭━╮┃╭━╮┣╯┃
#┃┃╱┃┃╰━╯┃╰━━╋╮┃
#┃╰━╯┃╭╮╭┻━━╮┃┃┃
#┃╭━╮┃┃┃╰┫╰━╯┣╯╰╮
#╰╯╱╰┻╯╰━┻━━━┻━━╯


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QFont, QColor, QPalette
import numpy as np
import random
import time
from tqdm import tqdm

class ArrayFillerApp(QMainWindow):
    def __init__(self):
   
        self.setWindowTitle("Array Filler App")
      
        
        layout = QVBoxLayout()
        layout.addWidget(self.rows1_label)
        layout.addWidget(self.rows1_input)
        layout.addWidget(self.cols1_label)
        layout.addWidget(self.cols1_input)
        layout.addWidget(self.rows2_label)
        layout.addWidget(self.rows2_input)
        layout.addWidget(self.cols2_label)
        layout.addWidget(self.cols2_input)
        layout.addWidget(self.fill_button)
        layout.addWidget(self.add_button)
        layout.addWidget(self.multiply_button)
        layout.addWidget(self.sort_button)
        layout.addWidget(self.max_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)
        
        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        self.array1 = None
        self.array2 = None

    def fill_arrays(self):
        rows1 = int(self.rows1_input.text())
        cols1 = int(self.cols1_input.text())
        rows2 = int(self.rows2_input.text())
        cols2 = int(self.cols2_input.text())
        
        self.array1 = self._fill_array(rows1, cols1)
        self.array2 = self._fill_array(rows2, cols2)
        
        array_output1 = self._print_array(self.array1, "Массив 1:")
        array_output2 = self._print_array(self.array2, "Массив 2:")
        
        self.output_text.setText(f"{array_output1}\n\n{array_output2}")
        
    def add_arrays(self):
        if self.array1 is not None and self.array2 is not None:
            result = np.add(self.array1, self.array2)
            array_output = self._print_array(result, "Сумма массивов:")
            self.output_text.setText(array_output)
        
    def multiply_arrays(self):
        if self.array1 is not None and self.array2 is not None:
            result = np.dot(self.array1, self.array2)
            array_output = self._print_array(result, "Произведение массивов:")
            self.output_text.setText(array_output)
        
    def sort_arrays(self):
        if self.array1 is not None and self.array2 is not None:
            sorted_array1 = np.sort(self.array1, axis=None)
            sorted_array2 = np.sort(self.array2, axis=None)
            array_output1 = self._print_array(sorted_array1, "Отсортированный Массив 1:")
            array_output2 = self._print_array(sorted_array2, "Отсортированный Массив 2:")
            self.output_text.setText(f"{array_output1}\n\n{array_output2}")
            
    def find_max(self):
        if self.array1 is not None and self.array2 is not None:
            max_element1 = np.max(self.array1)
            max_element2 = np.max(self.array2)
            self.output_text.setText(f"Максимальный элемент Массива 1: {max_element1}\nМаксимальный элемент Массива 2: {max_element2}")
        
    def _fill_array(self, rows, cols):
        array = np.random.randint(1, 100, size=(rows, cols))
        return array
    
    def _print_array(self, array, title):
        output = f"{title}\n"
        for row in array:
            for element in row:
                output += str(element) + " "
            output += "\n"
        return output

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Установка стиля Fusion
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(0, 0, 0))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.Base, QColor(0, 0, 0))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
    palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)
    array_filler_app = ArrayFillerApp()
    array_filler_app.show()
    sys.exit(app.exec_())
