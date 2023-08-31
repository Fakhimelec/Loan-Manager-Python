# First Step Is Writing The Working Code And Fixing Bugs
# SecondStep Is Editing The Appearance Of The Code
# Third Step Is To Modify Written Code If Any Redundant Part Exists

##############################################################################################################
# Modules
# PyQT5
# pandas
# numpy
# pillow
# arabic_reshaper
# python_bidi
# jdatetime
# screeninfo
# sys
# os
# warnings
# openpyxl

##############################################################################################################
# Python Program To Manage Loan Systems
# List Of Contents Of Functions And Sectiona
# %%%%%%%%%%%%%%%%%%%%%%%%
# Import The Required Modules
# Main Dataframes
# Global Variables    
    # Screen Dimensions
    # DateTime Information
    # Path Obtaining
    # Component Style Parameters
# Creating A Window Class (Main Class)
    # Main Window
    # Member Table Window
    # Loan Table Window
    # Expense Table Window
    # Repots Window
    # Lottery Window
    # Exit
# Focus In/Out Class For Search Box
# Pandas Model
# Add Member Prompt Window
# DeleteMemberPrompt
# MonthlyDepositePrompt
# ReturnPacePrompt
# AddLoanPrompt
# DeleteLoanPrompt
# AddExpensePrompt
# DeleteExpensePrompt
# PaymentCalcPrompt
# RandomPickPrompt
# ManualPickPrompt
# DeleteWinnerPrompt

############################################################################################################## 
# Import The Required Modules
# \
from PyQt5.QtWidgets import *                                           # To Create A Graphic User Interface
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *  
from PyQt5.QtCore import *  

import jdatetime                                                        # To Access Datetime

import numpy as np                                                      # To Do Mathematical Calculations

import pandas as pd                                                     # To Create And Work On Dataframes

from screeninfo import get_monitors

import sys                                                              # To 
import os                                                               # To Load And Save 


import warnings                                                         # To ignore the warnings
warnings.filterwarnings("ignore")

from PrintBills import *                                                # External Module To Print Bills


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Main Dataframes $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

## Preset Values Of DataBase That Will Be Deleted And Loaded From Last Saved Data Instead

# Member List
member_list             = pd.read_excel('Database\Member_List.xlsx')
member_list = member_list.fillna("")
member_list.drop(member_list.keys()[0], axis = 1, inplace=True)
member_list.reset_index(drop = True, inplace = True)



# Loan List
loan_list               = pd.read_excel('Database\Loan_List.xlsx')
loan_list = loan_list.fillna("")
loan_list.drop(loan_list.keys()[0], axis = 1, inplace=True)
loan_list.reset_index(drop = True, inplace = True)

# Expenses List
expense_list             = pd.read_excel('Database\Expense_List.xlsx')
expense_list = expense_list.fillna("")
expense_list.drop(expense_list.keys()[0], axis = 1, inplace=True)
expense_list.reset_index(drop = True, inplace = True)

# Payment List
payment_columns = ["شماره عضويت", "نام خانوادگي", "نام", "شماره وام", "تاريخ (سال)", "تاريخ (ماه)",
                   "مبلغ وام", "پس انداز ماهيانه", "مبلغ اقساط", "جمع پرداختي", "مانده بدهي",
                   "اقساط باقي مانده", "مبلغ پس انداز", "وضعيت قرعه کشي", "سرعت بازپرداخت"]
payment_list = pd.DataFrame(columns = payment_columns)
payment_list.reset_index(drop = True, inplace = True)

# Balance List
balance_list             = pd.read_excel('Database\Balance_List.xlsx')
balance_list = balance_list.fillna("")
balance_list.drop(balance_list.keys()[0], axis = 1, inplace=True)
balance_list.reset_index(drop = True, inplace = True)

# Lottery Win List
lottery_winner_list = pd.read_excel('Database\Lottery_Winner_List.xlsx')
lottery_winner_list = lottery_winner_list.fillna("")
lottery_winner_list.drop(lottery_winner_list.keys()[0], axis = 1, inplace=True)
lottery_winner_list.reset_index(drop = True, inplace = True)


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Global Variables $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Regulator Experssion Of Number/Persian String Validator
persian_reg_ex = QRegExp("[ء-ي 0-9 گچپژیلفقهموک]+")
number_reg_ex = QRegExp("[0-9]+")

total_deposit = member_list["مبلغ پس انداز"][1]
monthly_deposit = member_list["پس انداز ماهيانه"][1]
default_commision_rate = 1
# Number Of Monthes To Return The Loan
default_installment_count = 25

# Get The Privous Values Of Total Parameteres
balance_list_last_row = balance_list.shape[0]
# Total Assets (Deposits And Loan Commisions)
total_asset = balance_list["مجموع پس انداز و درصد"][balance_list_last_row - 1]

# Total Liabilities (Loan Debts And Expenses)
total_liability = balance_list["مجموع بدهي وام و هزينه ها"][balance_list_last_row - 1]

# Balance (Total Assets - Total Liabilities)
balance = total_asset - total_liability

# Bank Monthly Profit Which Is Added To Deposit
account_balance = balance_list["موجودي با حساب سود بانکي"][balance_list_last_row - 1]

# Bank Profit
bank_profit = balance_list["سود بانکي"][balance_list_last_row - 1]

# Total Balance (Balance + Bank Profit)
balance_diff = account_balance - balance - bank_profit

# Declare A Variable To Find Out That Clicking On Table Header Is Being Occured On Which Window
window_flag = ''

temp = ''
temp_year = 0
temp_month = 0
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Screen Related Parameters Are Needed In All Classes And Functions Hence It's Declared
# Outside Of Functions To Be Used By All
# Screen Dimensions
screen_dim = get_monitors()[0]
# Getting The Width Of The Window Screen
screen_width  = screen_dim.width
# Getting The Height Of The Window Screen 
screen_height = screen_dim.height

screen_center_hor = screen_width//2
screen_center_ver = screen_height//2

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# DateTime Information
now = jdatetime.datetime.today()
time =  now.strftime("%H:%M:%S")
date = now.strftime("%Y / %m / %d")
current_year = now.year
current_month = now.month
current_day = now.day
current_weekday = now.weekday()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Getting File Path Of The Current .py File
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'PyQt5_Loan_Project.py')

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Components Style Parameters $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Head Label Style
head_label_width = 400
head_label_height = 80
# DateTime Label Style
datetime_label_width = 200
datetime_label_height = 50
# Ordinary Label Style
ord_label_width = 100
ord_label_height = 30

# Button Style
button_width = screen_width//6
button_height = screen_height//8

hor_spacing = 0#screen_width//100
ver_spacing = screen_height//50       


#exit(0)

