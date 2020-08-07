from tkinter import *
from tkinter import ttk
from tkcalendar import *
import datetime
import shutil
import re
import mysql.connector
import smtplib
from email.mime.text import MIMEText


global window
window = Tk()
window.title("Worldscape Timesheet Login")
window.configure(background="white")

#connecting to the database
w_t_db = mysql.connector.connect(
    host="sql3.freemysqlhosting.net",
    user="sql3354636",
    passwd="amIxjTZ3iV",
    db="sql3354636"
)

global cursor
cursor = w_t_db.cursor()

global bufferedcursor
bufferedcursor = w_t_db.cursor(buffered=True)

def get_widgets(window):
    widget_list = window.winfo_children()

    for widget in widget_list:
        if widget.winfo_children():
            widget_list.extend(widget.winfo_children())

    return widget_list

def clear_screen():
    all_widget_list = get_widgets(window)
    for widget in all_widget_list:
        widget.destroy()

def force_close_session():
    window.destroy()

def logout():
    clear_screen()

    global logo
    logo = PhotoImage(file="worldscapeinc.png")
    logolabel = Label (window, image=logo, bg="white", justify="left") .pack()

    global title
    title = Label (window, text="Worldscape Timesheet", bg="white", fg="black", font="none 20 bold")
    title.pack()

    global loginbutton
    loginbutton = Button(text="Login", width=20, command=login)
    loginbutton.pack(pady=10)

    global manger_loginbutton
    manager_loginbutton = Button(text = "Manager Login", width=20, command=manager_login)
    manager_loginbutton.pack(pady=10)

    global admin_loginbutton
    admin_loginbutton = Button(text = "Administrator Login", width=20, command=admin_login)
    admin_loginbutton.pack(pady=10)

    global newuserbutton
    newuserbutton = Button(window, text="New User?", width=20, command=newuser)
    newuserbutton.pack(pady=10)


def close_queuedtimesheetdata():
    queued_timesheetselectedlabel.config(text = " ")
    queued_hourtypeselectedlabel.config(text = " ")
    queued_hoursinfo1label.config(text = " ")
    queued_hoursinfo2label.config(text = " ")
    queued_hoursinfo3label.config(text = " ")
    queued_hoursinfo4label.config(text = " ")
    queued_hoursinfo5label.config(text = " ")
    queued_hoursinfo6label.config(text = " ")
    queued_hoursinfo7label.config(text = " ")
    queued_hoursnoteslabel.config( text = " ")
    close_data.destroy()

def close_approvedtimesheetdata():
    approved_timesheetselectedlabel.config(text = " ")
    approved_hourtypeselectedlabel.config(text = " ")
    approved_hoursinfo1label.config(text = " ")
    approved_hoursinfo2label.config(text = " ")
    approved_hoursinfo3label.config(text = " ")
    approved_hoursinfo4label.config(text = " ")
    approved_hoursinfo5label.config(text = " ")
    approved_hoursinfo6label.config(text = " ")
    approved_hoursinfo7label.config(text = " ")
    approved_hoursnoteslabel.config(text = " ")
    approval_dateinfolabel.config(text = " ")
    close_data1.destroy()

def close_rejectedtimesheetdata():
    rejected_timesheetselectedlabel.config(text = " ")
    rejected_hourtypeselectedlabel.config(text = " ")
    rejected_hoursinfo1label.config(text = " ")
    rejected_hoursinfo2label.config(text = " ")
    rejected_hoursinfo3label.config(text = " ")
    rejected_hoursinfo4label.config(text = " ")
    rejected_hoursinfo5label.config(text = " ")
    rejected_hoursinfo6label.config(text = " ")
    rejected_hoursinfo7label.config(text = " ")
    rejected_hoursnoteslabel.config(text = " ")
    rejection_dateinfolabel.config(text = " ")
    edit_resubmit_timesheetbutton.destroy()
    close_data2.destroy()

def queued_timesheetselect():
    #Opening the selected queued timesheet in the database and defining its data
    timesheetselected = (queued_timesheetlistbox.get(ANCHOR),)
    timesheetselected_string = str(timesheetselected)
    timesheet_selected = timesheetselected_string.replace("(", "")
    timesheet_selected1 = timesheet_selected.replace(")", "")
    timesheet_selected2 = timesheet_selected1.replace("'", "")
    timesheet_selected_label = timesheet_selected2.replace(",", "")

    #getting the saved hourtype
    hourtype_get = "SELECT hourtype_selected FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(hourtype_get, timesheetselected)
    hourtype = cursor.fetchall()

    hourtype_string = str(hourtype)
    hourtype1 = hourtype_string.replace("[", "")
    hourtype2 = hourtype1.replace("]", "")
    hourtype3 = hourtype2.replace("(", "")
    hourtype4 = hourtype3.replace(")", "")
    hourtype5 = hourtype4.replace("'", "")
    hourtype_final = hourtype5.replace(",", "")

    #getting day1 hours saved
    day1_get = "SELECT day1 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day1_get, timesheetselected)
    day1 = cursor.fetchall()

    day1_string = str(day1)
    day1_1 = day1_string.replace("[", "")
    day1_2 = day1_1.replace("]", "")
    day1_3 = day1_2.replace("(", "")
    day1_4 = day1_3.replace(")", "")
    day1_5 = day1_4.replace("'", "")
    day1_final = day1_5.replace(",", "")

    #getting day2 hours saved
    day2_get = "SELECT day2 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day2_get, timesheetselected)
    day2 = cursor.fetchall()

    day2_string = str(day2)
    day2_1 = day2_string.replace("[", "")
    day2_2 = day2_1.replace("]", "")
    day2_3 = day2_2.replace("(", "")
    day2_4 = day2_3.replace(")", "")
    day2_5 = day2_4.replace("'", "")
    day2_final = day2_5.replace(",", "")

    #getting day3 hours saved
    day3_get = "SELECT day3 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day3_get, timesheetselected)
    day3 = cursor.fetchall()

    day3_string = str(day3)
    day3_1 = day3_string.replace("[", "")
    day3_2 = day3_1.replace("]", "")
    day3_3 = day3_2.replace("(", "")
    day3_4 = day3_3.replace(")", "")
    day3_5 = day3_4.replace("'", "")
    day3_final = day3_5.replace(",", "")

    #getting day4 hours saved
    day4_get = "SELECT day4 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day4_get, timesheetselected)
    day4 = cursor.fetchall()

    day4_string = str(day4)
    day4_1 = day4_string.replace("[", "")
    day4_2 = day4_1.replace("]", "")
    day4_3 = day4_2.replace("(", "")
    day4_4 = day4_3.replace(")", "")
    day4_5 = day4_4.replace("'", "")
    day4_final = day4_5.replace(",", "")

    #getting day5 hours saved
    day5_get = "SELECT day5 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day5_get, timesheetselected)
    day5 = cursor.fetchall()

    day5_string = str(day5)
    day5_1 = day5_string.replace("[", "")
    day5_2 = day5_1.replace("]", "")
    day5_3 = day5_2.replace("(", "")
    day5_4 = day5_3.replace(")", "")
    day5_5 = day5_4.replace("'", "")
    day5_final = day5_5.replace(",", "")

    #getting day6 hours saved
    day6_get = "SELECT day6 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day6_get, timesheetselected)
    day6 = cursor.fetchall()

    day6_string = str(day6)
    day6_1 = day6_string.replace("[", "")
    day6_2 = day6_1.replace("]", "")
    day6_3 = day6_2.replace("(", "")
    day6_4 = day6_3.replace(")", "")
    day6_5 = day6_4.replace("'", "")
    day6_final = day6_5.replace(",", "")

    #getting day7 hours_saved
    day7_get = "SELECT day7 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day7_get, timesheetselected)
    day7 = cursor.fetchall()

    day7_string = str(day7)
    day7_1 = day7_string.replace("[", "")
    day7_2 = day7_1.replace("]", "")
    day7_3 = day7_2.replace("(", "")
    day7_4 = day7_3.replace(")", "")
    day7_5 = day7_4.replace("'", "")
    day7_final = day7_5.replace(",", "")

    #getting notes that were saved
    notes_get = "SELECT notes FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(notes_get, timesheetselected)
    notes = cursor.fetchall()

    notes_string = str(notes)
    notes_1 = notes_string.replace("[", "")
    notes_2 = notes_1.replace("]", "")
    notes_3 = notes_2.replace("(", "")
    notes_4 = notes_3.replace(")", "")
    notes_5 = notes_4.replace("'", "")
    notes_final = notes_5.replace(",", "")

    #Labeling the screen with defined data
    queued_timesheetselectedlabel.config(text = timesheet_selected_label)
    queued_hourtypeselectedlabel.config(text = "Hourtype Selected: " + hourtype_final)
    queued_hoursinfo1label.config(text = day1_final + " hour(s)")
    queued_hoursinfo2label.config(text = day2_final + " hour(s)")
    queued_hoursinfo3label.config(text = day3_final + " hour(s)")
    queued_hoursinfo4label.config(text = day4_final + " hour(s)")
    queued_hoursinfo5label.config(text = day5_final + " hour(s)")
    queued_hoursinfo6label.config(text = day6_final + " hour(s)")
    queued_hoursinfo7label.config(text = day7_final + " hour(s)")
    queued_hoursnoteslabel.config(text = "Notes: " + notes_final)

    global close_data
    close_data= Button(window, text="Close", command=close_queuedtimesheetdata )
    close_data.place(x=165, y=600)

def approved_timesheetselect():
    #Opening the selected approved timesheet in the database and defining its data
    timesheetselected = (approved_timesheetlistbox.get(ANCHOR),)
    timesheetselected_string = str(timesheetselected)
    timesheet_selected = timesheetselected_string.replace("(", "")
    timesheet_selected1 = timesheet_selected.replace(")", "")
    timesheet_selected2 = timesheet_selected1.replace("'", "")
    timesheet_selected_label = timesheet_selected2.replace(",", "")

    #getting the saved hourtype
    hourtype_get = "SELECT hourtype_selected FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(hourtype_get, timesheetselected)
    hourtype = cursor.fetchall()

    hourtype_string = str(hourtype)
    hourtype1 = hourtype_string.replace("[", "")
    hourtype2 = hourtype1.replace("]", "")
    hourtype3 = hourtype2.replace("(", "")
    hourtype4 = hourtype3.replace(")", "")
    hourtype5 = hourtype4.replace("'", "")
    hourtype_final = hourtype5.replace(",", "")

    #getting day1 hours saved
    day1_get = "SELECT day1 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day1_get, timesheetselected)
    day1 = cursor.fetchall()

    day1_string = str(day1)
    day1_1 = day1_string.replace("[", "")
    day1_2 = day1_1.replace("]", "")
    day1_3 = day1_2.replace("(", "")
    day1_4 = day1_3.replace(")", "")
    day1_5 = day1_4.replace("'", "")
    day1_final = day1_5.replace(",", "")

    #getting day2 hours saved
    day2_get = "SELECT day2 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day2_get, timesheetselected)
    day2 = cursor.fetchall()

    day2_string = str(day2)
    day2_1 = day2_string.replace("[", "")
    day2_2 = day2_1.replace("]", "")
    day2_3 = day2_2.replace("(", "")
    day2_4 = day2_3.replace(")", "")
    day2_5 = day2_4.replace("'", "")
    day2_final = day2_5.replace(",", "")

    #getting day3 hours saved
    day3_get = "SELECT day3 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day3_get, timesheetselected)
    day3 = cursor.fetchall()

    day3_string = str(day3)
    day3_1 = day3_string.replace("[", "")
    day3_2 = day3_1.replace("]", "")
    day3_3 = day3_2.replace("(", "")
    day3_4 = day3_3.replace(")", "")
    day3_5 = day3_4.replace("'", "")
    day3_final = day3_5.replace(",", "")

    #getting day4 hours saved
    day4_get = "SELECT day4 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day4_get, timesheetselected)
    day4 = cursor.fetchall()

    day4_string = str(day4)
    day4_1 = day4_string.replace("[", "")
    day4_2 = day4_1.replace("]", "")
    day4_3 = day4_2.replace("(", "")
    day4_4 = day4_3.replace(")", "")
    day4_5 = day4_4.replace("'", "")
    day4_final = day4_5.replace(",", "")

    #getting day5 hours saved
    day5_get = "SELECT day5 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day5_get, timesheetselected)
    day5 = cursor.fetchall()

    day5_string = str(day5)
    day5_1 = day5_string.replace("[", "")
    day5_2 = day5_1.replace("]", "")
    day5_3 = day5_2.replace("(", "")
    day5_4 = day5_3.replace(")", "")
    day5_5 = day5_4.replace("'", "")
    day5_final = day5_5.replace(",", "")

    #getting day6 hours saved
    day6_get = "SELECT day6 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day6_get, timesheetselected)
    day6 = cursor.fetchall()

    day6_string = str(day6)
    day6_1 = day6_string.replace("[", "")
    day6_2 = day6_1.replace("]", "")
    day6_3 = day6_2.replace("(", "")
    day6_4 = day6_3.replace(")", "")
    day6_5 = day6_4.replace("'", "")
    day6_final = day6_5.replace(",", "")

    #getting day7 hours_saved
    day7_get = "SELECT day7 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day7_get, timesheetselected)
    day7 = cursor.fetchall()

    day7_string = str(day7)
    day7_1 = day7_string.replace("[", "")
    day7_2 = day7_1.replace("]", "")
    day7_3 = day7_2.replace("(", "")
    day7_4 = day7_3.replace(")", "")
    day7_5 = day7_4.replace("'", "")
    day7_final = day7_5.replace(",", "")

    #getting notes that were saved
    notes_get = "SELECT notes FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(notes_get, timesheetselected)
    notes = cursor.fetchall()

    notes_string = str(notes)
    notes_1 = notes_string.replace("[", "")
    notes_2 = notes_1.replace("]", "")
    notes_3 = notes_2.replace("(", "")
    notes_4 = notes_3.replace(")", "")
    notes_5 = notes_4.replace("'", "")
    notes_final = notes_5.replace(",", "")

    #Labeling the screen with defined data
    approved_timesheetselectedlabel.config(text = timesheet_selected_label)
    approved_hourtypeselectedlabel.config(text = "Hourtype Selected: " + hourtype_final)
    approved_hoursinfo1label.config(text =  day1_final + " hour(s)")
    approved_hoursinfo2label.config(text = day2_final + " hour(s)")
    approved_hoursinfo3label.config(text = day3_final + " hour(s)")
    approved_hoursinfo4label.config(text = day4_final + " hour(s)")
    approved_hoursinfo5label.config(text = day5_final + " hour(s)")
    approved_hoursinfo6label.config(text = day6_final + " hour(s)")
    approved_hoursinfo7label.config(text = day7_final + " hour(s)")
    approved_hoursnoteslabel.config(text = "Notes: " + notes_final)

    global close_data1
    close_data1= Button(window, text="Close", command=close_approvedtimesheetdata )
    close_data1.place(x=790, y=600)

def rejected_timesheetselect():
    #Opening the selected rejected timesheet in the database and defining its data
    timesheetselected = (rejected_timesheetlistbox.get(ANCHOR),)
    timesheetselected_string = str(timesheetselected)
    timesheet_selected = timesheetselected_string.replace("(", "")
    timesheet_selected1 = timesheet_selected.replace(")", "")
    timesheet_selected2 = timesheet_selected1.replace("'", "")
    timesheet_selected_label = timesheet_selected2.replace(",", "")

    #getting the saved hourtype
    hourtype_get = "SELECT hourtype_selected FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(hourtype_get, timesheetselected)
    hourtype = cursor.fetchall()

    hourtype_string = str(hourtype)
    hourtype1 = hourtype_string.replace("[", "")
    hourtype2 = hourtype1.replace("]", "")
    hourtype3 = hourtype2.replace("(", "")
    hourtype4 = hourtype3.replace(")", "")
    hourtype5 = hourtype4.replace("'", "")
    hourtype_final = hourtype5.replace(",", "")

    #getting day1 hours saved
    day1_get = "SELECT day1 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day1_get, timesheetselected)
    day1 = cursor.fetchall()

    day1_string = str(day1)
    day1_1 = day1_string.replace("[", "")
    day1_2 = day1_1.replace("]", "")
    day1_3 = day1_2.replace("(", "")
    day1_4 = day1_3.replace(")", "")
    day1_5 = day1_4.replace("'", "")
    day1_final = day1_5.replace(",", "")

    #getting day2 hours saved
    day2_get = "SELECT day2 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day2_get, timesheetselected)
    day2 = cursor.fetchall()

    day2_string = str(day2)
    day2_1 = day2_string.replace("[", "")
    day2_2 = day2_1.replace("]", "")
    day2_3 = day2_2.replace("(", "")
    day2_4 = day2_3.replace(")", "")
    day2_5 = day2_4.replace("'", "")
    day2_final = day2_5.replace(",", "")

    #getting day3 hours saved
    day3_get = "SELECT day3 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day3_get, timesheetselected)
    day3 = cursor.fetchall()

    day3_string = str(day3)
    day3_1 = day3_string.replace("[", "")
    day3_2 = day3_1.replace("]", "")
    day3_3 = day3_2.replace("(", "")
    day3_4 = day3_3.replace(")", "")
    day3_5 = day3_4.replace("'", "")
    day3_final = day3_5.replace(",", "")

    #getting day4 hours saved
    day4_get = "SELECT day4 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day4_get, timesheetselected)
    day4 = cursor.fetchall()

    day4_string = str(day4)
    day4_1 = day4_string.replace("[", "")
    day4_2 = day4_1.replace("]", "")
    day4_3 = day4_2.replace("(", "")
    day4_4 = day4_3.replace(")", "")
    day4_5 = day4_4.replace("'", "")
    day4_final = day4_5.replace(",", "")

    #getting day5 hours saved
    day5_get = "SELECT day5 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day5_get, timesheetselected)
    day5 = cursor.fetchall()

    day5_string = str(day5)
    day5_1 = day5_string.replace("[", "")
    day5_2 = day5_1.replace("]", "")
    day5_3 = day5_2.replace("(", "")
    day5_4 = day5_3.replace(")", "")
    day5_5 = day5_4.replace("'", "")
    day5_final = day5_5.replace(",", "")

    #getting day6 hours saved
    day6_get = "SELECT day6 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day6_get, timesheetselected)
    day6 = cursor.fetchall()

    day6_string = str(day6)
    day6_1 = day6_string.replace("[", "")
    day6_2 = day6_1.replace("]", "")
    day6_3 = day6_2.replace("(", "")
    day6_4 = day6_3.replace(")", "")
    day6_5 = day6_4.replace("'", "")
    day6_final = day6_5.replace(",", "")

    #getting day7 hours_saved
    day7_get = "SELECT day7 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day7_get, timesheetselected)
    day7 = cursor.fetchall()

    day7_string = str(day7)
    day7_1 = day7_string.replace("[", "")
    day7_2 = day7_1.replace("]", "")
    day7_3 = day7_2.replace("(", "")
    day7_4 = day7_3.replace(")", "")
    day7_5 = day7_4.replace("'", "")
    day7_final = day7_5.replace(",", "")

    #getting notes that were saved
    notes_get = "SELECT notes FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(notes_get, timesheetselected)
    notes = cursor.fetchall()

    notes_string = str(notes)
    notes_1 = notes_string.replace("[", "")
    notes_2 = notes_1.replace("]", "")
    notes_3 = notes_2.replace("(", "")
    notes_4 = notes_3.replace(")", "")
    notes_5 = notes_4.replace("'", "")
    notes_final = notes_5.replace(",", "")

    #Labeling the screen with defined data
    rejected_timesheetselectedlabel.config(text = timesheet_selected_label)
    rejected_hourtypeselectedlabel.config(text = "Hourtype Selected: " + hourtype_final)
    rejected_hoursinfo1label.config(text =  day1_final + " hour(s)")
    rejected_hoursinfo2label.config(text = day2_final + " hour(s)")
    rejected_hoursinfo3label.config(text = day3_final + " hour(s)")
    rejected_hoursinfo4label.config(text = day4_final + " hour(s)")
    rejected_hoursinfo5label.config(text = day5_final + " hour(s)")
    rejected_hoursinfo6label.config(text = day6_final + " hour(s)")
    rejected_hoursinfo7label.config(text = day7_final + " hour(s)")
    rejected_hoursnoteslabel.config(text = "Notes: " + notes_final)

    #for the rejected timesheet view, users will have the option to edit and resubmit their data by clicking this button
    global edit_resubmit_timesheetbutton
    edit_resubmit_timesheetbutton = Button(window, text="Edit + Resubmit this timesheet", command=open_editrejectmenu)
    edit_resubmit_timesheetbutton.place(x=1365, y=600)

    global close_data2
    close_data2= Button(window, text="Close", command=close_rejectedtimesheetdata )
    close_data2.place(x=1365, y=630)

