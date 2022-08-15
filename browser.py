import sys
from tokenize import String
from turtle import home
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import * 
from PyQt5.QtWebEngineWidgets import*


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        
        self.resize(900,700)
        self.browser = QWebEngineView()
        #added for search engine choose option
        url = QUrl("http://google.com")
        self.browser.setUrl(url)
        #
       
        self.setCentralWidget(self.browser)
        self.showNormal()
        self.setWindowIcon(QIcon('src/icons/window_title_icon.png'))
        navbar=QToolBar()
        self.addToolBar(navbar)
        navbar.setMovable(False)
        
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
        
        
        self.url_bar =QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)
        self.url_bar.setStyleSheet("""
                                   QLineEdit{
                                       margin:5px;
                                       padding:5px 10px;
                                       border:1px solid black;
                                       border-radius: 10px;
                                   }
                                   """)
        

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))
        
    def navigate_to_url(self):
        url= self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_bar.setText(q.toString())
    
app=QApplication(sys.argv)
QApplication.setApplicationName("Simple Browser")
window=MainWindow()
app.exec_()
    