#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Creating A Window Class (Main Class)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class MainWindow(QMainWindow):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> 
    #                           Using A Constructor (Main Application Window)
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> 
    def __init__(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().__init__()

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global window_flag
        
        # Change Window Flag To Main Window
        window_flag = 'main_window'

        # Setting The Title Of The Window
        self.setWindowTitle("صندوق پس انداز واقف")
        
        # Setting The Icon Image Of The Window
        self.setWindowIcon(QIcon('images/icon.png'))
           
        # Setting Geometry Of Main Window To Cover Whole Screen
        self.setGeometry(0, 0, screen_width, screen_height)
        
        # Setting The Backgrounf Of Main Window To Cover Whole Screen
        oImage = QImage("images/background.jpg")
        sImage = oImage.scaled(QSize(screen_width, screen_height))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        # Making Window Frame Invisible
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Making Window Background Invisible
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # Setting The Window Transparent
        self.setWindowOpacity(1)

        # Main Window Widget (Right Side Window) 
        # Setting A Grid Layout To Place The Widgets On The Form
        self.content_form_layout = QGridLayout()

        # Page Name
        self.title_label = QLabel("صفحه اصلي", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setGeometry(0, 0, head_label_width, head_label_height)
        self.title_label.setStyleSheet("color: white;"
                                      "font-family: Titr;"
                                      "padding: 2px;"
                                      "font-size: 100pt;"
                                      "font-weight: bold;")
        
        self.test_label = QLabel(date + "\n" + time , self)
        self.test_label.setAlignment(Qt.AlignCenter)
        self.test_label.setGeometry(0, 0, head_label_width, head_label_height)
        self.test_label.setStyleSheet("color: white;"
                                      "font-family: Titr;"
                                      "padding: 2px;"
                                      "font-size: 38pt;"
                                      "font-weight: bold;")
        
        # Placing The Needed Widgets (Button, Labels, TextBoxes . . .) On Top Of The Table
        self.content_form_layout.addWidget(self.title_label, 0, 0)
        self.content_form_layout.addWidget(self.test_label, 1, 0)
        # Constructing A Upper Level Widget To Hold Everthing Together
        widget = QWidget()
        widget.setLayout(self.content_form_layout)
        self.setCentralWidget(widget) 


        # Creating And Setting Of Left Side Dock Widget
        self.dock = QDockWidget('')
        self.dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)

        # Creating And Setting Of Up Side Dock Widget
##        dock2 = QDockWidget('Head')
##        dock2.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
##        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, dock2)

        
        # Creat Form Layout
        # Table Widget Goes To The Right Of The Page And Form Goes To The Left
        self.form = QWidget()
        self.layout = QFormLayout(self.form)
        self.form.setLayout(self.layout)
        self.layout.setVerticalSpacing(ver_spacing)
        
        # Header Label
        self.head_label = QLabel("   صندوق پس انداز واقف   ", self)
        self.head_label.setAlignment(Qt.AlignCenter)
        self.head_label.setGeometry(0, 0, head_label_width, head_label_height)
        self.head_label.setStyleSheet("color: yellow;"
                                      "padding: 2px;"
                                      "font-size: 22pt;"
                                      "font-family: Titr;"
                                      "font-weight: bold;")        
        self.layout.addRow(self.head_label)
        
        # Main Window Show Button  
        main_window_button = QPushButton("   صفحه ي اصلي   ", self)
        main_window_button.setGeometry(25, 150, button_width, button_height)
        main_window_button.clicked.connect(self.main_window_button_clicked)
        main_window_button.setStyleSheet("color: black;"
                                         "font-size: 18pt;"
                                         "font-family: Titr;"
                                         "font-weight: bold;")
        self.layout.addRow(main_window_button)
        
        # Member List Table Show Button  
        member_table_button = QPushButton("   ليست اعضاي صندوق   ", self)
        member_table_button.setGeometry(25, 150, button_width, button_height)
        member_table_button.clicked.connect(self.member_table_button_clicked)
        member_table_button.setStyleSheet("color: black;"
                                          "font-size: 18pt;"
                                          "font-family: Titr;"
                                          "font-weight: bold;")
        self.layout.addRow(member_table_button)

        
        # Loan List Table Show Button  
        loan_table_button = QPushButton("ليست وام هاي دريافتي", self)
        loan_table_button.setGeometry(25, 150, button_width, button_height)
        loan_table_button.clicked.connect(self.loan_table_button_clicked)
        loan_table_button.setStyleSheet("color: black;"
                                        "font-size: 18pt;"
                                        "font-family: Titr;"
                                        "font-weight: bold;")
        self.layout.addRow(loan_table_button)      

        # Expense Table Button  
        expense_table_button = QPushButton("   ليست هزينه ها   ", self)
        expense_table_button.setGeometry(25, 150, button_width, button_height)
        expense_table_button.clicked.connect(self.expense_table_button_clicked)
        expense_table_button.setStyleSheet("color: black;"
                                      "font-size: 18pt;"
                                      "font-family: Titr;"
                                      "font-weight: bold;")
        self.layout.addRow(expense_table_button)  

        # Reports Button  
        report_button = QPushButton("   گزارشات صندوق   ", self)
        report_button.setGeometry(25, 150, button_width, button_height)
        report_button.clicked.connect(self.report_button_clicked)
        report_button.setStyleSheet("color: black;"
                                    "font-size: 18pt;"
                                    "font-family: Titr;"
                                    "font-weight: bold;")
        self.layout.addRow(report_button)

        # Lottery Button  
        lottery_button = QPushButton("   قرعه کشي   ", self)
        lottery_button.setGeometry(25, 150, button_width, button_height)
        lottery_button.clicked.connect(self.lottery_button_clicked)
        lottery_button.setStyleSheet("color: black;"
                                     "font-size: 18pt;"
                                     "font-family: Titr;"
                                     "font-weight: bold;")
        self.layout.addRow(lottery_button)
        
        # Exit Button  
        exit_button = QPushButton("   خروج   ", self)
        exit_button.setGeometry(25, 150, button_width, button_height)
        exit_button.clicked.connect(self.exit_button_clicked)
        exit_button.setStyleSheet("color: black;"
                                  "font-size: 18pt;"
                                  "font-family: Titr;"
                                  "font-weight: bold;")
        self.layout.addRow(exit_button)

        
        #dock2.setWidget(dock)
        self.dock.setWidget(self.form)
        
        #  Displaying Window Maximized
        self.showMaximized()
        
        #  Displaying All the Widgets  
        self.show()

        #====================
##        # Creating a Timer Object
##        timer = QTimer(self)
##        # adding action to timer
##        timer.timeout.connect(self.timer_interval)
##        # update the timer every second
##        timer.start(1000)
        #====================
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def timer_interval(self):
        # Function for Timer Interval If Needed 
        self.datetime_label.setText('Heloo')
        print("Time")

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> 
    #                                               (Main Window)
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> 
    def main_window_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # This Code Will Create And Arrange Widgets On The Main Window
        
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global window_flag
        
        # Change Window Flag To Main Window
        window_flag = 'main_window'
        
        # Setting A Grid Layout To Place The Widgets On The Form
        self.content_form_layout = QGridLayout()

        # Page Name
        self.title_label = QLabel("صفحه اصلي", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setGeometry(0, 0, head_label_width, head_label_height)
        self.title_label.setStyleSheet("color: white;"
                                      "font-family: Titr;"
                                      "padding: 2px;"
                                      "font-size: 100pt;"
                                      "font-weight: bold;")
        # Persian DateTime
        self.test_label = QLabel(date + "\n" + time , self)
        self.test_label.setAlignment(Qt.AlignCenter)
        self.test_label.setGeometry(0, 0, head_label_width, head_label_height)
        self.test_label.setStyleSheet("color: white;"
                                      "font-family: Titr;"
                                      "padding: 2px;"
                                      "font-size: 38pt;"
                                      "font-weight: bold;")

        
        # Placing The Needed Widgets (Button, Labels, TextBoxes . . .) On Top Of The Table
        self.content_form_layout.addWidget(self.title_label, 0, 0)
        self.content_form_layout.addWidget(self.test_label, 1, 0)
        # Constructing A Upper Level Widget To Hold Everthing Together
        widget = QWidget()
        widget.setLayout(self.content_form_layout)
        self.setCentralWidget(widget)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> 
    #                                            (Member Table Window)
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <>
    def member_table_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # This Code Will Create And Arrange Widgets On The Member Table Window
        
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global window_flag
        global member_list

        # Change Window Flag To Member Window
        window_flag = 'member_window'
        
        # Setting A Grid Layout To Place The Widgets On The Form
        self.content_form_layout = QGridLayout()
        self.content_form_layout.setHorizontalSpacing(hor_spacing)

        # Putting a Image Object For Search Icon
        self.search_icon_label = QLabel(self)
        self.search_icon = QPixmap('images/search_icon.png')
        self.search_icon = self.search_icon.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.search_icon_label.setPixmap(self.search_icon)  

        # Creating a QLineEdit Object For Search/Filter
        self.search_box = SearchQLineEdit("جست و جو/فيلتر", self)

        # Prevent Inserting Any Value
        input_validator = QRegExpValidator(persian_reg_ex, self.search_box)
        self.search_box.setValidator(input_validator)
        
        self.search_box.textChanged.connect(self.search_box_text_changed)
        #self.search_box.setFixedWidth(600)
        self.search_box.setAlignment(Qt.AlignCenter)
        self.search_box.setStyleSheet("color: blue;"
                                 "font-size: 15pt;"
                                 "font-family: Kamran;"
                                 "font-weight: bold;")
        

        # Member Delete ALL Button  
        delete_all_member_button = QPushButton("   پاک کردن تمام ليست اعضا   ", self)
        delete_all_member_button.setGeometry(0, 0, button_width, button_height)
        delete_all_member_button.clicked.connect(self.delete_all_member_button_clicked)
        delete_all_member_button.setStyleSheet("color: black;"
                                           "font-size: 13pt;"
                                           "font-family: Titr;"
                                           "font-weight: bold;")
        
        # Member Delete Button  
        delete_member_button = QPushButton("   حذف عضو   ", self)
        delete_member_button.setGeometry(0, 0, button_width, button_height)
        delete_member_button.clicked.connect(self.delete_member_button_clicked)
        delete_member_button.setStyleSheet("color: black;"
                                           "font-size: 13pt;"
                                           "font-family: Titr;"
                                           "font-weight: bold;")
        
        # New Member Add Button  
        add_member_button = QPushButton("   افزودن عضو جديد   ", self)
        add_member_button.setGeometry(0, 0, button_width, button_height)
        add_member_button.clicked.connect(self.add_member_button_clicked)
        add_member_button.setStyleSheet("color: black;"
                                        "font-size: 13pt;"
                                        "font-family: Titr;"
                                        "font-weight: bold;")

        # Monthly Deposit Change Button  
        monthly_deposit_change_button = QPushButton("   تغيير مبلغ پس انداز ماهيانه   ", self)
        monthly_deposit_change_button.setGeometry(0, 0, button_width, button_height)
        monthly_deposit_change_button.clicked.connect(self.monthly_deposit_change_button_clicked)
        monthly_deposit_change_button.setStyleSheet("color: black;"
                                           "font-size: 13pt;"
                                           "font-family: Titr;"
                                           "font-weight: bold;")

        # Loan Return Pace Change Button  
        return_pace_change_button = QPushButton("   تغيير سرعت بازپرداخت اعضا   ", self)
        return_pace_change_button.setGeometry(0, 0, button_width, button_height)
        return_pace_change_button.clicked.connect(self.return_pace_change_button_clicked)
        return_pace_change_button.setStyleSheet("color: black;"
                                           "font-size: 13pt;"
                                           "font-family: Titr;"
                                           "font-weight: bold;")
        
        # Placing The Needed Widgets (Button, Labels, TextBoxes . . .) On Top Of The Table
        self.content_form_layout.addWidget(delete_all_member_button, 0, 0)
        self.content_form_layout.addWidget(delete_member_button, 0, 1)
        self.content_form_layout.addWidget(add_member_button, 0, 2)
        # Spacer Label
        #self.content_form_layout.addWidget(QLabel(""), 0, 3)
        self.content_form_layout.addWidget(self.search_box, 0, 4)
        self.content_form_layout.addWidget(self.search_icon_label, 0, 5)
        self.content_form_layout.addWidget(monthly_deposit_change_button, 1, 0)
        self.content_form_layout.addWidget(return_pace_change_button, 1, 1, 1, 2)
        


    
        # Create And Filling The Table With The Member Data List
        self.table = QtWidgets.QTableView()
        # Setting Table Visual Properties
        self.table.setStyleSheet("QTableView {background-color: rgba(255, 255, 255, 30);"
                                 "color: white;"
                                 "font-family: zar;"
                                 "font-size: 18pt;}")
        # Update The Table View With The member_list
        self.model = PandasModel(member_list)
        self.table.setModel(self.model)
        
        # Setting Header Columns Width On The Table
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Getting Header Click Event Of Table To Sort Column
        self.table.horizontalHeader().sectionClicked.connect(self.on_table_header_clicked)
        
        # Placing The Table Widgets At The Buttom Of The Page
        self.content_form_layout.addWidget(self.table, 2, 0, 1, 6)

        # Constructing A Upper Level Widget To Hold Everthing Together
        widget = QWidget()
        widget.setLayout(self.content_form_layout)
        self.setCentralWidget(widget)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               
    def add_member_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # This Slot Function Will Add New Member Data Into The Table Widget

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        
        dlg = AddMemberPrompt()
        dlg.exec()
        
        self.model = PandasModel(member_list)
        self.table.setModel(self.model)
        
            
    def delete_member_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # This Slot Function Will Delete The Member Data Out Of The Table Widget 
        dlg = DeleteMemberPrompt()
        dlg.exec()
        # Update The Table View With The member_list
        self.model = PandasModel(member_list)
        self.table.setModel(self.model)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            
    def delete_all_member_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # This Slot Function Will Delete All Loan On The List
        global member_list
        global loan_list
        
        dlg = QMessageBox(self)
        dlg.setWindowTitle(" حذف تمام اعضا ")
        dlg.setText(" تمام وام ها نیز حذف خواهند شد!\nآيا از حذف کامل ليست اعضا مطمئن هستيد ؟")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()        
        if button == QMessageBox.Yes:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            loan_list.drop(loan_list.index, inplace = True)
            loan_list.reset_index(drop = True, inplace = True)
            lottery_winner_list.drop(lottery_winner_list.index, inplace = True)
            lottery_winner_list.reset_index(drop = True, inplace = True)
            member_list.drop(member_list.index, inplace = True)
            member_list.reset_index(drop = True, inplace = True)
            self.model = PandasModel(member_list)
            self.table.setModel(self.model)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            
    def monthly_deposit_change_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # This Slot Function Will Delete The Member Data Out Of The Table Widget
        global monthly_deposit
        
        dlg = MonthlyDepositePrompt()
        dlg.exec()

        # Getting Number Of Rows And Columns
        member_index = member_list.index
        # Putting In The Pandas Data Into Table Cell By Cell
        for i in member_index:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            member_list["پس انداز ماهيانه"][i] = monthly_deposit
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # Update The Table View With The member_list    
        self.model = PandasModel(member_list)
        self.table.setModel(self.model)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    def return_pace_change_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # This Slot Function Will Change The Return Pace Of Specific Member
        dlg = ReturnPacePrompt()
        dlg.exec()
        # Update The Table View With The member_list
        self.model = PandasModel(member_list)
        self.table.setModel(self.model)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> 
    #                                            (Loan Table Window)
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <>
    def loan_table_button_clicked(self):
        # This Code Will Create And Arrange Widgets On The Loan Table Window

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global window_flag
            
        # Change Window Flag To Loan Window
        window_flag = 'loan_window'
        
        # Setting A Grid Layout To Place The Widgets On The Form
        self.content_form_layout = QGridLayout()
        self.content_form_layout.setHorizontalSpacing(hor_spacing)

        # Putting a Image Object For Search Icon
        search_icon_label = QLabel(self)
        search_icon = QPixmap('images/search_icon.png')
        search_icon = search_icon.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        search_icon_label.setPixmap(search_icon)  
        
        # Creating a QLineEdit Object For Search/Filter
        self.search_box = SearchQLineEdit("جست و جو/فيلتر", self)
        
        # Prevent Inserting Any Value
        input_validator = QRegExpValidator(persian_reg_ex, self.search_box)
        self.search_box.setValidator(input_validator)
        
        self.search_box.textChanged.connect(self.search_box_text_changed)
        self.search_box.setGeometry(0, 0, button_width, button_height)  
        self.search_box.setAlignment(Qt.AlignCenter)  
        self.search_box.setStyleSheet("color: blue;"
                                 "font-size: 15pt;"
                                 "font-family: Kamran;"
                                 "font-weight: bold;")       

        # New Loan Add Button  
        add_loan_button = QPushButton("   افزودن وام جديد   ", self)
        add_loan_button.setGeometry(0, 0, button_width, button_height)
        add_loan_button.clicked.connect(self.add_loan_button_clicked)
        add_loan_button.setStyleSheet("color: black;"
                                        "font-size: 13pt;"
                                        "font-family: Titr;"
                                        "font-weight: bold;")
        
        # Delete Loan Add Button  
        delete_loan_button = QPushButton("   حذف وام   ", self)
        delete_loan_button.setGeometry(0, 0, button_width, button_height)
        delete_loan_button.clicked.connect(self.delete_loan_button_clicked)
        delete_loan_button.setStyleSheet("color: black;"
                                        "font-size: 13pt;"
                                        "font-family: Titr;"
                                        "font-weight: bold;")
        
        # Loan Delete ALL Button  
        delete_all_loan_button = QPushButton("   پاک کرد تمام ليست وام ها   ", self)
        delete_all_loan_button.setGeometry(0, 0, button_width, button_height)
        delete_all_loan_button.clicked.connect(self.delete_all_loan_button_clicked)
        delete_all_loan_button.setStyleSheet("color: black;"
                                           "font-size: 13pt;"
                                           "font-family: Titr;"
                                           "font-weight: bold;")
        
        # Placing The Needed Widgets (Button, Labels, TextBoxes . . .) On Top Of The Table
        self.content_form_layout.addWidget(delete_all_loan_button, 0, 0)
        self.content_form_layout.addWidget(delete_loan_button, 0, 1)
        self.content_form_layout.addWidget(add_loan_button, 0, 2)
        # Spacer Label
        self.content_form_layout.addWidget(QLabel("                                      "), 0, 3)
        self.content_form_layout.addWidget(self.search_box, 0, 4)
        self.content_form_layout.addWidget(search_icon_label, 0, 5)
    
        # Create And Filling The Table With The Member Data List
        self.table = QtWidgets.QTableView()
        # Setting Table Visual Properties
        self.table.setStyleSheet("QTableView {background-color: rgba(255, 255, 255, 30);"
                                 "color: white;"
                                 "font-family: zar;"
                                 "font-size: 18pt;}")
        # Update The Table View With The member_list
        self.model = PandasModel(loan_list)
        self.table.setModel(self.model)

        # Setting Header Columns Width On The Table
        #self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.resizeColumnsToContents()

        # Getting Header Click Event Of Table To Sort Column
        self.table.horizontalHeader().sectionClicked.connect(self.on_table_header_clicked)
        
        # Placing The Table Widgets At The Buttom Of The Page
        self.content_form_layout.addWidget(self.table, 1, 0, 1, 6)

        # Constructing A Upper Level Widget To Hold Everthing Together
        widget = QWidget()
        widget.setLayout(self.content_form_layout)
        self.setCentralWidget(widget)
        
    # This Slot Function Will Put In The Loan Data Into The Table Widget
    def add_loan_button_clicked(self):
        dlg = AddLoanPrompt()
        dlg.exec()
        
        self.model = PandasModel(loan_list)
        self.table.setModel(self.model)
        
    # This Slot Function Will Put In The Loan Data Into The Table Widget
    def delete_loan_button_clicked(self):
        dlg = DeleteLoanPrompt()
        dlg.exec()

        self.model = PandasModel(loan_list)
        self.table.setModel(self.model)

    # This Slot Function Will Delete All Loan On The List
    def delete_all_loan_button_clicked(self):
        global loan_list
        global member_list

        dlg = QMessageBox(self)
        dlg.setWindowTitle("حذف تمام وام ها ")
        dlg.setText("آيا از حذف کامل ليست وام ها مطمئن هستيد ؟")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()        
        if button == QMessageBox.Yes:
            loan_list.drop(loan_list.index, inplace = True)
            loan_list.reset_index(drop = True, inplace = True)
            member_list.loc[:, "وضعيت وام"] = 0
            self.model = PandasModel(loan_list)
            self.table.setModel(self.model)
            
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> 
    #                                            (Expense Table Window)
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <>
    def expense_table_button_clicked(self):
        # This Code Will Create And Arrange Widgets On The Expense Table Window

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global window_flag
        
        # Change Window Flag To Expense Window
        window_flag = 'expense_window'
        
        # Setting A Grid Layout To Place The Widgets On The Form
        self.content_form_layout = QGridLayout()
        self.content_form_layout.setHorizontalSpacing(hor_spacing)

        # Putting a Image Object For Search Icon
        self.search_icon_label = QLabel(self)
        self.search_icon = QPixmap('images/search_icon.png')
        self.search_icon = self.search_icon.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.search_icon_label.setPixmap(self.search_icon)  

        # Creating a QLineEdit Object For Search/Filter
        self.search_box = SearchQLineEdit("جست و جو/فيلتر", self)

        # Prevent Inserting Any Value
        input_validator = QRegExpValidator(persian_reg_ex, self.search_box)
        self.search_box.setValidator(input_validator)
        
        self.search_box.textChanged.connect(self.search_box_text_changed)
        self.search_box.setGeometry(0, 0, button_width, button_height)  
        self.search_box.setAlignment(Qt.AlignCenter)
        self.search_box.setStyleSheet("color: blue;"
                                 "font-size: 15pt;"
                                 "font-family: Kamran;"
                                 "font-weight: bold;")
        

        # New Member Add Button  
        add_expense_button = QPushButton("   افزودن هزينه جديد   ", self)
        add_expense_button.setGeometry(0, 0, button_width, button_height)
        add_expense_button.clicked.connect(self.add_expense_button_clicked)
        add_expense_button.setStyleSheet("color: black;"
                                        "font-size: 13pt;"
                                        "font-family: Titr;"
                                        "font-weight: bold;")

        # Expense Delete Button  
        delete_expense_button = QPushButton("   پاک کردن هزينه   ", self)
        delete_expense_button.setGeometry(0, 0, button_width, button_height)
        delete_expense_button.clicked.connect(self.delete_expense_button_clicked)
        delete_expense_button.setStyleSheet("color: black;"
                                           "font-size: 13pt;"
                                           "font-family: Titr;"
                                           "font-weight: bold;")
        
        # Expense Delete ALL Button  
        delete_all_expense_button = QPushButton("   پاک کرد تمام ليست هزينه ها   ", self)
        delete_all_expense_button.setGeometry(0, 0, button_width, button_height)
        delete_all_expense_button.clicked.connect(self.delete_all_expense_button_clicked)
        delete_all_expense_button.setStyleSheet("color: black;"
                                           "font-size: 13pt;"
                                           "font-family: Titr;"
                                           "font-weight: bold;")
        
        # Placing The Needed Widgets (Button, Labels, TextBoxes . . .) On Top Of The Table
        self.content_form_layout.addWidget(delete_all_expense_button, 0, 0)
        self.content_form_layout.addWidget(delete_expense_button, 0, 1)
        self.content_form_layout.addWidget(add_expense_button, 0, 2)
        
        # Spacer Label
        self.content_form_layout.addWidget(QLabel("                                     "), 0, 3)
        self.content_form_layout.addWidget(self.search_box, 0, 4)
        self.content_form_layout.addWidget(self.search_icon_label, 0, 5)

    
        # Create And Filling The Table With The Member Data List
        self.table = QtWidgets.QTableView()
        # Setting Table Visual Properties
        self.table.setStyleSheet("QTableView {background-color: rgba(255, 255, 255, 30);"
                                 "color: white;"
                                 "font-family: zar;"
                                 "font-size: 18pt;}")
        
        self.model = PandasModel(expense_list)
        self.table.setModel(self.model)
        
        # Setting Header Columns Width On The Table
        #self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # Getting Header Click Event Of Table To Sort Column
        self.table.horizontalHeader().sectionClicked.connect(self.on_table_header_clicked)
        
        # Placing The Table Widgets At The Buttom Of The Page
        self.content_form_layout.addWidget(self.table, 1, 0, 1, 6)

        # Constructing A Upper Level Widget To Hold Everthing Together
        widget = QWidget()
        widget.setLayout(self.content_form_layout)
        self.setCentralWidget(widget)

    # This Slot Function Will Put In The Loan Data Into The Table Widget
    def add_expense_button_clicked(self):
        dlg = AddExpensePrompt()
        dlg.exec()

        self.model = PandasModel(expense_list)
        self.table.setModel(self.model)
        
    # This Slot Function Will Put In The Loan Data Into The Table Widget
    def delete_expense_button_clicked(self):

        dlg = DeleteExpensePrompt()
        dlg.exec()

        self.model = PandasModel(expense_list)
        self.table.setModel(self.model)

    # This Slot Function Will Delete All Expenses On The List
    def delete_all_expense_button_clicked(self):
        global expense_list

        dlg = QMessageBox(self)
        dlg.setWindowTitle("حذف تمام هزينه ها ")
        dlg.setText("آيا از حذف کامل ليست هزينه ها مطمئن هستيد ؟")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()        
        if button == QMessageBox.Yes:
            expense_list.drop(expense_list.index, inplace = True)
            expense_list.reset_index(drop = True, inplace = True)
            self.model = PandasModel(expense_list)
            self.table.setModel(self.model)
            

        
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> 
    #                                             (Repots Window)
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <>
    def report_button_clicked(self):
        # This Code Will Create And Arrange Widgets On The Reports Window

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global window_flag
        
        # Change Window Flag To Report Window
        window_flag = 'report_window'
        
        # Setting A Grid Layout To Place The Widgets On The Form
        self.content_form_layout = QGridLayout()
        self.content_form_layout.setHorizontalSpacing(hor_spacing)
        
        # Putting a Image Object For Search Icon
        self.search_icon_label = QLabel(self)
        self.search_icon = QPixmap('images/search_icon.png')
        self.search_icon = self.search_icon.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.search_icon_label.setPixmap(self.search_icon)  

        # Creating a QLineEdit Object For Search/Filter
        self.search_box = SearchQLineEdit("جست و جو/فيلتر", self)
        
        # Prevent Inserting Any Value
        input_validator = QRegExpValidator(persian_reg_ex, self.search_box)
        self.search_box.setValidator(input_validator)
        
        self.search_box.textChanged.connect(self.search_box_text_changed)
        self.search_box.setGeometry(0, 0, button_width, button_height)  
        self.search_box.setAlignment(Qt.AlignCenter)
        self.search_box.setStyleSheet("color: blue;"
                                 "font-size: 15pt;"
                                 "font-family: Kamran;"
                                 "font-weight: bold;")
        
        # Print Bill Button  
        print_bill_button = QPushButton("   چاپ قبض ها    ", self)
        print_bill_button.setGeometry(0, 0, button_width, button_height)
        print_bill_button.clicked.connect(self.print_bill_button_clicked)
        print_bill_button.setStyleSheet("color: black;"
                                           "font-size: 13pt;"
                                           "font-family: Titr;"
                                           "font-weight: bold;")

        # Print Report Button  
        print_report_button = QPushButton("   چاپ گزارشات    ", self)
        print_report_button.setGeometry(0, 0, button_width, button_height)
        print_bill_button.clicked.connect(self.print_report_button_clicked)
        print_report_button.setStyleSheet("color: black;"
                                           "font-size: 13pt;"
                                           "font-family: Titr;"
                                           "font-weight: bold;")
        
        # Monthly Payment Report Button  
        monthly_payment_report_button = QPushButton("   گزارش پرداخت ماهيانه   ", self)
        monthly_payment_report_button.setGeometry(0, 0, button_width, button_height)
        monthly_payment_report_button.clicked.connect(self.monthly_payment_report_button_clicked)
        monthly_payment_report_button.setStyleSheet("color: black;"
                                                    "font-size: 13pt;"
                                                    "font-family: Titr;"
                                                    "font-weight: bold;")

        # Winner List Delete Button  
        self.toggle_table_button = QPushButton("   نمايش جدول پرداخت    ", self)
        self.toggle_table_button.setGeometry(0, 0, button_width, button_height)
        self.toggle_table_button.clicked.connect(self.toggle_table_button_clicked)
        self.toggle_table_button.setStyleSheet("color: black;"
                                           "font-size: 13pt;"
                                           "font-family: Titr;"
                                           "font-weight: bold;")
        self.current_widget = "label"
        
        # Lottery Button  
        self.some_label = QLabel("گزارشات صندوق", self)
        self.some_label.setAlignment(Qt.AlignCenter)
        self.some_label.setGeometry(0, 0, head_label_width, head_label_height)
        self.some_label.setStyleSheet("color: white;"
                                      "border: 3px solid yellow;"
                                      "border-radius: 50px;"
                                      "font-family: Titr;"
                                      "padding: 2px;"
                                      "font-size: 50pt;"
                                      "font-weight: bold;")
        
    
        # Placing The Needed Widgets (Button, Labels, TextBoxes . . .) On Top Of The Table
        
        self.content_form_layout.addWidget(print_report_button, 0, 0)
        self.content_form_layout.addWidget(print_bill_button, 0, 1)
        self.content_form_layout.addWidget(monthly_payment_report_button, 0, 2)
        self.content_form_layout.addWidget(self.search_box, 0, 3)
        self.content_form_layout.addWidget(self.search_icon_label, 0, 4)
        self.content_form_layout.addWidget(self.toggle_table_button, 1, 0, 1, 5)
        self.content_form_layout.addWidget(self.some_label, 2, 0, 1,5)
        
        # Constructing A Upper Level Widget To Hold Everthing Together
        widget = QWidget()
        widget.setLayout(self.content_form_layout)
        self.setCentralWidget(widget)

    def print_report_button_clicked(self):
        print()
        
    def print_bill_button_clicked(self):
        
        global payment_list

        # Payment Papers
        payper = ListPrint()
        payper.printList(payment_list, temp_year, temp_month)

    def toggle_table_button_clicked(self):
        if (self.current_widget == "label"):
            # Lottery Button
            self.toggle_table_button.setText("   نمايش گزارشات عمومي صندوق    ")
            self.table_title_label = QLabel("جدول واريز ماهيانه", self)
            self.table_title_label.setAlignment(Qt.AlignCenter)
            self.table_title_label.setMaximumHeight(60)
            self.table_title_label.setStyleSheet("color: white;"
                                          "border: 1px solid white;"
                                          "border-radius: 10px;"
                                          "font-family: Titr;"
                                          "padding: 2px;"
                                          "font-size: 18pt;"
                                          "font-weight: bold;")
            # Create And Filling The Table With The Member Data List
            self.table = QtWidgets.QTableView()
            # Setting Table Visual Properties
            self.table.setStyleSheet("QTableView {background-color: rgba(255, 255, 255, 30);"
                                     "color: white;"
                                     "font-family: zar;"
                                     "font-size: 18pt;}")
            # Getting Header Click Event Of Table To Sort Column
            self.table.horizontalHeader().sectionClicked.connect(self.on_table_header_clicked)
        
            self.model = PandasModel(payment_list)
            self.table.setModel(self.model)
            
            self.layout.removeWidget(self.some_label)
            self.some_label.deleteLater()
            self.some_label = None


            self.content_form_layout.addWidget(self.table_title_label, 2, 0, 1,5)
            self.content_form_layout.addWidget(self.table, 3, 0, 1,5)
            widget = QWidget()
            widget.setLayout(self.content_form_layout)
            self.setCentralWidget(widget)
            
            self.current_widget = "table"
        else:
            self.toggle_table_button.setText("   نمايش جدول پرداخت    ")
            self.layout.removeWidget(self.table_title_label)
            self.table_title_label.deleteLater()
            self.table_title_label = None
            self.layout.removeWidget(self.table)
            self.table.deleteLater()
            self.table = None
                        

            # Lottery Button  
            self.some_label = QLabel("گزارشات صندوق", self)
            self.some_label.setAlignment(Qt.AlignCenter)
            self.some_label.setGeometry(0, 0, head_label_width, head_label_height)
            self.some_label.setStyleSheet("color: white;"
                                          "border: 3px solid yellow;"
                                          "border-radius: 50px;"
                                          "font-family: Titr;"
                                          "padding: 2px;"
                                          "font-size: 80pt;"
                                          "font-weight: bold;")
            self.content_form_layout.addWidget(self.some_label, 2, 0, 1,5)
            widget = QWidget()
            widget.setLayout(self.content_form_layout)
            self.setCentralWidget(widget)

            self.current_widget = "label"
            
    def monthly_payment_report_button_clicked(self):
        dlg = PaymentCalcPrompt()
        dlg.exec()
##        if (self.current_widget == "label"):
##            # Lottery Button
##            self.toggle_table_button.setText("   نمايش گزارشات عمومي صندوق    ")
##            self.table_title_label = QLabel("جدول واريز ماهيانه", self)
##            self.table_title_label.setAlignment(Qt.AlignCenter)
##            self.table_title_label.setMaximumHeight(60)
##            self.table_title_label.setStyleSheet("color: white;"
##                                          "border: 1px solid white;"
##                                          "border-radius: 25px;"
##                                          "font-family: Titr;"
##                                          "padding: 2px;"
##                                          "font-size: 18pt;"
##                                          "font-weight: bold;")
##            # Create And Filling The Table With The Member Data List
##            self.table = QtWidgets.QTableView()
##            # Setting Table Visual Properties
##            self.table.setStyleSheet("QTableView {background-color: rgba(255, 255, 255, 30);"
##                                     "color: white;"
##                                     "font-family: zar;"
##                                     "font-size: 18pt;}")
##                        # Getting Header Click Event Of Table To Sort Column
##            self.table.horizontalHeader().sectionClicked.connect(self.on_table_header_clicked)
##            
##            self.model = PandasModel(payment_list)
##            self.table.setModel(self.model)
##            
##            self.layout.removeWidget(self.some_label)
##            self.some_label.deleteLater()
##            self.some_label = None
##
##
##            self.content_form_layout.addWidget(self.table_title_label, 2, 0, 1,4)
##            self.content_form_layout.addWidget(self.table, 3, 0, 1,4)
##            widget = QWidget()
##            widget.setLayout(self.content_form_layout)
##            self.setCentralWidget(widget)
##            
##            self.current_widget = "table"
##        else:
##            self.model = PandasModel(payment_list)
##            self.table.setModel(self.model)
##            widget = QWidget()
##            widget.setLayout(self.content_form_layout)
##            self.setCentralWidget(widget)            
        
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> 
    #                                             (Lottery Window)
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <>
    def lottery_button_clicked(self):
        # This Code Will Create And Arrange Widgets On The Lottery Window

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global window_flag
        
        # Change Window Flag To Lottery Window
        window_flag = 'lottery_window'
        
        global member_list
        
        # Setting A Grid Layout To Place The Widgets On The Form
        self.content_form_layout = QGridLayout()
        self.content_form_layout.setHorizontalSpacing(hor_spacing)

        # Putting a Image Object For Search Icon
        self.search_icon_label = QLabel(self)
        self.search_icon = QPixmap('images/search_icon.png')
        self.search_icon = self.search_icon.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.search_icon_label.setPixmap(self.search_icon)  

        # Creating a QLineEdit Object For Search/Filter
        self.search_box = SearchQLineEdit("جست و جو/فيلتر", self)

        # Prevent Inserting Any Value
        input_validator = QRegExpValidator(persian_reg_ex, self.search_box)
        self.search_box.setValidator(input_validator)
        
        self.search_box.textChanged.connect(self.search_box_text_changed)
        self.search_box.setGeometry(0, 0, button_width, button_height)  
        self.search_box.setAlignment(Qt.AlignCenter)
        self.search_box.setStyleSheet("color: blue;"
                                 "font-size: 15pt;"
                                 "font-family: Kamran;"
                                 "font-weight: bold;")
        

        # Random Pick Button  
        random_pick_button = QPushButton("   انتخاب اتوماتيک اعضا   ", self)
        random_pick_button.setGeometry(0, 0, button_width, button_height)
        random_pick_button.clicked.connect(self.random_pick_button_clicked)
        random_pick_button.setStyleSheet("color: black;"
                                        "font-size: 13pt;"
                                        "font-family: Titr;"
                                        "font-weight: bold;")

        # Random Pick Button  
        manual_pick_button = QPushButton("   انتخاب دستي اعضا   ", self)
        manual_pick_button.setGeometry(0, 0, button_width, button_height)
        manual_pick_button.clicked.connect(self.manual_pick_button_clicked)
        manual_pick_button.setStyleSheet("color: black;"
                                        "font-size: 13pt;"
                                        "font-family: Titr;"
                                        "font-weight: bold;")
        

        # Winner Delete Button  
        delete_winner_button = QPushButton("   حذف برندگاه از ليست    ", self)
        delete_winner_button.setGeometry(0, 0, button_width, button_height)
        delete_winner_button.clicked.connect(self.delete_winner_button_clicked)
        delete_winner_button.setStyleSheet("color: black;"
                                           "font-size: 13pt;"
                                           "font-family: Titr;"
                                           "font-weight: bold;")

        # Winner List Delete Button  
        delete_winner_list_button = QPushButton("   پاک کردن تمام ليست برندگان    ", self)
        delete_winner_list_button.setGeometry(0, 0, button_width, button_height)
        delete_winner_list_button.clicked.connect(self.delete_all_winner_button_clicked)
        delete_winner_list_button.setStyleSheet("color: black;"
                                           "font-size: 13pt;"
                                           "font-family: Titr;"
                                           "font-weight: bold;")
        
        # Placing The Needed Widgets (Button, Labels, TextBoxes . . .) On Top Of The Table
        self.content_form_layout.addWidget(delete_winner_list_button, 0, 0)
        self.content_form_layout.addWidget(delete_winner_button, 0, 1)
        self.content_form_layout.addWidget(manual_pick_button, 0, 2)
        self.content_form_layout.addWidget(random_pick_button, 0, 3)
        
        # Spacer Label
        self.content_form_layout.addWidget(QLabel(" "), 0, 4)
        self.content_form_layout.addWidget(self.search_box, 0, 5)
        self.content_form_layout.addWidget(self.search_icon_label, 0, 6)

        
        # Create And Filling The Table With The Member Data List
        self.table = QtWidgets.QTableView()
        # Setting Table Visual Properties
        self.table.setStyleSheet("QTableView {background-color: rgba(255, 255, 255, 30);"
                                 "color: white;"
                                 "font-family: zar;"
                                 "font-size: 18pt;}")        
        self.model = PandasModel(lottery_winner_list)
        self.table.setModel(self.model)

        # Setting Header Columns Width On The Table
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Getting Header Click Event Of Table To Sort Column
        self.table.horizontalHeader().sectionClicked.connect(self.on_table_header_clicked)
        
        # Placing The Table Widgets At The Buttom Of The Page
        self.content_form_layout.addWidget(self.table, 1, 0, 1, 7)

        # Constructing A Upper Level Widget To Hold Everthing Together
        widget = QWidget()
        widget.setLayout(self.content_form_layout)
        self.setCentralWidget(widget)
        
    # This Slot Function Will Add New Member Data Into The Table Widget        
    def random_pick_button_clicked(self):
        dlg = RandomPickPrompt()
        dlg.exec()

        self.model = PandasModel(lottery_winner_list)
        self.table.setModel(self.model)

        
    def manual_pick_button_clicked(self):
        dlg = ManualPickPrompt()
        dlg.exec()

        self.model = PandasModel(lottery_winner_list)
        self.table.setModel(self.model)
    
    # This Slot Function Will Delete The Member Data Out Of The Table Widget        
    def delete_winner_button_clicked(self):
        dlg = DeleteWinnerPrompt()
        dlg.exec()

        self.model = PandasModel(lottery_winner_list)
        self.table.setModel(self.model) 

    # This Slot Function Will Delete The Member Data Out Of The Table Widget        
    def delete_all_winner_button_clicked(self):
        
        global lottery_winner_list
        global member_list
        
        dlg = QMessageBox(self)
        dlg.setWindowTitle("حذف تمام برنده ها ")
        dlg.setText("آيا از حذف کامل ليست هزينه ها مطمئن هستيد ؟")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()        
        if button == QMessageBox.Yes:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            lottery_winner_list.drop(lottery_winner_list.index, inplace = True)
            lottery_winner_list.reset_index(drop = True, inplace = True)
            member_list.loc[:, "وضعيت قرعه کشي"] = 0
            
            self.model = PandasModel(lottery_winner_list)
            self.table.setModel(self.model)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> 
    #                                                (Exit)
    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <>        
    def exit_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # This Code Will Exit The Window
        window.close()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    def on_table_header_clicked(self, columnIndex):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # This Slot Function Will Launch When Clicked On The Table Headers
        # Each Column Will Be Sorted By Clicking On It's Header
        
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global window_flag

        # First We Have To Know Where The Header Is Clicked And What Is The Source Of Click
        source = {
            'main_window'   :0,
            'member_window' : member_list,
            'loan_window'   : loan_list,
            'expense_window': expense_list,
            'report_window' : payment_list,
            'lottery_window': lottery_winner_list,
            }
        
        df = source[window_flag]
        row_index = df.index
        for i in row_index:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            for j in range(i+1, len(row_index)):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                if df.iloc[j, columnIndex] < df.iloc[i, columnIndex]:
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    df.iloc[i], df.iloc[j] =df.iloc[j].copy(), df.iloc[i].copy()
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.model = PandasModel(df)
        self.table.setModel(self.model)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def closeEvent(self, event):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # This Slot Function Will Save The Dataframes To xlsx And csv Files In Payment Folder
        member_list.to_excel('Database\Member_List.xlsx')
        loan_list.to_excel('Database\Loan_List.xlsx')
        expense_list.to_excel('Database\Expense_List.xlsx')
        balance_list.to_excel('Database\Balance_List.xlsx')
        lottery_winner_list.to_excel('Database\Lottery_Winner_List.xlsx')
        member_list.to_csv('Database\Member_List.csv')
        loan_list.to_csv('Database\Loan_List.csv')
        expense_list.to_csv('Database\Expense_List.csv')
        balance_list.to_csv('Database\Balance_List.csv')
        lottery_winner_list.to_csv('Database\Lottery_Winner_List.csv')        
##        if can_exit:
##            event.accept() # let the window close
##        else:
##            event.ignore()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    def search_box_text_changed(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # This Slot Function Will Launch When Some Text Is Written In The Search TextBox

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global window_flag

        # First We Have To Know Where The Header Is Clicked And What Is The Source Of Click
        source = {
            'main_window'   :0,
            'member_window' : member_list,
            'loan_window'   : loan_list,
            'expense_window': expense_list,
            'report_window' : payment_list,
            'lottery_window': lottery_winner_list,
            }
        
        df = source[window_flag]
        row, column = df.shape
        similar_row_index = []
        for i in range(0, row):
            for j in range(0, column):
                if self.search_box.text() in str(df.iloc[i, j]):
                    similar_row_index.append(i)
                    break
        self.model = PandasModel(df.iloc[similar_row_index])
        self.table.setModel(self.model)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Focus In/Out Class For Search Box
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class SearchQLineEdit(QtWidgets.QLineEdit):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    def focusInEvent(self, event):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        if (self.text() == "جست و جو/فيلتر"):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.setText("")
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().focusInEvent(event)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def focusOutEvent(self, event):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        if (self.text() == ""):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.setText("جست و جو/فيلتر")
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().focusOutEvent(event)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# New Class For Creating Table Model Using Pandas Dataframe
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class PandasModel(QtCore.QAbstractTableModel):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Class to populate a table view with a pandas dataframe
    def __init__(self, data, parent=None):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def rowCount(self, parent=None):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        return len(self._data.values)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def columnCount(self, parent=None):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        return self._data.columns.size
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def data(self, index, role=QtCore.Qt.DisplayRole):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        if index.isValid():
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            if role == QtCore.Qt.DisplayRole:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                return str(self._data.iloc[index.row()][index.column()])
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        return None
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def headerData(self, col, orientation, role):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            return self._data.columns[col]
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        return None
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# New Class For Add Member Prompt Window
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class AddMemberPrompt(QDialog):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def __init__(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().__init__()

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global total_deposit
        global member_list

        # Visual Arrangements Of The Form
        # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
        self.setWindowTitle("افزودن عضو")
        self.layout = QVBoxLayout()

        # This Codes Finds The Highest Member Number To Ease The Input Process
        row = member_list.shape[0]
        self.highest_member_number = 100000
        
        for i in range(0, row):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            if (self.highest_member_number < int(member_list.iat[i, 0])):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.highest_member_number = int(member_list.iat[i, 0])
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # Making A TextBox To Get The Member Number
        self.layout.addWidget(QLabel("شماره عضويت"))
        self.member_number_input = QLineEdit(str(self.highest_member_number + 1))
        input_validator = QRegExpValidator(number_reg_ex, self.member_number_input)
        self.member_number_input.setValidator(input_validator)
        self.layout.addWidget(self.member_number_input)        

        # Making A TextBox To Get The Member Prefix
        self.layout.addWidget(QLabel("پيشوند"))
        self.member_prefix_input = QComboBox()
        self.member_prefix_input.addItems(["جناب آقاي", "سرکار خانم"])
        input_validator = QRegExpValidator(persian_reg_ex, self.member_prefix_input)
        self.member_prefix_input.setValidator(input_validator)
        self.layout.addWidget(self.member_prefix_input)

        # Making A TextBox To Get The Member Name
        self.layout.addWidget(QLabel("نام"))
        self.member_name_input = QLineEdit()
        input_validator = QRegExpValidator(persian_reg_ex, self.member_name_input)
        self.member_name_input.setValidator(input_validator)
        self.layout.addWidget(self.member_name_input)

        # Making A TextBox To Get The Member Last Name
        self.layout.addWidget(QLabel("نام خانوادگي"))
        self.member_lname_input = QLineEdit()
        input_validator = QRegExpValidator(persian_reg_ex, self.member_lname_input)
        self.member_lname_input.setValidator(input_validator)
        self.layout.addWidget(self.member_lname_input)

        # Making A TextBox To Get The Member ID Number
        self.layout.addWidget(QLabel("کد ملي"))
        self.member_idnum_input = QLineEdit()
        input_validator = QRegExpValidator(number_reg_ex, self.member_idnum_input)
        self.member_idnum_input.setValidator(input_validator)
        self.layout.addWidget(self.member_idnum_input)

        # Making A TextBox To Get The Member Total Deposit
        self.layout.addWidget(QLabel("مبلغ پس انداز"))
        self.total_deposit_input = QLineEdit(str(total_deposit))
        input_validator = QRegExpValidator(number_reg_ex, self.total_deposit_input)
        self.total_deposit_input.setValidator(input_validator)
        self.layout.addWidget(self.total_deposit_input)

        # Making A TextBox To Get The Member Details
        self.layout.addWidget(QLabel("توضيحات"))
        self.member_detail_input = QLineEdit()
        input_validator = QRegExpValidator(persian_reg_ex, self.member_detail_input)
        self.member_detail_input.setValidator(input_validator)
        self.layout.addWidget(self.member_detail_input)
        
        # Making A Pushbutton To Submit The New Member When Pressed
        new_member_submit_button = QPushButton("ثبت عضو جديد")
        new_member_submit_button.clicked.connect(self.new_member_submit_button_clicked)
        self.layout.addWidget(new_member_submit_button)

        # Making A PushButton To Exit The Form When Pressed   
        close_button = QPushButton("خروج")
        close_button.clicked.connect(self.close_button_clicked)
        self.layout.addWidget(close_button)

        # Setting The Visual Layout Of The Form
        self.setLayout(self.layout)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def new_member_submit_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global balance_list
        global total_deposite
        global monthly_deposit
        global total_asset
        global total_liability
        global balance
        global bank_profit
        global account_balance
        global balance_diff
        
        
        # This Variable Ensures That The Newly Inserted Member Number Was Not Priviously Existed
        similarity = 0
        # Check If The Member Number Input Is Empty Or Not
        if (self.member_number_input.text() != ""):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> Member Number Input Is Not Empty
            row = member_list.shape[0]
            # Check For Similarity
            for i in range(0, row):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                if (str(member_list["شماره عضويت"][i]) == str(self.member_number_input.text())):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    # --> This Member Number Has Already Taken
                    similarity = 1
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            if (similarity == 0):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> Member Number Is Not Taken
                if (self.member_name_input.text() != ""):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    # --> Member Name Input Is Not Empty
                    if (self.member_lname_input.text() != ""):
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        # --> Member Last Name Input Is Not Empty
                        row = member_list.shape[0]
                        member_list.loc[row] = [int(self.member_number_input.text()),
                                                str(self.member_prefix_input.currentText()),
                                                str(self.member_lname_input.text()),
                                                str(self.member_name_input.text()),
                                                str(self.member_idnum_input.text()),
                                                int(self.total_deposit_input.text()),
                                                int(monthly_deposit),
                                                0,
                                                0,
                                                1,
                                                str(self.member_detail_input.text())]
                        
                        # Total Assets And Liabilities Should Be Updated
                        balance_list_new_row = balance_list.shape[0]
                        
                        total_asset     += int(self.total_deposit_input.text())

                        balance_list.loc[balance_list_new_row] = [int(balance_list_new_row + 1),
                                                                  int(current_year),
                                                                  int(current_month),
                                                                  int(current_day),
                                                                  int(total_asset),
                                                                  0,
                                                                  0,
                                                                  0,
                                                                  0,
                                                                  0,
                                                                  'افزايش پس انداز از بابت عضو جديد : ' +
                                                                  str(self.member_name_input.text()) + ' ' +
                                                                  str(self.member_lname_input.text())]

                        dlg = QMessageBox(self)
                        dlg.setWindowTitle("عضو جديد")
                        dlg.setText("عضو جديد به شماره : " + str(self.member_number_input.text())
                                    + "مربوط به\n" + str(self.member_name_input.text()) + " " +
                                    str(self.member_lname_input.text()) + "\n" + "اضافه گرديد")
                        dlg.setStandardButtons(QMessageBox.Ok)
                        dlg.setIcon(QMessageBox.Question)
                        button = dlg.exec()

                        self.highest_member_number += 1
                        self.member_number_input.setText(str(self.highest_member_number + 1))
                        self.member_name_input.setText("")
                        self.member_lname_input.setText("")
                        self.member_idnum_input.setText("")
                        self.member_detail_input.setText("")
                        member_list.reset_index(drop = True, inplace = True)
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    else:
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        # --> Member Last Name Input Is Empty
                        dlg = QMessageBox(self)
                        dlg.setWindowTitle("توجه")
                        dlg.setText("نام خانوادگي عضو را وارد کنيد")
                        dlg.setStandardButtons(QMessageBox.Ok)
                        dlg.setIcon(QMessageBox.Question)
                        button = dlg.exec()
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                else:
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    # --> Member Name Input Is Empty
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("توجه")
                    dlg.setText("نام عضو را وارد کنيد")
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setIcon(QMessageBox.Question)
                    button = dlg.exec()
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            else:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> Member Number Is Used Before
                dlg = QMessageBox(self)
                dlg.setWindowTitle("توجه")
                dlg.setText("فرد ديگري با اين شماره عضويت ثبت گرديده است\n شماره عضويت را تغيير دهيد")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Question)
                button = dlg.exec()
                self.member_number_input.setText("")
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> Member Number Input Is Not Empty
            # Making A Label To Say That Member Number Input Is Empty
            dlg = QMessageBox(self)
            dlg.setWindowTitle("توجه")
            dlg.setText("شماره عضويت را وارد کنيد")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Question)
            button = dlg.exec()
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def close_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.close()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# New Class For Delete Member Prompt Window
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class DeleteMemberPrompt(QDialog):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def __init__(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().__init__()

        # Visual Arrangements Of The Form
        # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
        self.setWindowTitle("حذف عضو")
        self.layout = QVBoxLayout()

        # Making A ComboBox To Show Existing Member Numbers
        self.layout.addWidget(QLabel("شماره عضويت"))
        self.member_number_combo = QComboBox()
        # Adding Members From member_list To ComboBox
        row = member_list.shape[0]
        # Check If There Is Any Members In The member_list
        if row != 0:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> member_list Is Not Empty
            # Making A ComboBox To Show Existing Member Numbers 
            self.layout.addWidget(QLabel("شماره عضويت"))
            self.member_number_combo = QComboBox()           
            # Filling ComboBox Items With The Member Number Data In The member_list Dataframe
            # And Using It's Item_Changed Event To Refresh The Member Data On The Member Data Label Below
            member_index = member_list.index
            for i in member_index:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.member_number_combo.addItem(str(member_list["شماره عضويت"][i]))
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.member_number_combo.currentTextChanged.connect(self.member_number_combo_changed)
            self.layout.addWidget(self.member_number_combo)            
            
            # Making A Label To Show The Member's Data (Prefix, Name and Last Name)
            self.layout.addWidget(QLabel(" نام عضو  :"))
            # Calculating Data (Member Numbers And Their Corresponding Indices)
            member_number = int(self.member_number_combo.currentText())
            member_index = member_list[member_list["شماره عضويت"] == member_number].index[0]
            member_prefix = member_list["پيشوند"][member_index]
            member_name  = member_list["نام"][member_index]
            member_lname = member_list["نام خانوادگي"][member_index]
            self.member_name_label = QLabel(member_prefix + "\n" + member_name + "\n" + member_lname)
            self.layout.addWidget(self.member_name_label)
            # Making A PushButton To Delete The Member When Pressed
            delete_member_submit_button = QPushButton("حذف عضو")
            delete_member_submit_button.clicked.connect(self.delete_member_submit_button_clicked)
            self.layout.addWidget(delete_member_submit_button)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> member_list Is Empty
            # Making A Label To Say That lottery_winner_list Is Empty
            self.layout.addWidget(QLabel(" ليست اعضا خاليست"))
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            
        # Making A PushButton To Exit The Form When Pressed
        close_button = QPushButton("خروج")
        close_button.clicked.connect(self.close_button_clicked)
        self.layout.addWidget(close_button)
        
        # Setting The Visual Layout Of The Form
        self.setLayout(self.layout)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def member_number_combo_changed(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # Making A Label To Show The Member's Data (Prefix, Name and Last Name) When 
        # Item_Changed Event Of ComboBox Happens
        # Calculating Data (Member Numbers And Their Corresponding Indices)
        member_number = int(self.member_number_combo.currentText())
        member_index = member_list[member_list["شماره عضويت" ] == member_number].index[0]
        member_prefix = member_list["پيشوند"][member_index]
        member_name  = member_list["نام"][member_index]
        member_lname = member_list["نام خانوادگي"][member_index]
        # Updating The Label To Show Newly Selected Item In ComboBox        
        self.member_name_label.setText(member_prefix + "\n" + member_name + "\n" + member_lname)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def delete_member_submit_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global balance_list
        global total_asset
        global total_liability
        global balance
        global bank_profit
        global account_balance
        global balance_diff

        
        # Calculating Data (Member Numbers And Their Corresponding Indices)
        member_number = int(self.member_number_combo.currentText())
        member_index = member_list[member_list["شماره عضويت" ] == member_number].index[0]
        # Showing A Message To Check If User Is Sure Or Not
        dlg1 = QMessageBox(self)
        dlg1.setWindowTitle("توجه")
        dlg1.setText("آيا از حذف عضو به شماره : " +
                     str(member_list["شماره عضويت"][member_index]) +
                     " مربوط به \n" +
                     str(member_list["نام"][member_index]) + " " +
                     str(member_list["نام خانوادگي"][member_index]) + "\n" +
                     "مطمئن هستيد؟")        
        dlg1.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg1.setIcon(QMessageBox.Question)
        button1 = dlg1.exec()               
        
        if button1 == QMessageBox.Yes:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> User Admits
            # Check If The Member Had Recieved A Loan So Far Or Not
            if (member_list["وضعيت وام"][member_index] == 1):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> Member Has A Loan Assigned For Him/Her
                # Calculating Data (Loan Numbers And Their Corresponding Indices)
                loan_index = loan_list.loc[loan_list["شماره عضويت" ] == member_number].index[0]
                loan_number = loan_list["شماره وام"][loan_index]
                # Showing A Message To Inform There Is A Loan Assigned To This Member
                dlg2 = QMessageBox(self)
                dlg2.setWindowTitle("توجه")
                dlg2.setText("وام به شماره :  " + "\n" + str(loan_number) + "\n" +
                            "توسط اين عضو هنوز تسويه نشده است" + "\n"
                            "آيا از پاک کردن اين عضو مطمين هستيد؟")                
                dlg2.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                dlg2.setIcon(QMessageBox.Question)
                button2 = dlg2.exec()
                if button2 == QMessageBox.Yes:
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    # --> User Admits
                    # Delete The Loan of That loan_index  
                    loan_list.drop(loan_index, axis = 0, inplace = True)
                    # Reset The Index Numbering To Start From 0 And Ascend Till Last Row
                    loan_list.reset_index(drop = True, inplace = True)
                    # Checking Whether If The Member Is In Lottery Winner List Or Not
                    if (member_list["وضعيت قرعه کشي"][member_index] == 1):
                        lottery_winner_index = lottery_winner_list[
                            lottery_winner_list["شماره عضويت" ] == member_number].index[0]
                        lottery_winner_list.drop(lottery_winner_index, axis = 0, inplace = True)
                        lottery_winner_list.reset_index(drop = True, inplace = True)

                    # Total Assets Should Be Subtracted By Deleted Member's Total Deposite
##                    total_asset -= member_list["مبلغ پس انداز"][member_index]
##                    balance_list["مجموع پس انداز و درصد"][balance_list_new_row] = total_asset
                    
                    # Delete The Member of That member_index
                    member_list.drop(member_index, axis = 0, inplace = True)
                    # Reset The Index Numbering To Start From 0 And Ascend Till Last Row
                    member_list.reset_index(drop = True, inplace = True)
                    # Checking Whether If The ComboBox Has At Least 1 Item Or It's Empty
                    if (self.member_number_combo.count() != 1):
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        # --> The member_number_input ComboBox Has At Least 1 Item
                        # Removing The Deleted Item Of member_list From ComboBox
                        self.member_number_combo.removeItem(self.member_number_combo.currentIndex())
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    else:
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        # --> The member_number_input ComboBox Has No Item
                        # Prompting A MessageBox To Inform The Situation
                        dlg = QMessageBox(self)
                        dlg.setWindowTitle("توجه")
                        dlg.setText( "آخرين فرد ليست حذف گرديد" + "\n" + "ليست اعضا خاليست")
                        dlg.setStandardButtons(QMessageBox.Ok)
                        dlg.setIcon(QMessageBox.Question)
                        button = dlg.exec()
                        self.close()
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            else:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> Member Does Not Have Assigned Loan
                # Checking Whether If The Member Is In Lottery Winner List Or Not
                if (member_list["وضعيت قرعه کشي"][member_index] == 1):
                    lottery_winner_index = lottery_winner_list[
                        lottery_winner_list["شماره عضويت" ] == member_number].index[0]
                    lottery_winner_list.drop(lottery_winner_index, axis = 0, inplace = True)
                    lottery_winner_list.reset_index(drop = True, inplace = True)
                # Delete The Member of That member_index  
                member_list.drop(member_index, axis = 0, inplace = True)
                # Reset The Index Numbering To Start From 0 And Ascend Till Last Row
                member_list.reset_index(drop = True, inplace = True)
                
                # Checking Whether If The ComboBox Has At Least 1 Item Or It's Empty
                if (self.member_number_combo.count() != 1):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    # --> The member_number_input ComboBox Has At Least 1 Item
                    # Removing The Deleted Item Of lottery_winner_list From ComboBox
                    self.member_number_combo.removeItem(self.member_number_combo.currentIndex())
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                else:
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    # --> The member_number_input ComboBox Has No Item
                    # Prompting A MessageBox To Inform The Situation
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("توجه")
                    dlg.setText( "آخرين فرد ليست حذف گرديد" + "\n" + "ليست اعضا خاليست")
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setIcon(QMessageBox.Question)
                    button = dlg.exec()
                    self.close()
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def close_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.close()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# New Class For Monthly Deposite Prompt Window
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class MonthlyDepositePrompt(QDialog):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def __init__(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().__init__()

        # Visual Arrangements Of The Form
        # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
        self.setWindowTitle("پس انداز ماهيانه")
        self.layout = QVBoxLayout()

        # Getting Number Of Members in member_list
        row = member_list.shape[0]
        # Check If There Is Any Members In The member_list       
        if row != 0:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
            self.layout.addWidget(QLabel("مبلغ پس انداز ماهيانه اعضا"))
            self.monthly_deposit_input = QLineEdit()
            input_validator = QRegExpValidator(number_reg_ex, self.monthly_deposit_input)
            self.monthly_deposit_input.setValidator(input_validator)
            self.layout.addWidget(self.monthly_deposit_input)
            
            monthly_deposit_submit_button = QPushButton("تغيير مبلغ پس انداز ماهيانه (تومان)")
            monthly_deposit_submit_button.clicked.connect(self.monthly_deposit_submit_button_clicked)
            self.layout.addWidget(monthly_deposit_submit_button)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # Making A Label To Say That lottery_winner_list Is Empty
            self.layout.addWidget(QLabel(" ليست اعضا خاليست"))
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        close_button = QPushButton("خروج")
        close_button.clicked.connect(self.close_button_clicked)
        self.layout.addWidget(close_button)
        
        self.setLayout(self.layout)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def monthly_deposit_submit_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global monthly_deposit

        
        if (self.monthly_deposit_input.text() != ""):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            dlg = QMessageBox(self)
            dlg.setWindowTitle("توجه")
            dlg.setText("آيا از تغيير مبلغ پس انداز ماهيانه به : " +
                        self.monthly_deposit_input.text() +
                        "  تومان مطمئن هستيد ؟ ")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Question)
            button = dlg.exec()

            if button == QMessageBox.Yes:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                monthly_deposit = self.monthly_deposit_input.text()
                self.close()
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            dlg = QMessageBox(self)
            dlg.setWindowTitle("توجه")
            dlg.setText("براي فيلد مبلغ پس انداز ماهيانه عدد وارد کنيد")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Question)
            button = dlg.exec()
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def close_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.close()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# New Class For Monthly Deposite Prompt Window
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class ReturnPacePrompt(QDialog):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def __init__(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().__init__()

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list

        # Visual Arrangements Of The Form
        # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
        self.setWindowTitle("پس انداز ماهيانه")
        self.layout = QVBoxLayout()

        # Getting Number Of Members in member_list
        row = member_list.shape[0]
        # Check If There Is Any Members In The member_list
        if row != 0:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> member_list Is Not Empty    
            # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
            self.layout.addWidget(QLabel("شماره عضويت"))
            self.member_number_combo = QComboBox()
            # Calculating Member Index
            member_index = member_list.index
            # Adding Members From member_list To ComboBox
            for i in member_index:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.member_number_combo.addItem(str(member_list["شماره عضويت"][i]))
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.member_number_combo.currentTextChanged.connect(self.member_number_combo_changed)
            self.layout.addWidget(self.member_number_combo)

            # Calculating Member Data Selected In ComboBox
            member_number = int(self.member_number_combo.currentText())
            member_index = member_list[member_list["شماره عضويت" ] == member_number].index[0]            
            member_prefix = member_list["پيشوند"][member_index]
            member_name  = member_list["نام"][member_index]
            member_lname = member_list["نام خانوادگي"][member_index]

            # Making A Label To Show Member Data Selected In ComboBox
            self.layout.addWidget(QLabel(" نام عضو  :"))
            self.member_name_label = QLabel(member_prefix + "\n" + member_name + "\n" + member_lname)            
            self.layout.addWidget(self.member_name_label)

            # Making A ComboBox To Get Return Pace Of Given Member
            self.layout.addWidget(QLabel("سرعت بازپرداخت وام"))
            self.loan_return_pace_combo = QComboBox()
            for i in range(1, 24):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.loan_return_pace_combo.addItem(str(i))
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.layout.addWidget(self.loan_return_pace_combo)
            
            # Making A Push Button To Change Te Retun Pace Of Member When Pressed
            loan_return_pace_submit_button = QPushButton("تغيير سرعت بازپرداخت وام")
            loan_return_pace_submit_button.clicked.connect(self.loan_return_pace_submit_button_clicked)
            self.layout.addWidget(loan_return_pace_submit_button)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> member_list Is Empty  
            # Making A Label To Say That Expense List Is Empty
            self.layout.addWidget(QLabel("ليست اعضا خاليست"))
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # Making A PushButton To Exit The Form When Pressed      
        close_button = QPushButton("خروج")
        close_button.clicked.connect(self.close_button_clicked)
        self.layout.addWidget(close_button)
        
        # Setting The Visual Layout Of The Form
        self.setLayout(self.layout)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def member_number_combo_changed(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # Calculating Member Data Selected In ComboBox
        member_number = int(self.member_number_combo.currentText())
        member_index = member_list[member_list["شماره عضويت" ] == member_number].index[0]        
        member_prefix = member_list["پيشوند"][member_index]
        member_name  = member_list["نام"][member_index]
        member_lname = member_list["نام خانوادگي"][member_index]
        # Updating The Label With New Selected Item
        self.member_name_label.setText(member_prefix + "\n" + member_name + "\n" + member_lname)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
    def loan_return_pace_submit_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list

        # Calculating Member Data Selected In ComboBox
        member_number = int(self.member_number_combo.currentText())
        member_index = member_list[member_list["شماره عضويت" ] == member_number].index[0]
        
        # Check If The Newly Inserted Data Is Different Than Privious One
        if (int(self.loan_return_pace_combo.currentText()) !=
            int(member_list["سرعت بازپرداخت"][member_index])):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # New Inserted Return Pace Is Different Than The Privious Value
            # Showing A Message To Check If The User Is Sure 
            dlg = QMessageBox(self)
            dlg.setWindowTitle("توجه")
            member_prefix = member_list["پيشوند"][member_index]
            member_name  = member_list["نام"][member_index]
            member_lname = member_list["نام خانوادگي"][member_index]
            dlg.setText(" آيا از تغيير سرعت بازپرداخت " + "\n" +
                        str(member_prefix) + "\n" +
                        str(member_name) + " " +
                        str(member_lname) + "\n" +
                        " از تعداد " + str(member_list["سرعت بازپرداخت"][member_index]) +
                        " قسط در هر ماه " + "\n" +
                        " به تعداد" + str(self.loan_return_pace_combo.currentText()) +
                        " قسط در هر ماه " + "\n" + "  مطمئن هستيد؟  ")
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Question)
            button = dlg.exec()

            if button == QMessageBox.Yes:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> User Admits
                member_list["سرعت بازپرداخت"][member_index] = int(self.loan_return_pace_combo.currentText())
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def close_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.close()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# New Class For Add Loan Prompt Window
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class AddLoanPrompt(QDialog):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def __init__(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().__init__()

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global default_commision_rate
        global default_installment_count
        global temp

        # Visual Arrangements Of The Form
        # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
        self.setWindowTitle("افزودن وام")
        self.layout = QVBoxLayout()

        # Find Members Who Have Not Recieved Loan Yet
        row = member_list[member_list["وضعيت وام"] == 0].shape[0]
        # Check If There Is Any Loan In The expense_list
        if row != 0:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> There Is At Least One Member Who Hase Not Received Loan
            # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
            self.layout.addWidget(QLabel("شماره عضويت"))
            self.member_number_combo = QComboBox()

            no_loan_index = member_list[member_list["وضعيت وام"] == 0].index
            for i in no_loan_index:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    self.member_number_combo.addItem(str(member_list["شماره عضويت"][i]))
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.member_number_combo.currentTextChanged.connect(self.member_number_combo_changed)
            self.layout.addWidget(self.member_number_combo)

            # Calculating Loan And Corresponding Member Data Selected In ComboBox
            member_number = int(self.member_number_combo.currentText())
            member_index = member_list[member_list["شماره عضويت" ] == member_number].index[0]           
            member_prefix = member_list["پيشوند"][member_index]
            member_name  = member_list["نام"][member_index]
            member_lname = member_list["نام خانوادگي"][member_index]

            # Making A Label To Show Loan And Member Data Selected In ComboBox
            self.layout.addWidget(QLabel(" نام عضو  :"))
            self.member_name_label = QLabel(member_prefix + "\n" + member_name + "\n" + member_lname)            
            self.layout.addWidget(self.member_name_label)

            # This Codes Finds The Highest Loan Number To Ease The Input Process
            row = loan_list.shape[0]
            self.highest_loan_number = 1000000
            for i in range(0, row):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                if (self.highest_loan_number < int(loan_list.iat[i, 3])):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    self.highest_loan_number =  int(loan_list.iat[i, 3])
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

            # Making A Textbox To Get The Loan Number
            self.layout.addWidget(QLabel("شماره وام"))
            self.loan_number_input = QLineEdit(str(self.highest_loan_number + 1))
            input_validator = QRegExpValidator(number_reg_ex, self.loan_number_input)
            self.loan_number_input.setValidator(input_validator)
            self.layout.addWidget(self.loan_number_input)

            # Making A ComboBox To Show The Year Date Set To Current Year
            self.layout.addWidget(QLabel("تاريخ (سال)"))
            self.loan_ydate_combo = QComboBox()
            now_index = 0
            for i in range(1300, 1501):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.loan_ydate_combo.addItem(str(i))            
                if i < int(current_year):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    now_index += 1
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.loan_ydate_combo.setCurrentIndex(now_index)
            self.layout.addWidget(self.loan_ydate_combo)

            # Making A ComboBox To Show The Month Date Set To Current Month
            self.layout.addWidget(QLabel("تاريخ (ماه)"))
            self.loan_mdate_combo = QComboBox()
            now_index = 0
            for i in range(1, 13):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.loan_mdate_combo.addItem(str(i))            
                if i < int(current_month):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    now_index += 1
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.loan_mdate_combo.setCurrentIndex(now_index)
            self.layout.addWidget(self.loan_mdate_combo)
            
            # Making A ComboBox To Show The Day Date Set To Current Day
            self.layout.addWidget(QLabel("تاريخ (روز)"))
            self.loan_ddate_combo = QComboBox()
            now_index = 0
            for i in range(1, 32):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.loan_ddate_combo.addItem(str(i))            
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.loan_ddate_combo.setCurrentIndex(0)
            self.layout.addWidget(self.loan_ddate_combo)

            # Making A Textbox To Get The Loan Price
            self.layout.addWidget(QLabel("مبلغ وام"))
            self.loan_price_input = QLineEdit()
            input_validator = QRegExpValidator(number_reg_ex, self.loan_price_input)
            self.loan_price_input.textChanged.connect(self.loan_price_input_text_changed)
            self.loan_price_input.setValidator(input_validator)
            self.layout.addWidget(self.loan_price_input)

            # Making A Textbox To Get The Loan Debt Left
            self.layout.addWidget(QLabel("مانده بدهي"))
            self.loan_debt_input = QLineEdit()
            input_validator = QRegExpValidator(number_reg_ex, self.loan_debt_input)
            self.loan_debt_input.setValidator(input_validator)
            self.layout.addWidget(self.loan_debt_input)
            
            # Making A ComboBox To Get The Commision Rate
            self.layout.addWidget(QLabel(" (%) درصد کارمزد"))
            self.loan_commision_rate_combo = QComboBox()
            self.loan_commision_rate_combo.addItem(str(0.5))
            self.loan_commision_rate_combo.addItem(str(0.6))
            self.loan_commision_rate_combo.addItem(str(0.7))
            self.loan_commision_rate_combo.addItem(str(0.8))
            self.loan_commision_rate_combo.addItem(str(0.9))
            loan_commision_rate = 5
            for i in range(1, 6):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.loan_commision_rate_combo.addItem(str(i))            
                if i < int(default_commision_rate):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    loan_commision_rate += 1
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.loan_commision_rate_combo.setCurrentIndex(loan_commision_rate)
            self.layout.addWidget(self.loan_commision_rate_combo)

            # Making A ComboBox To Get The Loan Installment Count
            self.layout.addWidget(QLabel("تعداد اقساط (ماه)"))
            self.installment_count_combo = QComboBox()
            installment_count = 0
            for i in range(20, 31):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.installment_count_combo.addItem(str(i))            
                if i < int(default_installment_count):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    installment_count += 1
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.installment_count_combo.setCurrentIndex(installment_count)
            self.layout.addWidget(self.installment_count_combo)

            # Making A Textbox To Get The Loan Details
            self.layout.addWidget(QLabel("توضيحات"))
            self.loan_detail_input = QLineEdit()
            input_validator = QRegExpValidator(persian_reg_ex, self.loan_detail_input)
            self.loan_detail_input.setValidator(input_validator)
            self.layout.addWidget(self.loan_detail_input)

            # Making A Pushbutton To Submit The New Loan When Pressed
            new_loan_submit_button = QPushButton("ثبت وام جديد")
            new_loan_submit_button.clicked.connect(self.new_loan_submit_button_clicked)
            self.layout.addWidget(new_loan_submit_button)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> Every One Has Received Loan
            # Making A Label To Say That Loan List Is Empty
            self.layout.addWidget(QLabel("هيچ کدام از اعضا وام تسويه شده ندارند"))
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # Making A PushButton To Exit The Form When Pressed
        close_button = QPushButton("خروج")
        close_button.clicked.connect(self.close_button_clicked)
        self.layout.addWidget(close_button)
        
        # Setting The Visual Layout Of The Form
        self.setLayout(self.layout)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def member_number_combo_changed(self, value):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # Calculating Data (Member Numbers And Their Corresponding Indices)
        member_number = int(self.member_number_combo.currentText())
        member_index = member_list[member_list["شماره عضويت" ] == member_number].index[0]        
        member_prefix = member_list["پيشوند"][member_index]
        member_name  = member_list["نام"][member_index]
        member_lname = member_list["نام خانوادگي"][member_index]
        # Updating The Label With Item Selected In The ComboBox
        self.member_name_label.setText(member_prefix + "\n" + member_name + "\n" + member_lname)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def loan_price_input_text_changed(self):
        self.loan_debt_input.setText(self.loan_price_input.text())
        
    def new_loan_submit_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global loan_list
        global balance_list
        global total_asset
        global total_liability
        global balance
        global bank_profit
        global account_balance
        global balance_diff
        
        # Calculating Data (Member Numbers And Their Corresponding Indices)
        member_number = int(self.member_number_combo.currentText())
        member_index = member_list[member_list["شماره عضويت" ] == member_number].index[0]
        
        # This Variable Ensures That The Newly Inserted Member Number Was Not Priviously Existed
        similarity = 0
        
        if (self.loan_number_input.text() != ""):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> Loan Number Input Is Not Empty
            row = loan_list.shape[0]
            # Check For Similarity
            for i in range(0, row):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                if (str(loan_list["شماره وام"][i]) == self.loan_number_input.text()):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    similarity = 1
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    
            if (similarity == 0):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> Loan Number Has Not Been Chosen Befor
                if(self.loan_price_input.text() != ""):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    # --> Loan Price Input Is Not Empty
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("توجه")
                    member_prefix = member_list["پيشوند"][member_index]
                    member_name  = member_list["نام"][member_index]
                    member_lname = member_list["نام خانوادگي"][member_index]
                    dlg.setText("آيا از ثبت وام به شماره " + str(self.loan_number_input.text()) +
                                "\n" +
                                "  به مبلغ  " +
                                str(self.loan_price_input.text())  +
                                "\n" +
                                "  در  " +
                                str(self.installment_count_combo.currentText())  +
                                "  قسط  " +
                                "\n" +
                                "  با کارمزد  " +
                                str(self.loan_commision_rate_combo.currentText())  +
                                "  درصد  " +
                                "\n" +
                                "  براي  " +
                                str(member_prefix)  + " " +
                                str(member_name) + " " +
                                str(member_lname) + "\n" +
                                "  مطمئن هستيد؟  ")
                    
                    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    dlg.setIcon(QMessageBox.Question)
                    button = dlg.exec()
                    if button == QMessageBox.Yes:
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        # --> User Admits
                        # Rest Of Code Continues To The Next Line
                        installment_amount = int((int(self.loan_price_input.text()) \
                                        // int(self.installment_count_combo.currentText()))//10000) * 10000
                        
                        # Calculating The Installments Left In Case The Member Has Paid Back
                        installment_left = int(int(self.installment_count_combo.currentText()) -
                                               (int(self.loan_price_input.text()) -
                                                int(self.loan_debt_input.text()))//installment_amount)

                        # Rest Of Code Continues To The Next Line
                        loan_commision_amount = int(int(self.loan_price_input.text()) \
                                                * float(self.loan_commision_rate_combo.currentText()) // 100)
                        #"مانده بدهي", "اقساط باقي مانده"
                        loan_list.loc[row] = [int(self.member_number_combo.currentText()),
                                              str(member_lname),
                                              str(member_name),
                                              int(self.loan_number_input.text()),
                                              int(self.loan_ydate_combo.currentText()),
                                              int(self.loan_mdate_combo.currentText()),
                                              int(self.loan_ddate_combo.currentText()),
                                              int(self.loan_price_input.text()),
                                              int(self.installment_count_combo.currentText()),
                                              int(installment_amount),
                                              int(self.loan_commision_rate_combo.currentText()),
                                              int(loan_commision_amount),
                                              int(self.loan_debt_input.text()),
                                              int(installment_left),
                                              str(self.loan_detail_input.text())]
                        # Find The Member And Set The Loan Status To 1
                        member_list["وضعيت وام"][member_index] = 1
                        
                        # Total Assets And Liabilities Should Be Updated
                        balance_list_new_row = balance_list.shape[0]
                        
                        total_asset += int(loan_commision_amount)

                        balance_list.loc[balance_list_new_row] = [int(balance_list_new_row + 1),
                                                                  int(self.loan_ydate_combo.currentText()),
                                                                  int(self.loan_mdate_combo.currentText()),
                                                                  int(self.loan_ddate_combo.currentText())+1,
                                                                  int(total_asset),
                                                                  0,
                                                                  0,
                                                                  0,
                                                                  0,
                                                                  0,
                                                                  'درصد وام اعطا شده به ' +
                                                                  member_prefix + ' ' +
                                                                  member_name + ' ' +
                                                                  member_lname + ' به مبلغ ' +
                                                                  str(loan_commision_amount)]
                                                        

                        # Checking Whether If The ComboBox Has At Least 1 Item Or It's Empty
                        if (self.member_number_combo.count() != 1):
                            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            # --> The member_number_input ComboBox Has At Least 1 Item
                            # Removing The Deleted Item Of lottery_winner_list From ComboBox
                            self.member_number_combo.removeItem(self.member_number_combo.currentIndex())
                            
                            self.highest_loan_number += 1
                            self.loan_number_input.setText(str(self.highest_loan_number + 1))

                            self.loan_price_input.setText("")
                            self.loan_debt_input.setText("")
                            self.loan_detail_input.setText("")
                            
                            loan_list.reset_index(drop = True, inplace = True)
                            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        else:
                            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            # --> The member_number_input ComboBox Has No Item
                            # Prompting A MessageBox To Inform The Situation
                            dlg = QMessageBox(self)
                            dlg.setWindowTitle("توجه")
                            dlg.setText( "و هيچ عضوي وام تسويه شده ندارد" + "\n" +
                                         "تمامي اعضا وام دريافت کرده اند")
                            dlg.setStandardButtons(QMessageBox.Ok)
                            dlg.setIcon(QMessageBox.Question)
                            button = dlg.exec()
                            self.close()
                            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                else:
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    # --> Loan Price Input Is Empty
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("توجه")
                    dlg.setText("مبلغ وام را وارد کنيد")
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setIcon(QMessageBox.Question)
                    button = dlg.exec()     
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            else:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> Loan Number Has Been Chosen Before
                dlg = QMessageBox(self)
                dlg.setWindowTitle("توجه")
                dlg.setText("وام ديگري با اين شماره ثبت گرديده است\n شماره وام را تغيير دهيد")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Question)
                button = dlg.exec()
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> Loan Number Input Is Empty
            dlg = QMessageBox(self)
            dlg.setWindowTitle("توجه")
            dlg.setText("شماره وام را وارد کنيد")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Question)
            button = dlg.exec()
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def close_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.close()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# New Class For Delete Loan Prompt Window
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class DeleteLoanPrompt(QDialog):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def __init__(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().__init__()

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global loan_list

        # Visual Arrangements Of The Form
        # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
        self.setWindowTitle("حذف وام")
        self.layout = QVBoxLayout()

        # Getting Number Of Loans In The loan_list
        row = loan_list.shape[0]
        # Check If There Is Any Loans In The loan_list
        if row != 0:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
             # --> loan_list Is Not Empty
             
            # Making A ComboBox To Show Existing Loan Numbers            
            self.layout.addWidget(QLabel("شماره وام"))
            self.loan_number_combo = QComboBox()            
            # Adding Loans From loan_list To ComboBox
            loan_index = loan_list.index 
            for i in loan_index:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.loan_number_combo.addItem(str(loan_list["شماره وام"][i]))
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.loan_number_combo.currentTextChanged.connect(self.loan_number_combo_changed)
            self.layout.addWidget(self.loan_number_combo)
            
            # Calculating Data (Loan And Member Numbers And Their Corresponding Indices)
            loan_number = int(self.loan_number_combo.currentText())
            loan_index = loan_list[loan_list["شماره وام"] == loan_number].index[0]
            member_number  = loan_list["شماره عضويت"][loan_index]
            member_index = member_list[member_list["شماره عضويت"] == member_number].index[0]

            # Making A Label To Show Member Data Selected In ComboBox
            self.loan_label = QLabel(" شماره وام انتخاب شده مربوط به : " + "\n" +
                                     "شماره وام" + str(loan_number) + "\n" +
                                     str(member_list["پيشوند"][member_index]) + "\n" +
                                     str(member_list["نام"][member_index]) + " " +
                                     str(member_list["نام خانوادگي"][member_index]) + "\n" +
                                     " به مبلغ " + str(loan_list["مبلغ وام"][loan_index]) + "\n" +
                                     " مي باشد")
            self.layout.addWidget(self.loan_label)

            # Making A PushButton To Delete The Loan When Pressed
            delete_loan_submit_button = QPushButton("حذف وام")
            delete_loan_submit_button.clicked.connect(self.delete_loan_submit_button_clicked)
            self.layout.addWidget(delete_loan_submit_button)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> loan_list Is Empty
            # Making A Label To Say That Loan List Is Empty
            self.layout.addWidget(QLabel("ليست وام ها خاليست"))
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # Making A PushButton To Exit The Form When Pressed
        close_button = QPushButton("خروج")
        close_button.clicked.connect(self.close_button_clicked)
        self.layout.addWidget(close_button)
        
        # Setting The Visual Layout Of The Form
        self.setLayout(self.layout)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def loan_number_combo_changed(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global loan_list

        # Calculating Data (Loan And Member Numbers And Their Corresponding Indices)
        loan_number = int(self.loan_number_combo.currentText())
        loan_index = loan_list[loan_list["شماره وام"] == loan_number].index[0]
        member_number  = loan_list["شماره عضويت"][loan_index]
        member_index = member_list[member_list["شماره عضويت"] == member_number].index[0]
        # Updating The Label To Show Loan Data Selected In ComboBox
        self.loan_label.setText(" شماره وام انتخاب شده مربوط به : " + "\n" +
                                 "شماره عضويت" + str(member_number) + "\n" +
                                 str(member_list["پيشوند"][member_index]) + "\n" +
                                 str(member_list["نام"][member_index]) + " " +
                                 str(member_list["نام خانوادگي"][member_index]) + "\n" +
                                 " به مبلغ " + str(loan_list["مبلغ وام"][loan_index]) + "\n" +
                                 " مي باشد")
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def delete_loan_submit_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global loan_list
        global balance_list
        global total_asset
        global total_liability
        global balance
        global bank_profit
        global account_balance
        global balance_diff

        # Calculating Data (Loan And Member Numbers And Their Corresponding Indices)
        loan_number = int(self.loan_number_combo.currentText())
        loan_index = loan_list[loan_list["شماره وام"] == loan_number].index[0]
        member_number  = loan_list["شماره عضويت"][loan_index]
        member_index = member_list[member_list["شماره عضويت"] == member_number].index[0]

        # Showing A Message To Ask User If He Is Sure
        dlg = QMessageBox(self)
        dlg.setWindowTitle("توجه")
        dlg.setText("آيا از حذف وام به شماره : " + str(loan_list["شماره وام"][loan_index]) +
                    " مربوط به \n" + str(loan_list["نام"][loan_index]) + " " +
                    str(loan_list["نام خانوادگي"][loan_index]) + "\n" + "مطمئن هستيد؟")        
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()               

        if button == QMessageBox.Yes:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> User Admits

            # Total Assets Should Be Subtracted By Deleted Loan's Commision Amount
##            total_asset -= loan_list["مبلغ کارمزد"][loan_index]
##            total_liability -= loan_list["مبلغ وام"][loan_index]
##            balance_list["مجموع پس انداز و درصد"][balance_list_new_row] = total_asset
##            balance_list["مجموع بدهي وام و هزينه ها"][balance_list_new_row] = total_liability
            
            # Delete The Loan of That loan_index                            
            loan_list.drop(loan_index, axis = 0, inplace = True)
            # Reset The Index Numbering To Start From 0 And Ascend Till Last Row
            loan_list.reset_index(drop = True, inplace = True)

            # Toggle The Loan Status Of Corresponding Member To 0 Which Means He Has Not Recieved Loan
            member_list["وضعيت وام"][member_index] = 0
            # Check If There Is At Least One Item In The member_number_combo
            if (self.loan_number_combo.count() != 1):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> The loan_number_input ComboBox Has At Least 1 Item
                # Removing The Deleted Item Of lottery_winner_list From ComboBox
                self.loan_number_combo.removeItem(self.loan_number_combo.currentIndex())
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            else:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> The loan_number_input ComboBox Has No Item
                # Prompting A MessageBox To Inform The Situation
                dlg = QMessageBox(self)
                dlg.setWindowTitle("توجه")
                dlg.setText( "آخرين وام ليست حذف گرديد" + "\n" + "ليست وام ها خاليست")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Question)
                button = dlg.exec()
                self.close()
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def close_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.close()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# New Class For Add Expense Prompt Window
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class AddExpensePrompt(QDialog):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def __init__(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().__init__()
        
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        
        # Visual Arrangements Of The Form
        # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
        self.setWindowTitle("افزودن هزينه")
        self.layout = QVBoxLayout()

        # This Codes Finds The Highest Expense Number To Ease The Input Process
        row = expense_list.shape[0]
        self.highest_expense_number = 5000000
        
        for i in range(0, row):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            if (self.highest_expense_number < int(expense_list.iat[i, 0])):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.highest_expense_number = int(expense_list.iat[i, 0])
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                
        # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
        self.layout.addWidget(QLabel("شماره هزينه"))
        self.expense_number_input = QLineEdit(str(self.highest_expense_number + 1))
        input_validator = QRegExpValidator(number_reg_ex, self.expense_number_input)
        self.expense_number_input.setValidator(input_validator)
        self.layout.addWidget(self.expense_number_input)

        # Making A TextBox To Get The Expense Name
        self.layout.addWidget(QLabel("عنوان هزينه"))
        self.expense_name_input = QLineEdit()
        input_validator = QRegExpValidator(persian_reg_ex, self.expense_name_input)
        self.expense_name_input.setValidator(input_validator)
        self.layout.addWidget(self.expense_name_input)

        # Making A TextBox To Get The Expense Price
        self.layout.addWidget(QLabel("مبلغ هزينه"))
        self.expense_price_input = QLineEdit()
        input_validator = QRegExpValidator(number_reg_ex, self.expense_price_input)
        self.expense_price_input.setValidator(input_validator)
        self.layout.addWidget(self.expense_price_input)
        
        # Making A ComboBox To Show The Year Date Set To Current Year
        self.layout.addWidget(QLabel("تاريخ (سال)"))
        self.expense_ydate_combo = QComboBox()
        now_index = 0
        for i in range(1300, 1501):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.expense_ydate_combo.addItem(str(i))            
            if i < int(current_year):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                now_index += 1
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.expense_ydate_combo.setCurrentIndex(now_index)
        self.layout.addWidget(self.expense_ydate_combo)

        # Making A ComboBox To Show The Month Date Set To Current Month
        self.layout.addWidget(QLabel("تاريخ (ماه)"))
        self.expense_mdate_combo = QComboBox()
        now_index = 0
        for i in range(1, 13):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.expense_mdate_combo.addItem(str(i))            
            if i < int(current_month):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                now_index += 1
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.expense_mdate_combo.setCurrentIndex(now_index)
        self.layout.addWidget(self.expense_mdate_combo)
        
        # Making A ComboBox To Show The Day Date Set To Current Day
        self.layout.addWidget(QLabel("تاريخ (روز)"))
        self.expense_ddate_combo = QComboBox()
        now_index = 0
        for i in range(1, 32):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.expense_ddate_combo.addItem(str(i))            
            if i < int(current_day):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                now_index += 1
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.expense_ddate_combo.setCurrentIndex(now_index)
        self.layout.addWidget(self.expense_ddate_combo)
        

        # Making A TextBox To Get The Expense Details
        self.layout.addWidget(QLabel("توضيحات"))
        self.expense_detail_input = QLineEdit()
        input_validator = QRegExpValidator(persian_reg_ex, self.expense_detail_input)
        self.expense_detail_input.setValidator(input_validator)
        self.layout.addWidget(self.expense_detail_input)

        
        new_expense_submit_button = QPushButton("ثبت هزينه")
        new_expense_submit_button.clicked.connect(self.new_expense_submit_button_clicked)
        self.layout.addWidget(new_expense_submit_button)

        close_button = QPushButton("خروج")
        close_button.clicked.connect(self.close_button_clicked)
        self.layout.addWidget(close_button)        
        self.setLayout(self.layout)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def new_expense_submit_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        global expense_list
        global balance_list
        global total_asset
        global total_liability
        global balance
        global bank_profit
        global account_balance
        global balance_diff
        
        expense_number = int(self.expense_number_input.text())
        
        # This Variable Ensures That The Newly Inserted Member Number Was Not Priviously Existed
        similarity = 0
        
        if (self.expense_number_input.text() != ""):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            row = expense_list.shape[0]
            # Check For Similarity
            for i in range(0, row):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                if (str(expense_list["شماره هزينه"][i]) == self.expense_number_input.text()):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    similarity = 1
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              
            if (similarity == 0):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                if(self.expense_name_input.text() != ""):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    if(self.expense_price_input.text() != ""):
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        dlg = QMessageBox(self)
                        dlg.setWindowTitle("توجه")
                        dlg.setText("آيا از ثبت هزینه به شماره  " +
                                    self.expense_number_input.text() + "\n" +
                                    "  به مبلغ  " +  self.expense_price_input.text()  + "\n" +
                                    "  براي  " +  self.expense_name_input.text() + "\n" +
                                    "  مطمئن هستيد؟  ")
                        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                        dlg.setIcon(QMessageBox.Question)
                        button = dlg.exec()

                        if button == QMessageBox.Yes:
                            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            expense_list.loc[row] = [int(self.expense_number_input.text()),
                                                     str(self.expense_name_input.text()),
                                                     int(self.expense_price_input.text()),
                                                     int(self.expense_ydate_combo.currentText()),
                                                     int(self.expense_mdate_combo.currentText()),
                                                     int(self.expense_ddate_combo.currentText()),
                                                     (int(expense_list["مجموع هزینه"][row - 1]) +
                                                     int(self.expense_price_input.text())),
                                                     str(self.expense_detail_input.text())]

                            # Total Assets And Liabilities Should Be Updated
                            balance_list_new_row = balance_list.shape[0]
                            
                            total_asset = balance_list["مجموع پس انداز و درصد"][balance_list_new_row - 1]
                            total_liability += int(self.expense_price_input.text())
                            balance          = total_asset - total_liability
                            bank_profit      = int(balance_list["سود بانکي"][balance_list_new_row - 1])
                            account_balance  = int(balance_list["موجودي با حساب سود بانکي"]
                                                   [balance_list_new_row - 1])
                            balance_diff     = account_balance - (balance + bank_profit)

                            balance_list.loc[balance_list_new_row] = [int(balance_list_new_row + 1),
                                                    int(self.expense_ydate_combo.currentText()),
                                                    int(self.expense_mdate_combo.currentText()),
                                                    int(self.expense_ddate_combo.currentText()),
                                                    int(total_asset),
                                                    int(total_liability),
                                                    int(balance),
                                                    int(bank_profit),
                                                    int(account_balance),
                                                    int(balance_diff),
                                                    'پرداخت بابت هزينه : ' +
                                                    str(self.expense_name_input.text())]
                            
                            
                            dlg = QMessageBox(self)
                            dlg.setWindowTitle("هزينه جديد")
                            dlg.setText("هزينه جديد ثبت گرديد")
                            dlg.setStandardButtons(QMessageBox.Ok)
                            dlg.setIcon(QMessageBox.Question)
                            button = dlg.exec()
                            
                            self.highest_expense_number += 1
                            self.expense_number_input.setText(str(self.highest_expense_number + 1))
                            self.expense_name_input.setText("")
                            self.expense_price_input.setText("")
                            self.expense_detail_input.setText("")
                            expense_list.reset_index(drop = True, inplace = True)
                            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    else:
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        dlg = QMessageBox(self)
                        dlg.setWindowTitle("توجه")
                        dlg.setText("مبلغ هزینه را وارد کنيد")
                        dlg.setStandardButtons(QMessageBox.Ok)
                        dlg.setIcon(QMessageBox.Question)
                        button = dlg.exec()
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                else:
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("توجه")
                    dlg.setText("عنوان هزینه را وارد کنيد")
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setIcon(QMessageBox.Question)
                    button = dlg.exec()
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            else:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                dlg = QMessageBox(self)
                dlg.setWindowTitle("توجه")
                dlg.setText("هزینه ديگري با اين شماره ثبت گرديده است\n شماره هزینه را تغيير دهيد")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Question)
                button = dlg.exec()
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            dlg = QMessageBox(self)
            dlg.setWindowTitle("توجه")
            dlg.setText("شماره هزینه را وارد کنيد")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Question)
            button = dlg.exec()
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def close_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.close()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# New Class For Delete Expense Prompt Window
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class DeleteExpensePrompt(QDialog):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def __init__(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().__init__()
        
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global expense_list

        # Visual Arrangements Of The Form
        # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
        self.setWindowTitle("حذف هزينه")
        self.layout = QVBoxLayout()
        
        # Getting Number Of Members With Loettery Win Status Of 0
        row = expense_list.shape[0]
        
        # Check If There Is Any Expenses In The expense_list
        if row != 0:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> expense_list Is Not Empty            
            # Making A ComboBox To Show Existing Expense Numbers
            self.layout.addWidget(QLabel("شماره هزينه"))
            self.expense_number_combo = QComboBox()
            
            # Adding Expenses From expense_list To ComboBox
            expense_index = expense_list.index 
            for i in expense_index:
                self.expense_number_combo.addItem(str(expense_list["شماره هزينه"][i]))
            self.expense_number_combo.currentTextChanged.connect(self.expense_number_combo_changed)
            self.layout.addWidget(self.expense_number_combo)

            # Calculating Expense Data Selected In ComboBox
            expense_number = int(self.expense_number_combo.currentText())
            expense_index = expense_list[expense_list["شماره هزينه" ] == expense_number].index[0]
            expense_name  = expense_list["عنوان هزينه"][expense_index]
            expense_price = expense_list["مبلغ کل هزينه"][expense_index]
            
            # Making A Label To Show Expense Data Selected In ComboBox
            self.expense_label = QLabel(" شماره هزينه انتخاب شده مربوط به : " + "\n" +
                                        str(expense_name) + "\n" +
                                        "به مبلغ : " + str(expense_price) + " مي باشد")
            self.layout.addWidget(self.expense_label)

            # Making A PushButton To Delete The current_Item On The ComboBox When Pressed
            delete_expense_submit_button = QPushButton("حذف هزينه")
            delete_expense_submit_button.clicked.connect(self.delete_expense_submit_button_clicked)
            self.layout.addWidget(delete_expense_submit_button)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> expense_list Is Empty
            # Making A Label To Say That Expense List Is Empty
            self.layout.addWidget(QLabel("ليست هزينه ها خاليست"))
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            
        # Making A PushButton To Exit The Form When Pressed     
        close_button = QPushButton("خروج")
        close_button.clicked.connect(self.close_button_clicked)
        self.layout.addWidget(close_button)

        # Setting The Visual Layout Of The Form
        self.setLayout(self.layout)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def expense_number_combo_changed(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global expense_list

        # Calculating Data (Member Numbers And Their Corresponding Indices)
        expense_number = int(self.expense_number_combo.currentText())
        expense_index = expense_list[expense_list["شماره هزينه"] == expense_number].index[0]

        # Calculating Data (Expense Number And Its Corresponding Indices)
        expense_name  = expense_list["عنوان هزينه"][expense_index]
        expense_price = expense_list["مبلغ کل هزينه"][expense_index]

        # Making A Label To Show Expense Data
        self.expense_label.setText("شماره هزينه انتخاب شده مربوط به : " + "\n" +
                                    str(expense_name) + "\n" +
                                    "به مبلغ : " + str(expense_price) + " مي باشد")
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def delete_expense_submit_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global expense_list
        global balance_list
        global total_asset
        global total_liability
        global balance
        global bank_profit
        global account_balance
        global balance_diff

        # Calculating Data (Member Numbers And Their Corresponding Indices)
        expense_number = int(self.expense_number_combo.currentText())
        expense_index = expense_list[expense_list["شماره هزينه" ] == expense_number].index[0]

        # Checking If The expense_list Dataframe Has Any Rows Or It's Empty
        row = expense_list.shape[0]
        if (row != 0):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> The expense_list Is Not Empty
            dlg = QMessageBox(self)
            dlg.setWindowTitle("توجه")
            dlg.setText(" آيا از حذف هزينه به شماره :  " +
                        str(expense_list["شماره هزينه"][expense_index]) +
                        " مربوط به \n" +
                        str(expense_list["عنوان هزينه"][expense_index]) +
                        "  به مبلغ  " +
                        str(expense_list["مبلغ کل هزينه"][expense_index]) +
                        "\n" + "مطمئن هستيد؟")            
            dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dlg.setIcon(QMessageBox.Question)
            button = dlg.exec()
            if button == QMessageBox.Yes:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> User Admitted

                # Total Assets Should Be Subtracted By Deleted Loan's Commision Amount
##                total_liability -= expense_list["مبلغ کل هزينه"][expense_index]
##                balance_list["مجموع بدهي وام و هزينه ها"][balance_list_new_row] = total_liability
                            
                # Delete The Expense Of Index 'winner_index' From lottery_winner_list Dataframe                                   
                expense_list.drop(expense_index, axis = 0, inplace = True)
                # Reset The Index Numbering To Start From 0 And Ascend Till Last Row
                expense_list.reset_index(drop = True, inplace = True)
                # Checking Whether If The ComboBox Has At Least 1 Item Or It's Empty
                if (self.expense_number_combo.count() != 1):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    # --> The member_number_input ComboBox Has At Least 1 Item
                    # Removing The Deleted Item Of lottery_winner_list From ComboBox
                    self.expense_number_combo.removeItem(self.expense_number_combo.currentIndex())
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                else:
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    # --> The member_number_input ComboBox Has No Item
                    # Prompting A MessageBox To Inform The Situation
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("توجه")
                    dlg.setText( "آخرين فرد ليست حذف گرديد" + "\n" + "ليست هزينه ها خاليست")
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setIcon(QMessageBox.Question)
                    button = dlg.exec()
                    self.close()
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> The expense_list Is Empty
            dlg = QMessageBox(self)
            dlg.setWindowTitle("توجه")
            dlg.setText( "آخرين فرد ليست حذف گرديد" + "\n" + "ليست اعضاي برنده خاليست")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Question)
            button = dlg.exec()
            self.close()
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def close_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.close()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# New Class For Calculating Monthly Payments Prompt Window
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class PaymentCalcPrompt(QDialog):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def __init__(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().__init__()
        
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global loan_list
        
        # Visual Arrangements Of The Form
        # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
        self.setWindowTitle("جدول پرداخت ماهيانه")
        self.layout = QVBoxLayout()

        # Getting Number Of Members With Loettery Win Status Of 0
        row_member = member_list.shape[0]
        # If There Is Any Members In The member_list
        if row_member != 0:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> There Is At Least One Member In The member_list
            row_loan = loan_list.shape[0]
            # If There Is Any Loans In The loan_list
            if row_loan != 0:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> There Is At Least One Loan In The loan_list

                # Making A Lable
                insert_date_label = QLabel("سال و ماه مورد نظر را انتخاب نماييد")
                self.layout.addWidget(insert_date_label)

                # Making A Gap
                self.winner_label = QLabel("\n\n")
                self.layout.addWidget(self.winner_label)
                
                # Making A ComboBox To Show The Year Date Set To Current Year
                self.layout.addWidget(QLabel("تاريخ (سال)"))
                self.payment_ydate_combo = QComboBox()
                now_index = 0
                for i in range(1300, 1501):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    self.payment_ydate_combo.addItem(str(i))            
                    if i < int(current_year):
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        now_index += 1
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.payment_ydate_combo.setCurrentIndex(now_index)
                self.layout.addWidget(self.payment_ydate_combo)

                # Making A ComboBox To Show The Month Date Set To Current Month
                self.layout.addWidget(QLabel("تاريخ (ماه)"))
                self.payment_mdate_combo = QComboBox()
                now_index = 0
                for i in range(1, 13):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    self.payment_mdate_combo.addItem(str(i))            
                    if i < int(current_month):
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        now_index += 1
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.payment_mdate_combo.setCurrentIndex(now_index)
                self.layout.addWidget(self.payment_mdate_combo)

                # Making A Textbox To Get The Loan Price
                self.layout.addWidget(QLabel("سود بانکي"))
                self.bank_profit_input = QLineEdit()
                input_validator = QRegExpValidator(number_reg_ex, self.bank_profit_input)
                self.bank_profit_input.setValidator(input_validator)
                self.layout.addWidget(self.bank_profit_input)

                # Making A Textbox To Get The Loan Price
                self.layout.addWidget(QLabel("موجودي کل حساب بانکي"))
                self.account_balance_input = QLineEdit()
                input_validator = QRegExpValidator(number_reg_ex, self.account_balance_input)
                self.account_balance_input.setValidator(input_validator)
                self.layout.addWidget(self.account_balance_input)
                
                # Making A PushButton To Calculate The Payment Table When Pressed
                payment_table_load_button = QPushButton("محاسبه جدول پرداخت")
                payment_table_load_button.clicked.connect(self.payment_table_load_button_clicked)
                self.layout.addWidget(payment_table_load_button)
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            else:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> There Is No Loan In The loan_list
                # Making A Label To Say That There Is No Loan In The loan_list
                self.layout.addWidget(QLabel("براي هيچکدام از اعضا وامي ثبت نشده است"))
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> There Is No Member In The member_list
            # Making A Label To Say That There Is No Member In The member_list
            self.layout.addWidget(QLabel("هيچ عضوي در ليست اعضا وجود ندارد"))
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # Making A PushButton To Exit The Form When Pressed     
        close_button = QPushButton("خروج")
        close_button.clicked.connect(self.close_button_clicked)
        self.layout.addWidget(close_button)

        # Setting The Visual Layout Of The Form
        self.setLayout(self.layout)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def payment_table_load_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global loan_list
        global payment_list
        global balance_list
        global expense_list
        global total_asset
        global total_liability
        global balance
        global bank_profit
        global account_balance
        global balance_diff
        global temp_year
        global temp_month
        
        temp_year = int(self.payment_ydate_combo.currentText())
        temp_month = int(self.payment_mdate_combo.currentText())
        monthly_asset = 0
        monthly_liability = 0
        total_expense = expense_list.iloc[-1]['مجموع هزینه']
        
        # Try Loading Privious Payment Lists And If It Results In Error
        # (File Does Not Exist) Make A New One
        try:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> The Needed File Is Available
            # Load Privious Files In The Path
            # Ceating A FilePath To Load Data From Privious .xlsx Files
            filepath_xlsx = ('Payment\Payment_' +
                        str(self.payment_ydate_combo.currentText()) + '_' +
                        str(self.payment_mdate_combo.currentText()) + '_' + '.xlsx')
            # Load .xlsx File
            payment_list = pd.read_excel(filepath_xlsx)
            # Change All NaN Cells With ""
            payment_list = payment_list.fillna("")
            # Drop The Index Column
            payment_list.drop(payment_list.keys()[0], axis = 1, inplace=True)
            # Reset The Indices
            payment_list.reset_index(drop = True, inplace = True)
            self.close()
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        except:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> No File Exists With That Name
            # Make A New File In The Path
            if (self.bank_profit_input.text() != '' and
                self.account_balance_input.text() != ''):
                # --> The bank_profit And account_balance Fields Are Not Empty

                                                       
                bank_profit = int(self.bank_profit_input.text())
                account_balance = int(self.account_balance_input.text())
                
                # Calculate Payments For Every Member One By One

                for i in member_list.index:
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    member_index = i
                    member_number = member_list["شماره عضويت"][member_index]
                    if member_list["وضعيت وام"][i] == 1:
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        # --> The Selected Member Has A Loan Assigned To Him/Her
                        # Find The Index Of The Loan Assigned To This Member
                        loan_index = loan_list[loan_list["شماره عضويت"] == member_number].index[0]
                        # Calculate The Month Difference Of Loan Recive Date And Now Date
                        month_difference = ((int(self.payment_ydate_combo.currentText()) -
                                            int(loan_list["تاريخ (سال)"][loan_index])) * 12 +
                                           (int(self.payment_mdate_combo.currentText()) -
                                            int(loan_list["تاريخ (ماه)"][loan_index])))
                        # Payment Of Deposite
                        deposit_pay = int(member_list["پس انداز ماهيانه"][member_index])

                        # Check If The Debt Of Member Is Less Than Two Time Installment
                        if (int(loan_list["مانده بدهي"][loan_index]) <
                            2 * int(loan_list["مبلغ اقساط"][loan_index])):
                            # Payment Of Loan
                            loan_pay = int(loan_list["مانده بدهي"][loan_index])
                        else:
                            # Payment Of Loan
                            loan_pay = (int(loan_list["مبلغ اقساط"][loan_index]) *
                                        int(member_list["سرعت بازپرداخت"][member_index]))
                                     
                        # Calculate The Total Payment Of The Member (Who Has Loan)                                  
                        total_pay = deposit_pay + loan_pay
                        
                        # Calculate The Debt Left
                        debt_left = int(loan_list["مانده بدهي"][loan_index]) - loan_pay
                        
                        # Calculate The Installment Left
                        installment_left = (int(loan_list["اقساط باقي مانده"][loan_index]) -
                                            int(member_list["سرعت بازپرداخت"][member_index]))
                        
                            
                        # Updating The Total Deposit After Doing Calculations Of Current Month
                        member_list["مبلغ پس انداز"][member_index] += deposit_pay

                        # Updating The Debt And Installment Left After Doing Calculations Of Current Month
                        loan_list["مانده بدهي"][loan_index] = int(debt_left)
                        loan_list["اقساط باقي مانده"][loan_index] = int(installment_left)

                        # Updating The Total Assets And Total Liabilities Doing Calculations Of Current Month
                        monthly_asset += deposit_pay
                        monthly_liability += debt_left
                        
                        # Add A New Row To payment_list With The Newly Calculated Data
                        payment_list.loc[i] = [int(member_list["شماره عضويت"][member_index]),
                                               str(member_list["نام خانوادگي"][member_index]),
                                               str(member_list["نام"][member_index]),
                                               int(loan_list["شماره وام"][loan_index]),
                                               int(loan_list["تاريخ (سال)"][loan_index]),
                                               int(loan_list["تاريخ (ماه)"][loan_index]),
                                               int(loan_list["مبلغ وام"][loan_index]),
                                               int(member_list["پس انداز ماهيانه"][member_index]),
                                               int(loan_list["مبلغ اقساط"][loan_index]),
                                               int(total_pay),
                                               int(loan_list["مانده بدهي"][loan_index]),
                                               int(loan_list["اقساط باقي مانده"][loan_index]),
                                               int(member_list["مبلغ پس انداز"][member_index]),
                                               int(member_list["وضعيت قرعه کشي"][member_index]),
                                               int(member_list["سرعت بازپرداخت"][member_index])]


                        # If The Debt Is Zero, Clear The Loan Status Of Corresponding Member
                        if (debt_left == 0):
                            member_list["وضعيت وام"][member_index] = 0
                            member_list["سرعت بازپرداخت"][member_index] = 1
                            loan_list.drop(loan_index, axis = 0, inplace = True)
                            loan_list.reset_index(drop = True, inplace = True)
                        
                        
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    else:
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        # --> There Is No Loan Assigned To This Member

                        # Payment Of Deposite
                        deposit_pay = int(member_list["پس انداز ماهيانه"][member_index])
                        
                        # Calculate Total Payment Of The Member (Who Doesn't Have Loan)
                        total_pay = deposit_pay
                        
                        # Updating The Total Assets And Total Liabilities Doing Calculations Of Current Month
                        monthly_asset += deposit_pay
                        
                        # Add A New Row To payment_list With The Newly Calculated Data
                        payment_list.loc[i] = [int(member_list["شماره عضويت"][member_index]),
                                               str(member_list["نام خانوادگي"][member_index]),
                                               str(member_list["نام"][member_index]),
                                               0,
                                               int(loan_list["تاريخ (سال)"][loan_index]),
                                               int(loan_list["تاريخ (ماه)"][loan_index]),
                                               0,
                                               int(member_list["پس انداز ماهيانه"][member_index]),
                                               0,
                                               int(total_pay),
                                               0,
                                               0,
                                               int(member_list["مبلغ پس انداز"][member_index]),
                                               int(member_list["وضعيت قرعه کشي"][member_index]),
                                               int(member_list["سرعت بازپرداخت"][member_index])]
                        # Updating The Total Deposit After Doing Calculations Of Current Month
                        member_list["مبلغ پس انداز"][member_index] += deposit_pay
                        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

                # Get The Last Row Of Balance List
                balance_list_new_row = balance_list.shape[0]
                
                # Total Assets And Liabilities Should Be Updated
                total_asset     += monthly_asset
                total_liability  = monthly_liability + total_expense
                
                balance          = total_asset - total_liability
                balance_diff     = account_balance - (balance + bank_profit)

                balance_list.loc[balance_list_new_row] = [int(balance_list_new_row + 1),
                                                          int(current_year),
                                                          int(current_month),
                                                          int(1),
                                                          int(total_asset),
                                                          int(total_liability),
                                                          int(balance),
                                                          int(bank_profit),
                                                          int(account_balance),
                                                          int(balance_diff),
                                                          'محاسبات پرداختهاي ماهيانه' + ' ' +
                                                          ' مجموع پس اندازهاي اين ماه ' +
                                                          str(monthly_asset) +
                                                          ' \nمجموع بدهي هاي اعضا در اين ماه ' +
                                                          str(monthly_liability) +
                                                          ' \nمجموع هزينه تا به اين ماه ' +
                                                          str(total_expense)]

                # Check To See Wether If The Payment Folder Exists Or If Not, Create One
                try:
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    # Creating A File Path For Saving payment_list In Payment Folder
                    os.mkdir('Payment')
                    filepath_xlsx = ('Payment\Payment_' +
                                str(self.payment_ydate_combo.currentText()) + '_' +
                                str(self.payment_mdate_combo.currentText()) + '_' + '.xlsx')
                    filepath_csv = ('Payment\Payment_' +
                                str(self.payment_ydate_combo.currentText()) + '_' +
                                str(self.payment_mdate_combo.currentText()) + '_' + '.csv')
                    # Saving payment_list To .xlsx And .csv Files
                    payment_list.to_excel(filepath_xlsx)            
                    payment_list.to_csv(filepath_csv)
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                except FileExistsError:
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    filepath_xlsx = ('Payment\Payment_' +
                                str(self.payment_ydate_combo.currentText()) + '_' +
                                str(self.payment_mdate_combo.currentText()) + '_' + '.xlsx')
                    filepath_csv = ('Payment\Payment_' +
                                str(self.payment_ydate_combo.currentText()) + '_' +
                                str(self.payment_mdate_combo.currentText()) + '_' + '.csv')
                    # Saving payment_list To .xlsx And .csv Files
                    payment_list.to_excel(filepath_xlsx)            
                    payment_list.to_csv(filepath_csv)
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

                
            else:
                # --> The bank_profit And account_balance Fields Are Empty
                dlg = QMessageBox(self)
                dlg.setWindowTitle("توجه")
                dlg.setText( "مقادير سود بانکي و موجودي کل بانک را وارد نماييد")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Question)
                button = dlg.exec()

            
                
            
            self.close()
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def close_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.close()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# New Class For Random Winner Pick Prompt Window
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class RandomPickPrompt(QDialog):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def __init__(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().__init__()
        
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global lottery_winner_list
        
        # Visual Arrangements Of The Form
        # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
        self.setWindowTitle("انتخاب تصادفي اعضا")        
        self.layout = QVBoxLayout()

        # Getting Number Of Members With Loettery Win Status Of 0
        row = member_list[member_list["وضعيت قرعه کشي"] == 0].shape[0]
        # If There Is Any Members Who Hasn't Won Ever
        if row != 0:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> There Is At Least One Member Who Hasn't Won
            
            # Making A PushButton To Random Select The Winner Among Winners
            random_pick_button = QPushButton("انتخاب تصادفي اعضا")
            random_pick_button.clicked.connect(self.random_pick_button_clicked)
            self.layout.addWidget(random_pick_button)
            
            # Making A Gap Below The Label
            self.winner_label = QLabel("\n\n\n")
            self.layout.addWidget(self.winner_label)
            
            # Making A ComboBox To Show The Year Date Set To Current Year
            self.layout.addWidget(QLabel("تاريخ (سال)"))
            self.lottery_ydate_combo = QComboBox()
            now_index = 0
            for i in range(1300, 1501):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.lottery_ydate_combo.addItem(str(i))            
                if i < int(current_year):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    now_index += 1
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.lottery_ydate_combo.setCurrentIndex(now_index)
            self.layout.addWidget(self.lottery_ydate_combo)

            # Making A ComboBox To Show The Month Date Set To Current Month
            self.layout.addWidget(QLabel("تاريخ (ماه)"))
            self.lottery_mdate_combo = QComboBox()
            now_index = 0
            for i in range(1, 13):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.lottery_mdate_combo.addItem(str(i))            
                if i < int(current_month):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    now_index += 1
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.lottery_mdate_combo.setCurrentIndex(now_index)
            self.layout.addWidget(self.lottery_mdate_combo)
            
            # Making A ComboBox To Show The Day Date Set To Current Day
            self.layout.addWidget(QLabel("تاريخ (روز)"))
            self.lottery_ddate_combo = QComboBox()
            now_index = 0
            for i in range(1, 32):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.lottery_ddate_combo.addItem(str(i))            
                if i < int(current_day):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    now_index += 1
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.lottery_ddate_combo.setCurrentIndex(now_index)
            self.layout.addWidget(self.lottery_ddate_combo)

            # Making A TextBox To Get The Winner Prize Name
            self.layout.addWidget(QLabel("جايزه ي برنده : "))
            self.prize_input = QLineEdit()
            input_validator = QRegExpValidator(persian_reg_ex, self.prize_input)
            self.prize_input.setValidator(input_validator)
            self.layout.addWidget(self.prize_input)
            
            # Making A PushButton To Submit The Winner Data When Pressed
            new_winner_submit_button = QPushButton("ثبت برنده جديد")
            new_winner_submit_button.clicked.connect(self.new_winner_submit_button_clicked)
            self.layout.addWidget(new_winner_submit_button)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # Making A Label To Say That Everyone's Lottery Win Status Is 1
            self.layout.addWidget(QLabel("تمام اعضا يک بار برنده شده اند" + "\n" +
                                         "براي شروع دوباره قرعه کشي" + "\n" +
                                         " ليست را به طور کامل پاک نماييد"))
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            
        # Making A PushButton To Exit The Form When Pressed    
        close_button = QPushButton("خروج")
        close_button.clicked.connect(self.close_button_clicked)
        self.layout.addWidget(close_button)

        # Setting The Visual Layout Of The Form
        self.setLayout(self.layout)

        # This Is A Flag To Show That If Random Winner Selected Or Not
        self.winner_selected = 0
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def random_pick_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global lottwry_win_list

        # Pick Out The Members Who Has The 0 Value For Lottery Win Status
        lottery_leftover = member_list[member_list["وضعيت قرعه کشي"] == 0]
        self.row = lottery_leftover.shape[0]
        # Check If There Is At Least One Member That Hasn't Won Yet
        if (self.row != 0):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> There Is A Member That Hasn't Won
            # Get The Index Of A Random Member From Leftover List
            self.winner_index = lottery_leftover.sample().index[0]
            # Update The winner_label Text With Newly Picked Winner
            self.winner_label.setText(" عضو انتخاب شده به صورت تصادفي  " + "\n" +
                               member_list.at[self.winner_index, "پيشوند"] + "\n" +
                               member_list.at[self.winner_index, "نام"] + " " +
                               member_list.at[self.winner_index, "نام خانوادگي"] + "\n" +
                               "مي باشد.")
            # Toggle The Flag To Demonstrate That A Winner Has Been Chosen
            self.winner_selected = 1
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> Everyone Has Won
            dlg = QMessageBox(self)
            dlg.setWindowTitle("توجه")
            dlg.setText("تمام اعضا يک بار برنده شدند")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Question)
            button = dlg.exec()
            self.close()
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def new_winner_submit_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global lottery_winner_list
        # Checking Whether If A Winner Has Been Chosen Or Not
        if (self.winner_selected == 1):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> There Is A Winner
            # Checking Whether If The Prize TextBox Is Empty Or Not
            if (self.prize_input.text() != ""):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> Prize TextBox Is Not Empty
                if (self.row != 0):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  
                    # --> There Is At Least a Member That Hasn't Won            
                    new_row_index = lottery_winner_list.shape[0]
                    # Add A New Row To lottery_winner_list With The Newly Won Member Data
                    lottery_winner_list.loc[new_row_index] = [member_list["شماره عضويت"][self.winner_index],
                                                              member_list["نام خانوادگي"][self.winner_index],
                                                              member_list["نام"][self.winner_index],
                                                              int(self.lottery_ydate_combo.currentText()),
                                                              int(self.lottery_mdate_combo.currentText()),
                                                              int(self.lottery_ddate_combo.currentText()),
                                                              str(self.prize_input.text())]
                    # Setting The Lottery Win Status Of The Deleted Member To 0 (Meaning Has Not Winned Yet)    
                    member_list["وضعيت قرعه کشي"][self.winner_index] = 1
                    # Clear The Prize TextBox
                    self.prize_input.setText("")            
                    # Reset The Index Numbering To Start From 0 And Ascend Till Last Row            
                    lottery_winner_list.reset_index(drop = True, inplace = True)
                    # Reset The Index Numbering To Start From 0 And Ascend Till Last Row
                    member_list.reset_index(drop = True, inplace = True)
                    # Clear The Winner Label
                    self.winner_label.setText("\n\n\n")
                    # Clear The Random Pick Flag
                    self.winner_selected = 0
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                else:
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    # --> No Member Left And Everyone Has Won Once   
                    # Prompting A MessageBox To Inform The Situation
                    dlg = QMessageBox(self)
                    dlg.setWindowTitle("توجه")
                    dlg.setText("تمام اعضا يک بار برنده شدند")
                    dlg.setStandardButtons(QMessageBox.Ok)
                    dlg.setIcon(QMessageBox.Question)
                    button = dlg.exec()
                    self.close()
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            else:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> Prize TextBox Is Empty
                # Prompting A MessageBox To Inform The Situation
                dlg = QMessageBox(self)
                dlg.setWindowTitle("توجه")
                dlg.setText("جايزه برنده را وارد نماييد")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Question)
                button = dlg.exec()
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> Winner Not Selected
            # Prompting A MessageBox To Inform The Situation
            dlg = QMessageBox(self)
            dlg.setWindowTitle("توجه")
            dlg.setText("ابتدا با زدن دکمه انتخاب تصادفي اعضا" + "\n" +
                        "عضوي را انتخاب نماييد")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Question)
            button = dlg.exec()
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def close_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.close()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# New Class For Manual Winner Pick Prompt Window
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class ManualPickPrompt(QDialog):
    ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def __init__(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().__init__()
        
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list

        # Visual Arrangements Of The Form
        # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
        self.setWindowTitle("افزودن برنده قرعه کشي")
        self.layout = QVBoxLayout()        
        
        # Getting Number Of Members With Loettery Win Status Of 0
        row = member_list[member_list["وضعيت قرعه کشي"] == 0].shape[0]
        # If There Is Any Members Who Hasn't Won Ever
        if row != 0:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> There Is At Least One Member Who Hasn't Won
            
            # Making A ComboBox To Show Existing Member Numbers
            self.layout.addWidget(QLabel("شماره عضويت"))
            self.member_number_combo = QComboBox()
            
            # Getting The Index Of Members In The member_list Who Hasn't Won Yet
            no_win_index = member_list[member_list["وضعيت قرعه کشي"] == 0].index
            # Adding Those Members From member_list To ComboBox
            for i in no_win_index:
                self.member_number_combo.addItem(str(member_list["شماره عضويت"][i]))
            self.member_number_combo.currentTextChanged.connect(self.member_number_combo_changed)
            self.layout.addWidget(self.member_number_combo)

            ## Calculating Data (Member Numbers And Their Corresponding Indices)
            member_number = int(self.member_number_combo.currentText())
            member_index = member_list[member_list["شماره عضويت" ] == member_number].index[0]        
            member_prefix = member_list["پيشوند"][member_index]
            member_name  = member_list["نام"][member_index]
            member_lname = member_list["نام خانوادگي"][member_index]

            
            # Making A Label To Show The Member's Data (Prefix, Name and Last Name) When 
            # Item_Changed Event Of ComboBox Happens        
            self.layout.addWidget(QLabel(" نام عضو  :"))

            self.member_name_label = QLabel(member_prefix + "\n" + member_name + "\n" + member_lname)        
            self.layout.addWidget(self.member_name_label)

            # Making A ComboBox To Show The Year Date Set To Current Year
            self.layout.addWidget(QLabel("تاريخ (سال)"))
            self.lottery_ydate_combo = QComboBox()
            now_index = 0
            for i in range(1300, 1501):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.lottery_ydate_combo.addItem(str(i))            
                if i < int(current_year):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    now_index += 1
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.lottery_ydate_combo.setCurrentIndex(now_index)
            self.layout.addWidget(self.lottery_ydate_combo)

            # Making A ComboBox To Show The Month Date Set To Current Month
            self.layout.addWidget(QLabel("تاريخ (ماه)"))
            self.lottery_mdate_combo = QComboBox()
            now_index = 0
            for i in range(1, 13):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.lottery_mdate_combo.addItem(str(i))            
                if i < int(current_month):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    now_index += 1
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.lottery_mdate_combo.setCurrentIndex(now_index)
            self.layout.addWidget(self.lottery_mdate_combo)
            
            # Making A ComboBox To Show The Day Date Set To Current Day
            self.layout.addWidget(QLabel("تاريخ (روز)"))
            self.lottery_ddate_combo = QComboBox()
            now_index = 0
            for i in range(1, 32):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                self.lottery_ddate_combo.addItem(str(i))            
                if i < int(current_day):
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    now_index += 1
                    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.lottery_ddate_combo.setCurrentIndex(now_index)
            self.layout.addWidget(self.lottery_ddate_combo)
            
            # Making A TextBox To Get The Winner Prize Name
            self.layout.addWidget(QLabel("جايزه ي برنده"))
            self.prize_input = QLineEdit()
            input_validator = QRegExpValidator(persian_reg_ex, self.prize_input)
            self.prize_input.setValidator(input_validator)
            self.layout.addWidget(self.prize_input)
            
            # Making A PushButton To Submit The Winner Data When Pressed
            winner_submit_button = QPushButton("ثبت برنده جديد")
            winner_submit_button.clicked.connect(self.winner_submit_button_clicked)
            self.layout.addWidget(winner_submit_button)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> Every Member Has Won Once
            # Making A Label To Say That Everyone's Lottery Win Status Is 1
            self.layout.addWidget(QLabel("تمام اعضا يک بار برنده شده اند" + "\n" +
                                         "براي شروع دوباره قرعه کشي" + "\n" +
                                         " ليست را به طور کامل پاک نماييد"))
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            
        # Making A PushButton To Exit The Form When Pressed
        close_button = QPushButton("خروج")
        close_button.clicked.connect(self.close_button_clicked)
        self.layout.addWidget(close_button)
        
        # Setting The Visual Layout Of The Form
        self.setLayout(self.layout)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    def member_number_combo_changed(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list

        # Calculating Data (Member Numbers And Their Corresponding Indices)
        member_number = int(self.member_number_combo.currentText())
        member_index = member_list[member_list["شماره عضويت" ] == member_number].index[0]

        # Updating The Member Data Label According To New Item Of ComboBox
        member_prefix = member_list["پيشوند"][member_index]
        member_name  = member_list["نام"][member_index]
        member_lname = member_list["نام خانوادگي"][member_index]
        self.member_name_label.setText(member_prefix + "\n" + member_name + "\n" + member_lname)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
    def winner_submit_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global lottery_winner_list

        # Calculating Data (Member Numbers And Their Corresponding Indices)
        member_number = int(self.member_number_combo.currentText())
        member_index = member_list[member_list["شماره عضويت" ] == member_number].index[0]            
        
        
        # Checking Whether If The Prize TextBox Is Empty Or Not
        if (self.prize_input.text() != ""):
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> Prize TextBox Is Not Empty
            new_row_index = lottery_winner_list.shape[0]
            # Add A New Row To lottery_winner_list With The Newly Won Member Data
            lottery_winner_list.loc[new_row_index] = [member_list["شماره عضويت"][member_index],
                                                      member_list["نام خانوادگي"][member_index],
                                                      member_list["نام"][member_index],
                                                      int(self.lottery_ydate_combo.currentText()),
                                                      int(self.lottery_mdate_combo.currentText()),
                                                      int(self.lottery_ddate_combo.currentText()),
                                                      str(self.prize_input.text())]
            # Setting The Lottery Win Status Of The Deleted Member To 0 (Meaning Has Not Winned Yet)    
            member_list["وضعيت قرعه کشي"][member_index] = 1
            # Clear The Prize TextBox
            self.prize_input.setText("")            
            # Reset The Index Numbering To Start From 0 And Ascend Till Last Row            
            lottery_winner_list.reset_index(drop = True, inplace = True)
            # Reset The Index Numbering To Start From 0 And Ascend Till Last Row
            member_list.reset_index(drop = True, inplace = True)
            # Check If There Is At Least One Item In The member_number_combo
            if (self.member_number_combo.count() != 1):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> member_number_combo Has More Than One Row
                self.member_number_combo.removeItem(self.member_number_combo.currentIndex())
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            else:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> No Rows In member_number_combo
                # Prompting A MessageBox To Inform The Situation
                dlg = QMessageBox(self)
                dlg.setWindowTitle("توجه")
                dlg.setText("تمام اعضا يک بار برنده شدند")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Question)
                button = dlg.exec()
                self.close()
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> Prize TextBox Is Empty
            # Prompting A MessageBox To Inform The Situation
            dlg = QMessageBox(self)
            dlg.setWindowTitle("توجه")
            dlg.setText("جايزه برنده را وارد نماييد")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Question)
            button = dlg.exec()
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def close_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.close()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        

#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# New Class For Delete Winner Prompt Window
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class DeleteWinnerPrompt(QDialog):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def __init__(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        super().__init__()

        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global lottery_winner_list

        # Visual Arrangements Of The Form
        # Adding Widgets With "self." Makes You Able To Use Them In Other "def"s Of Same Class
        self.setWindowTitle("حذف برنده از ليست")
        self.layout = QVBoxLayout()
        
        # Checking If The lottery_winner_list Dataframe Has Any Rows Or It's Empty
        row = lottery_winner_list.shape[0]        
        if row != 0:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> The lottery_winner_list Dataframe Has At Least 1 Row Of Data

            # ComboBox Widget To Show Existing Member Numbers 
            self.layout.addWidget(QLabel("شماره عضويت"))
            self.member_number_combo = QComboBox()           
            # Filling ComboBox Items With The Member Number Data In The lottery_winner_list Dataframe
            # And Using It's Item_Changed Event To Refresh The Member Data On The Member Data Label Below
            lottery_winner_index = lottery_winner_list.index
            for i in lottery_winner_index:
                    self.member_number_combo.addItem(str(lottery_winner_list["شماره عضويت"].astype(int)[i]))            
            self.member_number_combo.currentTextChanged.connect(self.member_number_combo_changed)
            self.layout.addWidget(self.member_number_combo)
            
            
            # Making A Label To Show The Member's Data (Prefix, Name and Last Name) When 
            # Item_Changed Event Of ComboBox Happens
            self.layout.addWidget(QLabel(" نام عضو  :"))
            member_number = int(self.member_number_combo.currentText())
            member_index = member_list[member_list["شماره عضويت" ] == member_number].index[0]
            member_prefix = member_list["پيشوند"][member_index]
            member_name  = member_list["نام"][member_index]
            member_lname = member_list["نام خانوادگي"][member_index]
            self.member_name_label = QLabel(member_prefix + "\n" + member_name + "\n" + member_lname)
            self.layout.addWidget(self.member_name_label)
            
            # Making A PushButton To Delete The current_Item On The ComboBox When Pressed
            delete_member_submit_button = QPushButton("حذف عضو")
            delete_member_submit_button.clicked.connect(self.delete_member_submit_button_clicked)
            self.layout.addWidget(delete_member_submit_button)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        else:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> The lottery_winner_list Dataframe Is Empty Meaning Everyone Has Won
            # Making A Label To Say That lottery_winner_list Is Empty
            self.layout.addWidget(QLabel(" ليست برندگاه قرعه کشي خاليست"))
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        # Making A PushButton To Exit The Form When Pressed        
        close_button = QPushButton("خروج")
        close_button.clicked.connect(self.close_button_clicked)
        self.layout.addWidget(close_button)
        
        # Setting The Visual Layout Of The Form
        self.setLayout(self.layout)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
    def member_number_combo_changed(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        
        # Calculating Data (Member Numbers And Their Corresponding Indices)
        member_number = int(self.member_number_combo.currentText())
        member_index = member_list.loc[member_list["شماره عضويت" ] == member_number].index[0]

        # Updating The Member Data Label According To New Item Of ComboBox
        member_prefix = member_list["پيشوند"][member_index]
        member_name  = member_list["نام"][member_index]
        member_lname = member_list["نام خانوادگي"][member_index]
        self.member_name_label.setText(member_prefix + "\n" + member_name + "\n" + member_lname)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def delete_member_submit_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # ReDeclare Variables That Have To Be Changed As Global Variable
        global member_list
        global lottery_winner_list

        # Calculating Data (Member Numbers And Their Corresponding Indices)
        member_number = int(self.member_number_combo.currentText())
        member_index = member_list.loc[member_list["شماره عضويت" ] == member_number].index[0]
        winner_index = lottery_winner_list.loc[lottery_winner_list["شماره عضويت" ] == member_number].index[0]

        # Prompting A Message Box To Make Sure The User Is Confident
        dlg = QMessageBox(self)
        dlg.setWindowTitle("توجه")
        dlg.setText("آيا از حذف عضو به شماره : " + str(member_list["شماره عضويت"][member_index]) +
                    " مربوط به \n" + str(member_list["نام"][member_index]) + " " +
                    str(member_list["نام خانوادگي"][member_index]) + "\n" + "مطمئن هستيد؟")            
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        # Checking If User Admitted
        if button == QMessageBox.Yes:
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            # --> User Admitted
            
            # Setting The Lottery Win Status Of The Deleted Member To 0 (Meaning Has Not Winned Yet)
            member_list.at[member_index, "وضعيت قرعه کشي"] = 0                
            # Delete The Winner Of Index 'winner_index' From lottery_winner_list Dataframe
            lottery_winner_list.drop(winner_index, axis = 0, inplace = True)
            # Reset The Index Numbering To Start From 0 And Ascend Till Last Row
            lottery_winner_list.reset_index(drop = True, inplace = True)
                
            # Checking Whether If The ComboBox Has At Least 1 Item Or It's Empty
            if (self.member_number_combo.count() != 1):
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> The member_number_input ComboBox Has At Least 1 Item
                # Removing The Deleted Item Of lottery_winner_list From ComboBox
                self.member_number_combo.removeItem(self.member_number_combo.currentIndex())
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            else:
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                # --> The member_number_input ComboBox Has No Item
                # Prompting A MessageBox To Inform The Situation
                dlg = QMessageBox(self)
                dlg.setWindowTitle("توجه")
                dlg.setText( "آخرين فرد ليست حذف گرديد" + "\n" + "ليست اعضاي برنده خاليست")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Question)
                button = dlg.exec()
                self.close()
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def close_button_clicked(self):
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.close()
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


        
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
# Main Window
if __name__ == "__main__":

    # creating the pyqt5 application  
    base = QApplication(sys.argv)  
    
    # creating an instance of the Window  
    window = MainWindow()
    window.show()
    # starting the application  
    sys.exit(base.exec())  
