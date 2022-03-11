import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        
        #back
        back_btn =QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
         
        #forward 
        
        fordward_btn = QAction('Fordward',self)
        fordward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(fordward_btn)

        #reload
        
        reload_btn = QAction('Reload',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        #home
        
        home_btn = QAction('home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        
        
        #navbar
        
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def update_url(self, q):
        self.url_bar.setText(q.toString())
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))
app = QApplication(sys.argv)
QApplication.setApplicationName('vandit_s Browser')
window = MainWindow()
app.exec_()