def save_editedtimesheet():
    remove_rejected = "DELETE FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(remove_rejected, rejected_timesheetselected)

    w_t_db.commit()

    rejected_timesheet_selected_string = str(rejected_timesheetselected)
    rejected_timesheet_selected1 = rejected_timesheet_selected_string.replace("(", "")
    rejected_timesheet_selected2 = rejected_timesheet_selected1.replace(")", "")
    rejected_timesheet_selected3 = rejected_timesheet_selected2.replace("'", "")
    rejected_timesheet_selected4 = rejected_timesheet_selected3.replace(",", "")

    hoursentry_data1 = rejected_hoursentrydata1.get()
    hoursentry_data2 = rejected_hoursentrydata2.get()
    hoursentry_data3 = rejected_hoursentrydata3.get()
    hoursentry_data4 = rejected_hoursentrydata4.get()
    hoursentry_data5 = rejected_hoursentrydata5.get()
    hoursentry_data6 = rejected_hoursentrydata6.get()
    hoursentry_data7 = rejected_hoursentrydata7.get()
    hoursentry_datanotes = rejected_hoursentry_notes.get()
    print(hoursentry_datanotes)

    timesheet_data_write = "INSERT INTO " + nameinfo1 + "_timesheetdata" + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    timesheet_data = (rejected_timesheet_selected4, str(rejected_hourtype_selected), str(hoursentry_data1), str(hoursentry_data2), str(hoursentry_data3), str(hoursentry_data4), str(hoursentry_data5), str(hoursentry_data6), str(hoursentry_data7), str(hoursentry_datanotes), 'Rejected')

    cursor.execute(timesheet_data_write, timesheet_data)

    w_t_db.commit()

    rejected_hourtype_listbox.config(background="light gray")
    rejected_hoursentry1.config(background="light gray")
    rejected_hoursentry2.config(background="light gray")
    rejected_hoursentry3.config(background="light gray")
    rejected_hoursentry4.config(background="light gray")
    rejected_hoursentry5.config(background="light gray")
    rejected_hoursentry6.config(background="light gray")
    rejected_hoursentry7.config(background="light gray")
    rejected_hoursentrynotes.config(background="light gray")
    Label(window, text = "Your edited timesheet has been saved; please don't forget to come back and resubmit it when you're ready.", bg="white", font="none 12 bold") .place(x=485, y=225)

def resubmit_timesheet():

    remove_rejected = "DELETE FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(remove_rejected, rejected_timesheetselected)

    w_t_db.commit()

    rejected_timesheet_selected_string = str(rejected_timesheetselected)
    rejected_timesheet_selected1 = rejected_timesheet_selected_string.replace("(", "")
    rejected_timesheet_selected2 = rejected_timesheet_selected1.replace(")", "")
    rejected_timesheet_selected3 = rejected_timesheet_selected2.replace("'", "")
    rejected_timesheet_selected4 = rejected_timesheet_selected3.replace(",", "")

    hoursentry_data1 = rejected_hoursentrydata1.get()
    hoursentry_data2 = rejected_hoursentrydata2.get()
    hoursentry_data3 = rejected_hoursentrydata3.get()
    hoursentry_data4 = rejected_hoursentrydata4.get()
    hoursentry_data5 = rejected_hoursentrydata5.get()
    hoursentry_data6 = rejected_hoursentrydata6.get()
    hoursentry_data7 = rejected_hoursentrydata7.get()
    hoursentry_datanotes = rejected_hoursentry_notes.get()

    timesheet_data_write = "INSERT INTO " + nameinfo1 + "_timesheetdata" + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    timesheet_data = (rejected_timesheet_selected4, str(rejected_hourtype_selected), str(hoursentry_data1), str(hoursentry_data2), str(hoursentry_data3), str(hoursentry_data4), str(hoursentry_data5), str(hoursentry_data6), str(hoursentry_data7), str(hoursentry_datanotes), 'Queued')

    cursor.execute(timesheet_data_write, timesheet_data)

    w_t_db.commit()

    rejected_hourtype_listbox.config(background="light gray")
    rejected_hoursentry1.config(background="light gray")
    rejected_hoursentry2.config(background="light gray")
    rejected_hoursentry3.config(background="light gray")
    rejected_hoursentry4.config(background="light gray")
    rejected_hoursentry5.config(background="light gray")
    rejected_hoursentry6.config(background="light gray")
    rejected_hoursentry7.config(background="light gray")
    rejected_hoursentrynotes.config(background="light gray")
    Label(window, text = "Your edited timesheet has been resubmitted.", bg="white", font="none 12 bold") .place(x=485, y=225)


def open_editrejectmenu():
    clear_screen()

    global rejected_timesheetselected
    rejected_timesheetselected = (rejected_timesheetlistbox.get(ANCHOR),)

    rejected_timesheet_string = str(rejected_timesheetselected)
    rejected_timesheet = rejected_timesheet_string.replace("'", "")
    rejected_timesheet1 = rejected_timesheet.replace("(", "")
    rejected_timesheet2 = rejected_timesheet1.replace(")", "")
    rejected_timesheet3 = rejected_timesheet2.replace(",", "")

    window.title("Edit + Resubmit Timesheet")
    window.configure(background="white")
    Label (window, image=logo, bg="white", justify="left") .pack()

    Label(window, text = rejected_timesheet3, bg="white", font="none 20 bold") .pack()

    Label(window, text="Hourtype Select", bg="white", font="none 12 bold") .place(x=325, y=125)
    rejected_hourtype_frame = Frame(window)
    rejected_hourtype_scrollbar = Scrollbar(rejected_hourtype_frame, orient=VERTICAL)
    global rejected_hourtype_listbox
    global rejected_hourtype_list
    rejected_hourtype_listbox = Listbox(rejected_hourtype_frame, yscrollcommand=rejected_hourtype_scrollbar.set)
    rejected_hourtype_scrollbar.config(command=rejected_hourtype_listbox.yview)
    rejected_hourtype_scrollbar.pack(side=RIGHT, fill=Y)
    rejected_hourtype_frame.place(x=325, y=150)
    rejected_hourtype_listbox.pack()
    rejected_hourtype_list = ["Standard", "Double", "Overtime", "Other"]
    for rejected_hourtype in hourtype_list:
        rejected_hourtype_listbox.insert(END, rejected_hourtype)
    Button(window, text="Select", command=rejected_hourtype_select) .place(x=365, y=325)
    global rejected_hourtype_label
    rejected_hourtype_label = Label(window, text='', bg="white", fg="green", font="none 12 bold")
    rejected_hourtype_label.place(x=300, y=325)

    global rejected_hoursentrydata1
    global rejected_hoursentry1
    rejected_hoursentrydata1 = StringVar()

    rejected_hoursentry1 = Entry(window, textvariable = rejected_hoursentrydata1, width=5)
    rejected_hoursentry1.place(x=500, y=150)

    global rejected_hoursentrydata2
    global rejected_hoursentry2
    rejected_hoursentrydata2 = StringVar()
    rejected_hoursentry2 = Entry(window, textvariable = rejected_hoursentrydata2, width=5)
    rejected_hoursentry2.place(x=575, y=150)

    global rejected_hoursentrydata3
    global rejected_hoursentry3
    rejected_hoursentrydata3 = StringVar()
    rejected_hoursentry3 = Entry(window, textvariable = rejected_hoursentrydata3, width=5)
    rejected_hoursentry3.place(x=650, y=150)

    global rejected_hoursentrydata4
    global rejected_hoursentry4
    rejected_hoursentrydata4 = StringVar()
    rejected_hoursentry4 = Entry(window, textvariable = rejected_hoursentrydata4, width=5)
    rejected_hoursentry4.place(x=725, y=150)

    global rejected_hoursentrydata5
    global rejected_hoursentry5
    rejected_hoursentrydata5 = StringVar()
    rejected_hoursentry5 = Entry(window, textvariable = rejected_hoursentrydata5, width=5)
    rejected_hoursentry5.place(x=800, y=150)

    global rejected_hoursentrydata6
    global rejected_hoursentry6
    rejected_hoursentrydata6 = StringVar()
    rejected_hoursentry6 = Entry(window, textvariable = rejected_hoursentrydata6, width=5)
    rejected_hoursentry6.place(x=875, y=150)

    global rejected_hoursentrydata7
    global rejected_hoursentry7
    rejected_hoursentrydata7 = StringVar()
    rejected_hoursentry7 = Entry(window, textvariable = rejected_hoursentrydata7, width=5)
    rejected_hoursentry7.place(x=950, y=150)

    global rejected_hoursentry_notes
    global rejected_hoursentrynotes
    rejected_hoursentry_notes = StringVar()
    Label(window, text="Notes", bg="white", fg="black", font="none 12 bold") .place(x=1020, y=125)
    rejected_hoursentrynotes = Entry(window, textvariable = rejected_hoursentry_notes, width=20)
    rejected_hoursentrynotes.place(x=1025, y=150)

    savetimesheet = Button(window, text = "Save Resubmit Draft", command = save_editedtimesheet) .place(x=1175, y=150)

    locktimesheet = Button(window, text="Resubmit Timesheet", command = resubmit_timesheet) .place(x=1300, y=150)

    edit_rejectedtimesheet()

def userviewtimesheet():
    clear_screen()

    window.title("View Previous Timesheets")
    Label(window, text="View Previous Timesheets", bg="white", font="none 20 bold") .pack()

    Button(window, text="Return to Dashboard", command=session) .place(x=50, y=50)

    #Opening Queued timesheets
    get_queued = "SELECT timesheet FROM " + nameinfo1 + """_timesheetdata WHERE approval_status = 'Queued'"""
    cursor.execute(get_queued)
    all_queued_timesheets = cursor.fetchall()

    #Yet to be approved/rejected Timesheets Listbox
    Label(window, text="Queued for Approval", bg="white", fg="gray", font="none 12 bold") .place(x=200, y=75)

    queued_timesheetframe = Frame(window)
    queued_timesheetscrollbar = Scrollbar(queued_timesheetframe, orient=VERTICAL)
    global queued_timesheetlistbox
    queued_timesheetlistbox = Listbox(queued_timesheetframe, yscrollcommand=queued_timesheetscrollbar.set, width=38)
    queued_timesheetscrollbar.config(command=queued_timesheetlistbox.yview)
    queued_timesheetscrollbar.pack(side=RIGHT, fill=Y)
    queued_timesheetframe.place(x=160, y=100)
    queued_timesheetlistbox.pack()

    #Insert queued_timesheet from database - all replace commands are modifying the string to be more visually pleasing
    for queued_timesheet in all_queued_timesheets:
        queued_timesheet_string = str(queued_timesheet)
        queued_timesheet = queued_timesheet_string.replace("'", "")
        queued_timesheet1 = queued_timesheet.replace("(", "")
        queued_timesheet2 = queued_timesheet1.replace(")", "")
        queued_timesheet3 = queued_timesheet2.replace(",", "")
        queued_timesheetlistbox.insert(0, queued_timesheet3)

    Button(window, text="Select", command=queued_timesheetselect) .place(x=265, y=275)

    #Creating configurable labels that will change according to what timesheet the user selects
    global queued_timesheetselectedlabel
    queued_timesheetselectedlabel = Label(window, text = '', bg="white", font="none 12 bold")
    queued_timesheetselectedlabel.place(x=165, y=325)

    global queued_hourtypeselectedlabel
    queued_hourtypeselectedlabel = Label(window, text = " ", bg="white", font="none 12")
    queued_hourtypeselectedlabel.place(x=165, y=350)

    global queued_hoursinfo1label
    queued_hoursinfo1label = Label(window, text = " ", bg="white", font="none 12")
    queued_hoursinfo1label.place(x=165, y=375)

    global queued_hoursinfo2label
    queued_hoursinfo2label = Label(window, text = " ", bg="white", font="none 12")
    queued_hoursinfo2label.place(x=165, y=400)

    global queued_hoursinfo3label
    queued_hoursinfo3label = Label(window, text = " ", bg="white", font="none 12")
    queued_hoursinfo3label.place(x=165, y=425)

    global queued_hoursinfo4label
    queued_hoursinfo4label = Label(window, text = " ", bg="white", font="none 12")
    queued_hoursinfo4label.place(x=165, y=450)

    global queued_hoursinfo5label
    queued_hoursinfo5label = Label(window, text = " ", bg="white", font="none 12")
    queued_hoursinfo5label.place(x=165, y=475)

    global queued_hoursinfo6label
    queued_hoursinfo6label = Label(window, text = " ", bg="white", font="none 12")
    queued_hoursinfo6label.place(x=165, y=500)

    global queued_hoursinfo7label
    queued_hoursinfo7label = Label(window, text = " ", bg="white", font="none 12")
    queued_hoursinfo7label.place(x=165, y=525)

    global queued_hoursnoteslabel
    queued_hoursnoteslabel = Label(window, text = " ", bg="white", font="none 12")
    queued_hoursnoteslabel.place(x=165, y=550)

    #Opening Approved timesheets
    get_approved = "SELECT timesheet FROM " + nameinfo1 + """_timesheetdata WHERE approval_status = 'Approved'"""
    cursor.execute(get_approved)
    all_approved_timesheets = cursor.fetchall()

    #Approved Timesheet Listbox
    Label(window, text="Approved", bg="white", fg="green", font="none 12 bold") .place(x=870, y=75)

    approved_timesheetframe = Frame(window)
    approved_timesheetscrollbar = Scrollbar(approved_timesheetframe, orient=VERTICAL)
    global approved_timesheetlistbox
    approved_timesheetlistbox = Listbox(approved_timesheetframe, yscrollcommand=approved_timesheetscrollbar.set, width=38)
    approved_timesheetscrollbar.config(command=approved_timesheetlistbox.yview)
    approved_timesheetscrollbar.pack(side=RIGHT, fill=Y)
    approved_timesheetframe.place(x=790, y=100)
    approved_timesheetlistbox.pack()

    #Insert approved_timesheet from database - all replace commands are modifying the string to be more visually pleasing
    for approved_timesheet in all_approved_timesheets:
        approved_timesheet_string = str(approved_timesheet)
        approved_timesheet = approved_timesheet_string.replace("'", "")
        approved_timesheet1 = approved_timesheet.replace("(", "")
        approved_timesheet2 = approved_timesheet1.replace(")", "")
        approved_timesheet3 = approved_timesheet2.replace(",", "")
        approved_timesheetlistbox.insert(0, approved_timesheet3)

    Button(window, text="Select", command=approved_timesheetselect) .place(x=890, y=275)

    #Creating configurable labels that will change according to what timesheet the user selects
    global approved_timesheetselectedlabel
    approved_timesheetselectedlabel = Label(window, text = '', bg="white", font="none 12 bold")
    approved_timesheetselectedlabel.place(x=790, y=325)

    global approved_hourtypeselectedlabel
    approved_hourtypeselectedlabel = Label(window, text = " ", bg="white", font="none 12")
    approved_hourtypeselectedlabel.place(x=790, y=350)

    global approved_hoursinfo1label
    approved_hoursinfo1label = Label(window, text = " ", bg="white", font="none 12")
    approved_hoursinfo1label.place(x=790, y=375)

    global approved_hoursinfo2label
    approved_hoursinfo2label = Label(window, text = " ", bg="white", font="none 12")
    approved_hoursinfo2label.place(x=790, y=400)

    global approved_hoursinfo3label
    approved_hoursinfo3label = Label(window, text = " ", bg="white", font="none 12")
    approved_hoursinfo3label.place(x=790, y=425)

    global approved_hoursinfo4label
    approved_hoursinfo4label = Label(window, text = " ", bg="white", font="none 12")
    approved_hoursinfo4label.place(x=790, y=450)

    global approved_hoursinfo5label
    approved_hoursinfo5label = Label(window, text = " ", bg="white", font="none 12")
    approved_hoursinfo5label.place(x=790, y=475)

    global approved_hoursinfo6label
    approved_hoursinfo6label = Label(window, text = " ", bg="white", font="none 12")
    approved_hoursinfo6label.place(x=790, y=500)

    global approved_hoursinfo7label
    approved_hoursinfo7label = Label(window, text = " ", bg="white", font="none 12")
    approved_hoursinfo7label.place(x=790, y=525)

    global approved_hoursnoteslabel
    approved_hoursnoteslabel = Label(window, text = " ", bg="white", font="none 12")
    approved_hoursnoteslabel.place(x=790, y=550)

    global approval_dateinfolabel
    approval_dateinfolabel = Label(window, text = " ", bg="white", font="none 12")
    approval_dateinfolabel.place(x=790, y=575)

    #Opening Rejected timesheets
    get_rejected = "SELECT timesheet FROM " + nameinfo1 + """_timesheetdata WHERE approval_status = 'Rejected'"""
    cursor.execute(get_rejected)
    all_rejected_timesheets = cursor.fetchall()

    #Rejected Timesheet Listbox
    Label(window, text="Rejected*", bg="white", fg="red", font="none 12 bold") .place(x=1450, y=75)

    rejected_timesheetframe = Frame(window)
    rejected_timesheetscrollbar = Scrollbar(rejected_timesheetframe, orient=VERTICAL)
    global rejected_timesheetlistbox
    rejected_timesheetlistbox = Listbox(rejected_timesheetframe, yscrollcommand=rejected_timesheetscrollbar.set, width=38)
    rejected_timesheetscrollbar.config(command=rejected_timesheetlistbox.yview)
    rejected_timesheetscrollbar.pack(side=RIGHT, fill=Y)
    rejected_timesheetframe.place(x=1365, y=100)
    rejected_timesheetlistbox.pack()

    #Insert rejected_timesheet from database - all replace commands are modifying the string to be more visually pleasing
    for rejected_timesheet in all_rejected_timesheets:
        rejected_timesheet_string = str(rejected_timesheet)
        rejected_timesheet = rejected_timesheet_string.replace("'", "")
        rejected_timesheet1 = rejected_timesheet.replace("(", "")
        rejected_timesheet2 = rejected_timesheet1.replace(")", "")
        rejected_timesheet3 = rejected_timesheet2.replace(",", "")
        rejected_timesheetlistbox.insert(0, rejected_timesheet3)

    Button(window, text="Select", command=rejected_timesheetselect) .place(x=1470, y=275)

    #Creating configurable labels that will change according to what timesheet the user selects
    global rejected_timesheetselectedlabel
    rejected_timesheetselectedlabel = Label(window, text = '', bg="white", font="none 12 bold")
    rejected_timesheetselectedlabel.place(x=1365, y=325)

    global rejected_hourtypeselectedlabel
    rejected_hourtypeselectedlabel = Label(window, text = " ", bg="white", font="none 12")
    rejected_hourtypeselectedlabel.place(x=1365, y=350)

    global rejected_hoursinfo1label
    rejected_hoursinfo1label = Label(window, text = " ", bg="white", font="none 12")
    rejected_hoursinfo1label.place(x=1365, y=375)

    global rejected_hoursinfo2label
    rejected_hoursinfo2label = Label(window, text = " ", bg="white", font="none 12")
    rejected_hoursinfo2label.place(x=1365, y=400)

    global rejected_hoursinfo3label
    rejected_hoursinfo3label = Label(window, text = " ", bg="white", font="none 12")
    rejected_hoursinfo3label.place(x=1365, y=425)

    global rejected_hoursinfo4label
    rejected_hoursinfo4label = Label(window, text = " ", bg="white", font="none 12")
    rejected_hoursinfo4label.place(x=1365, y=450)

    global rejected_hoursinfo5label
    rejected_hoursinfo5label = Label(window, text = " ", bg="white", font="none 12")
    rejected_hoursinfo5label.place(x=1365, y=475)

    global rejected_hoursinfo6label
    rejected_hoursinfo6label = Label(window, text=" ", bg="white", font="none 12")
    rejected_hoursinfo6label.place(x=1365, y=500)

    global rejected_hoursinfo7label
    rejected_hoursinfo7label = Label(window, text = " ", bg="white", font="none 12")
    rejected_hoursinfo7label.place(x=1365, y=525)

    global rejected_hoursnoteslabel
    rejected_hoursnoteslabel = Label(window, text = " ", bg="white", font="none 12")
    rejected_hoursnoteslabel.place(x=1365, y=550)

    global rejection_dateinfolabel
    rejection_dateinfolabel = Label(window, text = " ", bg="white", font="none 12")
    rejection_dateinfolabel.place(x=1365, y=575)

    #Quick note to remind users how to edit rejected timesheets
    Label(window, text = "*You can edit and resubmit rejected timesheets by selecting a rejected timesheet normally and then selecting to edit it.", bg="white", fg="red", font="none 12") .place(x=0, y=1100)

