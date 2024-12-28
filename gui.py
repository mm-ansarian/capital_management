from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import datetime
import options


# TODO: The dark mode options should add to the program.
class UiPage:
    """This class setups every visible things in the main window such as buttons, text boxes, etc. 
    """
    # Setup all the widgets in the main window.
    def setup_ui(self, main_window: object) -> None:
        _translate = QtCore.QCoreApplication.translate

        # Set the font and size of texts.
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(14)
        font.setItalic(True)

        # Setup main window.
        main_window.setObjectName("mainWindow")
        main_window.setFixedSize(1340, 800)
        main_window.setFont(font)
        main_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        main_window.setWindowTitle(_translate("mainWindow", "Capital Management"))
        if hasattr(sys, "_MEIPASS"):
            icon_path = os.path.join(sys._MEIPASS, "icon.ico")
        else:
            icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")

        # Setup the main tab in the window.
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(0, 0, 1345, 805))
        self.tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab.setElideMode(QtCore.Qt.ElideNone)
        self.tab.setTabBarAutoHide(False)
        self.tab.setObjectName("tab")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")

        # Setup the frame of the main page.
        self.frame = QtWidgets.QFrame(self.main_tab)
        self.frame.setGeometry(QtCore.QRect(-2, -2, 1380, 780))
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Setup the earn input field.
        self.earn_input_text_box = QtWidgets.QLineEdit(self.frame)
        self.earn_input_text_box.setGeometry(QtCore.QRect(10, 10, 310, 50))
        self.earn_input_text_box.setInputMask("")
        self.earn_input_text_box.setText("")
        self.earn_input_text_box.setMaxLength(19)
        self.earn_input_text_box.setFrame(True)
        self.earn_input_text_box.setObjectName("earnInput")
        self.earn_input_text_box.setToolTip(_translate("mainWindow", "Earn"))
        self.earn_input_text_box.setPlaceholderText(_translate("mainWindow", "Earn *"))

        # Setup the description input field.
        self.description_text_box = QtWidgets.QLineEdit(self.frame)
        self.description_text_box.setGeometry(QtCore.QRect(10, 80, 310, 50))
        self.description_text_box.setInputMask("")
        self.description_text_box.setText("")
        self.description_text_box.setMaxLength(70)
        self.description_text_box.setObjectName("description")
        self.description_text_box.setToolTip(_translate("mainWindow", "Description"))
        self.description_text_box.setPlaceholderText(_translate("mainWindow", "Description *"))

        # Setup the submit button.
        self.submit_button = QtWidgets.QPushButton(self.frame)
        self.submit_button.setGeometry(QtCore.QRect(50, 150, 220, 60))
        self.submit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        if hasattr(sys, "_MEIPASS"):
            icon_path = os.path.join(sys._MEIPASS, "Submit.ico")
        else:
            icon_path = os.path.join(os.path.dirname(__file__), "icons", "Submit.ico")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submit_button.setIcon(icon)
        self.submit_button.setObjectName("submitBtn")
        self.submit_button.setEnabled(False)
        self.submit_button.setToolTip(_translate("mainWindow", "Submit (Ctrl+Enter)"))
        self.submit_button.setText(_translate("mainWindow", "Submit"))
        self.submit_button.setShortcut(_translate("mainWindow", "Ctrl+Return"))

        # Setup a field for deleting an operation.
        self.delete_text_box = QtWidgets.QLineEdit(self.frame)
        self.delete_text_box.setEnabled(False)
        self.delete_text_box.setGeometry(QtCore.QRect(10, 270, 311, 50))
        self.delete_text_box.setInputMask("")
        self.delete_text_box.setText("")
        self.delete_text_box.setMaxLength(10)
        self.delete_text_box.setObjectName("deleteTxtbox")
        self.delete_text_box.setToolTip(_translate("mainWindow", "Operation ID"))
        self.delete_text_box.setPlaceholderText(_translate("mainWindow", "Operation ID"))

        # Setup a button for deleting an operation.
        self.delete_button = QtWidgets.QPushButton(self.frame)
        self.delete_button.setShortcut("Ctrl+F10")
        self.delete_button.setEnabled(False)
        self.delete_button.setGeometry(QtCore.QRect(50, 340, 220, 60))
        self.delete_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_button.setAutoFillBackground(False)
        if hasattr(sys, "_MEIPASS"):
            icon_path = os.path.join(sys._MEIPASS, "Trash bin.ico")
        else:
            icon_path = os.path.join(os.path.dirname(__file__), "icons", "Trash bin.ico")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon)
        self.delete_button.setFlat(False)
        self.delete_button.setObjectName("deleteBtn")
        self.delete_button.setToolTip(_translate("mainWindow", "Delete operation (Ctrl+F10)"))
        self.delete_button.setText(_translate("mainWindow", "Delete operation"))
        self.delete_button.setShortcut(_translate("mainWindow", "Ctrl+F10"))
        
        # Setup the text browser of operation details.
        self.details_text_browser = QtWidgets.QTextBrowser(self.frame)
        self.details_text_browser.setGeometry(QtCore.QRect(340, 10, 980, 400))
        self.details_text_browser.viewport().setProperty(
            "cursor",
            QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.details_text_browser.setTabChangesFocus(False)
        self.details_text_browser.setDocumentTitle("")
        self.details_text_browser.setObjectName("details")
        self.details_text_browser.setPlaceholderText(_translate("mainWindow", "Operation details"))

        # Setup the text browser of recent operations.
        self.recent_operations_text_browser = QtWidgets.QTextBrowser(self.frame)
        self.recent_operations_text_browser.setGeometry(QtCore.QRect(10, 420, 1311, 321))
        self.recent_operations_text_browser.viewport().setProperty(
            "cursor", 
            QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.recent_operations_text_browser.setObjectName("recentOperations")
        self.recent_operations_text_browser.setPlaceholderText(
            _translate(
                "mainWindow", 
                "Recent operations"))
        
        # Add a tab to display all operations.
        self.tab.addTab(self.main_tab, "")
        self.all_operations_tab = QtWidgets.QWidget()
        self.all_operations_tab.setObjectName("all_operations")

        # Setup the text browser of all operations.
        self.all_operations_text_browser = QtWidgets.QTextBrowser(self.all_operations_tab)
        self.all_operations_text_browser.setGeometry(QtCore.QRect(10, 10, 1311, 730))
        self.all_operations_text_browser.viewport().setProperty(
            "cursor", 
            QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.all_operations_text_browser.setObjectName("allOperations")
        self.all_operations_text_browser.setPlaceholderText(_translate("mainWindow", "All operations"))

        # Add the settings tab.
        self.tab.addTab(self.all_operations_tab, "")
        self.settings_tab = QtWidgets.QWidget()
        self.settings_tab.setObjectName("settings_tab")

        # Setup the frame of the settings page.
        self.frame2 = QtWidgets.QFrame(self.settings_tab)
        self.frame2.setGeometry(QtCore.QRect(-2, -2, 1380, 780))
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")

        # Setup a label of currency unit.
        self.currency_unit_label = QtWidgets.QLabel(self.frame2)
        self.currency_unit_label.setGeometry(QtCore.QRect(10, 10, 230, 50))
        self.currency_unit_label.setObjectName("CurrencyUnitLabel")
        self.currency_unit_label.setText(_translate("mainWindow", "Currency unit:"))

        # Setup a combo box to choosing the currency unit.
        self.currency_unit_combo_box = QtWidgets.QComboBox(self.frame2)
        self.currency_unit_combo_box.setGeometry(QtCore.QRect(280, 10, 250, 50))
        self.currency_unit_combo_box.setObjectName("currencyUnitComboBox")
        self.currency_unit_combo_box.addItem("")
        self.currency_unit_combo_box.addItem("Dollar")
        self.currency_unit_combo_box.addItem("Euro")
        self.currency_unit_combo_box.addItem("Pound")
        self.currency_unit_combo_box.addItem("Yen")
        self.currency_unit_combo_box.addItem("Dinar")
        self.currency_unit_combo_box.addItem("Dirham")
        self.currency_unit_combo_box.addItem("Rial")
        self.currency_unit_combo_box.addItem("Toman")
        self.currency_unit_combo_box.setToolTip(_translate("mainWindow", "Current currency unit"))

        # Setup a button to change the currency uint.
        self.currency_unit_button = QtWidgets.QPushButton(self.frame2)
        self.currency_unit_button.setGeometry(QtCore.QRect(600, 10, 150, 50))
        self.currency_unit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.currency_unit_button.setObjectName("changeCurrencyUnit")
        self.currency_unit_button.setText(_translate("mainWindow", "Change"))

        # Setup a label for program's theme.
        self.theme_label = QtWidgets.QLabel(self.frame2)
        self.theme_label.setGeometry(QtCore.QRect(10, 100, 230, 50))
        self.theme_label.setObjectName("themeLabel")
        self.theme_label.setText(_translate("mainWindow", "Theme:"))

        # Setup a combo box to choose the theme.
        self.theme_combo_box = QtWidgets.QComboBox(self.frame2)
        self.theme_combo_box.setGeometry(QtCore.QRect(280, 100, 250, 50))
        self.theme_combo_box.setObjectName("themeComboBox")
        self.theme_combo_box.addItem("")
        self.theme_combo_box.setToolTip(_translate("mainWindow", "Current theme"))
        self.theme_combo_box.setItemText(0, _translate("mainWindow", "Light"))

        # Set the texts of each part of tab.
        self.tab.addTab(self.settings_tab, "")
        self.tab.setTabText(self.tab.indexOf(self.main_tab), _translate("mainWindow", "Main tab"))
        self.tab.setTabText(self.tab.indexOf(self.all_operations_tab),_translate(
            "mainWindow", 
            "All operations"))
        self.tab.setTabText(self.tab.indexOf(self.settings_tab), _translate("mainWindow", "Settings"))
        
        # Create the order of each widget in the window. 
        main_window.setTabOrder(self.tab, self.earn_input_text_box)
        main_window.setTabOrder(self.earn_input_text_box, self.description_text_box)
        main_window.setTabOrder(self.description_text_box, self.submit_button)
        main_window.setTabOrder(self.submit_button, self.delete_text_box)
        main_window.setTabOrder(self.delete_text_box, self.delete_button)
        main_window.setTabOrder(self.delete_button, self.details_text_browser)
        main_window.setTabOrder(self.details_text_browser, self.recent_operations_text_browser)
        main_window.setTabOrder(self.recent_operations_text_browser, self.all_operations_text_browser)
        main_window.setCentralWidget(self.centralwidget)

        # Call the required methods and functions to start to run the program.
        self.tab.setCurrentIndex(0)   
        self.setup_signals()
        QtCore.QMetaObject.connectSlotsByName(main_window)
        self.setup_shortcuts()
        self.earn_input_text_box.setFocus()

    # A method to fix the requirements of the program which are related to database.
    def first_database_connection(self) -> None:
        self.database_command = """
            CREATE TABLE IF NOT EXISTS operations(
                id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL,
                earn DECIMAL(16, 2) NOT NULL,
                description TEXT(70) NOT NULL,
                operation_date DATETIME NOT NULL,
                balance DECIMAL(19, 2) NOT NULL
            )ENGINE=innoDB;
            """
        options.Options.call_database(command_arg=self.database_command)

        self.database_command = """
            CREATE TABLE IF NOT EXISTS settings(
                currency_unit ENUM('Dollar', 'Euro', 'Pound', 'Yen', 'Dinar',
                    'Dirham', 'Rial', 'Toman') DEFAULT Null,
                theme ENUM('Light', 'Dark') Not Null DEFAULT 'Light' 
            )ENGINE=innoDB;
            """
        options.Options.call_database(command_arg=self.database_command)

        self.database_command = """
        SELECT currency_unit FROM settings;
        """
        task = options.Options.call_database(command_arg=self.database_command)

        if task != []:
            self.currency_unit_combo_box.setCurrentText(str(task[0][0]))
            self.currency_unit_combo_box.setEnabled(False)
            index = self.currency_unit_combo_box.findText("")
            self.currency_unit_combo_box.removeItem(index)

    # A method to setup the signals of some widgets.
    def setup_signals(self) -> None:
        self.earn_input_text_box.textChanged.connect(
            lambda: UiReactions.show_details_action(self, mode="Submit"))
        
        self.description_text_box.textChanged.connect(
            lambda: UiReactions.show_details_action(self, mode="Submit"))

        self.delete_text_box.editingFinished.connect(
            lambda: UiReactions.show_details_action(self, mode="Delete"))
        
        self.submit_button.clicked.connect(lambda: UiReactions.submit_operation_action(self))

        self.delete_button.clicked.connect(lambda: UiReactions.delete_operation_method(self))

        self.currency_unit_button.clicked.connect(
            lambda: UiReactions.release_currency_unit_combo_box_action(self))

        self.tab.currentChanged.connect(lambda: UiReactions.tab_changed_action(self))

        self.currency_unit_combo_box.currentIndexChanged.connect(
            lambda: UiReactions.change_currency_unit_action(self))

    # A method to setup the shortcut keys of some widgets.
    def setup_shortcuts(self) -> None:
        text_box_shortcuts1 = QtWidgets.QShortcut(QtGui.QKeySequence("Down"), self.earn_input_text_box)
        text_box_shortcuts1.activated.connect(lambda: UiReactions.next_text_box_shortcut(self))

        text_box_shortcuts2 = QtWidgets.QShortcut(
            QtGui.QKeySequence("Return"), self.earn_input_text_box)
        text_box_shortcuts2.activated.connect(lambda: UiReactions.next_text_box_shortcut(self))

        text_box_shortcuts3 = QtWidgets.QShortcut(QtGui.QKeySequence("Up"), self.earn_input_text_box)
        text_box_shortcuts3.activated.connect(lambda: UiReactions.previous_text_box_shortcut(self))

        tab_shortcut1 = QtWidgets.QShortcut(QtGui.QKeySequence("Alt+Right"), self.tab)
        tab_shortcut1.activated.connect(lambda: UiReactions.next_tab_shortcut(self))

        tab_shortcut2 = QtWidgets.QShortcut(QtGui.QKeySequence("Alt+Left"), self.tab)
        tab_shortcut2.activated.connect(lambda: UiReactions.previous_tab_shortcut(self))


class UiReactions(UiPage):
    """This class setups the reactions of each widget in the window.
    In fact, this class specifies that what should happen if the user took an action
    on the window.
    """
    # Setup the widgets from the "UiPage" class.
    def setup_ui(self, main_window: object) -> None:
        super().setup_ui(main_window)

    # A method to detect the changes of tab indexes.
    def tab_changed_action(self) -> None:
        if self.tab.currentIndex() == 0 and self.currency_unit_combo_box.currentText() != "":
            self.currency_unit_combo_box.setEnabled(False)
            UiReactions.show_recent_operations_method(self)
            UiReactions.show_details_action(self, mode="Submit")
            UiReactions.show_details_action(self, mode="Delete")

        elif self.tab.currentIndex() == 1:
            self.currency_unit_combo_box.setEnabled(False)
            if self.currency_unit_combo_box.currentText() == "":
                options.Options.message_box(
                    "Not Enough Information", 
                    'Please specify your currency unit in the "Settings" tab.',
                    16)
                
            else:
                UiReactions.show_all_operations_method(self)

        elif self.tab.currentIndex() == 2:
            self.currency_unit_combo_box.setEnabled(False)
    
    # A method to focus on the next tab.
    def next_tab_shortcut(self) -> None:
        if self.tab.currentIndex() == 0:
            self.tab.setCurrentIndex(1)

        elif self.tab.currentIndex() == 1:
            self.tab.setCurrentIndex(2)

        elif self.tab.currentIndex() == 2:
            self.tab.setCurrentIndex(0)

    # A method to focus on the previous tab.
    def previous_tab_shortcut(self) -> None:
        if self.tab.currentIndex() == 2:
            self.tab.setCurrentIndex(1)

        elif self.tab.currentIndex() == 1:
            self.tab.setCurrentIndex(0)

        elif self.tab.currentIndex() == 0:
            self.tab.setCurrentIndex(2)

    # A method to focus on the next text box in the main page.
    def next_text_box_shortcut(self) -> None:
        if self.earn_input_text_box.hasFocus():
            self.description_text_box.setFocus()

        elif self.description_text_box.hasFocus():
            if self.delete_text_box.isEnabled():
                self.delete_text_box.setFocus()
            else:
                self.earn_input_text_box.setFocus()
                self.description_text_box.setFocus()

        elif self.delete_text_box.hasFocus():
            self.earn_input_text_box.setFocus()
            self.delete_text_box.setFocus()

    # A method to focus on the previous text box in the main page.
    def previous_text_box_shortcut(self) -> None:
        if self.delete_text_box.hasFocus():
            self.description_text_box.setFocus()

        elif self.description_text_box.hasFocus():
            self.description_text_box.setFocus()
            self.earn_input_text_box.setFocus()

    # A method that allows the user to change the currency unit.
    def release_currency_unit_combo_box_action(self) -> None:
        self.currency_unit_combo_box.setEnabled(True)
        options.Options.message_box(
            "Warning!",
            "Changing the currency unit, will change the units of all the "
            "operations",
            0)
    
    # A method to change the currency unit.
    def change_currency_unit_action(self) -> None:
        if self.currency_unit_combo_box.currentText() != "":
            index = self.currency_unit_combo_box.findText("")
            self.currency_unit_combo_box.removeItem(index)
            self.currency_unit = self.currency_unit_combo_box.currentText()

            self.database_command = """
            SELECT * 
            FROM settings;
            """
            task = options.Options.call_database(command_arg=self.database_command)
            
            if task != []:
                self.database_command = f"""
                UPDATE settings
                set
                    currency_unit = '{self.currency_unit}';
                """

            else:
                self.database_command = f"""
                INSERT INTO settings(currency_unit)
                VALUES
                    ('{self.currency_unit}');
                """
            options.Options.call_database(command_arg=self.database_command)
        self.currency_unit_combo_box.setEnabled(False)

    # A method to show the details of the specified operation.
    def show_details_action(self, mode: str) -> None:
        # When submitting an operation:
        if mode == "Submit":
            UiReactions.show_recent_operations_method(self)

            self.currency_unit = self.currency_unit_combo_box.currentText()
            
            if self.currency_unit == "":
                if self.earn_input_text_box.text() or self.description_text_box.text():
                    self.earn_input_text_box.clear()
                    self.description_text_box.clear()
                    options.Options.message_box(
                        "Not Enough Information", 
                        'Please specify your currency unit in the "Settings" tab.',
                        16)
                    return

            elif self.earn_input_text_box.text() and self.description_text_box.text():
                self.current_date = ", ".join(str(datetime.datetime.now().date()).split("-"))
                self.current_time = (str(datetime.datetime.now().time()).split("."))[0]
                self.earn = self.earn_input_text_box.text()
                self.description = self.description_text_box.text()

                if "_" in self.earn:
                    options.Options.message_box(
                        "Invalid Input", 
                        'You entered an invalid input for the "Earn" field\n'
                        "just integer and decimal numbers are accepted as input.", 
                        16)
                    self.earn_input_text_box.clear()
                    return
                
                try:
                    if float(self.earn) % 1 == 0:
                        self.earn = int(float(self.earn))

                    else:
                        self.earn = (float(self.earn))

                    if float(self.earn) > 1 and self.currency_unit != "":
                        self.currency_unit = f"{self.currency_unit}s"

                    self.details_text_browser.setPlainText(
                        f"**  Operation details  **\n\n\n"
                        f"Earn: {self.earn:,} {self.currency_unit}\n\n"
                        f"Description: {self.description}\n\n"
                        f"Operation date: {self.current_date}\n\n"
                        f"Operation time: {self.current_time}")
                    
                    self.delete_button.setText("Cancel operation")
                    self.delete_button.setEnabled(True)
                    self.delete_button.setShortcut("Ctrl+F10")
                    self.submit_button.setEnabled(True)

                except ValueError:
                    options.Options.message_box(
                        "Invalid Input", 
                        'You entered an invalid input for the "Earn" field.\n'
                        "just integer and decimal numbers are accepted as input.",
                        16)
                    self.earn_input_text_box.clear()

        # When deleting an operation:
        elif mode == "Delete":
            UiReactions.show_recent_operations_method(self)
            if self.delete_text_box.text():
                try:
                    self.operation_id = int(float(self.delete_text_box.text()))

                    self.database_command = f"""
                        SELECT * FROM operations
                        WHERE id = {self.operation_id};
                        """
                    self.task = options.Options.call_database(command_arg=self.database_command)

                    temp_ls = [[]] * len(self.task)
                    temp_ls = [list(map(str, i) ) for i in self.task][0]

                    self.currency_unit = self.currency_unit_combo_box.itemText(
                        self.currency_unit_combo_box.currentIndex())
                    self.earn = float(temp_ls[1])

                    if float(self.earn) % 1 == 0:
                        self.earn = int(float(self.earn))

                    if float(self.earn) > 1 and self.currency_unit != "":
                        self.currency_unit = f"{self.currency_unit}s"

                    self.details_text_browser.setPlainText(
                            f"**  Operation details  **\n\n\n"
                            f"ID: {temp_ls[0]}\n\n"
                            f"Earn: {self.earn:,} {self.currency_unit}\n\n"
                            f"Description: {temp_ls[2]}\n\n"
                            f"Operation date: {temp_ls[3].split(' ')[0]}\n\n"
                            f"Operation time: {temp_ls[3].split(' ')[1]}")
                    
                    self.delete_button.setEnabled(True)
                    self.delete_button.setShortcut("Ctrl+F10")

                except IndexError:
                    options.Options.message_box(
                        "Operation Not Found", 
                        f"There isn't any operation with ID: {self.operation_id}.",
                        16)
                    
                    self.delete_text_box.clear()
                    self.earn_input_text_box.clear()
                    self.description_text_box.clear()
                    self.delete_button.setShortcut("Ctrl+F10")
                    self.delete_button.setEnabled(False)

                except ValueError:
                    options.Options.message_box(
                        "Invalid Input", 
                        'You entered an invalid input for the "ID" field\n'
                        "operation IDs(integer) are accepted as input.",
                        16)
                    
                    self.delete_text_box.clear()
                    self.earn_input_text_box.clear()
                    self.description_text_box.clear()
                    self.delete_button.setShortcut("Ctrl+F10")
                    self.delete_button.setEnabled(False)

    # A method to submit an operation.
    def submit_operation_action(self) -> None:
        try:
            current_date = (str(datetime.datetime.now()).split("."))[0]

            self.database_command2 = """
                SELECT sum(earn) FROM operations;
                """
            try:
                balance = float(options.Options.call_database(
                    command_arg=self.database_command2)[0][0]) + float(self.earn)
                
            except TypeError:
                balance = float(self.earn)

            self.database_command2 = f"""
                ALTER TABLE operations AUTO_INCREMENT=1;
                """
            options.Options.call_database(command_arg=self.database_command2)

            self.database_command2 = f"""
                INSERT INTO operations(earn, description, operation_date, balance)
                VALUES
                    ({self.earn}, '{str(self.description_text_box.text())}', 
                    '{current_date}', {float(balance)});
                """
            options.Options.call_database(command_arg=self.database_command2)

            self.database_command2 = """
                SELECT id FROM operations
                ORDER BY id DESC
                LIMIT 1;
                """
            operation_id = int(options.Options.call_database(
                command_arg=self.database_command2)[0][0])

            self.earn_input_text_box.clear()
            self.description_text_box.clear()
            self.details_text_browser.clear()
            self.details_text_browser.setPlaceholderText("Operation details")

            self.delete_button.setText("Delete operation")
            self.delete_button.setShortcut("Ctrl+F10")
            self.delete_button.setEnabled(False)
            self.submit_button.setEnabled(False)

            options.Options.message_box(
                f"Operation Submitted", 
                f"The operation submitted with id: {operation_id}", 
                0)
            
            UiReactions.show_recent_operations_method(self)
            
            self.delete_text_box.setEnabled(True)
            self.earn_input_text_box.setFocus()
            self.database_command2 = None
            self.earn = None
            current_date = None

        except AttributeError:
            pass

        except ValueError:
            pass
    
    # A method to delete an operation.
    def delete_operation_method(self) -> None:
        if self.delete_button.text() == "Cancel operation":
            self.earn_input_text_box.clear()
            self.description_text_box.clear()
            self.delete_text_box.clear()
            self.details_text_browser.clear()

            self.details_text_browser.setPlaceholderText("Operation details")
            self.delete_button.setText("Delete operation")
            self.submit_button.setEnabled(False)
            self.delete_button.setShortcut("Ctrl+F10")
            self.delete_button.setEnabled(False)
            self.earn = None
            self.earn_input_text_box.setFocus()

        elif not self.delete_text_box.text():
            self.delete_button.setShortcut("Ctrl+F10")
            self.delete_button.setEnabled(False)

        else:
            self.database_command = f"""
            DELETE FROM operations
            WHERE id = {self.operation_id};
            """
            options.Options.call_database(command_arg=self.database_command)

            self.delete_text_box.clear()
            self.earn_input_text_box.clear()
            self.description_text_box.clear()
            self.details_text_browser.clear()

            self.delete_button.setShortcut("Ctrl+F10")
            self.delete_button.setEnabled(False)
            options.Options.message_box(
                f"Operation Deleted", 
                f"The operation with id: {self.operation_id}, successfully deleted.", 
                0)
            
            UiReactions.show_recent_operations_method(self)

    # A method to show all operations in the related tab.
    def show_all_operations_method(self) -> None:
        if self.currency_unit_combo_box.currentText() != "":
            self.delete_text_box.setEnabled(True)
            self.all_operations_text_browser.clear()

            self.database_command = """
                SELECT SUM(earn) 
                FROM operations;
                """
            
            self.database_command2 = """
                SELECT * 
                FROM operations
                ORDER BY operation_date DESC;
                """
            
            self.task = options.Options.call_database(command_arg=self.database_command)
            self.task2 = options.Options.call_database(command_arg=self.database_command2)

            if self.task2 != []:
                temp_ls = [[]] * len(self.task2)
                temp_ls = [list(map(str, i) ) for i in self.task2]
                result = []

                if float(self.task[0][0]) % 1 == 0:
                    balance = int(float(self.task[0][0]))
                else:
                    balance = (float(self.task[0][0]))

                currency_unit1 = self.currency_unit_combo_box.currentText()

                if balance > 1.0 and currency_unit1 != "":
                    currency_unit1 = f"{currency_unit1}s"

                self.all_operations_text_browser.setPlainText("Loading data...")

                for i in temp_ls:
                    self.earn = int(float(i[1])) if float(i[1]) % 1 == 0 else (float(i[1]))

                    currency_unit2 = self.currency_unit_combo_box.currentText()

                    if self.earn > 1.0 and currency_unit2 != "":
                        currency_unit2 = f"{currency_unit2}s"
                    
                    
                    result.append(
                        f"ID: {i[0]}\n\n"
                        f"Earn: {self.earn:,} {currency_unit2}\n\n"
                        f"Description: {i[2]}\n\n"
                        f"Date and time: {i[3]}")
                    
                    if temp_ls.index(i) != len(temp_ls) - 1:
                        result.append("\n\n")
                        result.append("-" * 159)
                        result.append("\n\n")
                
                self.all_operations_text_browser.setPlainText(
                    f"Current Balance: {balance:,} {currency_unit1}\n\n")
                self.all_operations_text_browser.append("**  All operations  **\n\n")
                self.all_operations_text_browser.append("".join(result))

            else:
                self.all_operations_text_browser.setPlainText("There is no operation yet!")
                self.delete_text_box.setEnabled(False)

            self.all_operations_text_browser.moveCursor(QtGui.QTextCursor.Start)

    # A method to show recent operations in the related tab.
    def show_recent_operations_method(self) -> None:
       if self.currency_unit_combo_box.currentText() != "":
            self.delete_text_box.setEnabled(True)
            self.all_operations_text_browser.clear()

            self.database_command = """
                SELECT SUM(earn)
                FROM operations;
                """
            self.database_command2 = """
                SELECT *
                FROM operations
                ORDER BY operation_date DESC
                LIMIT 20;
                """
            
            self.task = options.Options.call_database(command_arg=self.database_command)
            self.task2 = options.Options.call_database(command_arg=self.database_command2)

            if self.task2 != []:
                temp_ls = [[]] * len(self.task2)
                temp_ls = [list(map(str, i) ) for i in self.task2]
                result = []

                if float(self.task[0][0]) % 1 == 0:
                    balance = int(float(self.task[0][0]))
                else:
                    balance = (float(self.task[0][0]))

                currency_unit1 = self.currency_unit_combo_box.currentText()

                if balance > 1.0 and currency_unit1 != "":
                    currency_unit1 = f"{currency_unit1}s"

                self.all_operations_text_browser.setPlainText("Loading data...")


                for i in temp_ls:
                    self.earn = int(float(i[1])) if float(i[1]) % 1 == 0 else (float(i[1]))

                    currency_unit2 = self.currency_unit_combo_box.currentText()

                    if self.earn > 1.0 and currency_unit2 != "":
                        currency_unit2 = f"{currency_unit2}s"
                    
                    result.append(
                        f"ID: {i[0]}\n\n"
                        f"Earn: {self.earn:,} {currency_unit2}\n\n"
                        f"Description: {i[2]}\n\n"
                        f"Date and time: {i[3]}")
                    
                    if temp_ls.index(i) != len(temp_ls) - 1:
                        result.append("\n\n")
                        result.append("-" * 159)
                        result.append("\n\n")
                
                self.recent_operations_text_browser.setPlainText(
                    f"Current Balance: {balance:,} {currency_unit1}\n\n")
                self.recent_operations_text_browser.append("**  Recent operations  **\n\n")
                self.recent_operations_text_browser.append("".join(result))

            else:
                self.recent_operations_text_browser.setPlainText("There is no operation yet!")
                self.delete_text_box.setEnabled(False)

            self.recent_operations_text_browser.moveCursor(QtGui.QTextCursor.Start)
