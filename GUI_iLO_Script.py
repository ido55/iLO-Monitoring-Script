import shutil
import numpy as np
import pandas as pd
import subprocess
import threading
import tkinter
import os
global counter
global NUMiLOs
global iLOipFile
global iLOs
global iLOCoList
global root

global Username
global Password

from tkinter import *
from tkinter.ttk import *
counter = 0

iLOipFile = open("C:/ScriptFiles/iloListTestNew.txt")
iLOs = iLOipFile.read()
iLOCoList = iLOs.split("\n")
NUMiLOs = 0
for i in iLOCoList:
    if i:
        NUMiLOs += 1
print(NUMiLOs)



########################################################
# function for getting data from iLOs to a text file:s
def getDataToTextFile():
    localCounter = 0
    xmlScript = "C:/ScriptFiles/Get-ALL.xml"
    UserName = U_input
    Password = P_input
    logFile = "C:/ScriptFiles/log.txt"
    OutputFile = "C:/ScriptFiles/output1.txt"
    ResultsFile = "C:/ScriptFiles/results2.txt"
    ResultsFileNetwork = "C:/ScriptFiles/resultsN2.txt"

    # deleting the previous results at start of script:

    Results = open(ResultsFile, "w")
    Results.truncate(0)
    Results.close()
    Results = open(ResultsFile, "a")

    ResultsNetwork = open(ResultsFileNetwork, "w")
    ResultsNetwork.truncate(0)
    ResultsNetwork.close()
    ResultsNetwork = open(ResultsFileNetwork, "a")


    cmd1 = "cd C:\Program Files (x86)\Hewlett Packard Enterprise\HP Lights-Out Configuration Utility && "

    #for loop for all the iLOs to be checked:

    for i in iLOCoList:
        cmd2 = 'hpqlocfg -f {0} -s {1} -t user="{2}",password="{3}" -l {4} >> {5}'.format(xmlScript, i, UserName,
                                                                                          Password, logFile, OutputFile)
        subprocess.run(cmd1 + cmd2 , shell = TRUE)
        Output = open(OutputFile, "r")
        lines = Output.read().split("\n")
        Results.write("IP Address= " + i + "\n")
        ResultsNetwork.write("IP Address= " + i + "\n")
        for n in lines:
            if n.find("BIOS_HARDWARE") != -1 or n.find("FANS") != -1 or n.find("TEMPERATURE") != -1 or n.find(
                    "POWER_SUPPLIES") != -1 or n.find("PROCESSOR") != -1 or n.find("MEMORY") != -1 or n.find(
                    "NETWORK") != -1 or n.find("STORAGE") != -1 or n.find("SERVER_NAME") != -1 or n.find(
                    "PRODUCT_NAME") != -1 or n.find("FIRMWARE_VERSION") != -1:

                Results.write(n + "\n")

            else:
                if n.find("ILO_IP_Address") != -1 or n.find("NETWORK_PORT") != -1 or n.find(
                        "IP_ADDRESS") != -1 or n.find("STATUS VALUE") != -1:
                    ResultsNetwork.write(n + "\n")
        Output.close()
        Output = open(OutputFile, "w")
        Output.truncate(0)
        Output.close()
        localCounter += 1
        global counter
        counter = localCounter
        print(counter)

####################################################################

#Functions that Trnasfer the text data into the EXCEL#
global numOfCopy
numOfCopy = 0


