from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit)
from PyQt5.QtGui import QFont, QIcon
import sys 





app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle('Instagram')
window.setWindowIcon(QIcon('Pictures\\insta.png'))
window.setGeometry(500, 200, 800, 500)

font = QFont()
font.setPixelSize(30)
font.setBold(True)

name_label = QLabel("Login", window)
name_label.move(850, 20)
name_label.setFont(font)

window.setStyleSheet('background: #8A2BE2;')


user_label = QLabel("Ism: ", window)
user_label.move(580, 100)
user_label.setFont(font)
user_edit = QLineEdit(window)
user_edit.move(750, 100)
user_edit.setStyleSheet('background: #FFF8DC; border-radius: 10px; border: 3px solid red;')
user_edit.setFont(font)



surname_label = QLabel("Lastname: ", window)
surname_label.move(580, 200)
surname_label.setFont(font)
surname_edit = QLineEdit(window)
surname_edit.move(750, 200)
surname_edit.setStyleSheet('background: #FFF8DC; border-radius: 10px; border: 3px solid red;')
surname_edit.setFont(font)



adres_label = QLabel("Adress: ", window)
adres_label.move(580, 300)
adres_label.setFont(font)
adres_edit = QLineEdit(window)
adres_edit.move(750, 300)
adres_edit.setStyleSheet('background: #FFF8DC; border-radius: 10px; border: 3px solid red;')
adres_edit.setFont(font)


def save_user():
    with open('llogin.txt', mode='wt') as file:
        file.write(f"Name: {user_edit.text()}\nSurname: {surname_edit.text()}\nAdress: {adres_edit.text()}\n")
    user_edit.clear()
    surname_edit.clear()
    adres_edit.clear()
    
    s = QLabel("Saqlandi", window)
    s.move(845, 350)
    s.setFont(font)
    s.show()
def clear_fields():
    name_edit.clear()
    lastname_edit.clear()
    adress_edit.clear()
    age_edit.clear()
    

clear_button = QPushButton("Clear", window)
clear_button.move(980, 380)
clear_button.setFont(font)
clear_button.setStyleSheet("background-color: red; border: 3px solid #0000FF; border-radius: 20px")
clear_button.clicked.connect(clear_fields)

save_button = QPushButton("Save", window)
save_button.move(750, 380)
save_button.setStyleSheet("background-color: red; border: 3px solid #0000FF; border-radius: 20px")
save_button.setFont(font)
save_button.clicked.connect(save_user)



window.show()
app.exec()