def overwrite():
    overwritebutton.destroy()

    cancel_overwritebutton.destroy()

    delete_previous = "DELETE FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(delete_previous, (sunday_date + "-" + saturday_date,))

    hourtype_selected = hourtype_listbox.get(ANCHOR)
    hoursentry_data1 = hoursentrydata1.get()
    hoursentry_data2 = hoursentrydata2.get()
    hoursentry_data3 = hoursentrydata3.get()
    hoursentry_data4 = hoursentrydata4.get()
    hoursentry_data5 = hoursentrydata5.get()
    hoursentry_data6 = hoursentrydata6.get()
    hoursentry_data7 = hoursentrydata7.get()
    hoursentry_datanotes = hoursentry_notes.get()

    try:
        timesheet_data_write = "INSERT INTO " + nameinfo1 + "_timesheetdata" + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        timesheet_data = (sunday_date + "-" + saturday_date, str(hourtype_selected), sunday_date + ": " + str(int(hoursentry_data1)), monday_date + ": " + str(int(hoursentry_data2)), tuesday_date + ": " + str(int(hoursentry_data3)), wednesday_date + ": " + str(int(hoursentry_data4)), thursday_date + ": " + str(int(hoursentry_data5)), friday_date + ": " + str(int(hoursentry_data6)), saturday_date + ": " + str(int(hoursentry_data7)), str(hoursentry_datanotes), 'Queued')

        cursor.execute(timesheet_data_write, timesheet_data)

        w_t_db.commit()

        locked_label.config(text = "Your timesheet has been sent to a Manager for approval and will be updated shortly.")

    except ValueError:
        locked_label.config(text = "Please enter an integer value for all hour slots.")

def cancel_overwrite():
    locked_label.config(text=' ')

    overwritebutton.destroy()

    cancel_overwritebutton.destroy()


    hourtype_listbox.config(background="white")
    hoursentry1.config(background="white")
    hoursentry2.config(background="white")
    hoursentry3.config(background="white")
    hoursentry4.config(background="white")
    hoursentry5.config(background="white")
    hoursentry6.config(background="white")
    hoursentry7.config(background="white")
    hoursentrynotes.config(background="white")

def session_datawrite():

    week_check = "SELECT * FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(week_check, (sunday_date + "-" + saturday_date,))

    weekcheck = cursor.fetchall()

    if len(weekcheck) == 0:

        hourtype_selected = hourtype_listbox.get(ANCHOR)
        hoursentry_data1 = hoursentrydata1.get()
        hoursentry_data2 = hoursentrydata2.get()
        hoursentry_data3 = hoursentrydata3.get()
        hoursentry_data4 = hoursentrydata4.get()
        hoursentry_data5 = hoursentrydata5.get()
        hoursentry_data6 = hoursentrydata6.get()
        hoursentry_data7 = hoursentrydata7.get()
        hoursentry_datanotes = hoursentry_notes.get()

        try:
            timesheet_data_write = "INSERT INTO " + nameinfo1 + "_timesheetdata" + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            timesheet_data = (sunday_date + "-" + saturday_date, str(hourtype_selected), sunday_date + ": " + str(int(hoursentry_data1)), monday_date + ": " + str(int(hoursentry_data2)), tuesday_date + ": " + str(int(hoursentry_data3)), wednesday_date + ": " + str(int(hoursentry_data4)), thursday_date + ": " + str(int(hoursentry_data5)), friday_date + ": " + str(int(hoursentry_data6)), saturday_date + ": " + str(int(hoursentry_data7)), str(hoursentry_datanotes), 'Queued')

            cursor.execute(timesheet_data_write, timesheet_data)

            w_t_db.commit()

            locked_label.config(text = "Your timesheet has been sent to a Manager for approval and will be updated shortly.")

        except ValueError:
            locked_label.config(text = "Please enter an integer value for all hour slots.")

    else:
        locked_label.config(text="A timesheet for this week already exists. Would you like to overwrite it?")

        global overwritebutton
        overwritebutton = Button(window, text="Overwrite", command=overwrite)
        overwritebutton.place(x=485, y=255)

        global cancel_overwritebutton
        cancel_overwritebutton = Button(window, text="Cancel", command=cancel_overwrite)
        cancel_overwritebutton.place(x=550, y=255)

def save_overwrite():
    save_overwritebutton.destroy()

    cancel_save_overwritebutton.destroy()

    delete_previous = "DELETE FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    cursor.execute(delete_previous, (sunday_date + "-" + saturday_date,))

    w_t_db.commit()

    hoursentry_data1 = hoursentrydata1.get()
    hoursentry_data2 = hoursentrydata2.get()
    hoursentry_data3 = hoursentrydata3.get()
    hoursentry_data4 = hoursentrydata4.get()
    hoursentry_data5 = hoursentrydata5.get()
    hoursentry_data6 = hoursentrydata6.get()
    hoursentry_data7 = hoursentrydata7.get()
    hoursentry_datanotes = hoursentry_notes.get()

    timesheet_data_write = "INSERT INTO " + nameinfo1 + "_saveddrafts" + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    timesheet_data = (sunday_date + "-" + saturday_date, str(hourtype_selected), sunday_date + ": " + str(hoursentry_data1), monday_date + ": " + str(hoursentry_data2), tuesday_date + ": " + str(hoursentry_data3), wednesday_date + ": " + str(hoursentry_data4), thursday_date + ": " + str(hoursentry_data5), friday_date + ": " + str(hoursentry_data6), saturday_date + ": " + str(hoursentry_data7), str(hoursentry_datanotes), 'Saved Draft')

    cursor.execute(timesheet_data_write, timesheet_data)

    w_t_db.commit()

    locked_label.config(text="Your timesheet draft has been saved.")

def cancel_save_overwrite():
    locked_label.config(text=' ')

    save_overwritebutton.destroy()

    cancel_save_overwritebutton.destroy()


    hourtype_listbox.config(background="white")
    hoursentry1.config(background="white")
    hoursentry2.config(background="white")
    hoursentry3.config(background="white")
    hoursentry4.config(background="white")
    hoursentry5.config(background="white")
    hoursentry6.config(background="white")
    hoursentry7.config(background="white")
    hoursentrynotes.config(background="white")

def saved_sessiondatawrite():
    week_check = "SELECT * FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    cursor.execute(week_check, (sunday_date + "-" + saturday_date,))

    weekcheck = cursor.fetchall()

    if len(weekcheck) == 0:
        hoursentry_data1 = hoursentrydata1.get()
        hoursentry_data2 = hoursentrydata2.get()
        hoursentry_data3 = hoursentrydata3.get()
        hoursentry_data4 = hoursentrydata4.get()
        hoursentry_data5 = hoursentrydata5.get()
        hoursentry_data6 = hoursentrydata6.get()
        hoursentry_data7 = hoursentrydata7.get()
        hoursentry_datanotes = hoursentry_notes.get()

        timesheet_data_write = "INSERT INTO " + nameinfo1 + "_saveddrafts" + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        timesheet_data = (sunday_date + "-" + saturday_date, str(hourtype_selected), sunday_date + ": " + str(hoursentry_data1), monday_date + ": " + str(hoursentry_data2), tuesday_date + ": " + str(hoursentry_data3), wednesday_date + ": " + str(hoursentry_data4), thursday_date + ": " + str(hoursentry_data5), friday_date + ": " + str(hoursentry_data6), saturday_date + ": " + str(hoursentry_data7), str(hoursentry_datanotes), 'Saved Draft')

        cursor.execute(timesheet_data_write, timesheet_data)

        w_t_db.commit()

        saved_label.config(text = "Your timesheet has been saved.")

    else:
        locked_label.config(text="A save file for this week already exists. Would you like to overwrite it?")

        global save_overwritebutton
        save_overwritebutton = Button(window, text="Overwrite", command=save_overwrite)
        save_overwritebutton.place(x=485, y=255)

        global cancel_save_overwritebutton
        cancel_save_overwritebutton = Button(window, text="Cancel", command=cancel_save_overwrite)
        cancel_save_overwritebutton.place(x=550, y=255)


def rejected_hourtype_select():
    global rejected_hourtype_selected
    rejected_hourtype_selected = rejected_hourtype_listbox.get(ANCHOR)
    rejected_hourtype_label.config(text="HOURTYPE SELECTED:\n" + rejected_hourtype_selected)
    Button(window, text="Change", command=rejected_hourtype_select) .place(x=365, y=370)

def hourtype_select():
    hourtype_listbox.config(background="white")
    hoursentry1.config(background="white")
    hoursentry2.config(background="white")
    hoursentry3.config(background="white")
    hoursentry4.config(background="white")
    hoursentry5.config(background="white")
    hoursentry6.config(background="white")
    hoursentry7.config(background="white")
    hoursentrynotes.config(background="white")

    global hourtype_selected
    hourtype_selected = hourtype_listbox.get(ANCHOR)
    hourtype_label.config(text="HOURTYPE SELECTED:\n" + hourtype_selected)
    Button(window, text="Change", command=hourtype_select) .place(x=365, y=370)

def close_savedtimesheetselect():
    select_save_file_label.destroy()
    saved_timesheetframe.destroy()
    select_saved_timesheet.destroy()
    close_save_select.destroy()

def saved_timesheetselect():
    saved_timesheetselected = (saved_timesheetlistbox.get(ANCHOR),)

    #getting the saved hourtype
    hourtype_get = "SELECT hourtype_selected FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    bufferedcursor.execute(hourtype_get, saved_timesheetselected)
    saved_hourtype = bufferedcursor.fetchone()

    saved_hourtype_string = str(saved_hourtype)
    saved_hourtype1 = saved_hourtype_string.replace("[", "")
    saved_hourtype2 = saved_hourtype1.replace("]", "")
    saved_hourtype3 = saved_hourtype2.replace("(", "")
    saved_hourtype4 = saved_hourtype3.replace(")", "")
    saved_hourtype5 = saved_hourtype4.replace("'", "")
    saved_hourtype_final = saved_hourtype5.replace(",", "")


    #getting day1 hours saved
    day1_get = "SELECT day1 FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    bufferedcursor.execute(day1_get, saved_timesheetselected)
    saved_day1 = bufferedcursor.fetchone()

    saved_day1_string = str(saved_day1)
    saved_day1_1 = saved_day1_string.replace("[", "")
    saved_day1_2 = saved_day1_1.replace("]", "")
    saved_day1_3 = saved_day1_2.replace("(", "")
    saved_day1_4 = saved_day1_3.replace(")", "")
    saved_day1_5 = saved_day1_4.replace("'", "")
    saved_day1_final = saved_day1_5.replace(",", "")

    #getting day2 hours saved
    day2_get = "SELECT day2 FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    bufferedcursor.execute(day2_get, saved_timesheetselected)
    saved_day2 = bufferedcursor.fetchone()

    saved_day2_string = str(saved_day2)
    saved_day2_1 = saved_day2_string.replace("[", "")
    saved_day2_2 = saved_day2_1.replace("]", "")
    saved_day2_3 = saved_day2_2.replace("(", "")
    saved_day2_4 = saved_day2_3.replace(")", "")
    saved_day2_5 = saved_day2_4.replace("'", "")
    saved_day2_final = saved_day2_5.replace(",", "")

    #getting day3 hours saved
    day3_get = "SELECT day3 FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    bufferedcursor.execute(day3_get, saved_timesheetselected)
    saved_day3 = bufferedcursor.fetchone()

    saved_day3_string = str(saved_day3)
    saved_day3_1 = saved_day3_string.replace("[", "")
    saved_day3_2 = saved_day3_1.replace("]", "")
    saved_day3_3 = saved_day3_2.replace("(", "")
    saved_day3_4 = saved_day3_3.replace(")", "")
    saved_day3_5 = saved_day3_4.replace("'", "")
    saved_day3_final = saved_day3_5.replace(",", "")

    #getting day4 hours saved
    day4_get = "SELECT day4 FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    bufferedcursor.execute(day4_get, saved_timesheetselected)
    saved_day4 = bufferedcursor.fetchone()

    saved_day4_string = str(saved_day4)
    saved_day4_1 = saved_day4_string.replace("[", "")
    saved_day4_2 = saved_day4_1.replace("]", "")
    saved_day4_3 = saved_day4_2.replace("(", "")
    saved_day4_4 = saved_day4_3.replace(")", "")
    saved_day4_5 = saved_day4_4.replace("'", "")
    saved_day4_final = saved_day4_5.replace(",", "")

    #getting day5 hours saved
    day5_get = "SELECT day5 FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    bufferedcursor.execute(day5_get, saved_timesheetselected)
    saved_day5 = bufferedcursor.fetchone()

    saved_day5_string = str(saved_day5)
    saved_day5_1 = saved_day5_string.replace("[", "")
    saved_day5_2 = saved_day5_1.replace("]", "")
    saved_day5_3 = saved_day5_2.replace("(", "")
    saved_day5_4 = saved_day5_3.replace(")", "")
    saved_day5_5 = saved_day5_4.replace("'", "")
    saved_day5_final = saved_day5_5.replace(",", "")

    #getting day6 hours saved
    day6_get = "SELECT day6 FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    bufferedcursor.execute(day6_get, saved_timesheetselected)
    saved_day6 = bufferedcursor.fetchone()

    saved_day6_string = str(saved_day6)
    saved_day6_1 = saved_day6_string.replace("[", "")
    saved_day6_2 = saved_day6_1.replace("]", "")
    saved_day6_3 = saved_day6_2.replace("(", "")
    saved_day6_4 = saved_day6_3.replace(")", "")
    saved_day6_5 = saved_day6_4.replace("'", "")
    saved_day6_final = saved_day6_5.replace(",", "")

    #getting day7 hours_saved
    day7_get = "SELECT day7 FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    bufferedcursor.execute(day7_get, saved_timesheetselected)
    saved_day7 = bufferedcursor.fetchone()

    saved_day7_string = str(saved_day7)
    saved_day7_1 = saved_day7_string.replace("[", "")
    saved_day7_2 = saved_day7_1.replace("]", "")
    saved_day7_3 = saved_day7_2.replace("(", "")
    saved_day7_4 = saved_day7_3.replace(")", "")
    saved_day7_5 = saved_day7_4.replace("'", "")
    saved_day7_final = saved_day7_5.replace(",", "")

    #getting notes that were saved
    notes_get = "SELECT notes FROM " + nameinfo1 + "_saveddrafts WHERE timesheet = %s"

    bufferedcursor.execute(notes_get, saved_timesheetselected)
    saved_notes = bufferedcursor.fetchone()

    saved_notes_string = str(saved_notes)
    saved_notes_1 = saved_notes_string.replace("[", "")
    saved_notes_2 = saved_notes_1.replace("]", "")
    saved_notes_3 = saved_notes_2.replace("(", "")
    saved_notes_4 = saved_notes_3.replace(")", "")
    saved_notes_5 = saved_notes_4.replace("'", "")
    saved_notes_final = saved_notes_5.replace(",", "")

    #changing hourtype to the one on the save file
    hourtype_label.config(text="HOURTYPE SELECTED:\n" + saved_hourtype_final)
    Button(window, text="Change", command=hourtype_select) .place(x=365, y=370)

    #clearing all entries so they can be replaced by the ones on the save file
    hoursentry1.delete(0, END)
    hoursentry2.delete(0, END)
    hoursentry3.delete(0, END)
    hoursentry4.delete(0, END)
    hoursentry5.delete(0, END)
    hoursentry6.delete(0, END)
    hoursentry7.delete(0, END)
    hoursentrynotes.delete(0, END)

    #replacing the entries with save file data from database
    hoursentry1.insert(END, saved_day1_final[7:8])
    hoursentry2.insert(END, saved_day2_final[7:8])
    hoursentry3.insert(END, saved_day3_final[7:8])
    hoursentry4.insert(END, saved_day4_final[7:8])
    hoursentry5.insert(END, saved_day5_final[7:8])
    hoursentry6.insert(END, saved_day6_final[7:8])
    hoursentry7.insert(END, saved_day7_final[7:8])
    hoursentrynotes.insert(END, saved_notes_final)