def Text_To_Excel():
    global root
    global button
    button = Button(root, command=TDF, text='Start Process', width=12)  # Button for the data to get into text file
    button.pack()
    button.place(x=1065, y=449)
    if L3['text'] == "Script in Progress":
        root = Tk()
        root.geometry('300x100')
        root.title('ERROR')
        root.resizable("false", "false")
        ErrorLable = tkinter.Label(root, text='ERROR,',font=("David",11),fg="BLACK")
        ErrorLable2 = tkinter.Label(root,text ="WAIT FOR THE SCRIPT TO FINISH \n BEFOR EXPORTING TO EXCEL",font=("David",11),fg="BLACK")
        ErrorLable.place(x=0,y=0)
        ErrorLable2.place(x=0, y=20)

    else:
        df = pd.read_excel(r'C:/ScriptFiles/ILOs_And_Sites.xlsx', sheet_name="Sites")
        IP_Addresses = df["IP"]
        Sites = df["Site"]
        SiteCount = 0

        for i in IP_Addresses:
            SiteCount += 1

        #############DELETE BLANK LINES###################
        a_file = open("C:/ScriptFiles/results2.txt", "r")
        lines = a_file.readlines()
        a_file.close()

        new_file = open("C:/ScriptFiles/FinalResults1.txt", "w")

        for line in lines:
            if "=" in line:
                New_Line = line.replace("<", "")
                N1 = New_Line.replace(">", "")
                N2 = N1.replace("/", "")
                N3 = N2.replace('"', "")
                new_file.write(N3)

        new_file.close()
        ############ SORT EXCELL###################
        FinalResultsFile1 = "C:/ScriptFiles/FinalResults1.txt"
        file1 = open(FinalResultsFile1, 'r+')
        content = file1.readlines()
        list = []
        rows = 0
        columns = 2
        for i in content:
            row = i.split('=')
            T = [row[0], row[1]]
            list.append(T)
            rows = rows + 1
        print(list)

        improvedList = [
            ["ip address ","Site Name", "ServerName", "iLO Product verion", "iLO Version", "Bios Harware Status", "Fans Status",
             "Fans Redundancy", "Temperature Status", "PowerSupplies Status", "PowerSupplies Redundancy",
             "Proceesor Status", "Memory Status", "Storage Status"],
            ['', '', '', '', '', '', '', '', '', '', '', '', '', '','']]

        IPcount = 0
        for i in range(rows):
            if list[i][0] == 'IP Address':
                improvedList.append(['', '', '', '', '', '', '', '', '', '', '', '', '', ''])
                IPcount += 1
                improvedList[IPcount][0] = list[i][1]
                ipad1 =0
                for n in range(SiteCount):
                    if IP_Addresses[ipad1] in list[i][1]:
                        improvedList[IPcount][1] = Sites[ipad1]
                    ipad1+=1
            elif list[i][0] == '     SERVER_NAME VALUE':
                improvedList[IPcount][2] = list[i][1]
            elif list[i][0] == '    PRODUCT_NAME VALUE ':
                improvedList[IPcount][3] = list[i][1]
            elif list[i][0] == '   FIRMWARE_VERSION ':
                improvedList[IPcount][4] = list[i][1]
            elif list[i][0] == '          BIOS_HARDWARE STATUS':
                improvedList[IPcount][5] = list[i][1]
            elif list[i][0] == '          FANS STATUS':
                improvedList[IPcount][6] = list[i][1]
            elif list[i][0] == '          FANS REDUNDANCY':
                improvedList[IPcount][7] = list[i][1]
            elif list[i][0] == '          TEMPERATURE STATUS':
                improvedList[IPcount][8] = list[i][1]
            elif list[i][0] == '          POWER_SUPPLIES STATUS':
                improvedList[IPcount][9] = list[i][1]
            elif list[i][0] == '          POWER_SUPPLIES REDUNDANCY':
                improvedList[IPcount][10] = list[i][1]
            elif list[i][0] == '          PROCESSOR STATUS':
                improvedList[IPcount][11] = list[i][1]
            elif list[i][0] == '          MEMORY STATUS':
                improvedList[IPcount][12] = list[i][1]
            elif list[i][0] == '          STORAGE STATUS':
                improvedList[IPcount][13]= list[i][1]




        T_df = pd.DataFrame(improvedList)
        EXCEL_FILE = 'C:/ScriptFiles/Output.xlsx'

        with pd.ExcelWriter(EXCEL_FILE) as writer:
            def Formatting(Range, Value, Format):
                worksheet.conditional_format(Range,
                                             {'type': 'text',
                                              'criteria': 'containing',
                                              'value': Value,
                                              'format': Format})

            Range_All = 'A1:AAA1000'
            Range_First_Line = 'A1:O1'
            E_row = 'E1:E1000'
            Site_row = 'B2:B{}'.format(SiteCount+1)

            T_df.to_excel(writer, sheet_name='list', index=False, header=False)
            workbook = writer.book
            worksheet = writer.sheets['list']

            GreenFormat = workbook.add_format({'bg_color': '#82DD69', 'font_color': '#000000'})
            RedFormat = workbook.add_format({'bg_color': '#FF0000', 'font_color': '#000000'})
            OrangeFormat = workbook.add_format({'bg_color': '#E79603', 'font_color': '#000000'})
            YellowFormat = workbook.add_format({'bg_color': '#F2EC00', 'font_color': '#000000'})

            LightBlueFormat = workbook.add_format({'bg_color': '#C0F8D8', 'font_color': '#000000'})
            LightBrownFormat = workbook.add_format({'bg_color': '#FCD8C9', 'font_color': '#000000'})
            DarkYellowFormat = workbook.add_format({'bg_color': '#DEDE00', 'font_color': '#000000'})

            Formatting(Range_All, 'ok', GreenFormat)
            Formatting(Range_All, ' Link Down', RedFormat)
            Formatting(Range_All, ' Failed', RedFormat)
            Formatting(Range_All, '192.168', LightBlueFormat)
            Formatting(Range_All, 'RO-OP', LightBlueFormat)
            Formatting('A2:B100', 'DU', LightBlueFormat)
            Formatting(Range_All, 'NAHALG', LightBlueFormat)
            Formatting(Range_All, 'ProLiant', LightBrownFormat)
            Formatting(Range_All, ' Not', OrangeFormat)
            Formatting(Range_All, 'Degraded', OrangeFormat)

            Formatting(E_row, ' 2.', LightBrownFormat)
            Formatting(Range_First_Line, '', DarkYellowFormat)
            Formatting(Site_row,'',LightBlueFormat)

            worksheet.conditional_format(Range_All,
                                         {'type': 'text',
                                          'criteria': 'begins with',
                                          'value': ' Redundant',
                                          'format': YellowFormat})

        CopyFile = "C:/ScriptFiles/COPY111.xlsx"
        shutil.copy(EXCEL_FILE,CopyFile)
        os.system("start EXCEL.EXE /r {}".format(CopyFile))
        button2.destroy()


