import sys
from tokenize import String
from turtle import home
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import * 
from PyQt5.QtWebEngineWidgets import*
# from pyqt_custom_titlebar_window import CustomTitlebarWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        
        self.resize(1200,900)
        self.browser = QWebEngineView()
        #added for search engine choose option
        url = QUrl("http://google.com")
        self.browser.setUrl(url)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setCentralWidget(self.browser)
        self.showNormal()
        self.setWindowIcon(QIcon('src/icons/window_title_icon.png'))
        
        #Titlebar
        titlebar=QToolBar()
        self.addToolBar(titlebar)
        titlebar.setMovable(False)
        titlebar.setFixedHeight(40)
        titlebar.setStyleSheet("""
                              QToolBar {
                                background: #2d302e;
                                padding: 10px;
                                border: 0px;
                            }
                             """)
        
        #closebutton
        closeButton =QPushButton("",self)
        closeButton.clicked.connect(self.close)
        titlebar.addWidget(closeButton)
        closeButton.setIcon(QIcon("src/icons/cancel.png"))
        closeButton.setStyleSheet("""
                                 QPushButton{
                                     margin-left:1050%;
                                     icon-size:10px;
                                     background-color:#2d302e;
                                     padding:5px 10px;
                                     border-radius:2px;
                                 }
                                 QPushButton:hover{
                                     background-color:red;
                                 }
                                 """)
        
        #fullScreen
        fullScreenButton =QPushButton("",self)
        fullScreenButton.clicked.connect(self.showFullScreen)
        titlebar.addWidget(fullScreenButton)
        fullScreenButton.setIcon(QIcon("src/icons/empty_window.png"))
        fullScreenButton.setStyleSheet("""
                                 QPushButton{
                                     margin-left:2%;
                                     icon-size:10px;
                                     background-color:#2d302e;
                                     padding:5px 10px;
                                     border-radius:2px;
                                 }
                                 QPushButton:hover{
                                     background-color:red;
                                 }
                                 """)
        
        #minimizeButton
        minimizeButton =QPushButton("",self)
        minimizeButton.clicked.connect(self.showMinimized)
        titlebar.addWidget(minimizeButton)
        minimizeButton.setIcon(QIcon("src/icons/minimize.png"))
        minimizeButton.setStyleSheet("""
                                 QPushButton{
                                     margin-left:2%;
                                     icon-size:10px;
                                     background-color:#2d302e;
                                     padding:5px 10px;
                                     border-radius:2px;
                                 }
                                 QPushButton:hover{
                                     background-color:red;
                                 }
                                 """)
        self.addToolBarBreak()
        
        #Navbar
        navbar=QToolBar()
        self.addToolBar(navbar)
        navbar.setMovable(False)
        navbar.setFixedHeight(55)
        navbar.setStyleSheet("""
                              QToolBar {
                                background: #2d302e;
                                padding: 10px;
                                border: 0px;
                            }
                             """)
        
        #backbutton
        backButton = QPushButton("Geri",self)
        backButton.clicked.connect(self.browser.back)
        navbar.addWidget(backButton)
        backButton.setIcon(QIcon("src/icons/back_filled.png"))
        backButton.setStyleSheet("""
                                 QPushButton{
                                     background-color:grey;
                                     margin:5px;
                                     padding:5px 10px;
                                     border-radius:10px;
                                     
                                 }
                                 QPushButton:pressed{
                                     
                                     background-color:#cf801f;
                                 }
                                 """)
        
        #forwardbutton
        forwardButton = QPushButton("İleri",self)
        forwardButton.clicked.connect(self.browser.forward)
        navbar.addWidget(forwardButton)
        forwardButton.setIcon(QIcon("src/icons/forward.png"))
        forwardButton.setStyleSheet("""
                                 QPushButton{
                                     background-color:grey;
                                     margin:5px;
                                     padding:5px 10px;
                                     border-radius:10px;
                                 }
                                 QPushButton:pressed{
                                     
                                     background-color:#cf801f;
                                 }
                                 """)
        
        
        #reloadButton
        reloadButton = QPushButton("Yenile",self)
        reloadButton.clicked.connect(self.browser.reload)
        navbar.addWidget(reloadButton)
        reloadButton.setIcon(QIcon("src/icons/refresh.png"))
        reloadButton.setStyleSheet("""
                                 QPushButton{
                                     background-color:grey;
                                     margin:5px;
                                     padding:5px 10px;
                                     border-radius:10px;
                                 }
                                 QPushButton:pressed{
                                     
                                     background-color:#cf801f;
                                 }
                                 """)
        
        
        #homePageButton
        homeButton = QPushButton("Anasayfa",self)
        homeButton.clicked.connect(self.navigate_home)
        navbar.addWidget(homeButton)
        homeButton.setIcon(QIcon("src/icons/home.png"))
        homeButton.setStyleSheet("""
                                 QPushButton{
                                     background-color:grey;
                                     margin:5px;
                                     padding:5px 10px;
                                     border-radius:10px;
                                 }
                                 QPushButton:pressed{
                                     
                                     background-color:#cf801f;
                                 }
                                 """)
        
        #TextField
        self.url_bar =QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)
        self.url_bar.setStyleSheet("""
                                   QLineEdit{
                                       margin:5px;
                                       padding:5px 10px;
                                       border-radius: 10px;
                                   }
                                   """)
        
    #Custom pressAction
    def mousePressEvent(self,event):
        self.oldPosition =event.globalPos()
        
    #Custom moveAction    
    def mouseMoveEvent(self,event):
        delta = QPoint(event.globalPos()-self.oldPosition)
        self.move(self.x()+delta.x(),self.y()+delta.y())
        self.oldPosition =event.globalPos()
        
        
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))
        
    def navigate_to_url(self):
        url= self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_bar.setText(q.toString())
    