def timesheet_datetime():

    numweeks = 1

    global start_date
    start_date = start_date_mode

    weeks = {}

    offset = datetime.timedelta(days=0)

    for week in range(numweeks):
        this_week = []
        for day in range(1):
            date = start_date + offset
            date = date.strftime("%m/%d")
            this_week.append(date)
            offset += datetime.timedelta(days=1)

            weeks[week] = this_week

            global sunday_date
            global sunday_date_string
            sunday_date_string = str(this_week)[1:-1]
            sunday_date = sunday_date_string.translate({ord("'"): None})

            Label(window, text = weeks[week], bg="white", font="none 12 bold") .place(x=495, y=125)

    for week in range(numweeks):
        this_week = []
        for day in range(1,2):
            date = start_date + offset
            date = date.strftime("%m/%d")
            this_week.append(date)
            offset += datetime.timedelta(days=1)

            weeks[week] = this_week

            global monday_date
            monday_date_string= str(this_week)[1:-1]
            monday_date = monday_date_string.translate({ord("'"): None})

            Label(window, text = weeks[week], bg="white", font="none 12 bold") .place(x=570, y=125)

    for week in range(numweeks):
        this_week = []
        for day in range(2,3):
            date = start_date + offset
            date = date.strftime("%m/%d")
            this_week.append(date)
            offset += datetime.timedelta(days=1)

            weeks[week] = this_week

            global tuesday_date
            tuesday_date_string = str(this_week)[1:-1]
            tuesday_date = tuesday_date_string.translate({ord("'"): None})

            Label(window, text = weeks[week], bg="white", font="none 12 bold") .place(x=645, y=125)

    for week in range(numweeks):
        this_week = []
        for day in range(3,4):
            date = start_date + offset
            date = date.strftime("%m/%d")
            this_week.append(date)
            offset += datetime.timedelta(days=1)

            weeks[week] = this_week

            global wednesday_date
            wednesday_date_string = str(this_week)[1:-1]
            wednesday_date = wednesday_date_string.translate({ord("'"): None})

            Label(window, text = weeks[week], bg="white", font="none 12 bold") .place(x=720, y=125)

    for week in range(numweeks):
        this_week = []
        for day in range(4,5):
            date = start_date + offset
            date = date.strftime("%m/%d")
            this_week.append(date)
            offset += datetime.timedelta(days=1)

            weeks[week] = this_week

            global thursday_date
            thursday_date_string= str(this_week)[1:-1]
            thursday_date = thursday_date_string.translate({ord("'"): None})

            Label(window, text = weeks[week], bg="white", font="none 12 bold") .place(x=795, y=125)

    for week in range(numweeks):
        this_week = []
        for day in range(5,6):
            date = start_date + offset
            date = date.strftime("%m/%d")
            this_week.append(date)
            offset += datetime.timedelta(days=1)

            weeks[week] = this_week

            global friday_date
            friday_date_string = str(this_week)[1:-1]
            friday_date = friday_date_string.translate({ord("'"): None})

            Label(window, text = weeks[week], bg="white", font="none 12 bold") .place(x=870, y=125)

    for week in range(numweeks):
        this_week = []
        for day in range(6,7):
            date = start_date + offset
            date = date.strftime("%m/%d")
            this_week.append(date)
            offset += datetime.timedelta(days=1)

            weeks[week] = this_week

            global saturday_date
            saturday_date_string = str(this_week)[1:-1]
            saturday_date = saturday_date_string.translate({ord("'"): None})

            Label(window, text = weeks[week], bg="white", font="none 12 bold") .place(x=945, y=125)
def open_saved_timesheet():
    #Visually Clearing Screen if needed
    clear_bottom_session()

    #opening database and finding saved drafts

    open_saveddrafts_db = "SELECT timesheet FROM " + nameinfo1 + """_saveddrafts"""

    cursor.execute(open_saveddrafts_db)

    saveddrafts = cursor.fetchall()

    global select_save_file_label
    select_save_file_label = Label(window, text="Select Save File", bg="white", font="none 12 bold")
    select_save_file_label.place(x=745, y=275)

    #Creating Listbox with all saved drafts
    global saved_timesheetframe
    saved_timesheetframe = Frame(window)
    saved_timesheetscrollbar = Scrollbar(saved_timesheetframe, orient=VERTICAL)
    global saved_timesheetlistbox
    saved_timesheetlistbox = Listbox(saved_timesheetframe, yscrollcommand=saved_timesheetscrollbar.set, width=50)
    saved_timesheetscrollbar.config(command=saved_timesheetlistbox.yview)
    saved_timesheetscrollbar.pack(side=RIGHT, fill=Y)
    saved_timesheetframe.place(x=745, y=300)
    saved_timesheetlistbox.pack()
    for saved_draft in saveddrafts:
        saved_draft_string = str(saved_draft)
        saved_draft1 = saved_draft_string.replace("(", "")
        saved_draft2 = saved_draft1.replace(")", "")
        saved_draft3 = saved_draft2.replace("'", "")
        saved_draft4 = saved_draft3.replace(",", "")
        saved_timesheetlistbox.insert(0, saved_draft4)

    global select_saved_timesheet
    select_saved_timesheet = Button(window, text="Select", command=saved_timesheetselect)
    select_saved_timesheet.place(x=880, y=470)

    global close_save_select
    close_save_select = Button(window, text="Close", command=close_savedtimesheetselect)
    close_save_select.place(x=880, y=505)

def current_week_reset():
    #making Calendar on screen function
    today = datetime.date.today()

    idx = (today.weekday() + 1) % 7

    sun = today - datetime.timedelta(idx)

    global start_date_mode
    year = int(sun.strftime("%Y"))
    month = int(sun.strftime("%m"))
    day = int(sun.strftime("%d"))
    start_date_mode = datetime.datetime(year=year, month=month, day=day)
    timesheet_datetime()

def close_week_select():
    week_select_calendar.destroy()
    week_select_instructions.destroy()
    week_select_button.destroy()
    currentweekreset.destroy()
    closeweekselect.destroy()

def week_select():
    date_selected = week_select_calendar.get_date()
    if len(date_selected) == 6:
        month_selected = int(date_selected[0])
        day_selected = int(date_selected[2])
        year_selected_string= "20" + date_selected[4] + date_selected[5]
        year_selected = int(year_selected_string)

    if len(date_selected) == 7:
        month_selected = int(date_selected[0])
        day_selected = int(date_selected[2] + date_selected[3])
        year_selected_string= "20" + date_selected[5] + date_selected[6]
        year_selected = int(year_selected_string)

    global start_date_mode
    start_date_mode = datetime.datetime(year=year_selected, month=month_selected, day=day_selected)
    timesheet_datetime()

def change_week():
    #Visually clearing Screen
    clear_bottom_session()

    #Creating calendar to select week of choice
    global week_select_calendar
    week_select_calendar = Calendar(window, selectmode="day", year=2020, firstweekday="sunday")
    week_select_calendar.place(x=745, y=300)

    global week_select_instructions
    week_select_instructions= Label(window, text = "Select the week you would like to change the timesheet to.", bg="white", font="none 10")
    week_select_instructions.place(x=680, y=275)

    global week_select_button
    week_select_button = Button(window, text="Select", command=week_select)
    week_select_button.place(x=850, y=500)

    global currentweekreset
    currentweekreset = Button(window, text = "Reset to Current Week", command=current_week_reset)
    currentweekreset.place(x=807, y=540)

    global closeweekselect
    closeweekselect = Button(window, text= "Close Week Select", command=close_week_select)
    closeweekselect.place(x=815, y=580)

def save_timesheet():
    saved_sessiondatawrite()
    hourtype_listbox.config(background="light gray")
    hoursentry1.config(background="light gray")
    hoursentry2.config(background="light gray")
    hoursentry3.config(background="light gray")
    hoursentry4.config(background="light gray")
    hoursentry5.config(background="light gray")
    hoursentry6.config(background="light gray")
    hoursentry7.config(background="light gray")
    hoursentrynotes.config(background="light gray")




def lock_timesheet():
    session_datawrite()
    hourtype_listbox.config(background="light gray")
    hoursentry1.config(background="light gray")
    hoursentry2.config(background="light gray")
    hoursentry3.config(background="light gray")
    hoursentry4.config(background="light gray")
    hoursentry5.config(background="light gray")
    hoursentry6.config(background="light gray")
    hoursentry7.config(background="light gray")
    hoursentrynotes.config(background="light gray")

    locked_label.place(x=485, y=225)

def viewtimesheetdata():
    clear_screen()

    Label(window, text=nameinfo + "\'s Timesheet Data", bg="white", font="none 20 bold") .pack(pady=10)

    Button(window, text="Return to Dashboard", command=session) .place(x=200, y=50)

    treeviewframe = Frame(window, width=100)
    treeviewframe.pack(pady=15)

    #Treeview
    global timesheet
    timesheet = ttk.Treeview(treeviewframe)
    timesheet['columns'] = ("week", "hourtype", "sun", "mon", "tue", "wed", "thu", "fri", "sat", "notes", "approvalstatus")
    timesheet.pack()

    timesheet.heading("#0", text="", anchor="w")

    timesheet.column("#0",anchor="center", width=5, stretch=NO)

    timesheet.heading("week", text="Week", anchor="w")

    timesheet.column("week", anchor="w", width=80)

    timesheet.heading("hourtype", text="Hourtype", anchor="w")

    timesheet.column("hourtype", anchor="w", width=80)

    timesheet.heading("sun", text="Sunday", anchor="w")

    timesheet.column("sun", anchor="w", width=80)

    timesheet.heading("mon", text="Monday", anchor="w")

    timesheet.column("mon", anchor="w", width=80)

    timesheet.heading("tue", text="Tuesday", anchor="w")

    timesheet.column("tue", anchor="w", width=80)

    timesheet.heading("wed", text="Wednesday", anchor="w")

    timesheet.column("wed", anchor="w", width=80)

    timesheet.heading("thu", text="Thursday", anchor="w")

    timesheet.column("thu", anchor="w", width=80)

    timesheet.heading("fri", text="Friday", anchor="w")

    timesheet.column("fri", anchor="w", width=80)

    timesheet.heading("sat", text="Saturday", anchor="w")

    timesheet.column("sat", anchor="w", width=80)

    timesheet.heading("notes", text="Notes", anchor="w")

    timesheet.column("notes", anchor="w", width=200)

    timesheet.heading("approvalstatus", text="Status", anchor="w")

    timesheet.column("approvalstatus", anchor="w", width=80)

    get_timesheets = "SELECT timesheet FROM " + nameinfo1 + "_timesheetdata"
    cursor.execute(get_timesheets)
    all_timesheets = cursor.fetchall()

    for timesheet_got in all_timesheets:
        get_startdate = "SELECT day1 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"
        cursor.execute(get_startdate, timesheet_got)
        startdate = cursor.fetchall()
        startdate_string = str(startdate)
        startdate1 = startdate_string.replace("[", "")
        startdate2 = startdate1.replace("]", "")
        startdate3 = startdate2.replace("(", "")
        startdate4 = startdate3.replace(")", "")
        startdate5 = startdate4.replace("'", "")
        startdate6 = startdate5.replace(",", "")
        startdate7 = startdate6.replace("-", "/")
        print(startdate7[0:5])

        get_enddate = "SELECT day7 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"
        cursor.execute(get_enddate, timesheet_got)
        enddate = cursor.fetchall()
        enddate_string = str(enddate)
        enddate1 = enddate_string.replace("[", "")
        enddate2 = enddate1.replace("]", "")
        enddate3 = enddate2.replace("(", "")
        enddate4 = enddate3.replace(")", "")
        enddate5 = enddate4.replace("'", "")
        enddate6 = enddate5.replace(",", "")
        enddate7 = enddate6.replace("-", "/")
        print(enddate7[0:5])

        #getting the saved hourtype
        get_hourtype = "SELECT hourtype_selected FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(get_hourtype, timesheet_got)
        hourtype = cursor.fetchall()

        hourtype_string = str(hourtype)
        hourtype1 = hourtype_string.replace("[", "")
        hourtype2 = hourtype1.replace("]", "")
        hourtype3 = hourtype2.replace("(", "")
        hourtype4 = hourtype3.replace(")", "")
        hourtype5 = hourtype4.replace("'", "")
        hourtype_final = hourtype5.replace(",", "")

        #getting day1 hours saved
        day1_get = "SELECT day1 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day1_get, timesheet_got)
        day1 = cursor.fetchall()

        day1_string = str(day1)
        day1_1 = day1_string.replace("[", "")
        day1_2 = day1_1.replace("]", "")
        day1_3 = day1_2.replace("(", "")
        day1_4 = day1_3.replace(")", "")
        day1_5 = day1_4.replace("'", "")
        day1_final = day1_5.replace(",", "")

        #getting day2 hours saved
        day2_get = "SELECT day2 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day2_get, timesheet_got)
        day2 = cursor.fetchall()

        day2_string = str(day2)
        day2_1 = day2_string.replace("[", "")
        day2_2 = day2_1.replace("]", "")
        day2_3 = day2_2.replace("(", "")
        day2_4 = day2_3.replace(")", "")
        day2_5 = day2_4.replace("'", "")
        day2_final = day2_5.replace(",", "")

        #getting day3 hours saved
        day3_get = "SELECT day3 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day3_get, timesheet_got)
        day3 = cursor.fetchall()

        day3_string = str(day3)
        day3_1 = day3_string.replace("[", "")
        day3_2 = day3_1.replace("]", "")
        day3_3 = day3_2.replace("(", "")
        day3_4 = day3_3.replace(")", "")
        day3_5 = day3_4.replace("'", "")
        day3_final = day3_5.replace(",", "")

        #getting day4 hours saved
        day4_get = "SELECT day4 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day4_get, timesheet_got)
        day4 = cursor.fetchall()

        day4_string = str(day4)
        day4_1 = day4_string.replace("[", "")
        day4_2 = day4_1.replace("]", "")
        day4_3 = day4_2.replace("(", "")
        day4_4 = day4_3.replace(")", "")
        day4_5 = day4_4.replace("'", "")
        day4_final = day4_5.replace(",", "")

        #getting day5 hours saved
        day5_get = "SELECT day5 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day5_get, timesheet_got)
        day5 = cursor.fetchall()

        day5_string = str(day5)
        day5_1 = day5_string.replace("[", "")
        day5_2 = day5_1.replace("]", "")
        day5_3 = day5_2.replace("(", "")
        day5_4 = day5_3.replace(")", "")
        day5_5 = day5_4.replace("'", "")
        day5_final = day5_5.replace(",", "")

        #getting day6 hours saved
        day6_get = "SELECT day6 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day6_get, timesheet_got)
        day6 = cursor.fetchall()

        day6_string = str(day6)
        day6_1 = day6_string.replace("[", "")
        day6_2 = day6_1.replace("]", "")
        day6_3 = day6_2.replace("(", "")
        day6_4 = day6_3.replace(")", "")
        day6_5 = day6_4.replace("'", "")
        day6_final = day6_5.replace(",", "")

        #getting day7 hours_saved
        day7_get = "SELECT day7 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day7_get, timesheet_got)
        day7 = cursor.fetchall()

        day7_string = str(day7)
        day7_1 = day7_string.replace("[", "")
        day7_2 = day7_1.replace("]", "")
        day7_3 = day7_2.replace("(", "")
        day7_4 = day7_3.replace(")", "")
        day7_5 = day7_4.replace("'", "")
        day7_final = day7_5.replace(",", "")

        #getting notes that were saved
        notes_get = "SELECT notes FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(notes_get, timesheet_got)
        notes = cursor.fetchall()

        notes_string = str(notes)
        notes_1 = notes_string.replace("[", "")
        notes_2 = notes_1.replace("]", "")
        notes_3 = notes_2.replace("(", "")
        notes_4 = notes_3.replace(")", "")
        notes_5 = notes_4.replace("'", "")
        notes_final = notes_5.replace(",", "")

        #Getting approval Status
        approvalstatus_get = "SELECT approval_status FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(approvalstatus_get, timesheet_got)
        approvalstatus = cursor.fetchall()

        approvalstatus_string = str(approvalstatus)
        approvalstatus_1 = approvalstatus_string.replace("[", "")
        approvalstatus_2 = approvalstatus_1.replace("]", "")
        approvalstatus_3 = approvalstatus_2.replace("(", "")
        approvalstatus_4 = approvalstatus_3.replace(")", "")
        approvalstatus_5 = approvalstatus_4.replace("'", "")
        approvalstatus_final = approvalstatus_5.replace(",", "")

        timesheet.insert("", 'end', values = (startdate7[0:5] + "-" + enddate7[0:5], hourtype_final, day1_final[7:8], day2_final[7:8], day3_final[7:8], day4_final[7:8], day5_final[7:8], day6_final[7:8], day7_final[7:8], notes_final, approvalstatus_final))

def clear_bottom_session():
    hourtype_listbox.config(background="white")
    hoursentry1.config(background="white")
    hoursentry2.config(background="white")
    hoursentry3.config(background="white")
    hoursentry4.config(background="white")
    hoursentry5.config(background="white")
    hoursentry6.config(background="white")
    hoursentry7.config(background="white")
    hoursentrynotes.config(background="white")

    saved_label.config(text = ' ')
    locked_label.config(text = ' ')

    try:
        select_save_file_label.destroy()
        saved_timesheetframe.destroy()
        select_saved_timesheet.destroy()
        close_save_select.destroy()

    except:
        print(" ")

    try:
        week_select_calendar.destroy()
        week_select_instructions.destroy()
        week_select_button.destroy()
        currentweekreset.destroy()
        closeweekselect.destroy()

    except:
        print(" ")

