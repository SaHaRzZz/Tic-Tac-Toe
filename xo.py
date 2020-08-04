from PyQt5 import QtWidgets, uic, QtCore
import sys
import os

class SubUi(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SubUi, self).__init__(parent)
        uic.loadUi(os.path.dirname(sys.argv[0]) + '\\xoSetNames.ui', self)

        self.setWindowTitle("Set Names")

        self.b_cancel.clicked.connect(self.hide)
        self.b_confirm.clicked.connect(lambda: self.b_confirm_clicked())
        self.mainWindow = parent
    
    def b_confirm_clicked(self):
        if self.te_X.toPlainText() != '':
            self.mainWindow.xName = self.te_X.toPlainText()
        else:
            self.mainWindow.xName = 'X'
        if self.te_O.toPlainText() != '':
            self.mainWindow.oName = self.te_O.toPlainText()
        else:
            self.mainWindow.oName = 'O'
        self.mainWindow.XO()
        self.mainWindow.XO()
        self.hide()


class Ui(QtWidgets.QMainWindow):
    global xo
    xo = 'O'
    global gameOver
    gameOver = False
    xName = 'X'
    oName = 'O'

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(os.path.dirname(sys.argv[0]) + '\\xo.ui', self)

        self.setWindowTitle("Tic-Tac-Toe by Sahar")
        self.setFixedSize(300, 351)
        self.status.setText("X's turn")

        self.a_newGame.triggered.connect(self.a_newGame_clicked)
        self.a_quit.triggered.connect(quit)
        self.a_setNames.triggered.connect(lambda: self.a_actSubWindow())
        self.b1.clicked.connect(lambda: self.b_clicked1(str(1)))
        self.b2.clicked.connect(lambda: self.b_clicked2(str(2)))
        self.b3.clicked.connect(lambda: self.b_clicked3(str(3)))
        self.b4.clicked.connect(lambda: self.b_clicked4(str(4)))
        self.b5.clicked.connect(lambda: self.b_clicked5(str(5)))
        self.b6.clicked.connect(lambda: self.b_clicked6(str(6)))
        self.b7.clicked.connect(lambda: self.b_clicked7(str(7)))
        self.b8.clicked.connect(lambda: self.b_clicked8(str(8)))
        self.b9.clicked.connect(lambda: self.b_clicked9(str(9)))
        self.dialog = SubUi(self)
    
    def a_actSubWindow(self):
        self.dialog.te_X.setText(self.xName)
        self.dialog.te_O.setText(self.oName)
        self.dialog.show()

    def a_newGame_clicked(self):
        listOfButtons = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]
        for b in listOfButtons:
            b.setText('-')
            b.setStyleSheet("background-color: None")
        global gameOver
        gameOver = False
        self.XO()

    def b_clicked1(self, b_num):
        if self.b1.text() != '-' or gameOver:
            return
        self.b1.setText(self.XO())
        self.checkWin()

    def b_clicked2(self, b_num):
        if self.b2.text() != '-' or gameOver:
            return
        self.b2.setText(self.XO())
        self.checkWin()

    def b_clicked3(self, b_num):
        if self.b3.text() != '-' or gameOver:
            return
        self.b3.setText(self.XO())
        self.checkWin()

    def b_clicked4(self, b_num):
        if self.b4.text() != '-' or gameOver:
            return
        self.b4.setText(self.XO())
        self.checkWin()

    def b_clicked5(self, b_num):
        if self.b5.text() != '-' or gameOver:
            return
        self.b5.setText(self.XO())
        self.checkWin()

    def b_clicked6(self, b_num):
        if self.b6.text() != '-' or gameOver:
            return
        self.b6.setText(self.XO())
        self.checkWin()

    def b_clicked7(self, b_num):
        if self.b7.text() != '-' or gameOver:
            return
        self.b7.setText(self.XO())
        self.checkWin()

    def b_clicked8(self, b_num):
        if self.b8.text() != '-' or gameOver:
            return
        self.b8.setText(self.XO())
        self.checkWin()

    def b_clicked9(self, b_num):
        if self.b9.text() != '-' or gameOver:
            return
        self.b9.setText(self.XO())
        self.checkWin()
    
    def XO(self):
        global xo
        if xo == 'X':
            xo = 'O'
            self.status.setText(self.xName + "'s turn")
        else:
            xo = 'X'
            self.status.setText(self.oName + "'s turn")
        return xo

    def checkWin(self):
        b = [self.b1.text(), self.b2.text(), self.b3.text(), self.b4.text(), self.b5.text(), self.b6.text(), self.b7.text(), self.b8.text(), self.b9.text()]
        global gameOver
        if b[0] == b[1] == b[2] != '-':
            self.b1.setStyleSheet("background-color: green")
            self.b2.setStyleSheet("background-color: green")
            self.b3.setStyleSheet("background-color: green")
            if b[0] == 'X':
                winner = self.xName
            else:
                winner = self.oName
            self.status.setText(winner + ' won!')
            gameOver = True
        if b[3] == b[4] == b[5] != '-':
            self.b4.setStyleSheet("background-color: green")
            self.b5.setStyleSheet("background-color: green")
            self.b6.setStyleSheet("background-color: green")
            if b[3] == 'X':
                winner = self.xName
            else:
                winner = self.oName
            self.status.setText(winner + ' won!')
            gameOver = True
        if b[6] == b[7] == b[8] != '-':
            self.b7.setStyleSheet("background-color: green")
            self.b8.setStyleSheet("background-color: green")
            self.b9.setStyleSheet("background-color: green")
            if b[6] == 'X':
                winner = self.xName
            else:
                winner = self.oName
            self.status.setText(winner + ' won!')
            gameOver = True
        if b[0] == b[3] == b[6] != '-':
            self.b1.setStyleSheet("background-color: green")
            self.b4.setStyleSheet("background-color: green")
            self.b7.setStyleSheet("background-color: green")
            if b[0] == 'X':
                winner = self.xName
            else:
                winner = self.oName
            self.status.setText(winner + ' won!')
            gameOver = True
        if b[1] == b[4] == b[7] != '-':
            self.b2.setStyleSheet("background-color: green")
            self.b5.setStyleSheet("background-color: green")
            self.b8.setStyleSheet("background-color: green")
            if b[1] == 'X':
                winner = self.xName
            else:
                winner = self.oName
            self.status.setText(winner + ' won!')
            gameOver = True
        if b[2] == b[5] == b[8] != '-':
            self.b3.setStyleSheet("background-color: green")
            self.b6.setStyleSheet("background-color: green")
            self.b9.setStyleSheet("background-color: green")
            if b[2] == 'X':
                winner = self.xName
            else:
                winner = self.oName
            self.status.setText(winner + ' won!')
            gameOver = True
        if b[0] == b[4] == b[8] != '-':
            self.b1.setStyleSheet("background-color: green")
            self.b5.setStyleSheet("background-color: green")
            self.b9.setStyleSheet("background-color: green")
            if b[0] == 'X':
                winner = self.xName
            else:
                winner = self.oName
            self.status.setText(winner + ' won!')
            gameOver = True
        if b[2] == b[4] == b[6] != '-':
            self.b3.setStyleSheet("background-color: green")
            self.b5.setStyleSheet("background-color: green")
            self.b7.setStyleSheet("background-color: green")
            if b[2] == 'X':
                winner = self.xName
            else:
                winner = self.oName
            self.status.setText(winner + ' won!')
            gameOver = True
        if b[0] != '-' and b[1] != '-' and b[2] != '-' and b[3] != '-' and b[4] != '-' and b[5] != '-' and b[6] != '-' and b[7] != '-' and b[8] != '-' and gameOver != True:
            self.status.setText("Nobody won!")
            

app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()

app.exec_()

# b0 | b1 | b2
# b3 | b4 | b5
# b6 | b7 | b8