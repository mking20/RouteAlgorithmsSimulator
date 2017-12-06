
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
import random as r
import numpy as np
import time as t
from astar import *
from BellmanFord import *

class Ui_MainWindow(object):
    start = (0,0)
    end = (0,0)
    def setupUi(self, MainWindow):
        #Set MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 465)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("\n""background-color: rgb(255, 255, 255);")
        #Set Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        #Set GridLayout
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(260, 0, 291, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        #Set SpinBoxes
        self.sbN = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sbN.setObjectName("sbN")
        self.gridLayout.addWidget(self.sbN, 0, 0, 1, 1)
        self.sbM = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sbM.setObjectName("sbM")
        self.gridLayout.addWidget(self.sbM, 0, 1, 1, 1)
        ##Set Ranges
        self.sbN.setRange(8,16)
        self.sbM.setRange(8,16)
        #Set Button Crear
        self.btnCrear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnCrear.setObjectName("btnCrear")
        self.gridLayout.addWidget(self.btnCrear, 0, 2, 1, 1)
        #Set Combobox
        self.cbAlgoritmos = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cbAlgoritmos.setObjectName("cbAlgoritmos")
        self.gridLayout.addWidget(self.cbAlgoritmos, 2, 0, 1, 2)
        #Set Button Enter
        self.btnEnter = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnEnter.setObjectName("btnEnter")
        self.gridLayout.addWidget(self.btnEnter, 2, 2, 1, 1)
        ##Set Buttons Events
        self.btnCrear.clicked.connect(self.btnCrearClicked)            
        self.btnEnter.clicked.connect(self.btnEnterClicked)
        #Set a Vertical Layout
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 360, 551, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        #Set ProgressBar
        self.value=0
        self.bar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.bar.setAutoFillBackground(False)
        self.bar.setStyleSheet("")
        self.bar.setProperty("value", self.value)
        self.bar.setInvertedAppearance(False)
        self.bar.setObjectName("bar")
        #Set Vertical Layout
        self.verticalLayout.addWidget(self.bar)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 100, 551, 261))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        #Set Graphics View and Scene
        self.scene= QtWidgets.QGraphicsScene()
        self.graphics = QtWidgets.QGraphicsView(self.scene,self.verticalLayoutWidget_3)
        self.graphics.setAutoFillBackground(True)
        self.graphics.setObjectName("graphics")
        #Set Vertical Layout
        self.verticalLayout_3.addWidget(self.graphics)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 253, 96))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        #Set Label
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        #Set Menu Bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 21))
        self.menubar.setObjectName("menubar")
        self.menuHello_World = QtWidgets.QMenu(self.menubar)
        self.menuHello_World.setObjectName("menuHello_World")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHello_World.menuAction())
        #Translate UI
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #Agregar opciones al combobox
        self.cbAlgoritmos.addItems(["A estrella","Bellman-Ford","Dijkstra concurrente"])
        #Definir alineaminto del canvas
        self.graphics.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        #Laberinto
        self.array=[]

    def retranslateUi(self, MainWindow):
        #Translate UI
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proyecto Final"))
        self.btnCrear.setText(_translate("MainWindow", "Crear"))
        self.btnEnter.setText(_translate("MainWindow", "Enter"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/jerrylogo.png/jerrylogo.png\"/></p></body></html>"))
        self.menuHello_World.setTitle(_translate("MainWindow", "Hello World!"))

    def btnCrearClicked(self):
        #Vaciar escena y progressbar
        self.scene.clear()
        self.bar.setProperty("value", 0)
        #Obtener valores del Scene
        n= self.sbN.value()
        m= self.sbM.value()
        w= 545
        h= 255
        cw= 545/n
        ch= 255/m
        iw= 0
        ih= 0
        #Dibujar Grid
        for i in range(n):
            self.scene.addLine(QtCore.QLineF(iw, 0, iw, 255))
            iw=iw+cw
        for i in range(m):
            self.scene.addLine(QtCore.QLineF(0, ih, 545, ih))
            ih=ih+ch
        self.graphics.show()
        #Crear y dibujar laberinto
        l=self.crearLab(n,m)
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j] == 1:
                    color= QtGui.QColor(0,0,0,255)
                    brush= QtGui.QBrush(color)
                    rec= QtWidgets.QGraphicsRectItem(j*cw,i*ch,cw,ch)
                    rec.setBrush(brush)
                    self.scene.addItem(rec)

        print("Crear",n,m)

    def btnEnterClicked(self):
        start_in = input("Start")
        end_in = input("End")
        start_in = start_in.split(",")
        end_in = end_in.split(",")
        self.start = (int(start_in[0]), int(start_in[1]))
        self.end = (int(end_in[0]), int(end_in[1]))
        #Escoger algoritmo y resolver
        index= self.cbAlgoritmos.currentIndex()
        path=[]
        if index == 0:
            print("A estrella")
            path= self.estrella(self.array)
        elif index == 1:
            print("Bellman-Ford")
            path = self.bf(self.array)
            #bf() Introducir metodo y que regrese un camino
        elif index == 2:
            print("Dijsktra concurrente")
            #dc() Introducir metodo y que regrese un camino
        
        if len(path) > 0:
            valor= 100/len(path) #Para llenar el progress bar
            path= reversed(path)#El algoritmo de astar que tengo manda el camino del final hacia el inicio

        #Animacion para dibujar resolucion
        for i in path:
            self.value+=valor
            self.addPath(i) #Metodo para agregar un paso "step" de la solucion a la animacion
            QtTest.QTest.qWait(333) #Equivalente a time.sleep(sec) para esta interface Qt
            if self.value > 100: #Aqui ya es para trabajar con el progressbar
                self.value = 100
            self.bar.setProperty("value", self.value)
        print("Enter",index)

    def addPath(self,step):
        #De neuvo obteniendo valores de las dimensiones de la escena
        n= self.sbN.value()
        m= self.sbM.value()
        w= 545
        h= 255
        cw= 545/n
        ch= 255/m
        #Para que coloree el inicio de un color distinto
        if step[0] == self.start[0] and step[1] == self.start[1]:
            color= QtGui.QColor(200,0,100,255)
        #Para que coloree el final de un color distinto
        elif step[0] == self.end[0] and step[1] == self.end[1]:
            color= QtGui.QColor(0,200,100,255)
        #Color para el camino
        else:
            color= QtGui.QColor(0,0,200,255)
        #Instanciar rectangulo con su posicion tamanio para ser agregado a la escena
        brush= QtGui.QBrush(color)
        rec= QtWidgets.QGraphicsRectItem(step[1]*cw,step[0]*ch,cw,ch)
        rec.setBrush(brush)
        self.scene.addItem(rec)
        self.graphics.show()

    def crearLab(self,n,m):
        for i in range(n):
            array2=[]
            for j in range(m):
                numero = r.randint(0,3)
                if numero == 3:
                    print("3")
                    array2.append(1)
                else:
                    print("else")
                    array2.append(0)
            print("append")
            self.array.append(array2)
        return self.array


    
    def estrella(self,array): #Llamar al algoritmo a estrella con los siguientes parametros
        start=(0,0)
        end=(7,7)
        path= astar(array, start,end)
        path.append((0,0))
        print(path)
        return path

    def bf(self,array):
        print(self.start, self.end)
        print("Calling bf")
        path = bellmanFord(array, self.start, self.end)
        path.append((0, 0))
        print(path)
        return path

#Importar logo desde un archivo .py
import resources_rc

if __name__ == "__main__":
    #Inicializar applicacion
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