def session():
    clear_screen()

    global sessioninfo1
    global nameinfo
    global nameinfo1

    window.title("Dashboard")
    Label (window, image=logo, bg="white", justify="left") .pack()

    #Opening Database to get user's name

    get_name = "SELECT name FROM userinfo WHERE username = %s"
    username = (username1,)

    cursor.execute(get_name, username)

    name = cursor.fetchall()

    for result in name:
        name_string = str(result)
        name_label = name_string.replace("'", "")
        name_label1 = name_label.replace("(", "")
        name_label2 = name_label1.replace(")", "")
        name_label3 = name_label2.replace(",", "")

    nameinfo = name_label3
    nameinfo1 = name_label3.replace(" ", "")


    Label(window, text = name_label3 + "\'s Timesheet", bg="white", font="none 20 bold") .pack()

    #making Calendar on screen function
    today = datetime.date.today()

    idx = (today.weekday() + 1) % 7

    sun = today - datetime.timedelta(idx)

    global start_date_mode
    year = int(sun.strftime("%Y"))
    month = int(sun.strftime("%m"))
    day = int(sun.strftime("%d"))
    start_date_mode = datetime.datetime(year=year, month=month, day=day)
    timesheet_datetime()

    global logoutbutton
    logoutbutton = Button(window, text="Log Out", width=20, height=1, command=logout)
    logoutbutton.place(x=1300, y=75)
    Label(window, text=" ", bg="white") .pack()

    Label(window, text="Hourtype Select", bg="white", font="none 12 bold") .place(x=325, y=125)
    hourtype_frame = Frame(window)
    hourtype_scrollbar = Scrollbar(hourtype_frame, orient=VERTICAL)
    global hourtype_listbox
    global hourtype_list
    hourtype_listbox = Listbox(hourtype_frame, yscrollcommand=hourtype_scrollbar.set)
    hourtype_scrollbar.config(command=hourtype_listbox.yview)
    hourtype_scrollbar.pack(side=RIGHT, fill=Y)
    hourtype_frame.place(x=325, y=150)
    hourtype_listbox.pack()
    hourtype_list = ["Standard", "Double", "Overtime", "Other"]
    for hourtype in hourtype_list:
        hourtype_listbox.insert(END, hourtype)
    Button(window, text="Select", command=hourtype_select) .place(x=365, y=325)
    global hourtype_label
    hourtype_label = Label(window, text='', bg="white", fg="green", font="none 12 bold")
    hourtype_label.place(x=300, y=325)

    global hoursentrydata1
    global hoursentry1
    hoursentrydata1 = StringVar()

    hoursentry1 = Entry(window, textvariable = hoursentrydata1, width=5)
    hoursentry1.place(x=500, y=150)

    global hoursentrydata2
    global hoursentry2
    hoursentrydata2 = StringVar()
    hoursentry2 = Entry(window, textvariable = hoursentrydata2, width=5)
    hoursentry2.place(x=575, y=150)

    global hoursentrydata3
    global hoursentry3
    hoursentrydata3 = StringVar()
    hoursentry3 = Entry(window, textvariable = hoursentrydata3, width=5)
    hoursentry3.place(x=650, y=150)

    global hoursentrydata4
    global hoursentry4
    hoursentrydata4 = StringVar()
    hoursentry4 = Entry(window, textvariable = hoursentrydata4, width=5)
    hoursentry4.place(x=725, y=150)

    global hoursentrydata5
    global hoursentry5
    hoursentrydata5 = StringVar()
    hoursentry5 = Entry(window, textvariable = hoursentrydata5, width=5)
    hoursentry5.place(x=800, y=150)

    global hoursentrydata6
    global hoursentry6
    hoursentrydata6 = StringVar()
    hoursentry6 = Entry(window, textvariable = hoursentrydata6, width=5)
    hoursentry6.place(x=875, y=150)

    global hoursentrydata7
    global hoursentry7
    hoursentrydata7 = StringVar()
    hoursentry7 = Entry(window, textvariable = hoursentrydata7, width=5)
    hoursentry7.place(x=950, y=150)

    global hoursentry_notes
    global hoursentrynotes
    hoursentry_notes = StringVar()
    Label(window, text="Notes", bg="white", fg="black", font="none 12 bold") .place(x=1020, y=125)
    hoursentrynotes = Entry(window, textvariable = hoursentry_notes, width=20)
    hoursentrynotes.place(x=1025, y=150)

    open_savedtimesheet = Button(window, text="Open Saved Timesheet", command=open_saved_timesheet)  .place(x=325, y=75)

    changeweek = Button(window, text="Change Week", command=change_week) .place(x=500, y=75)

    savetimesheet = Button(window, text = "Save Timesheet", command = save_timesheet) .place(x=1175, y=150)

    locktimesheet = Button(window, text="Lock Timesheet", command = lock_timesheet) .place(x=1275, y=150)

    Button(window, text="Timesheet Queue", command=userviewtimesheet) .place(x=1375, y=150)

    Button(window, text="Timesheet Data", command = viewtimesheetdata) .place(x=1485, y=150)


    global saved_label
    saved_label = Label(window, text = " ", bg="white", font="none 12 bold")
    saved_label.place(x=485, y=200)

    global locked_label
    locked_label = Label(window, text = " ", bg="white", font="none 12 bold")
    locked_label.place(x=485, y=225)

def edit_rejectedtimesheet():
    #getting the rejected hourtype
    hourtype_get = "SELECT hourtype_selected FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(hourtype_get, rejected_timesheetselected)
    rejected_hourtype = cursor.fetchall()

    rejected_hourtype_string = str(rejected_hourtype)
    rejected_hourtype1 = rejected_hourtype_string.replace("[", "")
    rejected_hourtype2 = rejected_hourtype1.replace("]", "")
    rejected_hourtype3 = rejected_hourtype2.replace("(", "")
    rejected_hourtype4 = rejected_hourtype3.replace(")", "")
    rejected_hourtype5 = rejected_hourtype4.replace("'", "")
    rejected_hourtype_final = rejected_hourtype5.replace(",", "")

    #getting day1 hours rejected
    day1_get = "SELECT day1 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day1_get, rejected_timesheetselected)
    rejected_day1 = cursor.fetchall()

    rejected_day1_string = str(rejected_day1)
    rejected_day1_1 = rejected_day1_string.replace("[", "")
    rejected_day1_2 = rejected_day1_1.replace("]", "")
    rejected_day1_3 = rejected_day1_2.replace("(", "")
    rejected_day1_4 = rejected_day1_3.replace(")", "")
    rejected_day1_5 = rejected_day1_4.replace("'", "")
    rejected_day1_final = rejected_day1_5.replace(",", "")

    #getting day2 hours rejected
    day2_get = "SELECT day2 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day2_get, rejected_timesheetselected)
    rejected_day2 = cursor.fetchall()

    rejected_day2_string = str(rejected_day2)
    rejected_day2_1 = rejected_day2_string.replace("[", "")
    rejected_day2_2 = rejected_day2_1.replace("]", "")
    rejected_day2_3 = rejected_day2_2.replace("(", "")
    rejected_day2_4 = rejected_day2_3.replace(")", "")
    rejected_day2_5 = rejected_day2_4.replace("'", "")
    rejected_day2_final = rejected_day2_5.replace(",", "")

    #getting day3 hours rejected
    day3_get = "SELECT day3 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day3_get, rejected_timesheetselected)
    rejected_day3 = cursor.fetchall()

    rejected_day3_string = str(rejected_day3)
    rejected_day3_1 = rejected_day3_string.replace("[", "")
    rejected_day3_2 = rejected_day3_1.replace("]", "")
    rejected_day3_3 = rejected_day3_2.replace("(", "")
    rejected_day3_4 = rejected_day3_3.replace(")", "")
    rejected_day3_5 = rejected_day3_4.replace("'", "")
    rejected_day3_final = rejected_day3_5.replace(",", "")

    #getting day4 hours rejected
    day4_get = "SELECT day4 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day4_get, rejected_timesheetselected)
    rejected_day4 = cursor.fetchall()

    rejected_day4_string = str(rejected_day4)
    rejected_day4_1 = rejected_day4_string.replace("[", "")
    rejected_day4_2 = rejected_day4_1.replace("]", "")
    rejected_day4_3 = rejected_day4_2.replace("(", "")
    rejected_day4_4 = rejected_day4_3.replace(")", "")
    rejected_day4_5 = rejected_day4_4.replace("'", "")
    rejected_day4_final = rejected_day4_5.replace(",", "")

    #getting day5 hours rejected
    day5_get = "SELECT day5 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day5_get, rejected_timesheetselected)
    rejected_day5 = cursor.fetchall()

    rejected_day5_string = str(rejected_day5)
    rejected_day5_1 = rejected_day5_string.replace("[", "")
    rejected_day5_2 = rejected_day5_1.replace("]", "")
    rejected_day5_3 = rejected_day5_2.replace("(", "")
    rejected_day5_4 = rejected_day5_3.replace(")", "")
    rejected_day5_5 = rejected_day5_4.replace("'", "")
    rejected_day5_final = rejected_day5_5.replace(",", "")

    #getting day6 hours rejected
    day6_get = "SELECT day6 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day6_get, rejected_timesheetselected)
    rejected_day6 = cursor.fetchall()

    rejected_day6_string = str(rejected_day6)
    rejected_day6_1 = rejected_day6_string.replace("[", "")
    rejected_day6_2 = rejected_day6_1.replace("]", "")
    rejected_day6_3 = rejected_day6_2.replace("(", "")
    rejected_day6_4 = rejected_day6_3.replace(")", "")
    rejected_day6_5 = rejected_day6_4.replace("'", "")
    rejected_day6_final = rejected_day6_5.replace(",", "")

    #getting day7 hours_rejected
    day7_get = "SELECT day7 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(day7_get, rejected_timesheetselected)
    rejected_day7 = cursor.fetchall()

    rejected_day7_string = str(rejected_day7)
    rejected_day7_1 = rejected_day7_string.replace("[", "")
    rejected_day7_2 = rejected_day7_1.replace("]", "")
    rejected_day7_3 = rejected_day7_2.replace("(", "")
    rejected_day7_4 = rejected_day7_3.replace(")", "")
    rejected_day7_5 = rejected_day7_4.replace("'", "")
    rejected_day7_final = rejected_day7_5.replace(",", "")

    #getting notes that were rejected
    notes_get = "SELECT notes FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

    cursor.execute(notes_get, rejected_timesheetselected)
    rejected_notes = cursor.fetchall()

    rejected_notes_string = str(rejected_notes)
    rejected_notes_1 = rejected_notes_string.replace("[", "")
    rejected_notes_2 = rejected_notes_1.replace("]", "")
    rejected_notes_3 = rejected_notes_2.replace("(", "")
    rejected_notes_4 = rejected_notes_3.replace(")", "")
    rejected_notes_5 = rejected_notes_4.replace("'", "")
    rejected_notes_final = rejected_notes_5.replace(",", "")

    rejected_hourtype_label.config(text="HOURTYPE SELECTED:\n" + rejected_hourtype_final)
    Button(window, text="Change", command=rejected_hourtype_select) .place(x=365, y=370)

    rejected_hoursentry1.insert(END, rejected_day1_final[7:8])
    rejected_hoursentry2.insert(END, rejected_day2_final[7:8])
    rejected_hoursentry3.insert(END, rejected_day3_final[7:8])
    rejected_hoursentry4.insert(END, rejected_day4_final[7:8])
    rejected_hoursentry5.insert(END, rejected_day5_final[7:8])
    rejected_hoursentry6.insert(END, rejected_day6_final[7:8])
    rejected_hoursentry7.insert(END, rejected_day7_final[7:8])
    rejected_hoursentrynotes.insert(END, rejected_notes_final)

    global rejected_hourtype_selected
    rejected_hourtype_selected = rejected_hourtype_final

def approvetimesheet():

    approve_timesheet = "UPDATE " + userselected1 + "_timesheetdata SET approval_status = 'Approved' WHERE timesheet = %s"

    cursor.execute(approve_timesheet, timesheetselected)

    w_t_db.commit()

    get_email = "SELECT email FROM userinfo WHERE name = %s"

    cursor.execute(get_email, user_selected)

    email = cursor.fetchall()

    email_string = str(email)
    email1 = email_string.replace("[", "")
    email2 = email1.replace("]", "")
    email3 = email2.replace("(", "")
    email4 = email3.replace(")", "")
    email5 = email4.replace("'", "")
    email_final = email5.replace(",", "")

    #Sending an email notifying the user that the timesheet has been approved
    sender_email = "timesheettestemail@gmail.com"
    rec_email = email_final
    email_password = "worldscapetest1"
    msg = MIMEText('Dear ' + userselected + """, \n \n
    Your timesheet """ + usertimesheet_listbox.get(ANCHOR) + """ has been approved by a manager.\n
    If you have any questions or concerns about this approval, contact a manager or administrator. \n
    Sincerely, \n
    The Worldscape Timesheet Application Development Team""")
    msg['Subject'] = 'Worldscape Timesheet Approved'
    msg['From'] = 'timesheettestemail@gmail.com'
    msg['To'] = email_final

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, email_password)
    print("Login Success")
    server.sendmail(sender_email, rec_email, msg.as_string())
    print("Email has been sent to " + rec_email)

    server.quit()

    approvalstatus.config(text="You have approved " + userselected+ "\'s timesheet", bg="white", fg="green", font="none 12 bold")


def rejecttimesheet():

    reject_timesheet = "UPDATE " + userselected1 + "_timesheetdata SET approval_status = 'Rejected' WHERE timesheet = %s"

    cursor.execute(reject_timesheet, timesheetselected)

    w_t_db.commit()

    get_email = "SELECT email FROM userinfo WHERE name = %s"

    cursor.execute(get_email, user_selected)

    email = cursor.fetchall()

    email_string = str(email)
    email1 = email_string.replace("[", "")
    email2 = email1.replace("]", "")
    email3 = email2.replace("(", "")
    email4 = email3.replace(")", "")
    email5 = email4.replace("'", "")
    email_final = email5.replace(",", "")

    #Sending an email notifying the user that the timesheet has been approved
    sender_email = "timesheettestemail@gmail.com"
    rec_email = email_final
    email_password = "worldscapetest1"
    msg = MIMEText('Dear ' + userselected + """, \n \n
    Your timesheet """ + usertimesheet_listbox.get(ANCHOR) + """ has been rejected by a manager.\n
    It can be edited and resubmitted by selecting it in the \'View Previous Timesheets\' section of the application. \n
    If you have any questions or concerns about this rejection, contact a manager or administrator. \n
    Sincerely, \n
    The Worldscape Timesheet Application Development Team""")
    msg['Subject'] = 'Worldscape Timesheet Rejected'
    msg['From'] = 'timesheettestemail@gmail.com'
    msg['To'] = email_final

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, email_password)
    print("Login Success")
    server.sendmail(sender_email, rec_email, msg.as_string())
    print("Email has been sent to " + rec_email)

    server.quit()

    approvalstatus.config(text="You have rejected " + userselected + "\'s timesheet", bg="white", fg="red", font="none 12 bold")

def current_timesheet_destroy():
    try:
        title.destroy()
        manager_hourtypeselectedlabel.destroy()
        day1_label.destroy()
        day2_label.destroy()
        day3_label.destroy()
        day4_label.destroy()
        day5_label.destroy()
        day6_label.destroy()
        day7_label.destroy()
        manager_noteslabel.destroy()
        approvalstatus.destroy()
        approvebutton.destroy()
        rejectbutton.destroy()

    except:
        print(" ")
def viewselectedtimesheet():
        current_timesheet_destroy()

        global timesheetselected
        timesheetselected = (usertimesheet_listbox.get(ANCHOR),)

        #getting the saved hourtype
        hourtype_get = "SELECT hourtype_selected FROM " + userselected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(hourtype_get, timesheetselected)
        hourtype = cursor.fetchall()

        hourtype_string = str(hourtype)
        hourtype1 = hourtype_string.replace("[", "")
        hourtype2 = hourtype1.replace("]", "")
        hourtype3 = hourtype2.replace("(", "")
        hourtype4 = hourtype3.replace(")", "")
        hourtype5 = hourtype4.replace("'", "")
        hourtype_final = hourtype5.replace(",", "")

        #getting day1 hours saved
        day1_get = "SELECT day1 FROM " + userselected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day1_get, timesheetselected)
        day1 = cursor.fetchall()

        day1_string = str(day1)
        day1_1 = day1_string.replace("[", "")
        day1_2 = day1_1.replace("]", "")
        day1_3 = day1_2.replace("(", "")
        day1_4 = day1_3.replace(")", "")
        day1_5 = day1_4.replace("'", "")
        day1_final = day1_5.replace(",", "")

        #getting day2 hours saved
        day2_get = "SELECT day2 FROM " + userselected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day2_get, timesheetselected)
        day2 = cursor.fetchall()

        day2_string = str(day2)
        day2_1 = day2_string.replace("[", "")
        day2_2 = day2_1.replace("]", "")
        day2_3 = day2_2.replace("(", "")
        day2_4 = day2_3.replace(")", "")
        day2_5 = day2_4.replace("'", "")
        day2_final = day2_5.replace(",", "")

        #getting day3 hours saved
        day3_get = "SELECT day3 FROM " + userselected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day3_get, timesheetselected)
        day3 = cursor.fetchall()

        day3_string = str(day3)
        day3_1 = day3_string.replace("[", "")
        day3_2 = day3_1.replace("]", "")
        day3_3 = day3_2.replace("(", "")
        day3_4 = day3_3.replace(")", "")
        day3_5 = day3_4.replace("'", "")
        day3_final = day3_5.replace(",", "")

        #getting day4 hours saved
        day4_get = "SELECT day4 FROM " + userselected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day4_get, timesheetselected)
        day4 = cursor.fetchall()

        day4_string = str(day4)
        day4_1 = day4_string.replace("[", "")
        day4_2 = day4_1.replace("]", "")
        day4_3 = day4_2.replace("(", "")
        day4_4 = day4_3.replace(")", "")
        day4_5 = day4_4.replace("'", "")
        day4_final = day4_5.replace(",", "")

        #getting day5 hours saved
        day5_get = "SELECT day5 FROM " + userselected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day5_get, timesheetselected)
        day5 = cursor.fetchall()

        day5_string = str(day5)
        day5_1 = day5_string.replace("[", "")
        day5_2 = day5_1.replace("]", "")
        day5_3 = day5_2.replace("(", "")
        day5_4 = day5_3.replace(")", "")
        day5_5 = day5_4.replace("'", "")
        day5_final = day5_5.replace(",", "")

        #getting day6 hours saved
        day6_get = "SELECT day6 FROM " + userselected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day6_get, timesheetselected)
        day6 = cursor.fetchall()

        day6_string = str(day6)
        day6_1 = day6_string.replace("[", "")
        day6_2 = day6_1.replace("]", "")
        day6_3 = day6_2.replace("(", "")
        day6_4 = day6_3.replace(")", "")
        day6_5 = day6_4.replace("'", "")
        day6_final = day6_5.replace(",", "")

        #getting day7 hours_saved
        day7_get = "SELECT day7 FROM " + userselected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day7_get, timesheetselected)
        day7 = cursor.fetchall()

        day7_string = str(day7)
        day7_1 = day7_string.replace("[", "")
        day7_2 = day7_1.replace("]", "")
        day7_3 = day7_2.replace("(", "")
        day7_4 = day7_3.replace(")", "")
        day7_5 = day7_4.replace("'", "")
        day7_final = day7_5.replace(",", "")

        #getting notes that were saved
        notes_get = "SELECT notes FROM " + userselected1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(notes_get, timesheetselected)
        notes = cursor.fetchall()

        notes_string = str(notes)
        notes_1 = notes_string.replace("[", "")
        notes_2 = notes_1.replace("]", "")
        notes_3 = notes_2.replace("(", "")
        notes_4 = notes_3.replace(")", "")
        notes_5 = notes_4.replace("'", "")
        notes_final = notes_5.replace(",", "")

        global title
        title = Label(window, text = userselected + "\'s Timesheet Data", bg="white", font="none 12 bold")
        title.place(x=1075, y=145)

        global manager_hourtypeselectedlabel
        manager_hourtypeselectedlabel = Label(window, text = "Hourtype Selected: " + hourtype_final, bg="white", font="none 12")
        manager_hourtypeselectedlabel.place(x=1075, y=170)

        global day1_label
        day1_label = Label(window, text = day1_final + " hour(s)", bg="white", font="none 12")
        day1_label.place(x=1075, y=200)

        global day2_label
        day2_label = Label(window, text = day2_final + " hour(s)", bg="white", font="none 12")
        day2_label.place(x=1075, y=230)

        global day3_label
        day3_label = Label(window, text = day3_final + " hour(s)", bg="white", font="none 12")
        day3_label.place(x=1075, y=260)

        global day4_label
        day4_label = Label(window, text = day4_final + " hour(s)", bg="white", font="none 12")
        day4_label.place(x=1075, y=290)

        global day5_label
        day5_label = Label(window, text = day5_final + " hour(s)", bg="white", font="none 12")
        day5_label.place(x=1075, y=330)

        global day6_label
        day6_label = Label(window, text = day6_final + " hour(s)", bg="white", font="none 12")
        day6_label.place(x=1075, y=370)

        global day7_label
        day7_label = Label(window, text = day7_final + " hour(s)", bg="white", font="none 12")
        day7_label.place(x=1075, y=410)

        global manager_noteslabel
        manager_noteslabel = Label(window, text = "Notes: " + notes_final, bg="white", font="none 12")
        manager_noteslabel.place(x=1075, y=450)

        global approvalstatus
        approvalstatus = Label(window, text = "Please approve or reject this timesheet.", bg="white", fg="gray", font="none 12 bold")
        approvalstatus.place(x=1075, y=480)

        global approvebutton
        global rejectbutton
        approvebutton = Button(window, text = "Approve", command=approvetimesheet) .place(x=1075, y=510)
        rejectbutton = Button(window, text = "Reject", command=rejecttimesheet) .place(x=1075, y=540)

