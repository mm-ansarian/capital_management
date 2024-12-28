"""This is a module for the final run of the program.
In this file, all the modules join together and start to run the program.
"""


from PyQt5 import QtWidgets
import sys
import gui


# Run the program
app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()
ui = gui.UiPage()
ui.setup_ui(main_window)
main_window.show()
ui.first_database_connection()
sys.exit(app.exec_())
