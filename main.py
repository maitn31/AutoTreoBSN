import PyQt5.uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
import sys
import subprocess
import webbrowser
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import uuid
import platform


def show_alert(content):
    alert = QMessageBox()
    alert.setWindowTitle("Error")
    alert.setText(str(content))
    alert.exec_()


def is_paid(key, dictionary):
    for value in dictionary.values():
        if isinstance(value, dict):
            if is_paid(key, value):
                return True
        elif isinstance(value, str):
            if key in value:
                return True
    return False


def search_name(my_dict, search_str):
    for key, value in my_dict.items():
        if value == search_str:
            return key
        elif isinstance(value, dict):
            sub_key = search_name(value, search_str)
            if sub_key is not None:
                return key
    return None


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        PyQt5.uic.loadUi("AutoTreoBSN.ui", self)
        self.setWindowTitle("Auto Treo BSN")

        appdata_path = os.getenv('APPDATA')
        directory_path = os.path.join(appdata_path, 'AutoCry', 'AutoTreoBSN')
        id_path = os.path.join(directory_path, 'id_list.txt')
        password_path = os.path.join(directory_path, "password.txt")
        config_path = os.path.join(directory_path, "config.txt")
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        if not os.path.exists(id_path):
            with open(id_path, 'w') as file:
                file.write("")  # Create an empty file
        if not os.path.exists(password_path):
            with open(password_path, 'w') as file:
                file.write("")  # Create an empty file
        if not os.path.exists(config_path):
            with open(config_path, 'w') as file:
                file.write("")  # Create an empty file
        config_path = os.path.join(directory_path, "config.txt")
        with open(config_path, 'r') as config_read:
            config = [line.strip() for line in config_read]
        try:
            self.findChild(QSpinBox, "amount_box").setValue(int(config[0]))
        except Exception as e:
            print(f"An error occurred: {e}")

        def copy_button_clicked():
            App.clipboard().setText(str(my_uuid))

        def facebook_button_clicked():
            webbrowser.open("https://www.facebook.com/CryAway")

        def username_button_clicked():
            os.startfile(id_path)

        def password_button_clicked():
            os.startfile(password_path)

        def start_button_clicked():
            starting_id = self.findChild(QSpinBox, "amount_box").value()
            with open(id_path, 'r') as id_read:
                id_path_content = id_read.read().strip()
            with open(password_path, 'r') as password_read:
                password_path_content = password_read.read().strip()
            if id_path_content == "":
                show_alert("Chua dien ID")
            elif password_path_content == "":
                show_alert("Chua dien Password")
            else:
                with open(config_path, 'w') as start_app:
                    start_app.write(f"{starting_id}\n")
                if authentication:
                    print("got here")
                    subprocess.call(['java', '-jar', 'config', '-r', './build/'])

        authentication = False
        namespace = uuid.uuid5(uuid.NAMESPACE_DNS, f"{platform.node()}-{uuid.getnode()}")
        my_uuid = uuid.uuid5(namespace, "unique_identifier_for_device")
        cred = credentials.Certificate("./auth")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://pythonprojecttest-4a5f6-default-rtdb.firebaseio.com'
        })
        ref = db.reference("/users/AutoTreoBSN")
        print("Checking....")
        try:
            if is_paid(str(my_uuid), ref.get()):
                print("Checked okay")
                authentication = True
                print("Hello", search_name(ref.get(), str(my_uuid)))
                # subprocess.call(['java', '-jar', 'config', '-r', './build/'])
            else:
                print("Vui long lien he fb.com/CryAway de duoc cap ban quyen")
                print("Ma dang nhap cua ban la ", my_uuid)
        except (ValueError, Exception):
            print("Vui long lien he fb.com/CryAway de duoc cap ban quyen")
            print("Ma dang nhap cua ban la ", my_uuid)

        copy_button = self.findChild(QPushButton, "copy_button")
        copy_button.clicked.connect(copy_button_clicked)
        id_label = self.findChild(QLabel, "id_label")
        id_label.setText(f"Your user ID is: {str(my_uuid)}")
        if authentication:
            id_label.setText(f"Hello {search_name(ref.get(), str(my_uuid))}")

        facebook_button = self.findChild(QPushButton, "facebook_button")
        facebook_button.clicked.connect(facebook_button_clicked)

        start_button = self.findChild(QPushButton, "start_button")
        start_button.clicked.connect(start_button_clicked)

        username_button = self.findChild(QPushButton, "username_button")
        username_button.clicked.connect(username_button_clicked)

        password_button = self.findChild(QPushButton, "password_button")
        password_button.clicked.connect(password_button_clicked)

        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    # start the app
    sys.exit(App.exec())
