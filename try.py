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
    
    def setupUi(self, MainWindow):
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(9, 9, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setWindowIcon(QtGui.QIcon(os.path.join(path, r"icons\kanban1.png")))

        # fonts
        fonttblname = QtGui.QFont('Retro Gaming')
        fonttblname.setPointSize(13)
        font = QtGui.QFont('Retro Gaming')
        font.setPointSize(9)
        fontdone = QtGui.QFont('Retro Gaming')
        fontdone.setPointSize(9)
        fontdone.setStrikeOut(True)
        fontdesc = QtGui.QFont('Retro Gaming')
        fontdesc.setPointSize(8)
        
        # lbl
        self.lbl = QtWidgets.QLabel("To Do")
        self.lbl.setFont(fonttblname)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.lbl, 1, 0)

        # lbl1
        self.lbl1 = QtWidgets.QLabel("In Progress")
        self.lbl1.setFont(fonttblname)
        self.lbl1.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.lbl1, 1, 1)

        # lbl2
        self.lbl2 = QtWidgets.QLabel("Done")
        self.lbl2.setFont(fonttblname)
        self.lbl2.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.lbl2, 1, 2)

        # first qlist
        self.todoList = QtWidgets.QListWidget(self.centralwidget)
        self.todoList.setWordWrap(True)
        self.todoList.setFont(font)
        self.todoList.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.todoList.setAutoFillBackground(False)
        self.todoList.setStyleSheet("QWidget{background-color: qlineargradient( x2:2 y2:2, x1:1 y1:0, stop:0 #ffe0e4, stop:1 #ff96a3);}")
        self.todoList.setLineWidth(1)
        self.todoList.setModelColumn(0)
        self.todoList.setObjectName("todoList")
        self.gridLayout.addWidget(self.todoList, 2, 0, 1, 1)
        self.todoList.setAcceptDrops(True)
        self.todoList.setDragEnabled(True)
        self.todoList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.todoList.setDropIndicatorShown(True)
        self.todoList.setSelectionMode(1)
        
        # second qlist
        self.inprogressList = QtWidgets.QListWidget(self.centralwidget)
        self.inprogressList.setWordWrap(True)
        self.inprogressList.setFont(font)
        self.inprogressList.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.inprogressList.setAutoFillBackground(False)
        self.inprogressList.setStyleSheet("QWidget{background-color: qlineargradient( x2:2 y2:2, x1:1 y1:0, stop:0 #eadbff, stop:1 #c8a1ff);}")
        self.inprogressList.setLineWidth(1)
        self.inprogressList.setModelColumn(0)
        self.inprogressList.setObjectName("inprogressList")
        self.gridLayout.addWidget(self.inprogressList, 2, 1, 1, 1)
        self.inprogressList.setAcceptDrops(True)
        self.inprogressList.setDragEnabled(True)
        self.inprogressList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.inprogressList.setSelectionMode(1)

        # third qlist    
        self.doneList = QtWidgets.QListWidget(self.centralwidget)
        self.doneList.setWordWrap(True)
        self.doneList.setFont(fontdone)
        self.doneList.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.doneList.setAutoFillBackground(False)
        self.doneList.setStyleSheet("QWidget{background-color: qlineargradient( x2:2 y2:2, x1:1 y1:0, stop:0 #f8ffd4, stop:1 #edff91);}")
        self.doneList.setLineWidth(1)
        self.doneList.setModelColumn(0)      
        self.doneList.setObjectName("doneList")
        self.gridLayout.addWidget(self.doneList, 2, 2, 1, 1)
        self.doneList.setAcceptDrops(True)
        self.doneList.setDragEnabled(True)
        self.doneList.setDefaultDropAction(QtCore.Qt.MoveAction)

        # description for the 1st qlist
        self.description = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.description.setFont(fontdesc)
        self.description.setAutoFillBackground(False)
        self.description.setLineWidth(1)
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 3, 0, 2, 3)

        # description for the 2nd qlist
        self.description1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.description1.setFont(fontdesc)
        self.description1.setAutoFillBackground(False)
        self.description1.setLineWidth(1)
        self.description1.setObjectName("description1")
        self.gridLayout.addWidget(self.description1, 3, 0, 2, 3)

        # description for the 3rd qlist
        self.description2 = QtWidgets.QPlainTextEdit(self.centralwidget)         
        self.description2.setFont(fontdesc)
        self.description2.setAutoFillBackground(False)
        self.description2.setLineWidth(1)
        self.description2.setObjectName("description2")
        self.gridLayout.addWidget(self.description2, 3, 0, 2, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 288, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setFont(font)
        self.menuFile.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuFile.setToolTipsVisible(True)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setFont(font)
        self.menuEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuEdit.setToolTipsVisible(True)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setMovable(True)
        self.toolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar.setOrientation(QtCore.Qt.Vertical)
        self.toolBar.setIconSize(QtCore.QSize(20, 24))
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")

        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionAdd = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"icons\plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd.setIcon(icon)
        self.actionAdd.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionAdd.setAutoRepeat(True)
        self.actionAdd.setVisible(True)
        self.actionAdd.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionAdd.setIconVisibleInMenu(True)
        self.actionAdd.setShortcutVisibleInContextMenu(False)
        self.actionAdd.setObjectName("actionAdd")

        self.actionRemove = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r"icons\minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove.setIcon(icon1)
        self.actionRemove.setAutoRepeat(True)
        self.actionRemove.setVisible(True)
        self.actionRemove.setIconVisibleInMenu(True)
        self.actionRemove.setShortcutVisibleInContextMenu(False)
        self.actionRemove.setObjectName("actionRemove")
        self.actionRemove.setShortcut(QKeySequence("Del"))

        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(r"icons\save1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setIcon(icon7)
        self.actionSave.setAutoRepeat(True)
        self.actionSave.setVisible(True)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setShortcutVisibleInContextMenu(False)
        self.actionSave.setObjectName("actionSave")
        
        self.actionUp = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(r"icons\up-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUp.setIcon(icon2)
        self.actionUp.setAutoRepeat(True)
        self.actionUp.setVisible(True)
        self.actionUp.setIconVisibleInMenu(True)
        self.actionUp.setShortcutVisibleInContextMenu(False)
        self.actionUp.setObjectName("actionUp")

        self.actionDown = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(r"icons\down-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDown.setIcon(icon3)
        self.actionDown.setAutoRepeat(True)
        self.actionDown.setVisible(True)
        self.actionDown.setIconVisibleInMenu(True)
        self.actionDown.setShortcutVisibleInContextMenu(False)
        self.actionDown.setObjectName("actionDown")

        self.actionSort = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(r"icons\sort.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSort.setIcon(icon4)
        self.actionSort.setAutoRepeat(True)
        self.actionSort.setVisible(True)
        self.actionSort.setIconVisibleInMenu(True)
        self.actionSort.setShortcutVisibleInContextMenu(False)
        self.actionSort.setObjectName("actionSort")

        self.actionNew = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(r"icons\\new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon5)
        self.actionNew.setAutoRepeat(True)
        self.actionNew.setVisible(True)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setShortcutVisibleInContextMenu(False)
        self.actionNew.setObjectName("actionNew")

        self.actionRename = QtWidgets.QAction(MainWindow)

        self.hen = QtWidgets.QLabel(alignment=QtCore.Qt.AlignBottom)
        self.hen.setMinimumSize(QtCore.QSize(10, 10))
        self.hen.setMaximumSize(QtCore.QSize(40, 40))
        self.hen.setAlignment(QtCore.Qt.AlignBottom)
        self.hen.setObjectName("hen")
        self.movie = QMovie(r"icons\floppy2.gif")
        self.movie.setCacheMode(QMovie.CacheNone)

        self.changesCB = QtWidgets.QCheckBox("Changed")
        self.changesCB.setChecked(False)
        self.changesCB.hide()
        
        self.menuFile.addAction(self.actionNew)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(r"icons\recent1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.menuFile.addAction(self.actionSave)
        self.openRecentMenu = self.menuFile.addMenu("Open Recent")
        self.openRecentMenu.setFont(font)
        self.openRecentMenu.setIcon(icon6)
        self.openThemes = self.menuFile.addMenu("Themes")
        self.openThemes.setFont(font)
        # self.openThemes.setIcon(icon6)
        self.menuEdit.addAction(self.actionAdd)
        self.menuEdit.addAction(self.actionRemove)
        self.menuEdit.addAction(self.actionUp)
        self.menuEdit.addAction(self.actionDown)
        self.menuEdit.addAction(self.actionSort)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.toolBar.addAction(self.actionAdd)
        self.toolBar.addAction(self.actionRemove)
        self.toolBar.addAction(self.actionUp)
        self.toolBar.addAction(self.actionDown)
        self.toolBar.addAction(self.actionSort)
        self.toolBar.addWidget(self.hen)
        self.toolBar.addWidget(self.changesCB)

        self.contextmenu = self.centralwidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.centralwidget.addAction(self.actionRename)

        self.actionAdd.triggered.connect(self.actAdd)
        self.actionRemove.triggered.connect(self.actRemove)
        self.actionUp.triggered.connect(self.actUp)
        self.actionDown.triggered.connect(self.actDown)
        self.actionSort.triggered.connect(self.actSort)
        self.actionRename.triggered.connect(self.actRename)
        
        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.description.document().contentsChanged.connect(lambda: self.was_changed())
        self.description1.document().contentsChanged.connect(lambda: self.was_changed())
        self.description2.document().contentsChanged.connect(lambda: self.was_changed())
        
        
    def retranslateUi(self, MainWindow):
        """
            Menu naming
        """

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kanban"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save      Ctrl+S"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionRemove.setText(_translate("MainWindow", "Remove"))
        self.actionUp.setText(_translate("MainWindow", "Up"))
        self.actionDown.setText(_translate("MainWindow", "Down"))
        self.actionSort.setText(_translate("MainWindow", "Sort"))
        self.actionRename.setText(_translate("MainWindow", "Rename"))


    def actAdd(self):
        """
            Add new task (in 1st column by default)
        """

        row = self.todoList.currentRow()
        QInputDialog.setStyleSheet(self.MW,"QInputDialog{background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #f01657, stop:1 #c3083f);}")
        text, ok = QInputDialog.getText(self.MW,"Add","Add Task")
        if ok and text is not None:
            self.todoList.insertItem(row,text)

        self.was_changed()


    def actRemove(self):
        """
            Delete selected task
        """

        if self.todoList.selectedItems():
            row = self.todoList.currentRow()
            item = self.todoList.item(row)
            if item is None:
                return
            else:
                item = self.todoList.takeItem(row)
                del item     

        elif self.inprogressList.selectedItems():
            row = self.inprogressList.currentRow()
            item = self.inprogressList.item(row)
            if item is None:
                return
            else:
                item = self.inprogressList.takeItem(row)
                del item

        elif self.doneList.selectedItems():
            row = self.doneList.currentRow()
            item = self.doneList.item(row)
            if item is None:
                return
            else:
                item = self.doneList.takeItem(row)
                del item      

        self.was_changed()
    

    def actRename(self):
        """
            Rename selected task (by double click)
        """

        if self.todoList.selectedItems():
            row = self.todoList.currentRow()
            item = self.todoList.item(row)
            self.todoList.setEditTriggers(QAbstractItemView.NoEditTriggers)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.todoList.editItem(item)

        elif self.inprogressList.selectedItems():
            row = self.inprogressList.currentRow()
            item = self.inprogressList.item(row)
            self.inprogressList.setEditTriggers(QAbstractItemView.NoEditTriggers)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.inprogressList.editItem(item)

        elif self.doneList.selectedItems():
            row = self.doneList.currentRow()
            item = self.doneList.item(row)
            self.doneList.setEditTriggers(QAbstractItemView.NoEditTriggers)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.doneList.editItem(item)

        self.was_changed()


    def actUp(self):
        """
            Set task higher by button
        """

        row = self.todoList.currentRow()
        if row >=1:
            item = self.todoList.takeItem(row)
            self.todoList.insertItem(row -1, item)
            self.todoList.setCurrentItem(item)

        self.was_changed()
            

    def actDown(self):
        """
            Set task lower by button
        """

        row = self.todoList.currentRow()
        if row < self.todoList.count() -1:
            item = self.todoList.takeItem(row)
            self.todoList.insertItem(row +1, item)
            self.todoList.setCurrentItem(item)

        self.was_changed()


    def actSort(self):
        """
            Sorting tasks by abc
        """

        self.todoList.sortItems()
        self.inprogressList.sortItems()
        self.doneList.sortItems()
        self.was_changed()


    def was_changed(self):
        """
            Mark for asking about saving file if something was changed
        """

        self.changesCB.setChecked(True)
        


class MyMainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        """
            Initialize settings file, save file, theme from settings
        """

        path = os.path.dirname(os.path.abspath(__file__))
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = QSettings("pyqt_settings.ini", QSettings.IniFormat)
        
        self.save_file = self.settings.value("LastFile")
        self.theme = self.settings.value("Theme")
        if not self.save_file:
            self.save_file = os.path.join(path, 'saves1.json')
        self.read_from_file(self.save_file)
        
        self.change_theme(self.theme)
    
        actionSave = self.ui.actionSave
        actionSave.triggered.connect(lambda: self.write_to_file(self.save_file))
        self.shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.shortcut.activated.connect(lambda: self.write_to_file(self.save_file))
        

        openRecentMenu = self.ui.openRecentMenu
        openRecentMenu.aboutToShow.connect(self.actOpenRecent)

        openThemes = self.ui.openThemes
        openThemes.aboutToShow.connect(self.actTheme)

        actionNew = self.ui.actionNew
        actionNew.triggered.connect(self.newSaveFile)

        changesCB = self.ui.changesCB
        changesCB.setChecked(False)
    

    def actTheme(self):
        """
            Add themes
        """
    
        openThemes = self.ui.openThemes
        openThemes.clear()

        actions = []
        acts = []
        acts.append('light')
        acts.append('dark')
        
        for theme in acts:
            action = QAction(theme, self)
            action.triggered.connect(partial(self.change_theme, theme))
            actions.append(action)

        openThemes.addActions(actions)


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
        menubar = self.ui.menubar
        menuFile = self.ui.menuFile
        menuEdit = self.ui.menuEdit
        toolBar = self.ui.toolBar

        if theme is None:
            theme = 'dark'
        if theme == 'light':
            centralwidget.setStyleSheet("QWidget{background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #d1d1d1, stop:1 #dbdbdb);}")
            lbl.setStyleSheet("color: #000000; background: None")
            lbl1.setStyleSheet("color: #000000; background: None")
            lbl2.setStyleSheet("color: #000000; background: None")
            description.setStyleSheet("QWidget{""color: #000000; background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #f2f2f2, stop:1 #f2f2f2);}")
            description1.setStyleSheet("QWidget{""color: #000000; background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #f2f2f2, stop:1 #f2f2f2);}")
            description2.setStyleSheet("QWidget{""color: #000000; background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #f2f2f2, stop:1 #f2f2f2);}")
            menubar.setStyleSheet("QMenuBar{background-color: qlineargradient( x2:2 y2:2, x1:0 y1:2, stop:0 #ffffff, stop:1 #ededed);\n"
                                "color:#000000}")
            menuFile.setStyleSheet("QMenu {background-color:#798d9c;\n"
                                    "color:#FFFFFF;} QMenu:selected {background-color: #5b6a75;}")
            menuEdit.setStyleSheet("QMenu {background-color:#798d9c;\n"
                                    "color:#FFFFFF;} QMenu:selected {background-color: #5b6a75;}")
            toolBar.setStyleSheet("QToolBar{background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #ffffff, stop:1 #ededed);\n"
                                "border:#e41234;\n"
                                "padding:2px;\n"
                                "color:#e41234;}")
        if theme == 'dark':
            centralwidget.setStyleSheet("QWidget{background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #303030, stop:1 #383838)} QMenu{color: #ffffff};")
            # centralwidget.setStyleSheet("QMenu{color: #ffffff}")
            lbl.setStyleSheet("color: #ffffff; background: None")
            lbl1.setStyleSheet("color: #ffffff; background: None")
            lbl2.setStyleSheet("color: #ffffff; background: None")
            description.setStyleSheet("QWidget{""color: #ffffff; background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #3b3b3b, stop:1 #3d3d3d);}")
            description1.setStyleSheet("QWidget{""color: #ffffff; background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #3b3b3b, stop:1 #3d3d3d);}")
            description2.setStyleSheet("QWidget{""color: #ffffff; background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #3b3b3b, stop:1 #3d3d3d);}")
            menubar.setStyleSheet("QMenuBar{background-color: qlineargradient( x2:2 y2:2, x1:0 y1:2, stop:0 #404040, stop:1 #424242);\n"
                                "color:#ffffff}")
            menuFile.setStyleSheet("QMenu {background-color:#C3083F;\n"
                                    "color:#FFFFFF;} QMenu:selected {background-color: #85052b;}")
            menuEdit.setStyleSheet("QMenu {background-color:#C3083F;\n"
                                    "color:#FFFFFF;} QMenu:selected {background-color: #85052b;}")
            toolBar.setStyleSheet("QToolBar{background-color: qlineargradient( x2:2 y2:2, x1:2 y1:0, stop:0 #404040, stop:1 #424242);\n"
                                "border:#e41234;\n"
                                "padding:2px;\n"
                                "color:#e41234;}")
            
        self.settings.setValue("Theme", theme)


    def newSaveFile(self):
        """
            Create new save file with name 'saves1' by default.
            Name can be edit by saving file after create
        """

        path = os.path.dirname(os.path.abspath(__file__))
        self.save_file = os.path.join(path, 'saves1.json')
        self.read_from_file('saves1.json')
        

    def actOpenRecent(self):
        """
            Add open recent in file menu
        """
        
        path = os.path.dirname(os.path.abspath(__file__))
        openRecentMenu = self.ui.openRecentMenu
        openRecentMenu.clear()

        actions = []
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                action = QAction(filename, self)
                action.triggered.connect(partial(self.openRecentFile, filename))
                actions.append(action)

        openRecentMenu.addActions(actions)


    def openRecentFile(self, filename):
        """
            Open file from recents
        """
        
        path = os.path.dirname(os.path.abspath(__file__))
        changesCB = self.ui.changesCB
        self.save_file = os.path.join(path, filename)

        if changesCB.isChecked():
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

        todo_List = self.ui.todoList
        inprogress_List = self.ui.inprogressList
        done_List = self.ui.doneList
        description = self.ui.description
        description1 = self.ui.description1
        description2 = self.ui.description2
        changesCB = self.ui.changesCB
        hen = self.ui.hen
        movie = self.ui.movie
        hen.setMovie(movie)
        movie.start()
        path = os.path.dirname(os.path.abspath(__file__))

        if self.save_file == os.path.join(path, 'saves1.json'):
            file, _ = QFileDialog.getSaveFileName(self, "Save As..", "", "JSON Files (JSON);;Json Files (*.json)")
            if file:
                self.save_file = os.path.join(path, file)
            os.remove("saves1.json")
        # self.settings.setValue("LastFile", file)

        def stopAnimation(self):  
            """
                Floppy disk animation after saving
            """

            timer.stop()
            hen.setMovie(None)
            hen.close()

        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.start(2300)
        timer.timeout.connect(lambda: stopAnimation(self))

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
            changesCB.setChecked(False)

        except OSError as err:
            print(f"file {file} could not be written")
        
        self.settings.setValue("LastFile", file)


    def read_from_file(self, file):
        """
            Read data from file
        """

        todo_List = self.ui.todoList
        inprogress_List = self.ui.inprogressList
        done_List = self.ui.doneList
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

            def listw(self, column): 
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
            
            todo_List.itemClicked.connect(lambda: listw(self, 1))
            inprogress_List.itemClicked.connect(lambda: listw(self, 2))
            done_List.itemClicked.connect(lambda: listw(self, 3))

            readfile.close()

        except OSError as err:
            with open(file, 'w'):
                pass
        
        self.settings.setValue("LastFile", file)

    
    def closeEvent(self, event):
        """
            Saving message when exit
        """
        
        changesCB = self.ui.changesCB
        if changesCB.isChecked():
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