# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Storage X\About\Programirovanie\Python\Git\OverlayGT 2.0\main\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.f_main = QtWidgets.QFrame(MainWindow)
        self.f_main.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.f_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_main.setObjectName("f_main")
        self.stackedWidget = SlidingStackedWidget(self.f_main)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.stackedWidget.setObjectName("stackedWidget")
        self.f_child = QtWidgets.QFrame(MainWindow)
        self.f_child.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.f_child.setObjectName("f_child")
        self.f_menu = QtWidgets.QFrame(self.f_child)
        self.f_menu.setGeometry(QtCore.QRect(845, 55, 230, 60))
        self.f_menu.setObjectName("f_menu")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.f_menu)
        self.hboxlayout.setContentsMargins(4, 4, 4, 4)
        self.hboxlayout.setSpacing(4)
        self.hboxlayout.setObjectName("hboxlayout")
        self.btn_mixer = QtWidgets.QPushButton(self.f_menu)
        self.btn_mixer.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_mixer.setMaximumSize(QtCore.QSize(50, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_mixer.setIcon(icon)
        self.btn_mixer.setIconSize(QtCore.QSize(20, 20))
        self.btn_mixer.setObjectName("btn_mixer")
        self.hboxlayout.addWidget(self.btn_mixer)
        self.btn_interpreter = QtWidgets.QPushButton(self.f_menu)
        self.btn_interpreter.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_interpreter.setMaximumSize(QtCore.QSize(50, 50))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_interpreter.setIcon(icon1)
        self.btn_interpreter.setIconSize(QtCore.QSize(25, 25))
        self.btn_interpreter.setObjectName("btn_interpreter")
        self.hboxlayout.addWidget(self.btn_interpreter)
        self.line = QtWidgets.QFrame(self.f_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMaximumSize(QtCore.QSize(1, 52))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.hboxlayout.addWidget(self.line)
        self.l_time = MylTime(self.f_menu)
        font = QtGui.QFont()
        font.setFamily("Biennale Black")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.l_time.setFont(font)
        self.l_time.setText("")
        self.l_time.setAlignment(QtCore.Qt.AlignCenter)
        self.l_time.setObjectName("l_time")
        self.hboxlayout.addWidget(self.l_time)
        self.btn_settings = MybtnSettings(self.f_menu)
        self.btn_settings.setMinimumSize(QtCore.QSize(30, 50))
        self.btn_settings.setMaximumSize(QtCore.QSize(30, 50))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_settings.setIcon(icon2)
        self.btn_settings.setIconSize(QtCore.QSize(20, 20))
        self.btn_settings.setObjectName("btn_settings")
        self.hboxlayout.addWidget(self.btn_settings)
        self.AudioWidget = AudioWidget(self.f_child)
        self.AudioWidget.setGeometry(QtCore.QRect(6, 6, 320, 420))
        self.AudioWidget.setObjectName("AudioWidget")
        self.f_title = QtWidgets.QFrame(self.AudioWidget)
        self.f_title.setGeometry(QtCore.QRect(0, 0, 320, 25))
        self.f_title.setMaximumSize(QtCore.QSize(16777215, 25))
        self.f_title.setObjectName("f_title")
        self.hL = QtWidgets.QHBoxLayout(self.f_title)
        self.hL.setContentsMargins(3, 3, 3, 3)
        self.hL.setSpacing(10)
        self.hL.setObjectName("hL")
        self.l_icon_title = QtWidgets.QLabel(self.f_title)
        self.l_icon_title.setMinimumSize(QtCore.QSize(19, 19))
        self.l_icon_title.setMaximumSize(QtCore.QSize(19, 19))
        self.l_icon_title.setPixmap(QtGui.QPixmap(":/img/img_2.png"))
        self.l_icon_title.setScaledContents(True)
        self.l_icon_title.setObjectName("l_icon_title")
        self.hL.addWidget(self.l_icon_title)
        self.l_title = QtWidgets.QLabel(self.f_title)
        font = QtGui.QFont()
        font.setFamily("Biennale Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l_title.setFont(font)
        self.l_title.setObjectName("l_title")
        self.hL.addWidget(self.l_title)
        self.btn_hide = QtWidgets.QPushButton(self.f_title)
        self.btn_hide.setMaximumSize(QtCore.QSize(19, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/img_9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_hide.setIcon(icon3)
        self.btn_hide.setIconSize(QtCore.QSize(20, 20))
        self.btn_hide.setObjectName("btn_hide")
        self.hL.addWidget(self.btn_hide)
        self.frame = QtWidgets.QFrame(self.AudioWidget)
        self.frame.setGeometry(QtCore.QRect(0, 25, 320, 70))
        self.frame.setMinimumSize(QtCore.QSize(320, 68))
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_prev = QtWidgets.QPushButton(self.frame)
        self.btn_prev.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_prev.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_prev.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/img_14.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_prev.setIcon(icon4)
        self.btn_prev.setIconSize(QtCore.QSize(25, 25))
        self.btn_prev.setObjectName("btn_prev")
        self.horizontalLayout.addWidget(self.btn_prev)
        self.btn_pp = QtWidgets.QPushButton(self.frame)
        self.btn_pp.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_pp.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_pp.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/img_12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pp.setIcon(icon5)
        self.btn_pp.setIconSize(QtCore.QSize(25, 25))
        self.btn_pp.setObjectName("btn_pp")
        self.horizontalLayout.addWidget(self.btn_pp)
        self.btn_next = QtWidgets.QPushButton(self.frame)
        self.btn_next.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_next.setMaximumSize(QtCore.QSize(50, 50))
        self.btn_next.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/img_13.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next.setIcon(icon6)
        self.btn_next.setIconSize(QtCore.QSize(25, 25))
        self.btn_next.setObjectName("btn_next")
        self.horizontalLayout.addWidget(self.btn_next)
        self.f_speakers = QtWidgets.QFrame(self.AudioWidget)
        self.f_speakers.setGeometry(QtCore.QRect(0, 95, 320, 30))
        self.f_speakers.setMinimumSize(QtCore.QSize(320, 30))
        self.f_speakers.setObjectName("f_speakers")
        self.gL = QtWidgets.QGridLayout(self.f_speakers)
        self.gL.setContentsMargins(4, 4, 9, 4)
        self.gL.setSpacing(5)
        self.gL.setObjectName("gL")
        self.l_num = QtWidgets.QLabel(self.f_speakers)
        self.l_num.setMinimumSize(QtCore.QSize(20, 20))
        self.l_num.setMaximumSize(QtCore.QSize(20, 20))
        self.l_num.setAlignment(QtCore.Qt.AlignCenter)
        self.l_num.setObjectName("l_num")
        self.gL.addWidget(self.l_num, 0, 2, 1, 1)
        self.hS = QtWidgets.QSlider(self.f_speakers)
        self.hS.setMinimumSize(QtCore.QSize(243, 0))
        self.hS.setMaximum(100)
        self.hS.setSingleStep(10)
        self.hS.setOrientation(QtCore.Qt.Horizontal)
        self.hS.setObjectName("hS")
        self.gL.addWidget(self.hS, 0, 1, 1, 1)
        self.btn_mute = QtWidgets.QPushButton(self.f_speakers)
        self.btn_mute.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_mute.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_mute.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/img_7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_mute.setIcon(icon7)
        self.btn_mute.setIconSize(QtCore.QSize(20, 20))
        self.btn_mute.setObjectName("btn_mute")
        self.gL.addWidget(self.btn_mute, 0, 0, 1, 1)
        self.btn_move = QtWidgets.QPushButton(self.AudioWidget)
        self.btn_move.setGeometry(QtCore.QRect(0, 125, 320, 15))
        self.btn_move.setMaximumSize(QtCore.QSize(16777215, 15))
        self.btn_move.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/img_16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_move.setIcon(icon8)
        self.btn_move.setObjectName("btn_move")
        self.sA = QtWidgets.QScrollArea(self.AudioWidget)
        self.sA.setGeometry(QtCore.QRect(0, 140, 320, 280))
        self.sA.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.sA.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sA.setWidgetResizable(True)
        self.sA.setAlignment(QtCore.Qt.AlignCenter)
        self.sA.setObjectName("sA")
        self.sAWC = QtWidgets.QWidget()
        self.sAWC.setGeometry(QtCore.QRect(0, 0, 301, 278))
        self.sAWC.setObjectName("sAWC")
        self.vL = QtWidgets.QVBoxLayout(self.sAWC)
        self.vL.setContentsMargins(4, 4, 4, 4)
        self.vL.setSpacing(5)
        self.vL.setObjectName("vL")
        self.sA.setWidget(self.sAWC)
        self.TranslitWidget = TranslitWidget(self.f_child)
        self.TranslitWidget.setGeometry(QtCore.QRect(1410, 6, 505, 255))
        self.TranslitWidget.setObjectName("TranslitWidget")
        self.vL_1 = QtWidgets.QVBoxLayout(self.TranslitWidget)
        self.vL_1.setContentsMargins(0, 0, 0, 0)
        self.vL_1.setSpacing(0)
        self.vL_1.setObjectName("vL_1")
        self.f_title_2 = QtWidgets.QFrame(self.TranslitWidget)
        self.f_title_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.f_title_2.setObjectName("f_title_2")
        self.hL_1 = QtWidgets.QHBoxLayout(self.f_title_2)
        self.hL_1.setContentsMargins(3, 3, 3, 3)
        self.hL_1.setSpacing(10)
        self.hL_1.setObjectName("hL_1")
        self.l_icon_title_2 = QtWidgets.QLabel(self.f_title_2)
        self.l_icon_title_2.setMinimumSize(QtCore.QSize(19, 19))
        self.l_icon_title_2.setMaximumSize(QtCore.QSize(19, 19))
        self.l_icon_title_2.setPixmap(QtGui.QPixmap(":/img/img_1.png"))
        self.l_icon_title_2.setScaledContents(True)
        self.l_icon_title_2.setObjectName("l_icon_title_2")
        self.hL_1.addWidget(self.l_icon_title_2)
        self.l_title_2 = QtWidgets.QLabel(self.f_title_2)
        font = QtGui.QFont()
        font.setFamily("Biennale Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l_title_2.setFont(font)
        self.l_title_2.setObjectName("l_title_2")
        self.hL_1.addWidget(self.l_title_2)
        self.btn_hide_2 = QtWidgets.QPushButton(self.f_title_2)
        self.btn_hide_2.setMaximumSize(QtCore.QSize(19, 16777215))
        self.btn_hide_2.setIcon(icon3)
        self.btn_hide_2.setIconSize(QtCore.QSize(20, 20))
        self.btn_hide_2.setObjectName("btn_hide_2")
        self.hL_1.addWidget(self.btn_hide_2)
        self.vL_1.addWidget(self.f_title_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.l_from_lang = QtWidgets.QLabel(self.TranslitWidget)
        self.l_from_lang.setAlignment(QtCore.Qt.AlignCenter)
        self.l_from_lang.setObjectName("l_from_lang")
        self.gridLayout.addWidget(self.l_from_lang, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.btn_swap_lang = QtWidgets.QPushButton(self.TranslitWidget)
        self.btn_swap_lang.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_swap_lang.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_swap_lang.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_swap_lang.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/img/img_0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_swap_lang.setIcon(icon9)
        self.btn_swap_lang.setIconSize(QtCore.QSize(20, 20))
        self.btn_swap_lang.setObjectName("btn_swap_lang")
        self.gridLayout.addWidget(self.btn_swap_lang, 0, 1, 1, 1)
        self.l_to_lang = QtWidgets.QLabel(self.TranslitWidget)
        self.l_to_lang.setAlignment(QtCore.Qt.AlignCenter)
        self.l_to_lang.setObjectName("l_to_lang")
        self.gridLayout.addWidget(self.l_to_lang, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.tE_1 = QtWidgets.QTextEdit(self.TranslitWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tE_1.setFont(font)
        self.tE_1.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tE_1.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.tE_1.setObjectName("tE_1")
        self.gridLayout.addWidget(self.tE_1, 1, 0, 1, 1)
        self.btn_translite = QtWidgets.QPushButton(self.TranslitWidget)
        self.btn_translite.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_translite.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_translite.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_translite.setText("")
        self.btn_translite.setIcon(icon1)
        self.btn_translite.setIconSize(QtCore.QSize(20, 20))
        self.btn_translite.setObjectName("btn_translite")
        self.gridLayout.addWidget(self.btn_translite, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.tE_2 = QtWidgets.QTextEdit(self.TranslitWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tE_2.setFont(font)
        self.tE_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tE_2.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.tE_2.setReadOnly(True)
        self.tE_2.setObjectName("tE_2")
        self.gridLayout.addWidget(self.tE_2, 1, 2, 1, 1)
        self.vL_1.addLayout(self.gridLayout)
        self.SettingsWidget = SettingsWidget(self.f_child)
        self.SettingsWidget.setGeometry(QtCore.QRect(6, 430, 480, 340))
        self.SettingsWidget.setObjectName("SettingsWidget")
        self.f_title_3 = QtWidgets.QFrame(self.SettingsWidget)
        self.f_title_3.setGeometry(QtCore.QRect(0, 0, 480, 25))
        self.f_title_3.setMinimumSize(QtCore.QSize(0, 25))
        self.f_title_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.f_title_3.setObjectName("f_title_3")
        self.hL_2 = QtWidgets.QHBoxLayout(self.f_title_3)
        self.hL_2.setContentsMargins(3, 3, 3, 3)
        self.hL_2.setSpacing(10)
        self.hL_2.setObjectName("hL_2")
        self.l_icon_title_3 = QtWidgets.QLabel(self.f_title_3)
        self.l_icon_title_3.setMinimumSize(QtCore.QSize(19, 19))
        self.l_icon_title_3.setMaximumSize(QtCore.QSize(19, 19))
        self.l_icon_title_3.setPixmap(QtGui.QPixmap(":/img/img_3.png"))
        self.l_icon_title_3.setScaledContents(True)
        self.l_icon_title_3.setObjectName("l_icon_title_3")
        self.hL_2.addWidget(self.l_icon_title_3)
        self.l_title_3 = QtWidgets.QLabel(self.f_title_3)
        font = QtGui.QFont()
        font.setFamily("Biennale Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l_title_3.setFont(font)
        self.l_title_3.setObjectName("l_title_3")
        self.hL_2.addWidget(self.l_title_3)
        self.btn_hide_3 = QtWidgets.QPushButton(self.f_title_3)
        self.btn_hide_3.setMaximumSize(QtCore.QSize(19, 16777215))
        self.btn_hide_3.setIcon(icon3)
        self.btn_hide_3.setIconSize(QtCore.QSize(20, 20))
        self.btn_hide_3.setObjectName("btn_hide_3")
        self.hL_2.addWidget(self.btn_hide_3)
        self.f_container_1 = QtWidgets.QFrame(self.SettingsWidget)
        self.f_container_1.setGeometry(QtCore.QRect(0, 25, 480, 315))
        self.f_container_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_container_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.f_container_1.setObjectName("f_container_1")
        self.vL_2 = QtWidgets.QVBoxLayout(self.f_container_1)
        self.vL_2.setContentsMargins(5, 5, 5, 5)
        self.vL_2.setSpacing(5)
        self.vL_2.setObjectName("vL_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cBox_1 = QtWidgets.QCheckBox(self.f_container_1)
        self.cBox_1.setObjectName("cBox_1")
        self.gridLayout_2.addWidget(self.cBox_1, 6, 1, 1, 1, QtCore.Qt.AlignRight)
        self.hL_5 = QtWidgets.QHBoxLayout()
        self.hL_5.setSpacing(10)
        self.hL_5.setObjectName("hL_5")
        self.hS_2 = QtWidgets.QSlider(self.f_container_1)
        self.hS_2.setMaximum(100)
        self.hS_2.setOrientation(QtCore.Qt.Horizontal)
        self.hS_2.setObjectName("hS_2")
        self.hL_5.addWidget(self.hS_2)
        self.l_num_2 = QtWidgets.QLabel(self.f_container_1)
        self.l_num_2.setMinimumSize(QtCore.QSize(20, 0))
        self.l_num_2.setMaximumSize(QtCore.QSize(20, 16777215))
        self.l_num_2.setAlignment(QtCore.Qt.AlignCenter)
        self.l_num_2.setObjectName("l_num_2")
        self.hL_5.addWidget(self.l_num_2)
        self.gridLayout_2.addLayout(self.hL_5, 2, 1, 1, 1)
        self.l_name_4 = QtWidgets.QLabel(self.f_container_1)
        self.l_name_4.setWordWrap(True)
        self.l_name_4.setObjectName("l_name_4")
        self.gridLayout_2.addWidget(self.l_name_4, 3, 1, 1, 1)
        self.l_name_2 = QtWidgets.QLabel(self.f_container_1)
        self.l_name_2.setMinimumSize(QtCore.QSize(0, 25))
        self.l_name_2.setObjectName("l_name_2")
        self.gridLayout_2.addWidget(self.l_name_2, 2, 0, 1, 1)
        self.l_name_1 = QtWidgets.QLabel(self.f_container_1)
        self.l_name_1.setMinimumSize(QtCore.QSize(0, 25))
        self.l_name_1.setObjectName("l_name_1")
        self.gridLayout_2.addWidget(self.l_name_1, 1, 0, 1, 1)
        self.l_name_3 = QtWidgets.QLabel(self.f_container_1)
        self.l_name_3.setMinimumSize(QtCore.QSize(0, 25))
        self.l_name_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.l_name_3.setObjectName("l_name_3")
        self.gridLayout_2.addWidget(self.l_name_3, 3, 0, 1, 1)
        self.cBox_4 = QtWidgets.QCheckBox(self.f_container_1)
        self.cBox_4.setMinimumSize(QtCore.QSize(0, 25))
        self.cBox_4.setObjectName("cBox_4")
        self.gridLayout_2.addWidget(self.cBox_4, 7, 0, 1, 1)
        self.cBox_2 = QtWidgets.QCheckBox(self.f_container_1)
        self.cBox_2.setMinimumSize(QtCore.QSize(0, 25))
        self.cBox_2.setObjectName("cBox_2")
        self.gridLayout_2.addWidget(self.cBox_2, 5, 0, 1, 1)
        self.cBox = QtWidgets.QCheckBox(self.f_container_1)
        self.cBox.setStyleSheet("")
        self.cBox.setObjectName("cBox")
        self.gridLayout_2.addWidget(self.cBox, 5, 1, 1, 1, QtCore.Qt.AlignRight)
        self.cBox_3 = QtWidgets.QCheckBox(self.f_container_1)
        self.cBox_3.setMinimumSize(QtCore.QSize(0, 25))
        self.cBox_3.setObjectName("cBox_3")
        self.gridLayout_2.addWidget(self.cBox_3, 6, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lE = QtWidgets.QLineEdit(self.f_container_1)
        self.lE.setReadOnly(True)
        self.lE.setObjectName("lE")
        self.horizontalLayout_2.addWidget(self.lE)
        self.tB = QtWidgets.QToolButton(self.f_container_1)
        self.tB.setObjectName("tB")
        self.horizontalLayout_2.addWidget(self.tB)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.l_name = QtWidgets.QLabel(self.f_container_1)
        self.l_name.setMinimumSize(QtCore.QSize(0, 25))
        self.l_name.setObjectName("l_name")
        self.gridLayout_2.addWidget(self.l_name, 0, 0, 1, 1)
        self.cB = QtWidgets.QComboBox(self.f_container_1)
        self.cB.setObjectName("cB")
        self.cB.addItem("")
        self.cB.setItemText(0, "Blue")
        self.cB.addItem("")
        self.cB.setItemText(1, "Blue Red")
        self.cB.addItem("")
        self.cB.setItemText(2, "Cold")
        self.cB.addItem("")
        self.cB.setItemText(3, "Fire")
        self.cB.addItem("")
        self.cB.setItemText(4, "Fire Violet")
        self.cB.addItem("")
        self.cB.setItemText(5, "Fuxia Neon Violet")
        self.cB.addItem("")
        self.cB.setItemText(6, "Fuxia Neon Yellow")
        self.cB.addItem("")
        self.cB.setItemText(7, "Gray")
        self.cB.addItem("")
        self.cB.setItemText(8, "Green")
        self.cB.addItem("")
        self.cB.setItemText(9, "Green Violet")
        self.cB.addItem("")
        self.cB.setItemText(10, "Ice")
        self.cB.addItem("")
        self.cB.setItemText(11, "Ice Fire")
        self.cB.addItem("")
        self.cB.setItemText(12, "Ice Green")
        self.cB.addItem("")
        self.cB.setItemText(13, "Ice Violet")
        self.cB.addItem("")
        self.cB.setItemText(14, "Lineage")
        self.cB.addItem("")
        self.cB.setItemText(15, "Neon Yellow Ice")
        self.cB.addItem("")
        self.cB.setItemText(16, "Old Ice")
        self.cB.addItem("")
        self.cB.setItemText(17, "Orange")
        self.cB.addItem("")
        self.cB.setItemText(18, "Orange Gray")
        self.cB.addItem("")
        self.cB.setItemText(19, "Pink Gray")
        self.cB.addItem("")
        self.cB.setItemText(20, "Red")
        self.cB.addItem("")
        self.cB.setItemText(21, "Red Violet")
        self.cB.addItem("")
        self.cB.setItemText(22, "Violet")
        self.cB.addItem("")
        self.cB.setItemText(23, "Violet Fire")
        self.cB.addItem("")
        self.cB.setItemText(24, "Violet Green")
        self.cB.addItem("")
        self.cB.setItemText(25, "Violet Ice")
        self.cB.addItem("")
        self.cB.setItemText(26, "Violet Red")
        self.cB.addItem("")
        self.cB.setItemText(27, "White")
        self.cB.addItem("")
        self.cB.setItemText(28, "Yellow")
        self.gridLayout_2.addWidget(self.cB, 0, 1, 1, 1)
        self.btn_check_upd = QtWidgets.QPushButton(self.f_container_1)
        self.btn_check_upd.setMinimumSize(QtCore.QSize(466, 20))
        self.btn_check_upd.setMaximumSize(QtCore.QSize(466, 20))
        self.btn_check_upd.setObjectName("btn_check_upd")
        self.gridLayout_2.addWidget(self.btn_check_upd, 8, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(0, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 2)
        self.vL_2.addLayout(self.gridLayout_2)
        self.btn_save = QtWidgets.QPushButton(self.f_container_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QtCore.QSize(75, 20))
        self.btn_save.setMaximumSize(QtCore.QSize(75, 20))
        self.btn_save.setObjectName("btn_save")
        self.vL_2.addWidget(self.btn_save, 0, QtCore.Qt.AlignHCenter)
        self.StatsWidget = StatsWidget(self.f_child)
        self.StatsWidget.setGeometry(QtCore.QRect(0, 1030, 120, 50))
        self.StatsWidget.setObjectName("StatsWidget")
        self.vl_1 = QtWidgets.QVBoxLayout(self.StatsWidget)
        self.vl_1.setContentsMargins(0, 0, 0, 0)
        self.vl_1.setSpacing(0)
        self.vl_1.setObjectName("vl_1")
        self.l_stat = QtWidgets.QLabel(self.StatsWidget)
        self.l_stat.setObjectName("l_stat")
        self.vl_1.addWidget(self.l_stat, 0, QtCore.Qt.AlignBottom)
        self.l_stat_1 = QtWidgets.QLabel(self.StatsWidget)
        self.l_stat_1.setObjectName("l_stat_1")
        self.vl_1.addWidget(self.l_stat_1, 0, QtCore.Qt.AlignBottom)
        self.l_stat_2 = QtWidgets.QLabel(self.StatsWidget)
        self.l_stat_2.setObjectName("l_stat_2")
        self.vl_1.addWidget(self.l_stat_2, 0, QtCore.Qt.AlignBottom)
        self.VersionWidget = QtWidgets.QFrame(self.f_child)
        self.VersionWidget.setGeometry(QtCore.QRect(330, 4, 200, 60))
        self.VersionWidget.setObjectName("VersionWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.VersionWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.l_1 = QtWidgets.QLabel(self.VersionWidget)
        self.l_1.setText("")
        self.l_1.setAlignment(QtCore.Qt.AlignCenter)
        self.l_1.setObjectName("l_1")
        self.verticalLayout.addWidget(self.l_1)
        self.l_2 = QtWidgets.QLabel(self.VersionWidget)
        self.l_2.setAlignment(QtCore.Qt.AlignCenter)
        self.l_2.setObjectName("l_2")
        self.verticalLayout.addWidget(self.l_2)
        self.btn_exit = QtWidgets.QPushButton(self.f_child)
        self.btn_exit.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.btn_exit.setStyleSheet("background: none;\n"
"border: none;")
        self.btn_exit.setObjectName("btn_exit")
        self.TimeWidget = TimeWidget(self.f_child)
        self.TimeWidget.setGeometry(QtCore.QRect(330, 70, 260, 310))
        font = QtGui.QFont()
        font.setFamily("Biennale Black")
        font.setBold(True)
        font.setWeight(75)
        self.TimeWidget.setFont(font)
        self.TimeWidget.setObjectName("TimeWidget")
        self.vL_3 = QtWidgets.QVBoxLayout(self.TimeWidget)
        self.vL_3.setContentsMargins(5, 5, 5, 5)
        self.vL_3.setSpacing(5)
        self.vL_3.setObjectName("vL_3")
        self.container_1 = QtWidgets.QFrame(self.TimeWidget)
        self.container_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container_1.setObjectName("container_1")
        self.vL_4 = QtWidgets.QVBoxLayout(self.container_1)
        self.vL_4.setContentsMargins(0, 0, 0, 0)
        self.vL_4.setSpacing(0)
        self.vL_4.setObjectName("vL_4")
        self.l_time_1 = QtWidgets.QLabel(self.container_1)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.l_time_1.setFont(font)
        self.l_time_1.setText("")
        self.l_time_1.setObjectName("l_time_1")
        self.vL_4.addWidget(self.l_time_1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.l_date_1 = QtWidgets.QLabel(self.container_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_date_1.setFont(font)
        self.l_date_1.setText("")
        self.l_date_1.setObjectName("l_date_1")
        self.vL_4.addWidget(self.l_date_1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.vL_3.addWidget(self.container_1)
        self.calendar = QtWidgets.QCalendarWidget(self.TimeWidget)
        self.calendar.setMinimumSize(QtCore.QSize(0, 220))
        self.calendar.setGridVisible(False)
        self.calendar.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.NoHorizontalHeader)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(False)
        self.calendar.setObjectName("calendar")
        self.vL_3.addWidget(self.calendar)
        self.action_1 = QtWidgets.QAction(MainWindow)
        self.action_1.setObjectName("action_1")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")

        self.retranslateUi(MainWindow)
        self.btn_hide.clicked.connect(self.AudioWidget.hide) # type: ignore
        self.hS.valueChanged['int'].connect(self.l_num.setNum) # type: ignore
        self.btn_hide_2.clicked.connect(self.TranslitWidget.hide) # type: ignore
        self.btn_hide_3.clicked.connect(self.SettingsWidget.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.l_title.setText(_translate("MainWindow", " Аудио"))
        self.l_title_2.setText(_translate("MainWindow", " Переводчик"))
        self.l_from_lang.setText(_translate("MainWindow", "Русский"))
        self.btn_swap_lang.setToolTip(_translate("MainWindow", "Смена языка"))
        self.l_to_lang.setText(_translate("MainWindow", "Английский"))
        self.btn_translite.setToolTip(_translate("MainWindow", "Перевод"))
        self.l_title_3.setText(_translate("MainWindow", "Настройки"))
        self.cBox_1.setText(_translate("MainWindow", "Запускать свернутым"))
        self.l_name_4.setText(_translate("MainWindow", "Убирается весь интерфейс кроме фона. Включаеться по сочетанию клавиш Alt+1"))
        self.l_name_2.setText(_translate("MainWindow", "Blur эффект"))
        self.l_name_1.setText(_translate("MainWindow", "Фон"))
        self.l_name_3.setText(_translate("MainWindow", "Режим заставки"))
        self.cBox_4.setText(_translate("MainWindow", "Download"))
        self.cBox_2.setText(_translate("MainWindow", "Время работы ПК"))
        self.cBox.setText(_translate("MainWindow", "Автозапуск"))
        self.cBox_3.setText(_translate("MainWindow", "Ping"))
        self.tB.setText(_translate("MainWindow", "..."))
        self.l_name.setText(_translate("MainWindow", "Тема"))
        self.btn_check_upd.setText(_translate("MainWindow", "Проверить обновления"))
        self.btn_save.setText(_translate("MainWindow", "Сохранить"))
        self.l_2.setText(_translate("MainWindow", "Copyright (c) 2022 | OSx"))
        self.btn_exit.setShortcut(_translate("MainWindow", "4, 0, 4"))
        self.action_1.setText(_translate("MainWindow", "Отменить действие"))
        self.action_1.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.action_2.setText(_translate("MainWindow", "Повторить действие"))
        self.action_2.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.action_3.setText(_translate("MainWindow", "Вырезать"))
        self.action_3.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.action_4.setText(_translate("MainWindow", "Копировать"))
        self.action_4.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.action_5.setText(_translate("MainWindow", "Вставить"))
        self.action_5.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.action_6.setText(_translate("MainWindow", "Удалить все"))
        self.action_6.setShortcut(_translate("MainWindow", "Del"))
        self.action_7.setText(_translate("MainWindow", "Выбрать все"))
        self.action_7.setShortcut(_translate("MainWindow", "Ctrl+A"))
from modified_elements.btn_settings import MybtnSettings
from modified_elements.l_time import MylTime
from widgets.audio_widget import AudioWidget
from widgets.settings_widget import SettingsWidget
from widgets.sliding_stacked_widget import SlidingStackedWidget
from widgets.stats_widget import StatsWidget
from widgets.time_widget import TimeWidget
from widgets.translit_widget import TranslitWidget