####################################################################
#Threads getDataToTextFile:

def TDF():
    global counter
    global NUMiLOs
    global button2
    button.destroy()
    button2 = Button(root, command=Text_To_Excel, text='Export Excel', width=12)
    L3['text'] = "Script in Progress"
    L3['bg'] = 'YELLOW'
    BackEnd = threading.Thread(name='getDataToTextFile', target=getDataToTextFile)
    BackEnd.start()




#Graphic Interface:

def foreground():
    global root
    root.geometry('1300x912')
    root.title('iLO Health Support')
    global P1
    global L3
    L3 = tkinter.Label(root, text='Start Script',font=("David",22),bg='RED',fg="BLACK")
    L3.pack()
    Lable3 = L3.place(x=550, y=325)
    P1 = Progressbar(root, orient=HORIZONTAL, length=800, mode='determinate')
    global button
    button = Button(root, command=TDF, text = 'Start Process', width =12) #Button for the data to get into text file
    button.pack()
    def bar():
        global button2
        import time
        while True:
            global counter
            P1['value'] = (counter / NUMiLOs) * 100 #updates the prog
            root.update_idletasks()
            time.sleep(1)
            if counter == NUMiLOs:
                L3['text'] = "Script is Done"
                L3['fg'] = "BLACK"
                L3['bg'] = 'LIGHT GREEN'
                counter = 0
                button2.place(x=1065,y=449)

    button.place(x=1065,y=449)
    P1.place(x=250,y=450)
    barb=threading.Thread(name='bar', target=bar)
    barb.start()


# Getting UserName and Password from user
def Submit():
    global U_input
    global P_input
    U_input = Entry1.get()
    P_input = Entry2.get()
    L1.destroy()
    Entry1.destroy()
    L2.destroy()
    Entry2.destroy()
    B1.destroy()
    C1.destroy()
    FrontEnd.start()


#threading

BackEnd=threading.Thread(name='getDataToTextFile', target=getDataToTextFile)
FrontEnd=threading.Thread(name='foreground', target=foreground)

#creating the root tkinter page
root = Tk()
root.geometry('1300x912')
root.title('Submit')
root.resizable("false","false")

#Background
BackgroundImage = PhotoImage(file = "C:/ScriptFiles/background1.png")
Background = Label(root, image= BackgroundImage)
Background.place(x=0,y=0)


#Canvas
CanvasX = 150
CanvasY =275
C1=tkinter.Canvas(root,height=275,width=1000,bg="#E9FFFF")

#Page Title
TitleLable = tkinter.Label(root, text= 'iLO Health Monitoring',font=("David",30),bg='#E9FFFF')
Title1=TitleLable.place(x=CanvasX + 300,y=CanvasY - 50)

#username and password
L1=tkinter.Label(root, text= 'Enter username:   ',font=("David",22),bg='#E9FFFF')
L2=tkinter.Label(root, text= 'Enter password:   ',font=("David",22),bg='#E9FFFF')
Lable1 = L1.place(x=CanvasX +150,y=CanvasY +75)
Lable2 = L2.place(x=CanvasX + 150,y=CanvasY + 175)

ep = StringVar()
cp = StringVar()
Entry1 =Entry(root, textvariable = ep,font=("David",20))
UsernameEntry = Entry1.place(x=CanvasX + 400,y=CanvasY + 75)
Entry2 = Entry(root, textvariable = cp, show = '*',font=("David",20))
PasswordnameEntry = Entry2.place(x=CanvasX + 400,y=CanvasY + 175)


#submit button
LogInButton = PhotoImage(file = "C:/ScriptFiles/LogInButton.png")
B1 = Button(root,command=Submit, width = 50,image =LogInButton)
B1.place(x=CanvasX + 425,y=CanvasY+325)

root.mainloop()