def viewalltimesheets():
    global user_selected
    user_selected = (user_listbox.get(ANCHOR),)

    global userselected
    userselected = user_listbox.get(ANCHOR)

    #modifying user_selected to be the same as the database name - no spaces
    global userselected1
    userselected1 = userselected.replace(" ", "")

    #opening all timesheets from the user selected in the database
    all_timesheets_select = "SELECT timesheet FROM " + userselected1 + "_timesheetdata WHERE approval_status = 'Queued'"

    cursor.execute(all_timesheets_select)

    all_timesheets = cursor.fetchall()

    #Creating listbox of all timesheets to be selected from
    usertimesheet_frame = Frame(window)
    usertimesheet_scrollbar = Scrollbar(usertimesheet_frame, orient=VERTICAL)
    global usertimesheet_listbox
    usertimesheet_listbox = Listbox(usertimesheet_frame, width=45, yscrollcommand=usertimesheet_scrollbar.set)
    usertimesheet_scrollbar.config(command=usertimesheet_listbox.yview)
    usertimesheet_scrollbar.pack(side=RIGHT, fill=Y)
    usertimesheet_frame.place(x=700, y=150)
    usertimesheet_listbox.pack()

    for usertimesheet in all_timesheets:
        usertimesheet_string = str(usertimesheet)
        usertimesheet_name = usertimesheet_string.replace("'", "")
        usertimesheet_name1 = usertimesheet_name.replace("(", "")
        usertimesheet_name2 = usertimesheet_name1.replace(")", "")
        usertimesheet_name3 = usertimesheet_name2.replace(",", "")
        usertimesheet_listbox.insert(0, usertimesheet_name3)

    Button(window, text="Select", command=viewselectedtimesheet) .place(x=740, y=325)

def approvehours():
    manager_session()

    #Opening Database to get all user names
    get_all_users = "SELECT name FROM userinfo"

    cursor.execute(get_all_users)

    all_users = cursor.fetchall()

    user_frame = Frame(window)
    user_scrollbar = Scrollbar(user_frame, orient=VERTICAL)
    global user_listbox
    global user_list
    user_listbox = Listbox(user_frame, yscrollcommand=user_scrollbar.set)
    user_scrollbar.config(command=user_listbox.yview)
    user_scrollbar.pack(side=RIGHT, fill=Y)
    user_frame.place(x=445, y=150)
    user_listbox.pack()
    for name in all_users:
        name_string = str(name)
        name_label = name_string.replace("'", "")
        name_label1 = name_label.replace("(", "")
        name_label2 = name_label1.replace(")", "")
        name_label3 = name_label2.replace(",", "")
        user_listbox.insert(END, name_label3)

    Button(window, text="View Timesheet(s)", width=20, command=viewalltimesheets) .place(x=440, y=320)

def logout_manager():
    logout()

def close_viewuserdata():
    nameinfolabel.destroy()
    treeviewframe.destroy()
    closebutton.destroy()

def manager_viewuserdata():
    nameinfo = userdetails_listbox.get(ANCHOR)
    nameinfo1 = nameinfo.replace(" ", "")

    global nameinfolabel
    nameinfolabel = Label(window, text=nameinfo + "\'s Timesheet Data", bg="white", font="none 14 bold")
    nameinfolabel.pack(pady=[270,0])

    global treeviewframe
    treeviewframe = Frame(window, width=100)
    treeviewframe.pack()

    #Treeview
    global timesheet
    timesheet = ttk.Treeview(treeviewframe)
    timesheet['columns'] = ("week", "hourtype", "sun", "mon", "tue", "wed", "thu", "fri", "sat", "notes", "approvalstatus")
    timesheet.pack()

    timesheet.heading("#0", text="", anchor="w")

    timesheet.column("#0",anchor="center", width=5, stretch=NO)

    timesheet.heading("week", text="Week", anchor="w")

    timesheet.column("week", anchor="w", width=80)

    timesheet.heading("hourtype", text="Hourtype", anchor="w")

    timesheet.column("hourtype", anchor="w", width=80)

    timesheet.heading("sun", text="Sunday", anchor="w")

    timesheet.column("sun", anchor="w", width=80)

    timesheet.heading("mon", text="Monday", anchor="w")

    timesheet.column("mon", anchor="w", width=80)

    timesheet.heading("tue", text="Tuesday", anchor="w")

    timesheet.column("tue", anchor="w", width=80)

    timesheet.heading("wed", text="Wednesday", anchor="w")

    timesheet.column("wed", anchor="w", width=80)

    timesheet.heading("thu", text="Thursday", anchor="w")

    timesheet.column("thu", anchor="w", width=80)

    timesheet.heading("fri", text="Friday", anchor="w")

    timesheet.column("fri", anchor="w", width=80)

    timesheet.heading("sat", text="Saturday", anchor="w")

    timesheet.column("sat", anchor="w", width=80)

    timesheet.heading("notes", text="Notes", anchor="w")

    timesheet.column("notes", anchor="w", width=200)

    timesheet.heading("approvalstatus", text="Status", anchor="w")

    timesheet.column("approvalstatus", anchor="w", width=80)

    get_timesheets = "SELECT timesheet FROM " + nameinfo1 + "_timesheetdata"
    cursor.execute(get_timesheets)
    all_timesheets = cursor.fetchall()

    global closebutton
    closebutton = Button(window, text="Close", command=close_viewuserdata)
    closebutton.pack(pady=10)

    for timesheet_got in all_timesheets:
        get_startdate = "SELECT day1 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"
        cursor.execute(get_startdate, timesheet_got)
        startdate = cursor.fetchall()
        startdate_string = str(startdate)
        startdate1 = startdate_string.replace("[", "")
        startdate2 = startdate1.replace("]", "")
        startdate3 = startdate2.replace("(", "")
        startdate4 = startdate3.replace(")", "")
        startdate5 = startdate4.replace("'", "")
        startdate6 = startdate5.replace(",", "")
        startdate7 = startdate6.replace("-", "/")
        print(startdate7[0:5])

        get_enddate = "SELECT day7 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"
        cursor.execute(get_enddate, timesheet_got)
        enddate = cursor.fetchall()
        enddate_string = str(enddate)
        enddate1 = enddate_string.replace("[", "")
        enddate2 = enddate1.replace("]", "")
        enddate3 = enddate2.replace("(", "")
        enddate4 = enddate3.replace(")", "")
        enddate5 = enddate4.replace("'", "")
        enddate6 = enddate5.replace(",", "")
        enddate7 = enddate6.replace("-", "/")
        print(enddate7[0:5])

        #getting the saved hourtype
        get_hourtype = "SELECT hourtype_selected FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(get_hourtype, timesheet_got)
        hourtype = cursor.fetchall()

        hourtype_string = str(hourtype)
        hourtype1 = hourtype_string.replace("[", "")
        hourtype2 = hourtype1.replace("]", "")
        hourtype3 = hourtype2.replace("(", "")
        hourtype4 = hourtype3.replace(")", "")
        hourtype5 = hourtype4.replace("'", "")
        hourtype_final = hourtype5.replace(",", "")

        #getting day1 hours saved
        day1_get = "SELECT day1 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day1_get, timesheet_got)
        day1 = cursor.fetchall()

        day1_string = str(day1)
        day1_1 = day1_string.replace("[", "")
        day1_2 = day1_1.replace("]", "")
        day1_3 = day1_2.replace("(", "")
        day1_4 = day1_3.replace(")", "")
        day1_5 = day1_4.replace("'", "")
        day1_final = day1_5.replace(",", "")

        #getting day2 hours saved
        day2_get = "SELECT day2 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day2_get, timesheet_got)
        day2 = cursor.fetchall()

        day2_string = str(day2)
        day2_1 = day2_string.replace("[", "")
        day2_2 = day2_1.replace("]", "")
        day2_3 = day2_2.replace("(", "")
        day2_4 = day2_3.replace(")", "")
        day2_5 = day2_4.replace("'", "")
        day2_final = day2_5.replace(",", "")

        #getting day3 hours saved
        day3_get = "SELECT day3 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day3_get, timesheet_got)
        day3 = cursor.fetchall()

        day3_string = str(day3)
        day3_1 = day3_string.replace("[", "")
        day3_2 = day3_1.replace("]", "")
        day3_3 = day3_2.replace("(", "")
        day3_4 = day3_3.replace(")", "")
        day3_5 = day3_4.replace("'", "")
        day3_final = day3_5.replace(",", "")

        #getting day4 hours saved
        day4_get = "SELECT day4 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day4_get, timesheet_got)
        day4 = cursor.fetchall()

        day4_string = str(day4)
        day4_1 = day4_string.replace("[", "")
        day4_2 = day4_1.replace("]", "")
        day4_3 = day4_2.replace("(", "")
        day4_4 = day4_3.replace(")", "")
        day4_5 = day4_4.replace("'", "")
        day4_final = day4_5.replace(",", "")

        #getting day5 hours saved
        day5_get = "SELECT day5 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day5_get, timesheet_got)
        day5 = cursor.fetchall()

        day5_string = str(day5)
        day5_1 = day5_string.replace("[", "")
        day5_2 = day5_1.replace("]", "")
        day5_3 = day5_2.replace("(", "")
        day5_4 = day5_3.replace(")", "")
        day5_5 = day5_4.replace("'", "")
        day5_final = day5_5.replace(",", "")

        #getting day6 hours saved
        day6_get = "SELECT day6 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day6_get, timesheet_got)
        day6 = cursor.fetchall()

        day6_string = str(day6)
        day6_1 = day6_string.replace("[", "")
        day6_2 = day6_1.replace("]", "")
        day6_3 = day6_2.replace("(", "")
        day6_4 = day6_3.replace(")", "")
        day6_5 = day6_4.replace("'", "")
        day6_final = day6_5.replace(",", "")

        #getting day7 hours_saved
        day7_get = "SELECT day7 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day7_get, timesheet_got)
        day7 = cursor.fetchall()

        day7_string = str(day7)
        day7_1 = day7_string.replace("[", "")
        day7_2 = day7_1.replace("]", "")
        day7_3 = day7_2.replace("(", "")
        day7_4 = day7_3.replace(")", "")
        day7_5 = day7_4.replace("'", "")
        day7_final = day7_5.replace(",", "")

        #getting notes that were saved
        notes_get = "SELECT notes FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(notes_get, timesheet_got)
        notes = cursor.fetchall()

        notes_string = str(notes)
        notes_1 = notes_string.replace("[", "")
        notes_2 = notes_1.replace("]", "")
        notes_3 = notes_2.replace("(", "")
        notes_4 = notes_3.replace(")", "")
        notes_5 = notes_4.replace("'", "")
        notes_final = notes_5.replace(",", "")

        #Getting approval Status
        approvalstatus_get = "SELECT approval_status FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(approvalstatus_get, timesheet_got)
        approvalstatus = cursor.fetchall()

        approvalstatus_string = str(approvalstatus)
        approvalstatus_1 = approvalstatus_string.replace("[", "")
        approvalstatus_2 = approvalstatus_1.replace("]", "")
        approvalstatus_3 = approvalstatus_2.replace("(", "")
        approvalstatus_4 = approvalstatus_3.replace(")", "")
        approvalstatus_5 = approvalstatus_4.replace("'", "")
        approvalstatus_final = approvalstatus_5.replace(",", "")

        timesheet.insert("", 'end', values = (startdate7[0:5] + "-" + enddate7[0:5], hourtype_final, day1_final[7:8], day2_final[7:8], day3_final[7:8], day4_final[7:8], day5_final[7:8], day6_final[7:8], day7_final[7:8], notes_final, approvalstatus_final))


def manager_selectuserdetails():
    manager_session()

    #Opening Database to get all user names
    get_all_users = "SELECT name FROM userinfo"

    cursor.execute(get_all_users)

    all_users = cursor.fetchall()

    userdetails_frame = Frame(window)
    userdetails_scrollbar = Scrollbar(userdetails_frame, orient=VERTICAL)
    global userdetails_listbox
    global userdetails_list
    userdetails_listbox = Listbox(userdetails_frame, yscrollcommand=userdetails_scrollbar.set)
    userdetails_scrollbar.config(command=userdetails_listbox.yview)
    userdetails_scrollbar.pack(side=RIGHT, fill=Y)
    userdetails_frame.place(x=845, y=150)
    userdetails_listbox.pack()
    for name in all_users:
        name_string = str(name)
        name_label = name_string.replace("'", "")
        name_label1 = name_label.replace("(", "")
        name_label2 = name_label1.replace(")", "")
        name_label3 = name_label2.replace(",", "")
        userdetails_listbox.insert(END, name_label3)

    Button(window, text="View Data", width=20, command=manager_viewuserdata) .place(x=840, y=320)

def manager_session():
    clear_screen()

    window.title("Manager Dashboard")
    Label (window, image=logo, bg="white", justify="left") .pack()
    Label(window, text="Manager Dashboard", bg="white", font="none 20 bold") .pack()

    Button(window, text="Approve Hours", width=20, command=approvehours) .place(x=440, y=110)


    Button(window, text="View User Data", width=20, command=manager_selectuserdetails) .place(x=840, y=110)

    Button(window, text="Log Out", width=20, height=1, command=logout_manager) .place(x=1240, y=110)

def reject_newuser():
    name_selected = (unregistered_listbox.get(ANCHOR),)

    name_string = str(name_selected)
    name1 = name_string.replace("[", "")
    name2 = name1.replace("]", "")
    name3 = name2.replace("(", "")
    name4 = name3.replace(")", "")
    name5 = name4.replace("'", "")
    name6 = name5.replace(",", "")

    get_email = "SELECT email from userinfo WHERE name = %s"

    cursor.execute(get_email, name_selected)

    email = cursor.fetchall()

    email_string = str(email)
    email1 = email_string.replace("[", "")
    email2 = email1.replace("]", "")
    email3 = email2.replace("(", "")
    email4 = email3.replace(")", "")
    email5 = email4.replace("'", "")
    email_final = email5.replace(",", "")

    sender_email = "timesheettestemail@gmail.com"
    rec_email = email_final
    email_password = "worldscapetest1"
    msg = MIMEText('Dear ' + name6 + """, \n \n
    An administrator has rejected your registration to the Worldscape Timesheet Application. \n
    If you think this was a mistake, please contact a manager or administrator. \n
    Sincerely, \n
    The Worldscape Timesheet Application Development Team""")
    msg['Subject'] = 'Worldscape Timesheet Application Registration Success'
    msg['From'] = 'timesheettestemail@gmail.com'
    msg['To'] = email_final

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, email_password)
    print("Login Success")
    server.sendmail(sender_email, rec_email, msg.as_string())
    print("Email has been sent to " + rec_email)

    server.quit()

    reject_newuser = "DELETE FROM userinfo WHERE name = %s"

    cursor.execute(reject_newuser, name_selected)

    w_t_db.commit()

    registeredlabel.config(text= name6 + " \'s registration has been rejected.", fg="red")

def approve_newuser():
    name_selected = (unregistered_listbox.get(ANCHOR),)

    name_string = str(name_selected)
    name1 = name_string.replace("[", "")
    name2 = name1.replace("]", "")
    name3 = name2.replace("(", "")
    name4 = name3.replace(")", "")
    name5 = name4.replace("'", "")
    name6 = name5.replace(",", "")
    name_final = name6.replace(" ", "")

    approve_newuser = "UPDATE userinfo SET regstatus = 'registered' WHERE name = %s"

    cursor.execute(approve_newuser, name_selected)

    w_t_db.commit()

    #creating a user-specific table that all their timesheet data will be saved
    user_timesheet_table = "CREATE TABLE IF NOT EXISTS " + name_final + "_timesheetdata" + """ (timesheet VARCHAR(255), hourtype_selected VARCHAR(255), day1 VARCHAR(255), day2 VARCHAR(255), day3 VARCHAR(255), day4 VARCHAR(255), day5 VARCHAR(255), day6 VARCHAR(255), day7 VARCHAR(255), notes VARCHAR(255), approval_status VARCHAR(255))"""

    cursor.execute(user_timesheet_table)

    w_t_db.commit()

    #creating a user-specific table that all of their saved draft timesheets will be saved

    user_saveddraft_timesheet_table = "CREATE TABLE IF NOT EXISTS " + name_final + "_saveddrafts" + """ (timesheet VARCHAR(255), hourtype_selected VARCHAR(255), day1 VARCHAR(255), day2 VARCHAR(255), day3 VARCHAR(255), day4 VARCHAR(255), day5 VARCHAR(255), day6 VARCHAR(255), day7 VARCHAR(255), notes VARCHAR(255), approval_status VARCHAR(255))"""

    cursor.execute(user_saveddraft_timesheet_table)

    w_t_db.commit()

    get_email = "SELECT email from userinfo WHERE name = %s"

    cursor.execute(get_email, name_selected)

    email = cursor.fetchall()

    email_string = str(email)
    email1 = email_string.replace("[", "")
    email2 = email1.replace("]", "")
    email3 = email2.replace("(", "")
    email4 = email3.replace(")", "")
    email5 = email4.replace("'", "")
    email_final = email5.replace(",", "")

    sender_email = "timesheettestemail@gmail.com"
    rec_email = email_final
    email_password = "worldscapetest1"
    msg = MIMEText('Dear ' + name6 + """, \n \n
    An administrator has approved your registration to the Worldscape Timesheet Application. \n
    Your account credentials can now be used to log on and report timesheet data. \n
    Notifications will be sent to this email; if you would like, disable them or change the receiving email in the application's settings tab \n
    For any other questions or concerns, please reach out to an administrator. \n
    Sincerely, \n
    The Worldscape Timesheet Application Development Team""")
    msg['Subject'] = 'Worldscape Timesheet Application Registration Success'
    msg['From'] = 'timesheettestemail@gmail.com'
    msg['To'] = email_final

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, email_password)
    print("Login Success")
    server.sendmail(sender_email, rec_email, msg.as_string())
    print("Email has been sent to " + rec_email)

    server.quit()

    registeredlabel.config(text= name6 + " has now been registered.", fg="green")

def close_viewdetails():
    viewdetails_namelabel.destroy()
    viewdetails_namelabel1.destroy()
    viewdetails_emaillabel.destroy()
    viewdetails_emaillabel1.destroy()
    viewdetails_usernamelabel.destroy()
    viewdetails_usernamelabel1.destroy()
    viewdetails_passwordlabel.destroy()
    viewdetails_passwordlabel1.destroy()
    closeviewdetails.destroy()

