
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from AStar import *
from BellmanFord import *
from ConcurrentDijkstra import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Set Man Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1130, 656)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("\n""background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        #Set Layout with boxes and labels
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(270, 0, 841, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        #Set checkBox
        self.checkBox_Diagonals = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Diagonals.setObjectName("checkBox_Diagonals")
        self.gridLayout.addWidget(self.checkBox_Diagonals, 3, 1, 1, 1)
        #Set comboBox
        self.cbAlgoritmos = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cbAlgoritmos.setObjectName("cbAlgoritmos")
        self.gridLayout.addWidget(self.cbAlgoritmos, 3, 0, 1, 1)
        #Set spinBox for size
        self.sbM = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sbM.setObjectName("sbM")
        self.gridLayout.addWidget(self.sbM, 0, 1, 1, 1)
        self.sbN = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sbN.setObjectName("sbN")
        self.gridLayout.addWidget(self.sbN, 0, 0, 1, 1)
        ##Set ranges
        self.sbN.setRange(8,128)
        self.sbM.setRange(8,128)
        self.sbN.setSingleStep(8)
        self.sbM.setSingleStep(8)
        #Set labels and spinboxes for start and end
        #Start
        self.label_start = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_start.setFrameShape(QtWidgets.QFrame.Box)
        self.label_start.setObjectName("label_start")
        self.gridLayout.addWidget(self.label_start, 1, 0, 1, 1)
        self.spinBox_X1 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_X1.setObjectName("spinBox_X1")
        self.gridLayout.addWidget(self.spinBox_X1, 1, 1, 1, 1)
        self.spinBox_Y1 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_Y1.setObjectName("spinBox_Y1")
        self.gridLayout.addWidget(self.spinBox_Y1, 1, 3, 1, 1)
        self.label_end = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_end.setFrameShape(QtWidgets.QFrame.Box)
        self.label_end.setObjectName("label_end")
        self.spinBox_X1.setRange(1,1)
        self.spinBox_Y1.setRange(1,1)
        #End
        self.gridLayout.addWidget(self.label_end, 2, 0, 1, 1)
        self.spinBox_X2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_X2.setObjectName("spinBox_X2")
        self.gridLayout.addWidget(self.spinBox_X2, 2, 1, 1, 1)
        self.spinBox_Y2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_Y2.setObjectName("spinBox_Y2")
        self.gridLayout.addWidget(self.spinBox_Y2, 2, 3, 1, 1)
        self.spinBox_X2.setRange(8,8)
        self.spinBox_Y2.setRange(8,8)
        #Set buttons
        self.btnCrear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnCrear.setObjectName("btnCrear")
        self.gridLayout.addWidget(self.btnCrear, 0, 3, 1, 1)
        self.btnEnter = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnEnter.setObjectName("btnEnter")
        self.gridLayout.addWidget(self.btnEnter, 3, 3, 1, 1)
        #Set layout for progressbar
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 530, 1101, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        #Set progressbar
        self.bar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.bar.setAutoFillBackground(False)
        self.bar.setStyleSheet("")
        self.bar.setProperty("value", 24)
        self.bar.setInvertedAppearance(False)
        self.bar.setObjectName("bar")
        #Set layout for graphics
        self.verticalLayout.addWidget(self.bar)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 120, 1101, 411))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        #Set graphicsview
        self.scene= QtWidgets.QGraphicsScene() ##Create a scene
        self.graphics = QtWidgets.QGraphicsView(self.scene,self.verticalLayoutWidget_3)
        self.graphics.setAutoFillBackground(True)
        self.graphics.setObjectName("graphics")
        self.verticalLayout_3.addWidget(self.graphics)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 0, 211, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        #Set layout for Logo
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        #Set logo
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        #Set rest of stuff
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 21))
        self.menubar.setObjectName("menubar")
        self.menuHello_World = QtWidgets.QMenu(self.menubar)
        self.menuHello_World.setObjectName("menuHello_World")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHello_World.menuAction())

        #Translation of UI
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ##Set Buttons Events
        self.btnCrear.clicked.connect(self.btnCrearClicked)            
        self.btnEnter.clicked.connect(self.btnEnterClicked)
        ##Value for progressbar
        self.value=0
        self.bar.setProperty("value", self.value)
        ##Agregar opciones al combobox
        self.cbAlgoritmos.addItems(["A estrella","Bellman-Ford","Dijkstra concurrente"])
        ##Definir alineaminto del canvas
        self.graphics.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        ##Laberinto
        self.array=[]
        self.listaRec= []
        self.win=[]
        ##Click a un pixel para seleccionarlo
        self.graphics.mousePressEvent = self.pixelSelect

    def retranslateUi(self, MainWindow):
        #Set names for the component of main window
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proyecto Final"))
        self.checkBox_Diagonals.setText(_translate("MainWindow", "Diagonals"))
        self.label_start.setText(_translate("MainWindow", "Start"))
        self.btnCrear.setText(_translate("MainWindow", "Crear"))
        self.btnEnter.setText(_translate("MainWindow", "Enter"))
        self.label_end.setText(_translate("MainWindow", "End"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/jerrylogo.png/jerrylogo.png\"/></p></body></html>"))
        self.menuHello_World.setTitle(_translate("MainWindow", "Hello World!"))

    def pixelSelect(self,event):
        position = QtCore.QPoint(event.pos().x(),event.pos().y()) #Obtener un punto con las coordenadas clickeadas.

        #Brushes para los rectangulos
        negro= QtGui.QColor(0,0,0,255)
        blanco= QtGui.QColor(255,255,255,255)
        brushnegro= QtGui.QBrush(negro)
        brushblanco= QtGui.QBrush(blanco)
        
        for i in range(len(self.listaRec)):
            for j in range(len(self.listaRec[i])):
                #Rectangulo que clickees se volvera negro y el valor del laberinto sera 1 (bloqueo)
                if self.listaRec[i][j].contains(position) and self.array[i][j] == 0: 
                    self.listaRec[i][j].setBrush(brushnegro)
                    self.array[i][j] = 1
                #Lo  mismo pero diferente
                elif self.listaRec[i][j].contains(position) and self.array[i][j] == 1:
                    self.listaRec[i][j].setBrush(brushblanco)
                    self.array[i][j] = 0
    def btnCrearClicked(self):
        #Vaciar escena y progressa var
        self.scene.clear()
        self.listaRec=[]
        self.bar.setProperty("value", 0)
        #Obtener valores de los spinBox
        n= self.sbN.value()
        m= self.sbM.value()
        #Establecer valores para el poder decidir inicio y final
        self.spinBox_X1.setRange(0, n)
        self.spinBox_X2.setRange(0, n)
        self.spinBox_Y1.setRange(0, m)
        self.spinBox_Y2.setRange(0, m)
        #Hacer template del laberinto o GRID
        self.array= []
        for i in range(n):
            self.array.append([])
            for j in range(m):
                self.array[i].append(0)
        self.crearLaberinto() #Dibujar laberinto

    def crearLaberinto(self):
        #Datos de tamanios
        n= self.sbN.value()
        m= self.sbM.value()
        w= 1095
        h= 405
        cw= w/m
        ch= h/n
        #Color blanco para pintar
        color= QtGui.QColor(255,255,255,255)
        brush= QtGui.QBrush(color)
        #Hacer matriz de rectagulos y dibujarla
        for i in range(len(self.array)):
            self.listaRec.append([])
            for j in range(len(self.array[i])):
                rec= QtWidgets.QGraphicsRectItem(j*cw,i*ch,cw,ch)
                rec.setBrush(brush)
                self.scene.addItem(rec)
                self.listaRec[i].append(rec)     
        self.graphics.show() #Mostrar los rectangulos.
    def btnEnterClicked(self):
        #Borrar path anterior
