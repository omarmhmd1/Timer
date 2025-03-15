# Import Modules
import os
import sys
import time

import pyttsx3
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from playsound import playsound

# Check of kind OS
system_name = platform.system()

# Run the PYTTSX3 (For convert text to speech)
engine = pyttsx3.init()

# Create app
app = QtWidgets.QApplication(sys.argv)

# Create Main Window
root = QtWidgets.QWidget()
root.show()
root.resize(400,300)
root.setWindowTitle("Timer")
root.setWindowIcon(QtGui.QIcon("icon.png"))
root.setStyleSheet("background: #205781;border-radius: 10px;")
root.setFixedSize(400,300)


# Function for BUTTON
def store_values():
    # Get value from dropdown
    selected_option = dropdown.currentText()
    # Get value from input field
    entered_text = input_field.text()

    # Check OS
    if system_name not in ["Windows", "Darwin", "Linux"]:
        msg = QtWidgets.QMessageBox(root)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Error OS")
        msg.setText("Sorry, There app can't run on Your Operating System !") 
        msg.setStyleSheet("background:white;")
        msg.exec_()
        return

    if not entered_text.isdigit():
        msg1 = QtWidgets.QMessageBox(root)
        msg1.setIcon(QtWidgets.QMessageBox.Information)
        msg1.setWindowTitle("Error Value")
        msg1.setText("Please, Enter a correct value") 
        msg1.setStyleSheet("background:white;")
        msg1.exec_()
        return

    # Show Info

    msg = QtWidgets.QMessageBox(root)
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowTitle("Show Info")
    msg.setText(f"You choose {entered_text} {selected_option} for Timer") 
    msg.setStyleSheet("background:white;")
    msg.exec_()
    
    # Hide the window
    root.hide()

    # Variable 
    second = 1

    # Check the unit
    if selected_option == "Seconds":
        second = 1
    elif selected_option == "Minutes":
        second = 60
    elif selected_option == "Hours":
        second = 60 * 60 
    else:
        msg = QtWidgets.QMessageBox(root)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Error !!")
        msg.setText("Sorry, There is Error !") 
        msg.setStyleSheet("background:white;")
        msg.exec_()
        return

    # Calculate the total seconds
    
    entered_text = int(entered_text)
    total_seconds = second * entered_text
    total_seconds = int(total_seconds)

    target_time = time.time() + total_seconds  

    while time.time() < target_time:
        time.sleep(0.1)

    for i in range(2):
        playsound("whistle.wav")
        time.sleep(5)
    
    engine.say("Time Out")
    engine.say("Ready")
    engine.runAndWait()
    

    time.sleep(120)
    
    playsound("countdown.wav")
    
    if system_name == "Windows":
       os.system("shutdown /s /f /t 0")
       
    elif system_name == "Darwin" or system_name == "Linux":
        os.system("sudo shutdown -h now")

    else:
       msg = QtWidgets.QMessageBox(root)
       msg.setIcon(QtWidgets.QMessageBox.Information)
       msg.setWindowTitle("Error OS")
       msg.setText("Sorry, There app can run on Windows only!") 
       msg.setStyleSheet("background:white;")
       msg.exec_()  


    






dropdown = QtWidgets.QComboBox(root)
dropdown.addItem("Seconds")
dropdown.addItem("Minutes")
dropdown.addItem("Hours")
dropdown.setStyleSheet("background: white;color: black;border-radius: 10px;font-size: 15px;")
dropdown.resize(250,30)
dropdown.move(75,100)
dropdown.show()

# Create The Input Field 
input_field = QtWidgets.QLineEdit(root)
input_field.setPlaceholderText("Enter Number of (Seconds/Minutes/Hours)")
input_field.setStyleSheet("background: white;color: black;border-radius: 10px;font-size: 15px;")
input_field.resize(250,30)
input_field.move(75,150)
input_field.show()

# Create The Button
button = QtWidgets.QPushButton("START",root)
button.setStyleSheet("QPushButton{background-color: #205781;border-radius: 10px;font-size: 20px;font-family: 'Bauhaus 93';color: white;border: 2px solid white;}QPushButton:hover{background-color: white;cursor: pointer;color:#2b6ea1;}")
button.resize(150,50)
button.move(125,200)
button.clicked.connect(store_values)
button.show()

# Run the App
app.exec_()




