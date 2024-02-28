from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
from parser import *
import numpy

def parse_file(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        tree = ast.parse(text)
    return text,tree
class MainWindow(QMainWindow):
    # Override class constructor
    file_path = ""

    def __init__(self):
        # You must call the super class method
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(1800, 800))  # Set sizes
        self.setWindowTitle("Работа с QTableWidget")  # Set the window title
        central_widget = QWidget(self)  # Create a central widget
        self.setCentralWidget(central_widget)  # Install the central widget

        grid_layout = QGridLayout(self)  # Create QGridLayout
        central_widget.setLayout(grid_layout)  # Set this layout in central widget

        self.table = QTableWidget(self)  # Create a table
        self.table.setColumnCount(6)  # Set three columns
        self.table.setRowCount(1)  # and one row
        self.table.setMinimumWidth(500)
        self.table.setMinimumHeight(500)
        self.table.move(0, 30)

        self.file_content = QTextEdit(self)
        self.file_content.setReadOnly(True)
        self.file_content.setMinimumWidth(700)
        self.file_content.setMinimumHeight(800)
        self.file_content.move(800, 20)

        self.parse_button = QPushButton(self)
        self.parse_button.setText("Рассчитать метрику Холстеда")
        self.parse_button.setMinimumWidth(200)
        self.parse_button.move(200, 0)
        self.parse_button.setDisabled(True)
        self.parse_button.clicked.connect(self.on_parse_clicked)

        self.file_button = QPushButton(self)
        self.file_button.setText("Выбрать файл")
        self.file_button.setMinimumWidth(200)
        self.file_button.clicked.connect(self.on_file_clicked)

        # Set the table headers
        self.table.setHorizontalHeaderLabels(["j", "Оператор", "f1j", "i", "Операнд", "f2j"])
        self.table.verticalHeader().hide()
        self.table.resizeColumnsToContents()

        self.program_dict = QLineEdit(self)
        self.program_dict.setReadOnly(True)
        self.program_dict.setMinimumWidth(300)
        self.program_dict.move(500, 30)

        self.program_len = QLineEdit(self)
        self.program_len.setReadOnly(True)
        self.program_len.setMinimumWidth(300)
        self.program_len.move(500, 60)

        self.program_volume = QLineEdit(self)
        self.program_volume.setReadOnly(True)
        self.program_volume.setMinimumWidth(300)
        self.program_volume.move(500, 90)

    def on_parse_clicked(self):
        #self.file_content.toPlainText() ##Код программы
        # operators = get_operators ##Вернет словарь из операторов и числа их появлений
        #operands = get_operands ##Вернет словарь из операндов и числа их появлений

        text, tree = parse_file(self.file_path)
        vars = count_variables(tree)
        loops = count_loops(tree)
        tryes = count_try_excent(tree)
        opr = count_binaty_opr(tree)
        funcs = count_func(tree, vars)
        skobki = {"( )":count_skobki(text, funcs)}
        operators = loops | tryes | opr | funcs
        operands = vars | skobki



        operators = {item[0]: item[1] for item in operators.items() if item[1] != 0}
        operands = {item[0]: item[1] for item in operands.items() if item[1] != 0}

        len1 = len(operators)
        len2 = len(operands)
        rows = max(len1, len2)
        self.table.clear()
        self.table.setRowCount(rows + 1)

        j = 0
        operator_count = 0
        for operator in operators:
            self.table.setItem(j, 0, QTableWidgetItem(str(j + 1) + '.'))
            self.table.setItem(j, 1, QTableWidgetItem(operator))
            self.table.setItem(j, 2, QTableWidgetItem(str(operators[operator])))
            j = j + 1
            operator_count += operators[operator]

        i = 0
        operand_count = 0
        for operand in operands:
            self.table.setItem(i, 3, QTableWidgetItem(str(i + 1) + '.'))
            self.table.setItem(i, 4, QTableWidgetItem(operand))
            self.table.setItem(i, 5, QTableWidgetItem(str(operands[operand])))
            i = i + 1
            operand_count += operands[operand]

        self.table.setItem(rows, 0, QTableWidgetItem("n1 = " + str(j)))
        self.table.setItem(rows, 3, QTableWidgetItem("n2 = " + str(i)))
        self.table.setItem(rows, 2, QTableWidgetItem("N1 = " + str(operator_count)))
        self.table.setItem(rows, 5, QTableWidgetItem("N2 = " + str(operand_count)))

        self.table.setHorizontalHeaderLabels(["j", "Оператор", "f1j", "i", "Операнд", "f2j"])
        self.table.verticalHeader().hide()
        self.table.resizeColumnsToContents()

        self.program_dict.setText("Словарь программы n = " + str(j) + " + " + str(i) + " = " + str(j + i))
        self.program_len.setText("Длина программы n = " + str(operator_count) + " + " + str(operand_count) + " = " + str(operator_count + operand_count))
        self.program_volume.setText("Объем программы V = " + str(operator_count + operand_count) + "log2(" + str(j + i) + ") = " + str(round((operator_count + operand_count) * numpy.log2(j + i), 2)))

    def on_file_clicked(self):
        self.file_path = QFileDialog.getOpenFileNames(self, "Open file", None, "*.py")[0][0]
        file = open(self.file_path, 'r')
        content = file.read()
        file.close()
        self.file_content.setText(content)
        self.parse_button.setDisabled(False)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())