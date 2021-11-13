from PyQt5 import QtWidgets # формы надписи и тп
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
#QtWidgets позволяют добавлять кнопки, текст , и т п.

class TEST(QMainWindow):
    def __init__(self):
        super(TEST,self).__init__() # Базовые настройки для главного класса ## БЕЗ .__init__() НИХУЯ НЕ РАБОТАЕТ

# self - это самообращение.
        #  window2 = QMainWindow()  # Создание основного окна
        # window2.setWindowTitle("Название главного окна2")
        # window2.setGeometry(1000, 250, 500, 500)# Параметры окна ( 1 два числа это смещение слева, 2 числа это разрешение окна )
        self.setWindowTitle("Название главного окна")
        self.setGeometry(1000, 250, 500,
                           500)  # Параметры окна ( 1 два числа это смещение слева, 2 числа это разрешение окна )
# Здесь self указывает то, что эти переменные, кнопки и т п, принадлежат этому окну. ( классу )
        self.Peremennaya = QtWidgets.QLabel(self)  # что.чточто( В какое окно вывести )
        self.Peremennaya.setText("Словоываыаыаваываываываываываыа1")  # Указание надписи
        self.Peremennaya.move(100, 100)  # Отсуп от левого верхнего угла окна
        self.Peremennaya.adjustSize()  # Сам добавляет необходимое пространство для объекта

        self.Cnopka = QtWidgets.QPushButton(self)  # В данной ситуации мы добавляем кнопку к окну
        self.Cnopka.move(100, 150)
        self.Cnopka.setText("ЁП ТВОЮ МАТЬ")  # указывание текста для кнопки
        self.Cnopka.setFixedWidth(200)  # Установка фиксированной ширины
        self.Cnopka.clicked.connect(self.CnopkaWORK)  # Добввление кнопки клика и ссылание на действие


        # window2.show()  # Вызов окна

    def CnopkaWORK(self):  # Здесь мы метод в класс
        print("НЕУЖЕЛИ")





def OSNOVA():
    app = QApplication(sys.argv)  # Передача проге инфе о железе ( делается 1 раз )
    window = TEST()  # Создание основного окна # Поменяли класс на свой
    window.show()  # Вызов окна
    sys.exit(app.exec_())  # Корректное завершение программы

if __name__ == "__main__": # Если этот файл запустить как основной, то запуститься функция OSNOVA
    OSNOVA()