# class MyBar(QWidget):

#     def __init__(self, parent):
#         super(MyBar, self).__init__()
#         self.parent = parent
#         print(self.parent.width())
#         self.layout = QHBoxLayout()
#         self.layout.setContentsMargins(0,0,0,0)
#         self.title = QLabel("My Own Bar")

#         btn_size = 35

#         self.btn_close = QPushButton("x")
#         self.btn_close.clicked.connect(self.btn_close_clicked)
#         self.btn_close.setFixedSize(btn_size,btn_size)
#         self.btn_close.setStyleSheet("background-color: red;")

#         self.btn_min = QPushButton("-")
#         self.btn_min.clicked.connect(self.btn_min_clicked)
#         self.btn_min.setFixedSize(btn_size, btn_size)
#         self.btn_min.setStyleSheet("background-color: gray;")

#         self.btn_max = QPushButton("+")
#         self.btn_max.clicked.connect(self.btn_max_clicked)
#         self.btn_max.setFixedSize(btn_size, btn_size)
#         self.btn_max.setStyleSheet("background-color: gray;")

#         self.title.setFixedHeight(35)
#         self.title.setAlignment(Qt.AlignCenter)
#         self.layout.addWidget(self.title)
#         self.layout.addWidget(self.btn_min)
#         self.layout.addWidget(self.btn_max)
#         self.layout.addWidget(self.btn_close)

#         self.title.setStyleSheet("""
#             background-color: black;
#             color: white;
#         """)
#         # self.setLayout(self.layout)

#         self.start = QPoint(0, 0)
#         self.pressing = False

#     def resizeEvent(self, QResizeEvent):
#         super(MyBar, self).resizeEvent(QResizeEvent)
#         self.title.setFixedWidth(self.parent.width())

#     def mousePressEvent(self, event):
#         self.start = self.mapToGlobal(event.pos())
#         self.pressing = True

#     def mouseMoveEvent(self, event):
#         if self.pressing:
#             self.end = self.mapToGlobal(event.pos())
#             self.movement = self.end-self.start
#             self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
#                                 self.mapToGlobal(self.movement).y(),
#                                 self.parent.width(),
#                                 self.parent.height())
#             self.start = self.end

#     def mouseReleaseEvent(self, QMouseEvent):
#         self.pressing = False


#     def btn_close_clicked(self):
#         self.parent.close()

#     def btn_max_clicked(self):
#         self.parent.showMaximized()

#     def btn_min_clicked(self):
#         self.parent.showMinimized()

    
app=QApplication(sys.argv)
QApplication.setApplicationName("Simple Browser")
window=MainWindow()
app.exec_()
    
