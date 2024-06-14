from PyQt6.QtWidgets import QVBoxLayout,QHBoxLayout,QWidget,QPushButton,QApplication,QMainWindow,QTextEdit,QGridLayout,QLineEdit
import sys


class my_app(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("CALCULATOR")
        self.resize(700,500)

        btn_layout =QGridLayout()
        layout = QVBoxLayout()
        in_layout = QHBoxLayout()
        out_layout =QHBoxLayout()

         # buttons
        button1 = QPushButton("9")
        button1.clicked.connect(self.onclick)

        button2 = QPushButton("8")
        button2.clicked.connect(self.onclick)

        button3 = QPushButton("7")
        button3.clicked.connect(self.onclick)
        
        button4 = QPushButton("/")
        button4.clicked.connect(self.onclick)

        button5 = QPushButton("6")
        button5.clicked.connect(self.onclick)

        button6 = QPushButton("5")
        button6.clicked.connect(self.onclick)

        button7 = QPushButton("4")
        button7.clicked.connect(self.onclick)

        button8 = QPushButton("*")
        button8.clicked.connect(self.onclick)

        button9 = QPushButton("3")
        button9.clicked.connect(self.onclick)

        button10 = QPushButton("2")
        button10.clicked.connect(self.onclick)

        button11 = QPushButton("1")
        button11.clicked.connect(self.onclick)
        
        button12 = QPushButton("-")
        button12.clicked.connect(self.onclick)

        button13 = QPushButton("0")
        button13.clicked.connect(self.onclick)

        button14 = QPushButton(".")
        button14.clicked.connect(self.onclick)

        button15 = QPushButton("00")
        button15.clicked.connect(self.onclick)

        button16 = QPushButton("+")
        button16.clicked.connect(self.onclick)

        button17 = QPushButton("=")
        button17.clicked.connect(self.calculate)

        button18 = QPushButton("C")
        button18.clicked.connect(self.clear)

        button19 = QPushButton("<--")
        button19.clicked.connect(self.remove)

        button20 = QPushButton("%")
        button20.clicked.connect(self.onclick)

        # input field
        self.inputField = QLineEdit()

        # output field
        #self.output = QTextEdit()

        # Layout-1
        in_layout.addWidget(self.inputField)
        layout.addLayout(in_layout)

        # Layout-2
        #out_layout.addWidget(self.output)
        #layout.addLayout(out_layout)
        
        # Layout-3
        btn_layout.addWidget(button18,0,0)
        btn_layout.addWidget(button19,0,1)
        btn_layout.addWidget(button17,0,2)
        btn_layout.addWidget(button20,0,3)
        
        btn_layout.addWidget(button1,1,0)
        btn_layout.addWidget(button2,1,1)
        btn_layout.addWidget(button3,1,2)
        btn_layout.addWidget(button4,1,3)

        btn_layout.addWidget(button5,2,0)
        btn_layout.addWidget(button6,2,1)
        btn_layout.addWidget(button7,2,2)
        btn_layout.addWidget(button8,2,3)

        btn_layout.addWidget(button9,3,0)
        btn_layout.addWidget(button10,3,1)
        btn_layout.addWidget(button11,3,2)
        btn_layout.addWidget(button12,3,3)

        btn_layout.addWidget(button13,4,0)
        btn_layout.addWidget(button14,4,1)
        btn_layout.addWidget(button15,4,2)
        btn_layout.addWidget(button16,4,3)

        layout.addLayout(btn_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def onclick(self) :
        sender = self.sender()
        text = sender.text()
        pre_text = self.inputField.text()
        self.inputField.setText(pre_text+text)
    
    def clear(self) :
        self.inputField.clear()

    def clear_o(self):
        self.output.clear()
    
    def remove(self)  :
        text= self.inputField.text()
        if text :
            t = text[:-1]
            self.inputField.setText(t)

    def calculate(self):
        text = self.inputField.text()
        a = str(eval(text))
        #self.clear_o()
        self.inputField.setText(a)



        
app = QApplication(sys.argv)

app.setStyleSheet("""
    QWidget {

    background-color : Black;
    font-size : 25px;
    color : White ;

}
QLineEdit {
    padding : 20px ;
    border-radius : 25px ;
    font-size : 18px ;
    text-align: center;
    background-color : LightBlue ;
    color : Black ;
}
QTextEdit {
    padding : 0px ;
    border-radius : 25px ;
    font-size : 18px ;
    text-align: center;
    background-color : LightBlue ;
    color : Black ;
}
QGridLayout {
    grid ;
    

}
QPushButton {
    padding  : 20px ;
    font-size : 20px ;
    border-radius : 25px ;
    border = none ;
    background-color : LightBlue ;
    color : Black ;
    cursor : pointer ;
    transistion : background-color 0.3s ;

}
QPushButton:hover{
    background-color : White ;
}
QLineEdit:hover{
    background-color : White ;
}
QTextEdit:hover{
    background-color : White ;
}
""")

window = my_app()
window.show()

sys.exit(app.exec())
