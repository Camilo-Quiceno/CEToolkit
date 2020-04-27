"""Functions for the kpi tab."""

#PYQT
from PyQt5 import QtCore,QtGui

#CEToolkit
import CEToolkit
from func import stopwatchfunc

#Python
import datetime
import openpyxl
import os
import shutil

def register_button():
    """Take all the data of the KPI_register and write them in excel."""

    query = []
    case_id = parent.ui.lineEdit_kpi_caseid.text()
    surgery = parent.ui.comboBox_kpi_surgery.currentText()
    is_rev = parent.ui.comboBox_kpi_rev.currentText()
    is_qc = parent.ui.comboBox_kpi_qc.currentText()

    time = parent.ui.lineEdit_kpi_time.text()

    comments = parent.ui.textEdit_kpi_comments.toPlainText()

    if case_id is not '' or time is not '':
        try:
            time = int(time)

            query.extend((case_id,surgery,is_rev,is_qc,time,comments))
    
            send_data_excel(query)

        except ValueError:
            stopwatchfunc.error_message("Please input a number in the time field.")
    else:
        stopwatchfunc.error_message("Complete all the information (CaseID and time).")

def openkpi_button():
    """Get data of the file that user want to see."""

    month = parent.ui.comboBox_kpi_month.currentText()
    year = parent.ui.comboBox_kpi_year.currentText()

    template_to_use ="KPI" + month + year + ".xlsx"

    dirs = os.getcwd()+'/media/docs/kpi/'
    files = os.listdir(dirs)

    for i in files:
        if i == template_to_use:

            path = dirs + template_to_use
            os_url = "start "+path 
            os.system(os_url)

            break
        else:
            stopwatchfunc.error_message("There is no template for that date, contact admin.")
            break
            
def send_data_excel(query):
    """Send data to excel."""

    try:
        date = str(datetime.date.today())
        date = date.split("-")
        
        search_template(date)
        worksheet = define_sheet(query)
        write_info(query=query,date=date,worksheet=worksheet)

        stopwatchfunc.success_message("Your case was sended")

        parent.ui.lineEdit_kpi_caseid.setText("")
        
        parent.ui.comboBox_kpi_surgery.setCurrentIndex(0)
        parent.ui.comboBox_kpi_rev.setCurrentIndex(0)
        parent.ui.comboBox_kpi_qc.setCurrentIndex(0)

        parent.ui.lineEdit_kpi_time.setText("")
        parent.ui.textEdit_kpi_comments.setText("")


    except PermissionError:
        stopwatchfunc.error_message("Please close the Excel file to save the info.")
    
def search_template(date):
    """Look the file or create it."""

    dirs = os.getcwd()+'/media/docs/kpi/'
    files = os.listdir(dirs)

    template_to_use = "KPI" + date[1] + date[0] + ".xlsx"
    
    for i in files:
        if i == template_to_use:
            break
        else:
            origin = dirs + "KPITemplate.xlsx"
            destiny = dirs + template_to_use

            shutil.copy(origin, destiny)

            mydate = datetime.datetime.now()
            month = mydate.strftime("%B")

            wb = openpyxl.load_workbook(dirs+template_to_use)
            source = wb.worksheets[0]
            title = "{} {}".format(month,date[0])
            source["B1"] = title
            wb.save(dirs+template_to_use)
            break

def define_sheet(query):
    """Define in what sheet is going to write the info."""

    asa = query[1].split(" ")

    if asa[0] == "Seg" and query[3] == "NO":
        return 1

    if asa[0] == "Seg" and query[3] == "YES":
        return 2

    if asa[0] == "Des" and query[3] == "NO":
        return 3

    if asa[0] == "Des" and query[3] == "YES":
        return 4
    
def write_info(query,date,worksheet):
    """Write the info in excel."""

    path = os.getcwd()+'/media/docs/kpi/' + "KPI" + date[1] + date[0] + ".xlsx"
    wb = openpyxl.load_workbook(path)
    
    surgery = query[1].split(" ")
    query[1] = surgery[1]

    if worksheet ==1:
        source = wb.worksheets[worksheet]
        for idx,cell in enumerate(source['A']):
            if cell.value == None:
                
                cell.value = query[0]
                
                source["B"+str(idx+1)] = query[1]
                source["C"+str(idx+1)] = query[2]
                source["D"+str(idx+1)] = date[2]
                source["E"+str(idx+1)] = date[1]
                source["F"+str(idx+1)] = date[0]
                source["G"+str(idx+1)] = query[4]
                source["I"+str(idx+1)] = query[5]
                
                wb.save(path)
                break

    elif worksheet == 2:
        source = wb.worksheets[worksheet]
        for idx,cell in enumerate(source['A']):
            if cell.value == None:
                
                cell.value = query[0]
                
                source["B"+str(idx+1)] = query[1]
                source["C"+str(idx+1)] = query[2]
                source["D"+str(idx+1)] = date[2]
                source["E"+str(idx+1)] = date[1]
                source["F"+str(idx+1)] = date[0]
                source["G"+str(idx+1)] = query[4]
                source["H"+str(idx+1)] = query[5]
                
                wb.save(path)
                break
    
    elif worksheet == 3:
        source = wb.worksheets[worksheet]
        for idx,cell in enumerate(source['A']):
            if cell.value == None:
                
                cell.value = query[0]
                
                source["B"+str(idx+1)] = query[1]
                source["C"+str(idx+1)] = query[2]
                source["D"+str(idx+1)] = date[2]
                source["E"+str(idx+1)] = date[1]
                source["F"+str(idx+1)] = date[0]
                source["G"+str(idx+1)] = query[4]
                source["I"+str(idx+1)] = query[5]

                wb.save(path)
                break

    elif worksheet == 4:
        source = wb.worksheets[worksheet]
        for idx,cell in enumerate(source['A']):
            if cell.value == None:
                
                cell.value = query[0]
                
                source["B"+str(idx+1)] = query[1]
                source["C"+str(idx+1)] = query[2]
                source["D"+str(idx+1)] = date[2]
                source["E"+str(idx+1)] = date[1]
                source["F"+str(idx+1)] = date[0]
                source["G"+str(idx+1)] = query[4]
                source["H"+str(idx+1)] = query[5]

                wb.save(path)
                break