def view_details():
    name_selected = (unregistered_listbox.get(ANCHOR),)

    name_string = str(name_selected)
    name1 = name_string.replace("[", "")
    name2 = name1.replace("]", "")
    name3 = name2.replace("(", "")
    name4 = name3.replace(")", "")
    name5 = name4.replace("'", "")
    name_final = name5.replace(",", "")

    get_username = "SELECT username from userinfo WHERE name = %s"

    cursor.execute(get_username, name_selected)

    username = cursor.fetchall()

    username_string = str(username)
    username1 = username_string.replace("[", "")
    username2 = username1.replace("]", "")
    username3 = username2.replace("(", "")
    username4 = username3.replace(")", "")
    username5 = username4.replace("'", "")
    username_final = username5.replace(",", "")

    get_password = "SELECT password from userinfo WHERE name = %s"

    cursor.execute(get_password, name_selected)

    password = cursor.fetchall()

    password_string = str(password)
    password1 = password_string.replace("[", "")
    password2 = password1.replace("]", "")
    password3 = password2.replace("(", "")
    password4 = password3.replace(")", "")
    password5 = password4.replace("'", "")
    password_final = password5.replace(",", "")

    get_email = "SELECT email from userinfo WHERE name = %s"

    cursor.execute(get_email, name_selected)

    email = cursor.fetchall()

    email_string = str(email)
    email1 = email_string.replace("[", "")
    email2 = email1.replace("]", "")
    email3 = email2.replace("(", "")
    email4 = email3.replace(")", "")
    email5 = email4.replace("'", "")
    email_final = email5.replace(",", "")

    global viewdetails_namelabel
    global viewdetails_namelabel1
    global viewdetails_emaillabel
    global viewdetails_emaillabel1
    global viewdetails_passwordlabel
    global viewdetails_passwordlabel1
    global viewdetails_usernamelabel
    global viewdetails_usernamelabel1
    global closeviewdetails

    viewdetails_namelabel = Label(window, text="Name: ", bg="white", font="none 12 bold")
    viewdetails_namelabel.place(x=200, y=150)
    viewdetails_namelabel1 = Label(window, text= name_final, bg="white", font="none 12")
    viewdetails_namelabel1.place(x=255, y=150)

    viewdetails_emaillabel = Label(window, text="Email: ", bg="white", font="none 12 bold")
    viewdetails_emaillabel.place(x=200, y=180)
    viewdetails_emaillabel1 = Label(window, text=email_final, bg="white", font="none 12")
    viewdetails_emaillabel1.place(x=257, y=180)

    viewdetails_usernamelabel = Label(window, text="Username: ", bg="white", font="none 12 bold")
    viewdetails_usernamelabel.place(x=200, y=210)
    viewdetails_usernamelabel1 = Label(window, text=username_final, bg="white", font="none 12")
    viewdetails_usernamelabel1.place(x=285, y=210)

    viewdetails_passwordlabel = Label(window, text="Password: ", bg="white", font="none 12 bold")
    viewdetails_passwordlabel.place(x=200, y=240)
    viewdetails_passwordlabel1 = Label(window, text=password_final, bg="white", font="none 12")
    viewdetails_passwordlabel1.place(x=285, y=240)

    closeviewdetails = Button(window, text="Close", command=close_viewdetails)
    closeviewdetails.place(x=200, y=250)

def register_new_users():
    admin_session()

    approvenewusers.config(state='disabled')

    #Opening Database to get all unregistered users
    get_all_unregistered = "SELECT name FROM userinfo WHERE regstatus = 'unregistered'"

    cursor.execute(get_all_unregistered)

    all_unregistered = cursor.fetchall()

    global unregistered_frame
    unregistered_frame = Frame(window)
    unregistered_scrollbar = Scrollbar(unregistered_frame, orient=VERTICAL)
    global unregistered_listbox
    global unregistered_list
    unregistered_listbox = Listbox(unregistered_frame, yscrollcommand=unregistered_scrollbar.set)
    unregistered_scrollbar.config(command=unregistered_listbox.yview)
    unregistered_scrollbar.pack(side=RIGHT, fill=Y)
    unregistered_frame.place(x=45, y=150)
    unregistered_listbox.pack()
    for name in all_unregistered:
        name_string = str(name)
        name_label = name_string.replace("'", "")
        name_label1 = name_label.replace("(", "")
        name_label2 = name_label1.replace(")", "")
        name_label3 = name_label2.replace(",", "")
        unregistered_listbox.insert(END, name_label3)

    global viewdetails
    viewdetails = Button(window, text = "View Details", command=view_details)
    viewdetails.place(x=70, y=320)

    global approvenewuser
    approvenewuser = Button(window, text = "Approve New User", command=approve_newuser)
    approvenewuser.place(x=55, y=350)

    global rejectnewuser
    rejectnewuser = Button(window, text = "Reject New User", command=reject_newuser)
    rejectnewuser.place(x=60, y=380)

    global registeredlabel
    registeredlabel = Label(window, text= " ", bg="white", font="none 12 bold")
    registeredlabel.place(x=40, y=410)

def manager_close_viewdetails():
    manager_viewdetails_namelabel.destroy()
    manager_viewdetails_namelabel1.destroy()
    manager_viewdetails_emaillabel.destroy()
    manager_viewdetails_emaillabel1.destroy()
    manager_viewdetails_usernamelabel.destroy()
    manager_viewdetails_usernamelabel1.destroy()
    manager_viewdetails_passwordlabel.destroy()
    manager_viewdetails_passwordlabel1.destroy()
    manager_closeviewdetails.destroy()

def view_manager_details():
    name_selected = (manager_listbox.get(ANCHOR),)

    name_string = str(name_selected)
    name1 = name_string.replace("[", "")
    name2 = name1.replace("]", "")
    name3 = name2.replace("(", "")
    name4 = name3.replace(")", "")
    name5 = name4.replace("'", "")
    name_final = name5.replace(",", "")

    get_username = "SELECT username from managerinfo WHERE name = %s"

    cursor.execute(get_username, name_selected)

    username = cursor.fetchall()

    username_string = str(username)
    username1 = username_string.replace("[", "")
    username2 = username1.replace("]", "")
    username3 = username2.replace("(", "")
    username4 = username3.replace(")", "")
    username5 = username4.replace("'", "")
    username_final = username5.replace(",", "")

    get_password = "SELECT password from managerinfo WHERE name = %s"

    cursor.execute(get_password, name_selected)

    password = cursor.fetchall()

    password_string = str(password)
    password1 = password_string.replace("[", "")
    password2 = password1.replace("]", "")
    password3 = password2.replace("(", "")
    password4 = password3.replace(")", "")
    password5 = password4.replace("'", "")
    password_final = password5.replace(",", "")

    get_email = "SELECT email from managerinfo WHERE name = %s"

    cursor.execute(get_email, name_selected)

    email = cursor.fetchall()

    email_string = str(email)
    email1 = email_string.replace("[", "")
    email2 = email1.replace("]", "")
    email3 = email2.replace("(", "")
    email4 = email3.replace(")", "")
    email5 = email4.replace("'", "")
    email_final = email5.replace(",", "")

    global manager_viewdetails_namelabel
    global manager_viewdetails_namelabel1
    global manager_viewdetails_emaillabel
    global manager_viewdetails_emaillabel1
    global manager_viewdetails_passwordlabel
    global manager_viewdetails_passwordlabel1
    global manager_viewdetails_usernamelabel
    global manager_viewdetails_usernamelabel1
    global manager_closeviewdetails

    manager_viewdetails_namelabel = Label(window, text="Name: ", bg="white", font="none 12 bold")
    manager_viewdetails_namelabel.place(x=590, y=150)
    manager_viewdetails_namelabel1 = Label(window, text= name_final, bg="white", font="none 12")
    manager_viewdetails_namelabel1.place(x=645, y=150)

    manager_viewdetails_emaillabel = Label(window, text="Email: ", bg="white", font="none 12 bold")
    manager_viewdetails_emaillabel.place(x=590, y=180)
    manager_viewdetails_emaillabel1 = Label(window, text=email_final, bg="white", font="none 12")
    manager_viewdetails_emaillabel1.place(x=644, y=180)

    manager_viewdetails_usernamelabel = Label(window, text="Username: ", bg="white", font="none 12 bold")
    manager_viewdetails_usernamelabel.place(x=590, y=210)
    manager_viewdetails_usernamelabel1 = Label(window, text=username_final, bg="white", font="none 12")
    manager_viewdetails_usernamelabel1.place(x=682, y=210)

    manager_viewdetails_passwordlabel = Label(window, text="Password: ", bg="white", font="none 12 bold")
    manager_viewdetails_passwordlabel.place(x=590, y=240)
    manager_viewdetails_passwordlabel1 = Label(window, text=password_final, bg="white", font="none 12")
    manager_viewdetails_passwordlabel1.place(x=682, y=240)

    manager_closeviewdetails = Button(window, text="Close", command=manager_close_viewdetails)
    manager_closeviewdetails.place(x=590, y=300)

def add_manager():
    manager_name = managername.get()
    manager_email = manageremail.get()
    manager_username = managerusername.get()
    manager_password = managerpassword.get()

    add_managerlabel.destroy()
    manager_namelabel.destroy()
    manager_nameentry.destroy()
    manager_emaillabel.destroy()
    manager_emailentry.destroy()
    manager_usernamelabel.destroy()
    manager_usernameentry.destroy()
    manager_passwordlabel.destroy()
    manager_passwordentry.destroy()

    add_manager = "INSERT INTO managerinfo (name, email, username, password) VALUES (%s, %s, %s, %s)"

    cursor.execute(add_manager, (manager_name, manager_email, manager_username, manager_password))

    w_t_db.commit()

    manager_listbox.insert(END, manager_name)

def add_manager_info():
    global managername
    global manageremail
    global managerusername
    global managerpassword
    managername = StringVar()
    manageremail = StringVar()
    managerusername = StringVar()
    managerpassword = StringVar()

    global add_managerlabel
    add_managerlabel = Label(window, text="Add Manager", bg="white", font="none 12 bold")
    add_managerlabel.place(x=605, y=150)

    global manager_namelabel
    manager_namelabel = Label(window, text = "Name", bg="white", font="none 12")
    manager_namelabel.place(x=632, y=180)

    global manager_nameentry
    manager_nameentry = Entry(window, textvariable = managername)
    manager_nameentry.place(x=595, y=200)

    global manager_emaillabel
    manager_emaillabel = Label(window, text = "Email", bg="white", font="none 12")
    manager_emaillabel.place(x=632, y=230)

    global manager_emailentry
    manager_emailentry = Entry(window, textvariable = manageremail)
    manager_emailentry.place(x=595, y=250)

    global manager_usernamelabel
    manager_usernamelabel = Label(window, text = "Username", bg="white", font="none 12")
    manager_usernamelabel.place(x=620, y=280)

    global manager_usernameentry
    manager_usernameentry = Entry(window, textvariable = managerusername)
    manager_usernameentry.place(x=595, y=300)

    global manager_passwordlabel
    manager_passwordlabel = Label(window, text = "Password", bg="white", font="none 12")
    manager_passwordlabel.place(x=620, y=330)

    global manager_passwordentry
    manager_passwordentry = Entry(window, textvariable = managerpassword)
    manager_passwordentry.place(x=595, y=350)

    global addmanager
    addmanager = Button(window, text = "Add Manager", command=add_manager)
    addmanager.place(x=615, y=400)

def remove_manager():
    name_selected = (manager_listbox.get(ANCHOR),)

    remove_manager = "DELETE FROM managerinfo WHERE name = %s"

    cursor.execute(remove_manager, name_selected)

    w_t_db.commit()

    manager_listbox.delete(ANCHOR)

    manager_statuslabel.config(text="Manager has been removed.", fg="red")

def add_remove_managers():
    admin_session()

    addremovemanagers.config(state='disabled')

    get_all_managers = "SELECT name from managerinfo"

    cursor.execute(get_all_managers)

    all_managers = cursor.fetchall()

    global manager_frame
    manager_frame = Frame(window)
    manager_scrollbar = Scrollbar(manager_frame, orient=VERTICAL)
    global manager_listbox
    global manager_list
    manager_listbox = Listbox(manager_frame, yscrollcommand=manager_scrollbar.set)
    manager_scrollbar.config(command=manager_listbox.yview)
    manager_scrollbar.pack(side=RIGHT, fill=Y)
    manager_frame.place(x=845, y=150)
    manager_listbox.pack()
    for name in all_managers:
        name_string = str(name)
        name_label = name_string.replace("'", "")
        name_label1 = name_label.replace("(", "")
        name_label2 = name_label1.replace(")", "")
        name_label3 = name_label2.replace(",", "")
        manager_listbox.insert(END, name_label3)

    global viewmanagerdetails
    viewmanagerdetails = Button(window, text = "View Details", command=view_manager_details)
    viewmanagerdetails.place(x=875, y=320)

    global addmanagerinfo
    addmanagerinfo = Button(window, text = "Add Manager", command= add_manager_info)
    addmanagerinfo.place(x=870, y=350)

    global removemanager
    removemanager = Button(window, text = "Remove Manager", command=remove_manager)
    removemanager.place(x=860, y=380)

    global manager_statuslabel
    manager_statuslabel = Label(window, text= " ", bg="white", font="none 12 bold")
    manager_statuslabel.place(x=845, y=410)

def delete_user():
    name_selected = (all_user_listbox.get(ANCHOR),)
    nameselected = all_user_listbox.get(ANCHOR)
    nameselected1 = nameselected.replace(" ", "")

    delete_user = "DELETE FROM userinfo WHERE name = %s"

    cursor.execute(delete_user, name_selected)

    w_t_db.commit()

    delete_timesheet_table = "DROP TABLE " + nameselected1 + "_timesheetdata"

    cursor.execute(delete_timesheet_table)

    w_t_db.commit()

    delete_timesheet_drafts = "DROP TABLE " + nameselected1 + "_saveddrafts"

    cursor.execute(delete_timesheet_drafts)

    w_t_db.commit()

    all_user_listbox.delete(ANCHOR)

    deletionlabel.config(text = nameselected + "\'s account has been deleted along with their respective data.", fg="red")

def remove_users():
    admin_session()

    removeusers.config(state='disabled')

    get_all_users = "SELECT name FROM userinfo WHERE regstatus = 'registered'"

    cursor.execute(get_all_users)

    all_users = cursor.fetchall()

    global all_user_frame
    all_user_frame = Frame(window)
    all_user_scrollbar = Scrollbar(all_user_frame, orient=VERTICAL)
    global all_user_listbox
    global all_user_list
    all_user_listbox = Listbox(all_user_frame, yscrollcommand=all_user_scrollbar.set)
    all_user_scrollbar.config(command=all_user_listbox.yview)
    all_user_scrollbar.pack(side=RIGHT, fill=Y)
    all_user_frame.place(x=445, y=150)
    all_user_listbox.pack()
    for name in all_users:
        name_string = str(name)
        name_label = name_string.replace("'", "")
        name_label1 = name_label.replace("(", "")
        name_label2 = name_label1.replace(")", "")
        name_label3 = name_label2.replace(",", "")
        all_user_listbox.insert(END, name_label3)

    global removeuser1
    removeuser1 = Button(window, text = "Remove User", command=delete_user)
    removeuser1.place(x=470, y=320)

    global deletionlabel
    deletionlabel = Label(window, text= " ", bg="white", font="none 12 bold")
    deletionlabel.place(x=440, y=360)