##        print(self.scene)
##        items= self.scene.items()
##        for i in items:
##            print(i.color)
##            if i.color != QtGui.QColor(0,0,0,255) and i.color != QtGui.QColor(255,255,255,255):
##                print("hi")
##                self.scene.removeItem(i)
        #If vacio no hagas nada.
        if len(self.listaRec) == 0:
            return
        #Escoger algoritmo y resolver
        self.value=0 #Volver el valor de la barra a 0
        self.bar.setProperty("value", self.value) #Volver la barra de progreso a 0
        index= self.cbAlgoritmos.currentIndex() #Obtener el indice del combobox
        path=[] #Crear path
        path= self.algoritmos(self.array)
        #Para llenar el progress bar
        if index == 0 or index == 1: #A estrella y Bellman
            if len(path) > 0:
                valor= 100/len(path) 
            path= reversed(path)
        else:  #Dijkstra
            path=path[1]
            if len(path) > 0:
                valor= 100/len(path) 
        #Animacion para dibujar resolucion
        for i in path:
            self.value+=valor
            self.addPath(i) #Metodo para agregar un paso "step" de la solucion a la animacion
            QtTest.QTest.qWait(333) #Equivalente a time.sleep(sec) para esta interface Qt
            if self.value > 100: #Aqui ya es para trabajar con el progressbar
                self.value = 100
            self.bar.setProperty("value", self.value)

    def addPath(self, step):
        #De neuvo obteniendo valores de las dimensiones de la escena
        n= self.sbN.value()
        m= self.sbM.value()
        w= 1095
        h= 405
        cw= w/m
        ch= h/n

        #Para que coloree el inicio de un color distinto
        if step[0] == self.spinBox_X1.value()-1 and step[1] == self.spinBox_Y1.value()-1:
            color= QtGui.QColor(200,0,100,255)
        #Para que coloree el final de un color distinto
        elif step[0] == self.spinBox_X2.value()-1 and step[1] == self.spinBox_Y2.value()-1:
            color= QtGui.QColor(0,200,100,255)
        #Color para el camino
        else:
            color= QtGui.QColor(0,0,200,255)
        #Instanciar rectangulo con su posicion tamanio para ser agregado a la escena
        index= self.cbAlgoritmos.currentIndex() #Obtener el indice del combobox
        if index == 0: #A estrella
            brush= QtGui.QBrush(color)
            rec= QtWidgets.QGraphicsRectItem(step[1]*cw,step[0]*ch,cw,ch)
            rec.setBrush(brush)
            self.scene.addItem(rec)
            self.graphics.show()
        elif index == 1: #Bellman Ford
            brush= QtGui.QBrush(color)
            rec= QtWidgets.QGraphicsRectItem(step[1]*cw,step[0]*ch,cw,ch)
            rec.setBrush(brush)
            self.scene.addItem(rec)
            self.graphics.show()
        elif index == 2: #D Concurrente
            brush= QtGui.QBrush(color)
            rec= QtWidgets.QGraphicsRectItem(step[0]*cw,step[1]*ch,cw,ch)
            rec.setBrush(brush)
            self.scene.addItem(rec)
            self.graphics.show()
            
    def algoritmos(self,array):
        index= self.cbAlgoritmos.currentIndex()
        start=(self.spinBox_X1.value()-1,self.spinBox_Y1.value()-1) #Obtiene valores de los sBox
        end=(self.spinBox_X2.value()-1,self.spinBox_Y2.value()-1) #Obtiene valores de los sBox
        diagonales= self.checkBox_Diagonals.isChecked() #Checa si la diagonal esta permitida
        if index == 0: #A estrella
            path= astar(array, start, end, diagonales)
        elif index == 1: #Bellman Ford
            path= bellmanFord(array, start, end, diagonales) 
        elif index == 2: #D Concurrente
            path= dijkstraParallel(array, start, end, diagonales)
        if path == False: #Si no hay solucion
            return []
        return path

import resources_rc #Add Logo

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
