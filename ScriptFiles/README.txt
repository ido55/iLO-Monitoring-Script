iLO Monitoring Script 

MADE BY: Ido Rennert 2022
----------------------------
DISCLAMER: the IPs presented in the files are for presentation purposes only. You must edit the files to include the IPs of the servers you wish to be sampled by it.


DESCRIPTION:
-------------
this application was made to streamline and automate the monitoring of Servers with iLO management interfaces
in your network.

the application was made by the scripting language Python3.9 and it uses various packages and access 
to the command prompt (CMD) of the local computer that runs the program.

It is also uses an HPE proprietary program called hponcfg that it's job is to sample 
the iLO's servers' information and prompt it into a text file while using XML queries.

	*********************************************************************************************************
	*	THIS PROGRAM DOES NOT CONTAIN SENSETIVE INFORMATION                                      	*
	*												  	*
	*	ALL USERNAMES AND PASSWORD ARE INSERTED DURING THE PROGRAM'S RUNTIME AND ARE NOT BUILT IN IT.	*
	*********************************************************************************************************

also this program ASSUME ALL iLO web interfaces have THE SAME ADMIN USERNAME AND THE SAME PASSWORD FOR THAT USERNAME

INSTRUCTIONS:
--------------

A) SETUP:
----------

To setup the program on your local ROEI computer you must first install
a few programs and copy important files from the shared folder.


1)	First you must copy the Program’s folder into the local computer. the folder is called "ScriptFiles" and is 
	located on my  repository on GitHub.
	You must copy it to the C:\ path in your local computer

2)	you have to install an HP proprietary application called "HP Lights-Out Configuration Utility" or hponcfg.
	To install the program, you must run the .msi file called "SP99166-Hewlett Packard Enterprise" with administrator privileges.
	the program should be installed and be found in the path "C:\Program Files (x86)\Hewlett Packard Enterprise\HP Lights-Out Configuration Utility"

3) 	Finally you must confirm that an Office Excel is installed on your local computer.

Once you completed all the steps above you can proceed and run the program


B) RUNNING THE APPLICATION:
----------------------------

1)	To use this program you first must double-click on the .exe file called "iLO Monitoring" which is located either in  
	my repository on Github or locally on your local computer under "C:\ScriptFiles\iLO Monitoring.exe"

2)	After a few moments a pop up screen will appear with two entry boxes and a LOGIN button. 
	You must insert the username of the iLO web interface and it's password in 
	the "Enter username" and "Enter password" respectfully	

3)	Press the LOGIN button to continue to the next screen.

4)	In the next screen there is a caption in black over red background that reads "Start Script", IT IS NOT the start button of the process. 
	To start the process, you should press the "Start Process" button located the right of blank progress bar.

5)	progress bar will start filling and will update in sync with the Servers that were checked by the program. 
	the box which said "Run Script" will change it's text and color to read "Script in Progress" in Bright Yellow background.

6) 	Once the progress bar is filled the text bow up top will change it's text and color to "Script is Done" in bright green color and a
	new button will appear below the "Start Process" button that was mentioned above. The button will read "Export to Excel"

7) 	Finally, you must press the "Export to Excel" button and it will open a Read-only Excel file with the data gathered from the various iLOs.
	This file you are free to observe and save under a different name on your local computer or in the shared folder.
 
C) ADDING AN iLO SERVER:
------------------------

To add an iLO server to the list you must update it in the right files that are connected to the application. 

	*****************************************************************************************
	*	YOU MUST CONFIRM YOU CHANGED THE FILES BOTH ON YOUR LOCAL MACHINE AND IN THE   	*
	*										       	*
	*	SHARED FOLDER FOR OTHER USERS TO UPDATE THEIR FOLDER AS WELL.		       	*
	*****************************************************************************************

1) 	You must add the IP of said iLO server to a txt file called "iloListTestNew" which is found in the ScriptFiles folder locally.

	WARNING, Be careful not to add excessive blank rows during the editing of the file (at the end of the txt file),
	the application will not work if those blank rows are present.

2)	To enable the iLO's site's name to appear next to the IP in the OUTPUT Excel file the 
	program creates you have to add in the ILOs_And_Sites.xlsx file on the Local machine in the ScriptFiles folder"

	in those files you add the IP address of the iLO server under the column called "IP" and the site name under the column "Site"

D) REMOVING AN iLO SERVER:
--------------------------

To remove an iLO server to the list you must update it in the right files that are connected to the application. 

	*****************************************************************************************
	*	YOU MUST CONFIRM YOU UPDATED THE FILES BOTH ON YOUR LOCAL MACHINE AND IN THE   	*
	*										       	*
	*	SHARED FOLDER FOR OTHER USERS TO UPDATE THEIR FOLDER AS WELL.		       	*
	*****************************************************************************************

1) 	You must remove the IP of said iLO server to a txt file called "iloListTestNew" which is found in the ScriptFiles folder locally.

	WARNING, be careful not to add excessive blank rows during the editing of the file (at the end of the txt file),
	the application will not work if those blank rows are present.

2)	remove the iLO's IP and site name in the ILOs_And_Sites.xlsx file on the Local machine in the ScriptFiles folder.

	in those files you remove the IP address of the iLO server under the column called "IP" and the site name under the column "Site"


NOTES:
------

ABOUT THE FILES:
----------------
In the ScriptFiles folder you have about 15 different files that all have crucial part in the program.

1) background1.png   	- the background image shown in the application's GUI (Graphical User Interface).
2) COPY111.xlsx      	- the excel file the application exports it's results to at the end of the process.
3) FinalResults1.txt 	- one of the text files that application uses while it runs, it uses it as the final result to reorganize into an excel file.
4) Get-ALL.xml			- the XML file the hponcfg program uses to sample the iLO servers.
5) iLO Monitoring.exe	- the exe file of application, you execute this file to run the program.
6) iloListTestNew.txt	- the file with the IPs of the iLO servers that are sampled by the program
7) ILOs_And_Sites.xlsx	- an excel files that correlates between an IP address and a site name and the program will use it to assign a site name to a sampled server.
8)log.txt				- a log file the program initially uses this file to log the information sampled by the hponcfg program.
9)LogInButton.png		- the image shown as the LOGIN button in the application's GUI (Graphical User Interface).
10)Output.xlsx			- an intermedium excel file the program writes appropriate information on.
11)output1.txt			- a text file the program uses while running to store temporary information.
12)README.txt			- this text file for help and instructions 
13)results2.txt 		- a text file which the results from the iLOs are gathered into before it is handled
14)resultsN2.txt		- a text file which the results about port and network status from the iLOs are gathered into before it is handled

15)SP99166-Hewlett Packard Enterprise.msi - an msi file used to install the hponcfg program. Must be run with administrative privileges.