def admin_viewuserdetails():
    nameinfo = admin_userdetails_listbox.get(ANCHOR)
    nameinfo1 = nameinfo.replace(" ", "")

    global nameinfolabel
    nameinfolabel = Label(window, text=nameinfo + "\'s Timesheet Data", bg="white", font="none 14 bold")
    nameinfolabel.place(x=160, y=150)

    global treeviewframe
    treeviewframe = Frame(window, width=100)
    treeviewframe.place(x=160, y=180)

    #Treeview
    global timesheet
    timesheet = ttk.Treeview(treeviewframe)
    timesheet['columns'] = ("week", "hourtype", "sun", "mon", "tue", "wed", "thu", "fri", "sat", "notes", "approvalstatus")
    timesheet.pack()

    timesheet.heading("#0", text="", anchor="w")

    timesheet.column("#0",anchor="center", width=5, stretch=NO)

    timesheet.heading("week", text="Week", anchor="w")

    timesheet.column("week", anchor="w", width=80)

    timesheet.heading("hourtype", text="Hourtype", anchor="w")

    timesheet.column("hourtype", anchor="w", width=80)

    timesheet.heading("sun", text="Sunday", anchor="w")

    timesheet.column("sun", anchor="w", width=80)

    timesheet.heading("mon", text="Monday", anchor="w")

    timesheet.column("mon", anchor="w", width=80)

    timesheet.heading("tue", text="Tuesday", anchor="w")

    timesheet.column("tue", anchor="w", width=80)

    timesheet.heading("wed", text="Wednesday", anchor="w")

    timesheet.column("wed", anchor="w", width=80)

    timesheet.heading("thu", text="Thursday", anchor="w")

    timesheet.column("thu", anchor="w", width=80)

    timesheet.heading("fri", text="Friday", anchor="w")

    timesheet.column("fri", anchor="w", width=80)

    timesheet.heading("sat", text="Saturday", anchor="w")

    timesheet.column("sat", anchor="w", width=80)

    timesheet.heading("notes", text="Notes", anchor="w")

    timesheet.column("notes", anchor="w", width=200)

    timesheet.heading("approvalstatus", text="Status", anchor="w")

    timesheet.column("approvalstatus", anchor="w", width=80)

    get_timesheets = "SELECT timesheet FROM " + nameinfo1 + "_timesheetdata"
    cursor.execute(get_timesheets)
    all_timesheets = cursor.fetchall()

    for timesheet_got in all_timesheets:
        get_startdate = "SELECT day1 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"
        cursor.execute(get_startdate, timesheet_got)
        startdate = cursor.fetchall()
        startdate_string = str(startdate)
        startdate1 = startdate_string.replace("[", "")
        startdate2 = startdate1.replace("]", "")
        startdate3 = startdate2.replace("(", "")
        startdate4 = startdate3.replace(")", "")
        startdate5 = startdate4.replace("'", "")
        startdate6 = startdate5.replace(",", "")
        startdate7 = startdate6.replace("-", "/")
        print(startdate7[0:5])

        get_enddate = "SELECT day7 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"
        cursor.execute(get_enddate, timesheet_got)
        enddate = cursor.fetchall()
        enddate_string = str(enddate)
        enddate1 = enddate_string.replace("[", "")
        enddate2 = enddate1.replace("]", "")
        enddate3 = enddate2.replace("(", "")
        enddate4 = enddate3.replace(")", "")
        enddate5 = enddate4.replace("'", "")
        enddate6 = enddate5.replace(",", "")
        enddate7 = enddate6.replace("-", "/")
        print(enddate7[0:5])

        #getting the saved hourtype
        get_hourtype = "SELECT hourtype_selected FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(get_hourtype, timesheet_got)
        hourtype = cursor.fetchall()

        hourtype_string = str(hourtype)
        hourtype1 = hourtype_string.replace("[", "")
        hourtype2 = hourtype1.replace("]", "")
        hourtype3 = hourtype2.replace("(", "")
        hourtype4 = hourtype3.replace(")", "")
        hourtype5 = hourtype4.replace("'", "")
        hourtype_final = hourtype5.replace(",", "")

        #getting day1 hours saved
        day1_get = "SELECT day1 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day1_get, timesheet_got)
        day1 = cursor.fetchall()

        day1_string = str(day1)
        day1_1 = day1_string.replace("[", "")
        day1_2 = day1_1.replace("]", "")
        day1_3 = day1_2.replace("(", "")
        day1_4 = day1_3.replace(")", "")
        day1_5 = day1_4.replace("'", "")
        day1_final = day1_5.replace(",", "")

        #getting day2 hours saved
        day2_get = "SELECT day2 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day2_get, timesheet_got)
        day2 = cursor.fetchall()

        day2_string = str(day2)
        day2_1 = day2_string.replace("[", "")
        day2_2 = day2_1.replace("]", "")
        day2_3 = day2_2.replace("(", "")
        day2_4 = day2_3.replace(")", "")
        day2_5 = day2_4.replace("'", "")
        day2_final = day2_5.replace(",", "")

        #getting day3 hours saved
        day3_get = "SELECT day3 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day3_get, timesheet_got)
        day3 = cursor.fetchall()

        day3_string = str(day3)
        day3_1 = day3_string.replace("[", "")
        day3_2 = day3_1.replace("]", "")
        day3_3 = day3_2.replace("(", "")
        day3_4 = day3_3.replace(")", "")
        day3_5 = day3_4.replace("'", "")
        day3_final = day3_5.replace(",", "")

        #getting day4 hours saved
        day4_get = "SELECT day4 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day4_get, timesheet_got)
        day4 = cursor.fetchall()

        day4_string = str(day4)
        day4_1 = day4_string.replace("[", "")
        day4_2 = day4_1.replace("]", "")
        day4_3 = day4_2.replace("(", "")
        day4_4 = day4_3.replace(")", "")
        day4_5 = day4_4.replace("'", "")
        day4_final = day4_5.replace(",", "")

        #getting day5 hours saved
        day5_get = "SELECT day5 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day5_get, timesheet_got)
        day5 = cursor.fetchall()

        day5_string = str(day5)
        day5_1 = day5_string.replace("[", "")
        day5_2 = day5_1.replace("]", "")
        day5_3 = day5_2.replace("(", "")
        day5_4 = day5_3.replace(")", "")
        day5_5 = day5_4.replace("'", "")
        day5_final = day5_5.replace(",", "")

        #getting day6 hours saved
        day6_get = "SELECT day6 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day6_get, timesheet_got)
        day6 = cursor.fetchall()

        day6_string = str(day6)
        day6_1 = day6_string.replace("[", "")
        day6_2 = day6_1.replace("]", "")
        day6_3 = day6_2.replace("(", "")
        day6_4 = day6_3.replace(")", "")
        day6_5 = day6_4.replace("'", "")
        day6_final = day6_5.replace(",", "")

        #getting day7 hours_saved
        day7_get = "SELECT day7 FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(day7_get, timesheet_got)
        day7 = cursor.fetchall()

        day7_string = str(day7)
        day7_1 = day7_string.replace("[", "")
        day7_2 = day7_1.replace("]", "")
        day7_3 = day7_2.replace("(", "")
        day7_4 = day7_3.replace(")", "")
        day7_5 = day7_4.replace("'", "")
        day7_final = day7_5.replace(",", "")

        #getting notes that were saved
        notes_get = "SELECT notes FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(notes_get, timesheet_got)
        notes = cursor.fetchall()

        notes_string = str(notes)
        notes_1 = notes_string.replace("[", "")
        notes_2 = notes_1.replace("]", "")
        notes_3 = notes_2.replace("(", "")
        notes_4 = notes_3.replace(")", "")
        notes_5 = notes_4.replace("'", "")
        notes_final = notes_5.replace(",", "")

        #Getting approval Status
        approvalstatus_get = "SELECT approval_status FROM " + nameinfo1 + "_timesheetdata WHERE timesheet = %s"

        cursor.execute(approvalstatus_get, timesheet_got)
        approvalstatus = cursor.fetchall()

        approvalstatus_string = str(approvalstatus)
        approvalstatus_1 = approvalstatus_string.replace("[", "")
        approvalstatus_2 = approvalstatus_1.replace("]", "")
        approvalstatus_3 = approvalstatus_2.replace("(", "")
        approvalstatus_4 = approvalstatus_3.replace(")", "")
        approvalstatus_5 = approvalstatus_4.replace("'", "")
        approvalstatus_final = approvalstatus_5.replace(",", "")

        timesheet.insert("", 'end', values = (startdate7[0:5] + "-" + enddate7[0:5], hourtype_final, day1_final[7:8], day2_final[7:8], day3_final[7:8], day4_final[7:8], day5_final[7:8], day6_final[7:8], day7_final[7:8], notes_final, approvalstatus_final))

def admin_selectuserdetails():
    admin_session()

    adminviewuserdata.config(state="disabled")

    #Opening Database to get all user names
    get_all_users = "SELECT name FROM userinfo"

    cursor.execute(get_all_users)

    all_users = cursor.fetchall()

    admin_userdetails_frame = Frame(window)
    admin_userdetails_scrollbar = Scrollbar(admin_userdetails_frame, orient=VERTICAL)
    global admin_userdetails_listbox
    global admin_userdetails_list
    admin_userdetails_listbox = Listbox(admin_userdetails_frame, yscrollcommand=admin_userdetails_scrollbar.set)
    admin_userdetails_scrollbar.config(command=admin_userdetails_listbox.yview)
    admin_userdetails_scrollbar.pack(side=RIGHT, fill=Y)
    admin_userdetails_frame.place(x=1245, y=180)
    admin_userdetails_listbox.pack()
    for name in all_users:
        name_string = str(name)
        name_label = name_string.replace("'", "")
        name_label1 = name_label.replace("(", "")
        name_label2 = name_label1.replace(")", "")
        name_label3 = name_label2.replace(",", "")
        admin_userdetails_listbox.insert(END, name_label3)

    Button(window, text="View Data", width=20, command=admin_viewuserdetails) .place(x=1240, y=350)

def admin_logout():
    logout()

def admin_session():
    clear_screen()

    window.title("Administrator Dashboard")
    Label (window, image=logo, bg="white", justify="left") .pack()
    Label(window, text="Administrator Dashboard", bg="white", font="none 20 bold") .pack()

    global approvenewusers
    approvenewusers = Button(window, text="Approve New Users", width=20, command=register_new_users)
    approvenewusers.place(x=40, y=110)

    global removeusers
    removeusers = Button(window, text = "Remove Users", width=20, command=remove_users)
    removeusers.place(x=440, y=110)

    global addremovemanagers
    addremovemanagers = Button(window, text="Add/Remove Managers", width=20, command=add_remove_managers)
    addremovemanagers.place(x=840, y=110)

    global adminviewuserdata
    adminviewuserdata = Button(window, text = "View User Data", width=20, command=admin_selectuserdetails)
    adminviewuserdata.place(x=1240, y=110)

    admin_logoutbutton = Button(window, text = "Log Out", width=20, command=admin_logout)
    admin_logoutbutton.place(x=1640, y=110)

def login_success():
    session()
def password_not_recognized():
        verificationerror_label.config(text="Password not recognized.", bg="white", fg="red", font="none 12 bold")
def user_not_found():
        verificationerror_label.config(text="User not recognized.", bg="white", fg="red", font="none 12 bold")

def login():
    clear_screen()

    window.title("Login")
    Label(window, text="Please enter details below to login.", bg="white", font="none 14 bold") .pack()
    Label(window, text=" ", bg="white") .pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()


    global username_entry1
    global password_entry1

    Label(window, text = "Username *", bg="white", font="none 12") .pack()
    username_entry1 = Entry(window, textvariable = username_verify)
    username_entry1.pack()
    Label(window, text=" ", bg="white") .pack()
    Label(window, text="Password *", bg="white", font = "none 12") .pack()
    password_entry1 = Entry(window, textvariable = password_verify)
    password_entry1.pack()
    Label(window, text=" ", bg="white") .pack()
    Button(window, text="Login", width=10, height=1, bg="white", command=login_verify) .pack()


    Button(window, text="New User?", width=10, height=1, bg="white", command=newuser) .pack(pady=10)

    Button(window, text="Go Back", bg="white", width=10, height=1, command=logout) .pack()

    global verificationerror_label
    verificationerror_label = Label(window, text=" ", bg="white")
    verificationerror_label.pack()

def login_verify():
    global username1

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    username_entered = (username1,)

    username_search = "SELECT password FROM userinfo WHERE username = %s"

    cursor.execute(username_search, username_entered)

    password_returned = cursor.fetchall()

    if len(password_returned) == 0:
        user_not_found()
    else:
        registered_check = "SELECT regstatus FROM userinfo WHERE username = %s"
        cursor.execute(registered_check, username_entered)

        registration_status = cursor.fetchall()

        registration_string = str(registration_status)
        registration1 = registration_string.replace("[", "")
        registration2 = registration1.replace("]", "")
        registration3 = registration2.replace("(", "")
        registration4 = registration3.replace(")", "")
        registration5 = registration4.replace("'", "")
        registration_final = registration5.replace(",", "")

        if registration_final == 'registered':
            password_string = str(password_returned)
            password_replace1 = password_string.replace("'", "")
            password_replace2 = password_replace1.replace("(", "")
            password_replace3 = password_replace2.replace(")", "")
            password_replace4 = password_replace3.replace("[", "")
            password_replace5 = password_replace4.replace("]","")
            password_final = password_replace5.replace(",", "")
            if password_final == password1:
                login_success()
            else:
                password_not_recognized()

        else:
            verificationerror_label.config(text="""
            Your account has not been registered \n
            by an administrator yet. \n
            Please wait until you receive an email \n
            confirming your registration and then \n
            you will be able to log on successfully. """)

def manager_login():
    clear_screen()

    window.title("Login")
    Label(window, text="Please enter details below to login.", bg="white", font="none 14 bold") .pack()
    Label(window, text=" ", bg="white") .pack()

    global manager_username_verify
    global manager_password_verify

    manager_username_verify = StringVar()
    manager_password_verify = StringVar()


    global manager_username_entry1
    global manager_password_entry1

    Label(window, text = "Manager Username *", bg="white", font="none 12") .pack()
    manager_username_entry1 = Entry(window, textvariable = manager_username_verify)
    manager_username_entry1.pack()
    Label(window, text=" ", bg="white") .pack()
    Label(window, text="Password *", bg="white", font = "none 12") .pack()
    manager_password_entry1 = Entry(window, textvariable = manager_password_verify)
    manager_password_entry1.pack()
    Label(window, text=" ", bg="white") .pack()
    Button(window, text="Login", width=10, height=1, command=manager_login_verify) .pack()

    Button(window, text="Go Back", width=10, height=1, command=logout) .pack(pady=10)

    global manager_verificationerror_label
    manager_verificationerror_label = Label(window, text=" ", bg="white")
    manager_verificationerror_label.pack()

def manager_login_verify():
    global manager_username1
    manager_username1 = manager_username_verify.get()
    manager_password1 = manager_password_verify.get()
    manager_username_entry1.delete(0, END)
    manager_password_entry1.delete(0, END)

    manager_username_search = "SELECT password FROM managerinfo WHERE username = %s"
    manager_username_entered = (manager_username1,)
    cursor.execute(manager_username_search, manager_username_entered)

    password_returned = cursor.fetchall()

    if len(password_returned) == 0:
        manager_not_found()
    else:
         password_string = str(password_returned)
         password_replace1 = password_string.replace("'", "")
         password_replace2 = password_replace1.replace("(", "")
         password_replace3 = password_replace2.replace(")", "")
         password_replace4 = password_replace3.replace("[", "")
         password_replace5 = password_replace4.replace("]","")
         password_final = password_replace5.replace(",", "")
         if password_final == manager_password1:
             manager_session()
         else:
             manager_password_not_recognized()

def manager_password_not_recognized():
    manager_verificationerror_label.config(text="Password not recognized.", bg="white", fg="red", font="none 12 bold")

def manager_not_found():
    manager_verificationerror_label.config(text="Username not recognized.", bg="white", fg="red", font="none 12 bold")

def admin_login():
    clear_screen()

    window.title("Login")
    Label(window, text="Please enter the details below to login.", bg="white", font="none 14 bold") .pack()
    Label(window, text=" ", bg="white") .pack()

    global admin_username_verify
    global admin_password_verify

    admin_username_verify = StringVar()
    admin_password_verify = StringVar()


    global admin_username_entry1
    global admin_password_entry1

    Label(window, text = "Administrator Username *", bg="white", font="none 12") .pack()
    admin_username_entry1 = Entry(window, textvariable = admin_username_verify)
    admin_username_entry1.pack()
    Label(window, text=" ", bg="white") .pack()
    Label(window, text="Password *", bg="white", font = "none 12") .pack()
    admin_password_entry1 = Entry(window, textvariable = admin_password_verify)
    admin_password_entry1.pack()
    Label(window, text=" ", bg="white") .pack()
    Button(window, text="Login", width=10, height=1, command=admin_login_verify) .pack()

    Button(window, text="Go Back", width=10, height=1, command=logout) .pack(pady=10)

    global admin_verificationerror_label
    admin_verificationerror_label = Label(window, text=" ", bg="white")
    admin_verificationerror_label.pack()

def admin_login_verify():
    global admin_username1
    admin_username1 = admin_username_verify.get()
    admin_password1 = admin_password_verify.get()
    admin_username_entry1.delete(0, END)
    admin_password_entry1.delete(0, END)

    admin_username_search = "SELECT password FROM admininfo WHERE username = %s"
    admin_username_entered = (admin_username1,)
    cursor.execute(admin_username_search, admin_username_entered)

    password_returned = cursor.fetchall()

    if len(password_returned) == 0:
        admin_not_found()
    else:
         password_string = str(password_returned)
         password_replace1 = password_string.replace("'", "")
         password_replace2 = password_replace1.replace("(", "")
         password_replace3 = password_replace2.replace(")", "")
         password_replace4 = password_replace3.replace("[", "")
         password_replace5 = password_replace4.replace("]","")
         password_final = password_replace5.replace(",", "")
         if password_final == admin_password1:
             admin_session()
         else:
             admin_password_not_recognized()

def admin_password_not_recognized():
    admin_verificationerror_label.config(text="Password not recognized.", bg="white", fg="red", font="none 12 bold")

def admin_not_found():
    admin_verificationerror_label.config(text="Username not recognized.", bg="white", fg="red", font="none 12 bold")

def register_user():
    firstname_get = firstname.get()
    lastname_get = lastname.get()
    email_get = email.get()
    username_get = username.get()
    password_get = password.get()

    register_user = "INSERT INTO userinfo (name, email, username, password, regstatus) VALUES (%s, %s, %s, %s, %s)"

    cursor.execute(register_user, (firstname_get + " " + lastname_get, email_info, username_get, password_get, 'unregistered'))

    w_t_db.commit()

    registration_status.config(text="Registration Success. \n Please wait for an administrator \n to approve your credentials; \n then you will be able to log on.", fg="green")

#Verifying that the user has entered a password of a strong length
def verify_password():
    global password_get
    password_get = password.get()

    if len(password_get) <= 7:
        print(len(password_get))
        password_entry.delete(0, END)
        registration_status.config(text="Please make your password strong and longer than 8 characters", fg="red")

    else:
        print(len(password_get))
        register_user()

#Verifying that the username entered is unique
def verify_username():
    global username_get
    username_get = username.get()

    username_tuple = (username_get,)

    username_taken = "SELECT name FROM userinfo WHERE username = %s"

    cursor.execute(username_taken, username_tuple)

    username_match = cursor.fetchall()

    if len(username_match) == 0:
        verify_password()

    else:
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        registration_status.config(text="Username has been taken.", fg="red")

#Verifying the email by sending a test email to the address
def verify_email():
    global email_info
    email_info = email.get()

    sender_email = "timesheettestemail@gmail.com"
    rec_email = email_info
    email_password = "worldscapetest1"
    msg = MIMEText('Dear ' + firstname_get + """, \n \n
    You have successfully registered for the Worldscape Timesheet Application. \n
    Please note that your login credentials and account will not be valid until an adminstrator approves your account creation. \n
    Sincerely, \n
    The Worldscape Timesheet Application Development Team""")
    msg['Subject'] = 'Worldscape Timesheet Application Registration Success'
    msg['From'] = 'timesheettestemail@gmail.com'
    msg['To'] = email_info

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, email_password)
        print("Login Success")
        server.sendmail(sender_email, rec_email, msg.as_string())
        print("Email has been sent to " + rec_email)

        server.quit()

        verify_username()

    except smtplib.SMTPRecipientsRefused:
        email_entry.delete(0, END)
        Label(window, text = "Email Invalid", fg="red", font="none 12 bold") .pack()

#verifying that the name and last name were actually username_entered
def verify_name():
    global firstname_get
    firstname_get = firstname.get()

    if len(firstname_get) == 0:
        registration_status.config(text="Please fill out all required fields")

    else:
        global lastname_get
        lastname_get = lastname.get()
        if len(lastname_get) == 0:
            registration_status.config(text="Please fill out all required fields")
        else:
            verify_email()


def newuser():
    clear_screen()

    window.title("New User")

    global firstname
    global lastname
    global email
    global username
    global password
    global firstname_entry
    global lastname_entry
    global email_entry
    global username_entry
    global password_entry

    firstname = StringVar()
    lastname = StringVar()
    email = StringVar()
    username = StringVar()
    password = StringVar()


    Label(window, text="Please enter details below to register.", bg="white", font="none 14 bold") .pack()
    Label(window, text=" ", bg="white") .pack()
    Label(window, text="First Name", bg="white", font="none 12") .pack()
    firstname_entry = Entry(window, textvariable = firstname)
    firstname_entry.pack()
    Label(window, text="Last Name", bg="white", font="none 12") .pack()
    lastname_entry = Entry(window, textvariable = lastname)
    lastname_entry.pack()
    Label(window, text="Email", bg="white", font="none 12") .pack()
    email_entry = Entry(window, textvariable = email)
    email_entry.pack()
    Label(window, text="Username", bg="white", font="none 12") .pack()
    username_entry = Entry(window, textvariable = username)
    username_entry.pack()
    Label(window, text="Password", bg="white", font="none 12") .pack()
    password_entry = Entry(window, textvariable = password)
    password_entry.pack()
    Label(window, text=" ", bg="white") .pack()
    Button(window, text="Register", width=10, height=1, command=verify_name) .pack()
    Label(window, text=" ", bg="white") .pack()
    Button(window, text="Go Back", width=10, height=1, command=logout) .pack()
    Label(window, text=" ", bg="white") .pack()

    global registration_status
    registration_status = Label(window, text=" ", bg="white")
    registration_status.pack()

global logo
logo = PhotoImage(file="worldscapeinc.png")
logolabel = Label (window, image=logo, bg="white", justify="left") .pack()

global title
title = Label (window, text="Worldscape Timesheet", bg="white", fg="black", font="none 20 bold")
title.pack()

global loginbutton
loginbutton = Button(text="Login", width=20, command=login)
loginbutton.pack(pady=10)

global manger_loginbutton
manager_loginbutton = Button(text = "Manager Login", width=20, command=manager_login)
manager_loginbutton.pack(pady=10)

global admin_loginbutton
admin_loginbutton = Button(text = "Administrator Login", width=20, command=admin_login)
admin_loginbutton.pack(pady=10)

global newuserbutton
newuserbutton = Button(window, text="New User?", width=20, command=newuser)
newuserbutton.pack(pady=10)

window.mainloop()
