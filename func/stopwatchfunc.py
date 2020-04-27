"""Functions for the stopwatch tab."""

#PYQT
from PyQt5 import QtCore
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QMessageBox

#CEToolkit
import CEToolkit

def calculate_time_up():
    """Do the logic of the clock up."""

    CEToolkit.second += 1
    if CEToolkit.second == 60:
        CEToolkit.minute+=1
        CEToolkit.second = 0
        CEToolkit.secondLCD ="00"
    if CEToolkit.minute == 60:
        CEToolkit.hour+=1
        CEToolkit.minute = 0
        CEToolkit.minuteLCD = "00"
    if CEToolkit.hour == 60:
        pass
    if CEToolkit.second<10:
        CEToolkit.secondLCD = "0" + str(CEToolkit.second)
    else:
        CEToolkit.secondLCD = CEToolkit.second
    if CEToolkit.minute<10:
        CEToolkit.minuteLCD = "0" + str(CEToolkit.minute)
    else:
        CEToolkit.minuteLCD = CEToolkit.minute
    if CEToolkit.hour<10:
        CEToolkit.hourLCD = "0" + str(CEToolkit.hour)
    else:
        CEToolkit.hourLCD = CEToolkit.hour
    CEToolkit.text = "{}:{}:{}".format(CEToolkit.hourLCD,CEToolkit.minuteLCD,CEToolkit.secondLCD)
    parent.ui.lcdNumber_stopwatch.display(CEToolkit.text)

def calculate_time_down():
    """Do the logic of the clock dowmn."""

    if CEToolkit.second >= 60:
        CEToolkit.second = 59

    if CEToolkit.minute >= 60:
        CEToolkit.second = 59

    if CEToolkit.second >= 100:
        CEToolkit.second = 99
 
    if CEToolkit.second<10:
        CEToolkit.secondLCD = "0" + str(CEToolkit.second)
    else:
        CEToolkit.secondLCD = CEToolkit.second

    if CEToolkit.minute<10:
        CEToolkit.minuteLCD = "0" + str(CEToolkit.minute)
    else:
        CEToolkit.minuteLCD = CEToolkit.minute

    if CEToolkit.hour<10:
        CEToolkit.hourLCD = "0" + str(CEToolkit.hour)
    else:
         CEToolkit.hourLCD = CEToolkit.hour

    CEToolkit.text = "{}:{}:{}".format(CEToolkit.hourLCD,CEToolkit.minuteLCD,CEToolkit.secondLCD)
    parent.ui.lcdNumber_stopwatch.display(CEToolkit.text)

    if CEToolkit.second == 0:
        CEToolkit.minute-=1
        CEToolkit.second = 60
        CEToolkit.secondLCD="00"

    if CEToolkit.minute == (-1) and CEToolkit.second == 60:
        if CEToolkit.hour == 0:
            parent.ui.timer.stop()
        CEToolkit.hour -= 1
        CEToolkit.minute = 59
        CEToolkit.minuteLCD = "59"

    CEToolkit.second -= 1

def stop_time():
    """Add the values of the current clock to the line edit text."""

    parent.ui.lineEdit_stopwatch_seconds.setText(str(CEToolkit.secondLCD))
    parent.ui.lineEdit_stopwatch_minutes.setText(str(CEToolkit.minuteLCD))
    parent.ui.lineEdit_stopwatch_hour.setText(str(CEToolkit.hourLCD))

def reset_time():
    """Reset timer variables, makes lcd display 00:00:00."""

    CEToolkit.second = 0
    CEToolkit.minute = 0
    CEToolkit.hour = 0
    parent.ui.lcdNumber_stopwatch.display("00:00:00")

def set_countdown_values(hour,minute,second):
    """Set the values requested by the user in the lcd display."""

    CEToolkit.second = second
    CEToolkit.minute = minute
    CEToolkit.hour = hour

def comboBox_stopwatch_targets_change():
    """Assing the correct values to the line edit text depending of the comboBox index."""

    if parent.ui.comboBox_stopwatch_targets.currentIndex() == 1:
        parent.ui.lcdNumber_stopwatch.display("01:30:00")
        parent.ui.lineEdit_stopwatch_hour.setText("01")
        parent.ui.lineEdit_stopwatch_minutes.setText("30")
        set_countdown_values(1,30,0)

    if parent.ui.comboBox_stopwatch_targets.currentIndex() == 2:
        parent.ui.lcdNumber_stopwatch.display("02:00:00")
        parent.ui.lineEdit_stopwatch_hour.setText("02")
        parent.ui.lineEdit_stopwatch_minutes.setText("00")
        set_countdown_values(2,00,0)

    if parent.ui.comboBox_stopwatch_targets.currentIndex() == 3:
        parent.ui.lcdNumber_stopwatch.display("00:13:00")
        parent.ui.lineEdit_stopwatch_hour.setText("00")
        parent.ui.lineEdit_stopwatch_minutes.setText("13")
        set_countdown_values(0,13,0)
    
    if parent.ui.comboBox_stopwatch_targets.currentIndex() == 4:
        parent.ui.lcdNumber_stopwatch.display("00:30:00")
        parent.ui.lineEdit_stopwatch_hour.setText("00")
        parent.ui.lineEdit_stopwatch_minutes.setText("30")
        set_countdown_values(0,30,0)

    if parent.ui.comboBox_stopwatch_targets.currentIndex() == 5:
        parent.ui.lcdNumber_stopwatch.display("03:00:00")
        parent.ui.lineEdit_stopwatch_hour.setText("03")
        parent.ui.lineEdit_stopwatch_minutes.setText("00")
        set_countdown_values(3,0,0)
    
    if parent.ui.comboBox_stopwatch_targets.currentIndex() == 6:
        parent.ui.lcdNumber_stopwatch.display("04:00:00")
        parent.ui.lineEdit_stopwatch_hour.setText("04")
        parent.ui.lineEdit_stopwatch_minutes.setText("00")
        set_countdown_values(4,0,0)

def calculate_diff(ValueError):
    """Calculate the dif time."""

    try:
        adjust_time = int(parent.ui.lineEdit_stopwatch_adjustment.text())
    
        start_time = parent.ui.dateTimeEdit_stopwatch_start.dateTime()
        start_time_string = start_time.toString(parent.ui.dateTimeEdit_stopwatch_start.displayFormat())
        start_time_hour = int(start_time_string[1]+start_time_string[2])
        start_time_minute = int(start_time_string[4]+start_time_string[5])

        end_time = parent.ui.dateTimeEdit_stopwatch_end.dateTime()
        end_time_string = end_time.toString(parent.ui.dateTimeEdit_stopwatch_end.displayFormat())
        end_time_hour = int(end_time_string[1]+end_time_string[2])
        end_time_minute = int(end_time_string[4]+end_time_string[5])

        total_time_hour = end_time_hour - start_time_hour
        total_time_hour = total_time_hour*60

        if end_time_minute > start_time_minute:
            total_time_minute = end_time_minute - start_time_minute
            total_time = total_time_hour + total_time_minute - adjust_time
        else:
            total_time_minute = start_time_minute - end_time_minute
            total_time = total_time_hour - total_time_minute - adjust_time

        parent.ui.lineEdit_stopwatch_total.setText(str(total_time))

    except:
        error_message("Please input a number")

def error_message(message):
    """Create the error box of a message."""

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(message)
    msg.setWindowTitle("Error")
    msg.exec_()

def success_message(message):
    """Create the success box of a message."""

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Success")
    msg.setInformativeText(message)
    msg.setWindowTitle("Send")
    msg.exec_()