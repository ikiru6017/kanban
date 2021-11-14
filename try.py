# I am using Pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QKeySequence, QMovie
from PyQt5.QtWidgets import QAction, QDialog, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QPushButton, QShortcut, QAbstractItemView, QSizePolicy, QCheckBox
from PyQt5.QtCore import Qt, QTimer, QSettings
import csv
import json
import time
import os
from functools import partial


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)



class Ui_MainWindow(object):
    
    def setup_ui(self, MainWindow):
        """
            Initialize interface
        """
        
        self.MW = MainWindow
        path = os.path.dirname(os.path.abspath(__file__))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 400)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("QMainWindow{background-color:#ffffff;}")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.grid_layout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.grid_layout_2.setContentsMargins(9, 9, -1, -1)
        self.grid_layout_2.setObjectName("grid_layout_2")
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setContentsMargins(0, -1, -1, -1)
        self.grid_layout.setObjectName("grid_layout")
        self.grid_layout_2.addLayout(self.grid_layout, 0, 0, 1, 1)

        MainWindow.setWindowIcon(QtGui.QIcon(os.path.join(path, r"icons\kanban1.png")))

        # fonts
        font_tbl_name = QtGui.QFont('Retro Gaming')
        font_tbl_name.setPointSize(13)
        font = QtGui.QFont('Retro Gaming')
        font.setPointSize(9)
        font_done = QtGui.QFont('Retro Gaming')
        font_done.setPointSize(9)
        font_done.setStrikeOut(True)
        font_desc = QtGui.QFont('Retro Gaming')
        font_desc.setPointSize(8)
        
        # lbl
        self.lbl = QtWidgets.QLabel("To Do")
        self.lbl.setFont(font_tbl_name)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.grid_layout.addWidget(self.lbl, 1, 0)

        # lbl1
        self.lbl1 = QtWidgets.QLabel("In Progress")
        self.lbl1.setFont(font_tbl_name)
        self.lbl1.setAlignment(Qt.AlignCenter)
        self.grid_layout.addWidget(self.lbl1, 1, 1)

        # lbl2
        self.lbl2 = QtWidgets.QLabel("Done")
        self.lbl2.setFont(font_tbl_name)
        self.lbl2.setAlignment(Qt.AlignCenter)
        self.grid_layout.addWidget(self.lbl2, 1, 2)

        # first qlist
        self.todo_list = QtWidgets.QListWidget(self.centralwidget)
        self.todo_list.setWordWrap(True)
        self.todo_list.setFont(font)
        self.todo_list.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.todo_list.setAutoFillBackground(False)
        self.todo_list.setStyleSheet("QWidget{background-color: qlineargradient( x2:2 y2:2, x1:1 y1:0, stop:0 #ffe0e4, stop:1 #ff96a3);}")
        self.todo_list.setLineWidth(1)
        self.todo_list.setModelColumn(0)
        self.todo_list.setObjectName("todo_list")
        self.grid_layout.addWidget(self.todo_list, 2, 0, 1, 1)
        self.todo_list.setAcceptDrops(True)
        self.todo_list.setDragEnabled(True)
        self.todo_list.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.todo_list.setDropIndicatorShown(True)
        self.todo_list.setSelectionMode(1)
        
        # second qlist
        self.inprogress_list = QtWidgets.QListWidget(self.centralwidget)
        self.inprogress_list.setWordWrap(True)
        self.inprogress_list.setFont(font)
        self.inprogress_list.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.inprogress_list.setAutoFillBackground(False)
        self.inprogress_list.setStyleSheet("QWidget{background-color: qlineargradient( x2:2 y2:2, x1:1 y1:0, stop:0 #eadbff, stop:1 #c8a1ff);}")
        self.inprogress_list.setLineWidth(1)
        self.inprogress_list.setModelColumn(0)
        self.inprogress_list.setObjectName("inprogress_list")
        self.grid_layout.addWidget(self.inprogress_list, 2, 1, 1, 1)
        self.inprogress_list.setAcceptDrops(True)
        self.inprogress_list.setDragEnabled(True)
        self.inprogress_list.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.inprogress_list.setSelectionMode(1)

        # third qlist    
        self.done_list = QtWidgets.QListWidget(self.centralwidget)
        self.done_list.setWordWrap(True)
        self.done_list.setFont(font_done)
        self.done_list.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.done_list.setAutoFillBackground(False)
        self.done_list.setStyleSheet("QWidget{background-color: qlineargradient( x2:2 y2:2, x1:1 y1:0, stop:0 #f8ffd4, stop:1 #edff91);}")
        self.done_list.setLineWidth(1)
        self.done_list.setModelColumn(0)      
        self.done_list.setObjectName("done_list")
        self.grid_layout.addWidget(self.done_list, 2, 2, 1, 1)
        self.done_list.setAcceptDrops(True)
        self.done_list.setDragEnabled(True)
        self.done_list.setDefaultDropAction(QtCore.Qt.MoveAction)

        # description for the 1st qlist
        self.description = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.description.setFont(font_desc)
        self.description.setAutoFillBackground(False)
        self.description.setLineWidth(1)
        self.description.setObjectName("description")
        self.grid_layout.addWidget(self.description, 3, 0, 2, 3)

        # description for the 2nd qlist
        self.description1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.description1.setFont(font_desc)
        self.description1.setAutoFillBackground(False)
        self.description1.setLineWidth(1)
        self.description1.setObjectName("description1")
        self.grid_layout.addWidget(self.description1, 3, 0, 2, 3)

        # description for the 3rd qlist
        self.description2 = QtWidgets.QPlainTextEdit(self.centralwidget)         
        self.description2.setFont(font_desc)
        self.description2.setAutoFillBackground(False)
        self.description2.setLineWidth(1)
        self.description2.setObjectName("description2")
        self.grid_layout.addWidget(self.description2, 3, 0, 2, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 288, 21))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.menu_bar.sizePolicy().hasHeightForWidth())
        self.menu_bar.setSizePolicy(size_policy)
        self.menu_bar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menu_bar.setDefaultUp(False)
        self.menu_bar.setNativeMenuBar(True)
        self.menu_bar.setObjectName("menu_bar")
        self.menu_file = QtWidgets.QMenu(self.menu_bar)
        self.menu_file.setFont(font)
        self.menu_file.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menu_file.setToolTipsVisible(True)
        self.menu_file.setObjectName("menu_file")
        self.menu_edit = QtWidgets.QMenu(self.menu_bar)
        self.menu_edit.setFont(font)
        self.menu_edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menu_edit.setToolTipsVisible(True)
        self.menu_edit.setObjectName("menu_edit")
        MainWindow.setMenuBar(self.menu_bar)
        self.tool_bar = QtWidgets.QToolBar(MainWindow)
        self.tool_bar.setEnabled(True)
        self.tool_bar.setSizePolicy(size_policy)
        self.tool_bar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tool_bar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tool_bar.setMovable(True)
        self.tool_bar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.tool_bar.setOrientation(QtCore.Qt.Vertical)
        self.tool_bar.setIconSize(QtCore.QSize(20, 24))
        self.tool_bar.setFloatable(True)
        self.tool_bar.setObjectName("tool_bar")

        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.tool_bar)
        self.action_add = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"icons\plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_add.setIcon(icon)
        self.action_add.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_add.setAutoRepeat(True)
        self.action_add.setVisible(True)
        self.action_add.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.action_add.setIconVisibleInMenu(True)
        self.action_add.setShortcutVisibleInContextMenu(False)
        self.action_add.setObjectName("action_add")

        self.action_remove = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r"icons\minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_remove.setIcon(icon1)
        self.action_remove.setAutoRepeat(True)
        self.action_remove.setVisible(True)
        self.action_remove.setIconVisibleInMenu(True)
        self.action_remove.setShortcutVisibleInContextMenu(False)
        self.action_remove.setObjectName("action_remove")
        self.action_remove.setShortcut(QKeySequence("Del"))

        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(r"icons\save1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setIcon(icon7)
        self.action_save.setAutoRepeat(True)
        self.action_save.setVisible(True)
        self.action_save.setIconVisibleInMenu(True)
        self.action_save.setShortcutVisibleInContextMenu(False)
        self.action_save.setObjectName("action_save")
        
        self.action_up = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(r"icons\up-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_up.setIcon(icon2)
        self.action_up.setAutoRepeat(True)
        self.action_up.setVisible(True)
        self.action_up.setIconVisibleInMenu(True)
        self.action_up.setShortcutVisibleInContextMenu(False)
        self.action_up.setObjectName("action_up")

        self.action_down = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(r"icons\down-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_down.setIcon(icon3)
        self.action_down.setAutoRepeat(True)
        self.action_down.setVisible(True)
        self.action_down.setIconVisibleInMenu(True)
        self.action_down.setShortcutVisibleInContextMenu(False)
        self.action_down.setObjectName("action_down")

        self.action_sort = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(r"icons\sort.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_sort.setIcon(icon4)
        self.action_sort.setAutoRepeat(True)
        self.action_sort.setVisible(True)
        self.action_sort.setIconVisibleInMenu(True)
        self.action_sort.setShortcutVisibleInContextMenu(False)
        self.action_sort.setObjectName("action_sort")

        self.action_new = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(r"icons\\new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new.setIcon(icon5)
        self.action_new.setAutoRepeat(True)
        self.action_new.setVisible(True)
        self.action_new.setIconVisibleInMenu(True)
        self.action_new.setShortcutVisibleInContextMenu(False)
        self.action_new.setObjectName("action_new")

        self.actionRename = QtWidgets.QAction(MainWindow)

        self.gif_label = QtWidgets.QLabel(alignment=QtCore.Qt.AlignBottom)
        self.gif_label.setMinimumSize(QtCore.QSize(10, 10))
        self.gif_label.setMaximumSize(QtCore.QSize(40, 40))
        self.gif_label.setAlignment(QtCore.Qt.AlignBottom)
        self.gif_label.setObjectName("gif_label")
        self.gif = QMovie(r"icons\floppy2.gif")
        self.gif.setCacheMode(QMovie.CacheNone)

        self.change_cbox = QtWidgets.QCheckBox("Changed")
        self.change_cbox.setChecked(False)
        self.change_cbox.hide()
        
        self.menu_file.addAction(self.action_new)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(r"icons\recent1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.menu_file.addAction(self.action_save)
        self.openRecentMenu = self.menu_file.addMenu("Open Recent")
        self.openRecentMenu.setFont(font)
        self.openRecentMenu.setIcon(icon6)
        self.openThemes = self.menu_file.addMenu("Themes")
        self.openThemes.setFont(font)
        # self.openThemes.setIcon(icon6)
        self.menu_edit.addAction(self.action_add)
        self.menu_edit.addAction(self.action_remove)
        self.menu_edit.addAction(self.action_up)
        self.menu_edit.addAction(self.action_down)
        self.menu_edit.addAction(self.action_sort)

        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_edit.menuAction())
        self.tool_bar.addAction(self.action_add)
        self.tool_bar.addAction(self.action_remove)
        self.tool_bar.addAction(self.action_up)
        self.tool_bar.addAction(self.action_down)
        self.tool_bar.addAction(self.action_sort)
        self.tool_bar.addWidget(self.gif_label)
        self.tool_bar.addWidget(self.change_cbox)

        self.contextmenu = self.centralwidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.centralwidget.addAction(self.actionRename)

        self.action_add.triggered.connect(self.add_new_task)
        self.action_remove.triggered.connect(self.remove_task)
        self.action_up.triggered.connect(self.up_task)
        self.action_down.triggered.connect(self.down_task)
        self.action_sort.triggered.connect(self.sort_task)
        self.actionRename.triggered.connect(self.rename_task)
        
        self.retranslate_ui(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.description.document().contentsChanged.connect(lambda: self.was_changed())
        self.description1.document().contentsChanged.connect(lambda: self.was_changed())
        self.description2.document().contentsChanged.connect(lambda: self.was_changed())
        
        
    def retranslate_ui(self, MainWindow):
        """
            Menu naming
        """

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kanban"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_edit.setTitle(_translate("MainWindow", "Edit"))
        self.tool_bar.setWindowTitle(_translate("MainWindow", "tool_bar"))
        self.action_new.setText(_translate("MainWindow", "New"))
        self.action_save.setText(_translate("MainWindow", "Save      Ctrl+S"))
        self.action_add.setText(_translate("MainWindow", "Add"))
        self.action_remove.setText(_translate("MainWindow", "Remove"))
        self.action_up.setText(_translate("MainWindow", "Up"))
        self.action_down.setText(_translate("MainWindow", "Down"))
        self.action_sort.setText(_translate("MainWindow", "Sort"))
        self.actionRename.setText(_translate("MainWindow", "Rename"))


    def add_new_task(self):
        """
            Add new task (in 1st column by default)
        """

        row = self.todo_list.currentRow()
        QInputDialog.setStyleSheet(self.MW,"QInputDialog{background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #f01657, stop:1 #c3083f);}")
        text, ok = QInputDialog.getText(self.MW,"Add","Add Task")
        if ok and text is not None:
            self.todo_list.insertItem(row,text)

        self.was_changed()


    def remove_task(self):
        """
            Delete selected task
        """

        if self.todo_list.selectedItems():
            row = self.todo_list.currentRow()
            item = self.todo_list.item(row)
            if item is None:
                return
            else:
                item = self.todo_list.takeItem(row)
                del item     

        elif self.inprogress_list.selectedItems():
            row = self.inprogress_list.currentRow()
            item = self.inprogress_list.item(row)
            if item is None:
                return
            else:
                item = self.inprogress_list.takeItem(row)
                del item

        elif self.done_list.selectedItems():
            row = self.done_list.currentRow()
            item = self.done_list.item(row)
            if item is None:
                return
            else:
                item = self.done_list.takeItem(row)
                del item      

        self.was_changed()
    

    def rename_task(self):
        """
            Rename selected task (by double click)
        """

        if self.todo_list.selectedItems():
            row = self.todo_list.currentRow()
            item = self.todo_list.item(row)
            self.todo_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.todo_list.editItem(item)

        elif self.inprogress_list.selectedItems():
            row = self.inprogress_list.currentRow()
            item = self.inprogress_list.item(row)
            self.inprogress_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.inprogress_list.editItem(item)

        elif self.done_list.selectedItems():
            row = self.done_list.currentRow()
            item = self.done_list.item(row)
            self.done_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.done_list.editItem(item)

        self.was_changed()


    def up_task(self):
        """
            Set task higher by button
        """

        row = self.todo_list.currentRow()
        if row >= 1:
            item = self.todo_list.takeItem(row)
            self.todo_list.insertItem(row - 1, item)
            self.todo_list.setCurrentItem(item)

        self.was_changed()
            

    def down_task(self):
        """
            Set task lower by button
        """

        row = self.todo_list.currentRow()
        if row < self.todo_list.count() - 1:
            item = self.todo_list.takeItem(row)
            self.todo_list.insertItem(row + 1, item)
            self.todo_list.setCurrentItem(item)

        self.was_changed()


    def sort_task(self):
        """
            Sorting tasks by abc
        """

        self.todo_list.sortItems()
        self.inprogress_list.sortItems()
        self.done_list.sortItems()
        self.was_changed()


    def was_changed(self):
        """
            Hidden checkbox for asking about saving file if something was changed
        """

        self.change_cbox.setChecked(True)
        


class MyMainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        """
            Initialize settings file, save file, theme from settings
        """

        path = os.path.dirname(os.path.abspath(__file__))
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)
        self.settings = QSettings("pyqt_settings.ini", QSettings.IniFormat)
        
        self.save_file = self.settings.value("LastFile")
        self.theme = self.settings.value("Theme")
        if not self.save_file:
            self.save_file = os.path.join(path, 'saves1.json')
        self.read_from_file(self.save_file)
        
        self.change_theme(self.theme)
    
        action_save = self.ui.action_save
        action_save.triggered.connect(lambda: self.write_to_file(self.save_file))
        self.shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.shortcut.activated.connect(lambda: self.write_to_file(self.save_file))
        

        openRecentMenu = self.ui.openRecentMenu
        openRecentMenu.aboutToShow.connect(self.add_open_recent_to_menu)

        openThemes = self.ui.openThemes
        openThemes.aboutToShow.connect(self.add_themes_to_menu)

        action_new = self.ui.action_new
        action_new.triggered.connect(self.new_save_file)

        change_cbox = self.ui.change_cbox
        change_cbox.setChecked(False)
    

    def add_themes_to_menu(self):
        """
            Add themes to menu
        """
    
        openThemes = self.ui.openThemes
        openThemes.clear()

        act_type_themes_list = []
        acts = ['light', 'dark']
        
        for theme in acts:
            action = QAction(theme, self)
            action.triggered.connect(partial(self.change_theme, theme))
            act_type_themes_list.append(action)

        openThemes.addActions(act_type_themes_list)


    def change_theme(self, theme):
        """
            Change theme (dark by default)
        """

        centralwidget = self.ui.centralwidget
        lbl = self.ui.lbl
        lbl1 = self.ui.lbl1
        lbl2 = self.ui.lbl2
        description = self.ui.description
        description1 = self.ui.description1
        description2 = self.ui.description2
        menu_bar = self.ui.menu_bar
        menu_file = self.ui.menu_file
        menu_edit = self.ui.menu_edit
        tool_bar = self.ui.tool_bar

        if theme == 'light':
            centralwidget.setStyleSheet("QWidget{background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #d1d1d1, stop:1 #dbdbdb);}")
            lbl.setStyleSheet("color: #000000; background: None")
            lbl1.setStyleSheet("color: #000000; background: None")
            lbl2.setStyleSheet("color: #000000; background: None")
            description.setStyleSheet("QWidget{""color: #000000; background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #f2f2f2, stop:1 #f2f2f2);}")
            description1.setStyleSheet("QWidget{""color: #000000; background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #f2f2f2, stop:1 #f2f2f2);}")
            description2.setStyleSheet("QWidget{""color: #000000; background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #f2f2f2, stop:1 #f2f2f2);}")
            menu_bar.setStyleSheet("QMenuBar{background-color: qlineargradient( x2:2 y2:2, x1:0 y1:2, stop:0 #ffffff, stop:1 #ededed);\n"
                                "color:#000000}")
            menu_file.setStyleSheet("QMenu {background-color:#798d9c;\n"
                                    "color:#FFFFFF;} QMenu:selected {background-color: #5b6a75;}")
            menu_edit.setStyleSheet("QMenu {background-color:#798d9c;\n"
                                    "color:#FFFFFF;} QMenu:selected {background-color: #5b6a75;}")
            tool_bar.setStyleSheet("QToolBar{background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #ffffff, stop:1 #ededed);\n"
                                "border:#e41234;\n"
                                "padding:2px;\n"
                                "color:#e41234;}")
        elif theme == 'dark':
            centralwidget.setStyleSheet("QWidget{background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #303030, stop:1 #383838)} QMenu{color: #ffffff};")
            # centralwidget.setStyleSheet("QMenu{color: #ffffff}")
            lbl.setStyleSheet("color: #ffffff; background: None")
            lbl1.setStyleSheet("color: #ffffff; background: None")
            lbl2.setStyleSheet("color: #ffffff; background: None")
            description.setStyleSheet("QWidget{""color: #ffffff; background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #3b3b3b, stop:1 #3d3d3d);}")
            description1.setStyleSheet("QWidget{""color: #ffffff; background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #3b3b3b, stop:1 #3d3d3d);}")
            description2.setStyleSheet("QWidget{""color: #ffffff; background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #3b3b3b, stop:1 #3d3d3d);}")
            menu_bar.setStyleSheet("QMenuBar{background-color: qlineargradient( x2:2 y2:2, x1:0 y1:2, stop:0 #404040, stop:1 #424242);\n"
                                "color:#ffffff}")
            menu_file.setStyleSheet("QMenu {background-color:#C3083F;\n"
                                    "color:#FFFFFF;} QMenu:selected {background-color: #85052b;}")
            menu_edit.setStyleSheet("QMenu {background-color:#C3083F;\n"
                                    "color:#FFFFFF;} QMenu:selected {background-color: #85052b;}")
            tool_bar.setStyleSheet("QToolBar{background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #404040, stop:1 #424242);\n"
                                "border:#e41234;\n"
                                "padding:2px;\n"
                                "color:#e41234;}")
        else:
            theme = 'dark'
            
        self.settings.setValue("Theme", theme)


    def new_save_file(self):
        """
            Create new save file with name 'saves1' by default.
            Name can be edit by saving file after create
        """

        path = os.path.dirname(os.path.abspath(__file__))
        self.save_file = os.path.join(path, 'saves1.json')
        self.read_from_file('saves1.json')
        

    def add_open_recent_to_menu(self):
        """
            Add open recent in file menu
        """
        
        path = os.path.dirname(os.path.abspath(__file__))
        openRecentMenu = self.ui.openRecentMenu
        openRecentMenu.clear()

        act_type_file_list = []
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                action = QAction(filename, self)
                action.triggered.connect(partial(self.open_recent_file, filename))
                act_type_file_list.append(action)

        openRecentMenu.addActions(act_type_file_list)


    def open_recent_file(self, filename):
        """
            Open file from recents
        """
        
        path = os.path.dirname(os.path.abspath(__file__))
        changes_cbox = self.ui.change_cbox
        self.save_file = os.path.join(path, filename)

        if changes_cbox.isChecked():
            should_save = QtWidgets.QMessageBox.question(self, "Save data", 
                                                        "Should the data be saved?",
                                                        defaultButton = QtWidgets.QMessageBox.Yes)
            if should_save == QtWidgets.QMessageBox.Yes:
                self.write_to_file(self.save_file)
                
        self.read_from_file(filename)

        
    def write_to_file(self, file):
        """
            Saving file and if it`s name 'saves1' then you can edit name whatever you want
        """

        todo_List = self.ui.todo_list
        inprogress_List = self.ui.inprogress_list
        done_List = self.ui.done_list
        description = self.ui.description
        description1 = self.ui.description1
        description2 = self.ui.description2
        change_cbox = self.ui.change_cbox
        gif_label = self.ui.gif_label
        gif = self.ui.gif
        gif_label.setMovie(gif)
        gif.start()
        path = os.path.dirname(os.path.abspath(__file__))

        if self.save_file == os.path.join(path, 'saves1.json'):
            file, _ = QFileDialog.getSaveFileName(self, "Save As..", "", "JSON Files (JSON);;Json Files (*.json)")
            if file:
                self.save_file = os.path.join(path, file)
            os.remove("saves1.json")
        # self.settings.setValue("LastFile", file)

        def stop_animation():  
            """
                Floppy disk animation after saving
            """

            timer.stop()
            gif_label.setMovie(None)
            gif_label.close()

        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.start(2300)
        timer.timeout.connect(lambda: stop_animation())

        try:
            data = []
            for ii in range(todo_List.count()):
                data.append({
                    "column": "1",
                    "task": todo_List.item(ii).text(),
                    "description": description.toPlainText()
            })
            for ii in range(inprogress_List.count()):
                data.append({
                    "column": "2",
                    "task": inprogress_List.item(ii).text(),
                    "description": description1.toPlainText()
            })
            for ii in range(done_List.count()):
                data.append({
                    "column": "3",
                    "task": done_List.item(ii).text(),
                    "description": description2.toPlainText()
            })

            with open(file, 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, indent=4)
            change_cbox.setChecked(False)

        except OSError as err:
            print(f"file {file} could not be written")
        
        self.settings.setValue("LastFile", file)


    def read_from_file(self, file):
        """
            Read data from file
        """

        todo_List = self.ui.todo_list
        inprogress_List = self.ui.inprogress_list
        done_List = self.ui.done_list
        description = self.ui.description
        description1 = self.ui.description1
        description2 = self.ui.description2

        todo_List.clear()
        inprogress_List.clear()
        done_List.clear()
        description.clear()
        description1.clear()
        description2.clear()

        try:
            readfile = open(file, 'r', encoding='utf-8')
            obj = json.load(readfile)

            col1_dict = [x["description"] for x in obj if x['column'] == "1"]
            if col1_dict:
                if not description.toPlainText() == col1_dict[0]:
                    description.insertPlainText(col1_dict[0])

            col2_dict = [x["description"] for x in obj if x['column'] == "2"]
            if col2_dict:
                if not description1.toPlainText() == col2_dict[0]:
                    description1.insertPlainText(col2_dict[0])

            col3_dict = [x["description"] for x in obj if x['column'] == "3"]
            if col3_dict:
                if not description2.toPlainText() == col3_dict[0]:
                    description2.insertPlainText(col3_dict[0])

            def show_description_on_click(column): 
                """
                    Show description from selected column and hide others. Clear selections. 
                """

                if column == 1:     
                    description1.hide()
                    description2.hide()
                    description.show()
                    inprogress_List.clearSelection()
                    done_List.clearSelection()

                elif column == 2:    
                    description.hide()
                    description2.hide()
                    description1.show()
                    todo_List.clearSelection()
                    done_List.clearSelection()

                elif column == 3:
                    description.hide()
                    description1.hide()
                    description2.show()
                    todo_List.clearSelection()
                    inprogress_List.clearSelection()

            for task in obj:
                                
                if (task["column"] == "1"):
                    item1 = QtWidgets.QListWidgetItem(task["task"])
                    todo_List.addItem(item1)     
                                    
                if (task["column"] == "2"):
                    item2 = QtWidgets.QListWidgetItem(task["task"])
                    inprogress_List.addItem(item2)
                                          
                if (task["column"] == "3"):
                    item3 = QtWidgets.QListWidgetItem(task["task"])
                    done_List.addItem(item3)
            
            todo_List.itemClicked.connect(lambda: show_description_on_click(column=1))
            inprogress_List.itemClicked.connect(lambda: show_description_on_click(column=2))
            done_List.itemClicked.connect(lambda: show_description_on_click(column=3))

            readfile.close()

        except OSError as err:
            with open(file, 'w'):
                pass
        
        self.settings.setValue("LastFile", file)

    
    def closeEvent(self, event):
        """
            Saving message when exit
        """
        
        change_cbox = self.ui.change_cbox
        if change_cbox.isChecked():
            should_save = QtWidgets.QMessageBox.question(self, "Save data", 
                                                        "Should the data be saved?",
                                                        defaultButton = QtWidgets.QMessageBox.Yes)
            if should_save == QtWidgets.QMessageBox.Yes:
                self.write_to_file(self.save_file)
            return super().closeEvent(event)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())