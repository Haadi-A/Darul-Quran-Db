import flet as ft
from urllib.parse import urlparse
import queue
import sqlite3


APP_NAME = "STACKS DATABASE"

landingPageRoute = "/"
selectStudentClassRoute = "/selectClass"
addStudentPageRoute = "/addStudent"
studentsListViewPageRoute = "/studentsList"
studentProfileViewPageRoute = "/studentProfilePage"
editStudentPageViewRoute = "/editStudentPage"

mallama_Azumi = "Mallama Azumi"
mallama_Rabi = "Mallama Rabi"
mallam_Musah = "Mallam Musah"
mallam_Awal = "Mallam Awal"
mallam_Sahnun = "Mallam Sahnun"
mallam_Umar = "Mallam Umar"
mallam_Haadi = "Mallam Haadi"
metaData = "MetaData"

listOfClassNames = [
    mallama_Azumi,
    mallama_Rabi,
    mallam_Musah,
    mallam_Awal,
    mallam_Sahnun,
    mallam_Umar,
    mallam_Haadi,
]

# parent container infos
containerBgColor: ft.colors = ft.colors.BLUE_100
borderRadiusForEverything = 35
containerBorderColor: ft.colors = ft.colors.BLACK
containerBorderWidth = 3


EXCEL_FILE_NAME = "NIGHT MAKARANTA STUDENTS DATA.xlsx"



mallama_Azumi_max_id_cell_id = "B2"
mallama_Rabi_max_id_cell_id = "B3"
mallam_Musah_max_id_cell_id = "B4"
mallam_Awal_max_id_cell_id = "B5"
mallam_Sahnun_max_id_cell_id = "B6"
mallam_Umar_max_id_cell_id = "B7"
mallam_Haadi_max_id_cell_id = "B8"

addUserTileIcon = "add user tile icon.svg"
removeUserTileIcon = "delete user.svg"
editStudentTileIcon = "edit user tile icon.svg"
showStudentProfileTileIcon = "student profile.svg"
listUsersTileIcon = "lsit students.svg"
userTribeIconLocation = "tribe.svg"
userLocationIconLocation = "location.svg"
userIdImageLocation = "user_id.svg"
userGenderIconLocation = "gender.svg"
userIdIconLocation = "user_id.svg"
userClassIconLoaction = "class.svg"
userBirthDayIconLocation = "Birthday.svg"
usersFathersIcon = "Father.svg"
usersMotherIcon = "Mother.svg"
boyAvatar = "boy.png"
girAvatar = "girl.png"
assestsDir = "/home/mr-robot/Documents/PROGRAMS/flet/nightMakaranta_gui/assets"
mafiaFont = "/fonts/Mafia.ttf"

classMaxCellIdMap = {
    mallama_Azumi: mallama_Azumi_max_id_cell_id,
    mallama_Rabi: mallama_Rabi_max_id_cell_id,
    mallam_Musah: mallam_Musah_max_id_cell_id,
    mallam_Awal: mallam_Awal_max_id_cell_id,
    mallam_Sahnun: mallam_Sahnun_max_id_cell_id,
    mallam_Umar: mallam_Umar_max_id_cell_id,
    mallam_Haadi: mallam_Haadi_max_id_cell_id,
}

months_of_the_yr = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
monthsToNumbersDicts = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

delAction:str = "Delete Operation"
editAction:str = "Edit Operation"
showProfileAction:str = "Students Profile" 
listStudentsAction:str = "List Students"


tableName = "Daarul_Quran_Students"
dataBaseName = "stacks.db"



def addStudentPage(page: ft.Page, paramsFrmPrevPage:str ="None", editMode:bool=False,) -> ft.View:
    LENGTH_ERROR = "LENGTH"
    MIXED_TYPE_ERROR = "MIXED"
    LEGIT = "LEGIT"

    if editMode:
        idOfStudentToEdit, previousPage, selectedAction  = paramsFrmPrevPage.split("-")[0], paramsFrmPrevPage.split("-")[1], paramsFrmPrevPage.split("-")[2],
        dObj = DarulQuranDb(connection = sqlite3.connect(dataBaseName, isolation_level=None))
        theStudentsData = dObj.getSpecificStudentsFullData(id=idOfStudentToEdit)[0]
        page.title = f"Edit {theStudentsData[1]} {theStudentsData[2]}'s data - {APP_NAME}"
    
    if not editMode:
        page.title = f"Add data - {APP_NAME}"

    stdentNamefeildWith = 250
    parentsField = 400
    dropDownFieldWidth = 150
    dobColumnsWidth = 80
    fieldsBorderRadiusValue = 12
    fontSize = 18
    cursorRadiusValue = 50
    fieldBorderWidth = 3
    cursorWidthValue, cursorHeightValue = 12, 30
    classDropDownFieldHintText = "Select Student class"
    genderDropDownFieldHintText = "Gender"

    

    backButton: ft.Control = ft.ElevatedButton(
        color=ft.colors.BLUE_300,
        text="back",
        icon=ft.icons.ARROW_BACK_SHARP,
        on_click=lambda _: onBackutonClicked(),
    )

    students_first_name = ft.TextField(
        autofocus=True, label="Student's first name",
        label_style=ft.TextStyle(size=fontSize - 5,
                                 weight=ft.FontWeight.NORMAL,
                                 font_family="Ubuntu",
                                 color=ft.colors.BLACK),
        bgcolor=ft.colors.WHITE,
        width=stdentNamefeildWith,
        border_radius=fieldsBorderRadiusValue, cursor_radius=cursorRadiusValue,
        cursor_width=cursorWidthValue, cursor_height=cursorHeightValue,
        border_width=fieldBorderWidth, color=ft.colors.BLACK,
        border_color=ft.colors.BLACK,
        text_style=ft.TextStyle(size=fontSize,
                                weight=ft.FontWeight.BOLD,
                                font_family="Ubuntu",
                                color=ft.colors.BLACK),
    )

    students_middle_name = ft.TextField(
        label="Student's middle name",
        label_style=ft.TextStyle(size=fontSize - 5,
                                 weight=ft.FontWeight.NORMAL,
                                 font_family="Ubuntu",
                                 color=ft.colors.BLACK),
        bgcolor=ft.colors.WHITE,
        width=stdentNamefeildWith,
        border_radius=fieldsBorderRadiusValue, cursor_radius=cursorRadiusValue,
        cursor_width=cursorWidthValue, cursor_height=cursorHeightValue,        border_width=fieldBorderWidth,
        border_color=ft.colors.BLACK,
        text_style=ft.TextStyle(size=fontSize,
                                weight=ft.FontWeight.BOLD,
                                font_family="Ubuntu",
                                color=ft.colors.BLACK),
    )

    students_last_name = ft.TextField(
        label="Student's last name",
        label_style=ft.TextStyle(size=fontSize - 5,
                                 weight=ft.FontWeight.NORMAL,
                                 font_family="Ubuntu",
                                 color=ft.colors.BLACK),
        bgcolor=ft.colors.WHITE,
        width=stdentNamefeildWith,
        border_radius=fieldsBorderRadiusValue, cursor_radius=cursorRadiusValue,
        cursor_width=cursorWidthValue, cursor_height=cursorHeightValue,
        border_width=fieldBorderWidth,
        border_color=ft.colors.BLACK,
        text_style=ft.TextStyle(size=fontSize,
                                weight=ft.FontWeight.BOLD,
                                font_family="Ubuntu",
                                color=ft.colors.BLACK),
    )

    fathers_name = ft.TextField(label="Father's full name",
                                label_style=ft.TextStyle(size=fontSize - 5,
                                                         weight=ft.FontWeight.NORMAL,
                                                         font_family="Ubuntu",
                                                         color=ft.colors.BLACK),
                                bgcolor=ft.colors.WHITE,
                                width=parentsField,
                                border_radius=fieldsBorderRadiusValue, cursor_radius=cursorRadiusValue,
                                cursor_width=cursorWidthValue, cursor_height=cursorHeightValue,
                                border_width=fieldBorderWidth,
                                border_color=ft.colors.BLACK,
                                text_style=ft.TextStyle(size=fontSize,
                                                        weight=ft.FontWeight.BOLD,
                                                        font_family="Ubuntu",
                                                        color=ft.colors.BLACK),
                                )

    mothers_name = ft.TextField(label="Mother's full name",
                                label_style=ft.TextStyle(size=fontSize - 5,
                                                         weight=ft.FontWeight.NORMAL,
                                                         font_family="Ubuntu",
                                                         color=ft.colors.BLACK),
                                bgcolor=ft.colors.WHITE,
                                width=parentsField,
                                border_radius=fieldsBorderRadiusValue, cursor_radius=cursorRadiusValue,
                                cursor_width=cursorWidthValue, cursor_height=cursorHeightValue,
                                border_width=fieldBorderWidth,
                                border_color=ft.colors.BLACK,
                                text_style=ft.TextStyle(size=fontSize,
                                                        weight=ft.FontWeight.BOLD,
                                                        font_family="Ubuntu",
                                                        color=ft.colors.BLACK),
                                )

    fathers_telephone = ft.TextField(
        max_lines=1, max_length=10, label="Father's telephone",
        label_style=ft.TextStyle(size=fontSize - 5,
                                 weight=ft.FontWeight.NORMAL,
                                          font_family="Ubuntu",
                                          color=ft.colors.BLACK),
        bgcolor=ft.colors.WHITE,
        width=stdentNamefeildWith,
        border_radius=fieldsBorderRadiusValue, cursor_radius=cursorRadiusValue,
        cursor_width=cursorWidthValue, cursor_height=cursorHeightValue,
        border_width=fieldBorderWidth,
        border_color=ft.colors.BLACK,
        text_style=ft.TextStyle(size=fontSize,
                                weight=ft.FontWeight.BOLD,
                                font_family="Ubuntu",
                                color=ft.colors.BLACK),
    )

    mothers_telephone = ft.TextField(
        max_lines=1, max_length=10, label="mother's telephone",
        label_style=ft.TextStyle(size=fontSize - 5,
                                 weight=ft.FontWeight.NORMAL,
                                          font_family="Ubuntu",
                                          color=ft.colors.BLACK),
        bgcolor=ft.colors.WHITE,
        width=stdentNamefeildWith,
        border_radius=fieldsBorderRadiusValue, cursor_width=cursorWidthValue,
        cursor_radius=cursorRadiusValue, cursor_height=cursorHeightValue,
        border_width=fieldBorderWidth,
        border_color=ft.colors.BLACK,
        text_style=ft.TextStyle(size=fontSize,
                                weight=ft.FontWeight.BOLD,
                                font_family="Ubuntu",
                                color=ft.colors.BLACK),
    )

    student_location = ft.TextField(
        label="Student's location",
        label_style=ft.TextStyle(size=fontSize - 5,
                                 weight=ft.FontWeight.NORMAL,
                                 font_family="Ubuntu",
                                 color=ft.colors.BLACK),
        bgcolor=ft.colors.WHITE,
        width=parentsField,
        border_radius=fieldsBorderRadiusValue, cursor_radius=cursorRadiusValue,
        cursor_width=cursorWidthValue, cursor_height=cursorHeightValue,
        border_width=fieldBorderWidth,
        border_color=ft.colors.BLACK,
        text_style=ft.TextStyle(size=fontSize,
                                weight=ft.FontWeight.BOLD,
                                font_family="Ubuntu",
                                color=ft.colors.BLACK),
    )

    students_tribe = ft.TextField(label="Student's tribe",
                                  label_style=ft.TextStyle(size=fontSize - 5,
                                                           weight=ft.FontWeight.NORMAL,
                                                           font_family="Ubuntu",
                                                           color=ft.colors.BLACK),
                                  bgcolor=ft.colors.WHITE,
                                  width=parentsField,
                                  border_radius=fieldsBorderRadiusValue, cursor_radius=cursorRadiusValue,
                                  cursor_width=cursorWidthValue, cursor_height=cursorHeightValue,
                                  border_width=fieldBorderWidth,
                                  border_color=ft.colors.BLACK,
                                  text_style=ft.TextStyle(size=fontSize,
                                                          weight=ft.FontWeight.BOLD,
                                                          font_family="Ubuntu",
                                                          color=ft.colors.BLACK),
                                  )

    class_drop_down_field = ft.Dropdown(
        border_width=fieldBorderWidth,
        border_color=ft.colors.BLACK,
        text_style=ft.TextStyle(size=fontSize,
                                weight=ft.FontWeight.BOLD,
                                font_family="Ubuntu",
                                color=ft.colors.BLACK,
                                ),
        width=dropDownFieldWidth + 55,
        label="Class",
        hint_text=classDropDownFieldHintText,
        options=[
            ft.dropdown.Option(mallama_Azumi),
            ft.dropdown.Option(mallama_Rabi),
            ft.dropdown.Option(mallam_Musah),
            ft.dropdown.Option(mallam_Awal),
            ft.dropdown.Option(mallam_Sahnun),
            ft.dropdown.Option(mallam_Umar),
            ft.dropdown.Option(mallam_Haadi),
        ],
        border_radius=fieldsBorderRadiusValue,
    )

    gender_dropdown_field = ft.Dropdown(
        color=ft.colors.BLACK,
        bgcolor=ft.colors.WHITE,
        border_width=fieldBorderWidth,
        border_color=ft.colors.BLACK,
        text_style=ft.TextStyle(size=fontSize,
                                weight=ft.FontWeight.BOLD,
                                font_family="Ubuntu",
                                color=ft.colors.BLACK,
                                ),
        width=dropDownFieldWidth,
        label="Gender",
        hint_text=genderDropDownFieldHintText,
        options=[
            ft.dropdown.Option("Male"),
            ft.dropdown.Option("Female"),
        ],
        border_radius=fieldsBorderRadiusValue,
    )

    dob_day_drp_dwn_field = ft.Dropdown(
        color=ft.colors.BLACK,
        bgcolor=ft.colors.WHITE,
        border_width=fieldBorderWidth,
        border_color=ft.colors.BLACK,
        text_style=ft.TextStyle(size=fontSize,
                                weight=ft.FontWeight.BOLD,
                                font_family="Ubuntu",
                                color=ft.colors.BLACK,
                                ),
        width=dobColumnsWidth,
        label="Day",
        hint_text="DD",
        border_radius=fieldsBorderRadiusValue,
        options=[ft.dropdown.Option(str(number)) for number in range(1, 32)],
    )

    dob_month_drp_dwn_field = ft.Dropdown(
        color=ft.colors.BLACK,
        bgcolor=ft.colors.WHITE,
        border_width=fieldBorderWidth,
        border_color=ft.colors.BLACK,
        text_style=ft.TextStyle(size=fontSize,
                                weight=ft.FontWeight.BOLD,
                                font_family="Ubuntu",
                                color=ft.colors.BLACK,
                                ),
        width=dobColumnsWidth+40,
        label="Month",
        hint_text="MM",
        border_radius=fieldsBorderRadiusValue,
        options=[ft.dropdown.Option(month)
                 for month in months_of_the_yr],
    )

    dob_year_drp_dwn_field = ft.Dropdown(
        color=ft.colors.BLACK,
        bgcolor=ft.colors.WHITE,
        border_width=fieldBorderWidth,
        border_color=ft.colors.BLACK,
        text_style=ft.TextStyle(size=fontSize,
                                weight=ft.FontWeight.BOLD,
                                font_family="Ubuntu",
                                color=ft.colors.BLACK,
                                ),
        width=dobColumnsWidth,
        label="Year",
        hint_text="YYYY",
        border_radius=fieldsBorderRadiusValue,
        options=[ft.dropdown.Option(str(year)) for year in range(2000, 2023)],
    )

    dob_intro_text = ft.Text(value="Date of birth:",                             
                             color=ft.colors.BLACK, size=fontSize - 3,
                             weight=ft.FontWeight.BOLD,
                             font_family="Ubuntu",
                             selectable=True,)

    def onBackutonClicked():
        '''
        You can come to the edit page in three ways\n 
        1- ListView page student tile is clicked when selected action for the listView page is Edit Action or\n   
        2- ListView page using the edit button when the selection action for the listView is not Edit Action and\n  
        2- Profile page's edit button.
        
        So to go back to the previous page we need to check what was the previous page:\n
        if the previous page was the PROFILE PAGE, then it came from the student listView where selected action is Edit Action\n 
        \tWe should go back to profile page whiles providing id of student so that the data about the student can displayed and \n
        \talso class of the student so that the listView page can show students of a specific class, incase the user goes back\n
        \tto the student listView page from the profile page.\n  
        \tSo we go back to the profile page without providing Action context because you can come to the student profile page\n
        \tWITH ONLY ONE ACTION CONTEXT and that is the View Profile Action context so we don't need to specify which action context\n 
        \tthe list view gave the profile page becuase there can be only one action context and no confusion will occur\n 
        \twhen going back to the list view from the profile page.\n
        elif the previous page was STUDENT'S LISTVIEW then:\n
          \tWe should go back to the listView whiles providing it with the id along with the action selected for it,\n
          \tso as to not break the context, the listView should always have an Action Context.\n
        else if it was not from list View or profile page then it not edit mode but add student mode:\n 
          \tthat only comes from the landing page so we go back to the landing page\n 
        '''
        if editMode:
            dbObj = DarulQuranDb(connection=sqlite3.connect(dataBaseName))
            className = dbObj.getStudentClassNameUsingId(id=idOfStudentToEdit)
            # print(f"TEST_EDIT_DATA-Here is previous page {previousPage} can it go to {showProfileAction}? : {previousPage == showProfileAction}")
            # print(f"TEST_EDIT_DATA-can go to {previousPage}? : {previousPage == listStudentsAction}")
            if previousPage == listStudentsAction:
                # print(f'TEST_EDIT_DATA-GO back to student listVIew page with className as {className} and selected action as :{selectedAction}')
                page.go(f"{studentsListViewPageRoute}/{className}-{selectedAction}")
            elif previousPage == showProfileAction:
                # gonig back to student profile page route with className and id of student 
                page.go(f"{studentProfileViewPageRoute}/{className}-{idOfStudentToEdit}")
            
        else:
            page.go(landingPageRoute)

    def pumpUserDataIntoEntryField(idOfStudentToEdit:int):
        students_first_name.value = theStudentsData[1] 
        students_middle_name.value = theStudentsData[2] 
        students_last_name.value = theStudentsData[3] 
        gender_dropdown_field.value = theStudentsData[4] 
        dob = theStudentsData[5].split("-")
        dob_day_drp_dwn_field.value = dob[0]
        dob_month_drp_dwn_field.value = [key for key,value in monthsToNumbersDicts.items() if value==int(dob[1])][0]
        dob_year_drp_dwn_field.value =  dob[2]  
        class_drop_down_field.value = theStudentsData[6] 
        fathers_name.value = theStudentsData[7] 
        mothers_name.value = theStudentsData[8] 
        fathers_telephone.value = f"0{theStudentsData[9]}" 
        mothers_telephone.value = f"0{theStudentsData[10]}" 
        students_tribe.value = theStudentsData[11] 
        student_location.value = theStudentsData[12]         
    
    if editMode == True:
        pumpUserDataIntoEntryField(idOfStudentToEdit=idOfStudentToEdit)

    def isPhoneNumberOk(e) -> str:
        
        # print(
        #     f"Here is the phone Number {len(fathers_telephone.value)} and length {len({mothers_telephone.value})}")
        if len(f"{fathers_telephone.value}{mothers_telephone.value}") == 10 or len(f"{fathers_telephone.value}{mothers_telephone.value}") == 20:
            for number, character in enumerate(f"{fathers_telephone.value}{mothers_telephone.value}", start=1):
                if not character.isalpha():
                    # print(LEGIT)
                    pass
                else:
                    # print(f"Here is the letter:{character} number{number}")
                    # print(MIXED_TYPE_ERROR)
                    return MIXED_TYPE_ERROR
            else:
                return LEGIT
        else:
            val = f"{fathers_telephone.value}{mothers_telephone.value}"
            # print(
            #     f"Here is the val: {val} and her is the length of the characters {len(val)}")
            # print(LENGTH_ERROR)
            return LENGTH_ERROR

    def onBttonClicked(e):
        student_first_name_value = students_first_name.value
        student_middle_name_value = students_middle_name.value
        student_last_name_value = students_last_name.value
        fathers_name_value = fathers_name.value
        mothers_name_value = mothers_name.value
        fathers_telephone_value = fathers_telephone.value
        mothers_telephone_value = mothers_telephone.value
        studens_tribe_value = students_tribe.value
        students_location_value = student_location.value
        students_gender = gender_dropdown_field.value
        students_class_value = class_drop_down_field.value
        dob_day_value = dob_day_drp_dwn_field.value
        dob_month_value = dob_month_drp_dwn_field.value
        dob_year_drp_year_value = dob_year_drp_dwn_field.value

        # FUNCTIONS TO USE

        def clearFields(e):
            students_first_name.value = ""
            students_middle_name.value = ""
            students_last_name.value = ""
            fathers_name.value = ""
            mothers_name.value = ""
            fathers_telephone.value = ""
            mothers_telephone.value = ""
            students_tribe.value = ""
            student_location.value = ""
            class_drop_down_field.value = genderDropDownFieldHintText
            gender_dropdown_field.value = genderDropDownFieldHintText
            dob_day_drp_dwn_field.value = "DD"
            dob_month_drp_dwn_field.value = "MM"
            dob_year_drp_dwn_field.value = "YYYY"

            students_first_name.update()
            students_middle_name.update()
            students_last_name.update()
            fathers_name.update()
            mothers_name.update()
            fathers_telephone.update()
            mothers_telephone.update()
            students_tribe.update()
            student_location.update()
            class_drop_down_field.update()
            gender_dropdown_field.update()
            dob_day_drp_dwn_field.update()
            dob_month_drp_dwn_field.update()
            dob_year_drp_dwn_field.update()
        
        def showErrorDialouges(message:str):
            alrtDialogue = ft.AlertDialog(
                title=ft.Text("Empty fields", size=15, text_align=ft.TextAlign.LEFT), 
                content = ft.Text(message, size=13, text_align=ft.TextAlign.LEFT), 
                actions_alignment=ft.MainAxisAlignment.CENTER,
            )

            page.dialog = alrtDialogue
            alrtDialogue.open = True
            page.update()


            
        #CHECK WHETHER  THE NOT NULL FIELDS ARE NULL SO AN ALERT DIALOGUE CAN BE SHOWN

        # ELSE IF ITS LENGHT ISSUE SHOW ALERT FOR THAT
        if isPhoneNumberOk(f"{fathers_telephone}{mothers_telephone}") == LENGTH_ERROR:
            checkPhoneNumberLength = ft.AlertDialog(
                title=ft.Text("Please, check the phone number length."), on_dismiss=lambda e: print("Dialog dismissed!")
            )
            page.dialog = checkPhoneNumberLength
            checkPhoneNumberLength.open = True
            page.update()
        # ELSE IF IT INVALID CHARACTER ISSUE SHOW ALERT FOR THAT
        elif isPhoneNumberOk(f"{fathers_telephone}{mothers_telephone}") == MIXED_TYPE_ERROR:
            ckeckPhoneNumberCharacters = ft.AlertDialog(
                title=ft.Text("Please, check phone the number, phone numbers cannot containt alphabets."),
                on_dismiss=lambda e: print("Dialog dismissed!")
            )
            page.dialog = ckeckPhoneNumberCharacters
            ckeckPhoneNumberCharacters.open = True
            page.update()
        elif students_first_name.value == "" or students_first_name == None:
            # errorMessages.append("Student first name cannot be empty")
            showErrorDialouges("Student first name cannot be empty")
        elif students_last_name.value == "" or students_last_name.value  == None:
            showErrorDialouges("Student last name cannot be empty")
            # errorMessages.append("Student last name cannot be empty") 
        elif dob_day_drp_dwn_field.value == "" or dob_day_drp_dwn_field.value == None:
            showErrorDialouges("Day of birth has not been chosen.")
            # errorMessages.append("Day of birth has not been chosen.")
        elif dob_month_drp_dwn_field.value == "" or dob_month_drp_dwn_field.value == None:
            showErrorDialouges("Month of birth has not been chosen")
            # errorMessages.append("Month of birth has not been chosen")  
        elif dob_year_drp_dwn_field.value == "" or dob_year_drp_dwn_field.value == None:
            showErrorDialouges("Year of birth has not been chosen")
            # errorMessages.append("Year of birth has not been chosen")  
        elif class_drop_down_field.value == "" or class_drop_down_field.value == None:
            showErrorDialouges("Student's class has not been chosen")
            # errorMessages.append("Student's class has not been chosen")  
        elif gender_dropdown_field.value == "" or gender_dropdown_field.value == None:
            showErrorDialouges("Student's gender has not been chosen")
            # errorMessages.append("Student's gender has not been chosen")  
        elif fathers_name.value == "" or fathers_name.value == None:
            showErrorDialouges("Father's name cannot be empty")
            # errorMessages.append("Father's name cannot be empty")  
        elif mothers_name.value == "" or mothers_name.value == None:
            showErrorDialouges("Mother's name cannot be empty")
            # errorMessages.append("Mother's name cannot be empty")  
                # CHECK WHETHER PHONE NUMBER IS OK
        elif student_location.value == "" or student_location.value == None:
            showErrorDialouges("Student location cannot be empty")
        elif fathers_telephone.value == "0000000000":
            showErrorDialouges("Phone number cannot be only zeros.")
        elif list(fathers_telephone.value)[0] != "0" or list(mothers_telephone.value)[0] != "0":
            print(f"the first char show {list(mothers_telephone.value)[0]}")
            showErrorDialouges("Phone number should start with a zero.")     
        elif isPhoneNumberOk(f"{fathers_telephone}{mothers_telephone}") == LEGIT:
            action = "edit" if editMode else "write"
            # ASK USER TO CONFIRM WRITE IF CONFIRMED
            alrtDialogue = ft.AlertDialog(
                title=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Text(text_align=ft.TextAlign.LEFT,
                                value=f"Are you sure you want to {action} this data to the database", size=15),
                        ft.Text(text_align=ft.TextAlign.LEFT,
                                value=f"Student first name: {students_first_name.value}", size=10),
                        ft.Text(text_align=ft.TextAlign.LEFT,
                                value=f"Student middle name: {students_middle_name.value}", size=10),
                        ft.Text(text_align=ft.TextAlign.LEFT,
                                value=f"Student last name: {students_last_name.value}", size=10),
                        ft.Text(text_align=ft.TextAlign.LEFT,
                                value=f"Student gender: { gender_dropdown_field.value}", size=10),
                        ft.Text(text_align=ft.TextAlign.LEFT,
                                value=f"student class: {class_drop_down_field.value}", size=10),
                        ft.Text(text_align=ft.TextAlign.LEFT,
                                value=f"Father's full name: {fathers_name.value}", size=10),
                        ft.Text(text_align=ft.TextAlign.LEFT,
                                value=f"Mother's full name: { mothers_name.value}", size=10),
                        ft.Text(text_align=ft.TextAlign.LEFT,
                                value=f"Father's tele: {fathers_telephone.value}", size=10),
                        ft.Text(text_align=ft.TextAlign.LEFT,
                                value=f"Mother's tele: {mothers_telephone.value}", size=10),
                        ft.Text(text_align=ft.TextAlign.LEFT,
                                value=f"Student's tribe: {students_tribe.value}", size=10),
                        ft.Text(text_align=ft.TextAlign.LEFT,
                                value=f"Student's location: {student_location.value}", size=10)

                    ]
                ),
                actions=[
                    ft.ElevatedButton(
                        "Yes", on_click=lambda e: hasConsentedToWrite(e),
                        icon=ft.icons.THUMB_UP, color=ft.colors.BLUE_600,
                        bgcolor=ft.colors.WHITE, elevation=10),
                    ft.ElevatedButton("No", on_click=lambda e: hasNotConsented(
                        e), icon=ft.icons.THUMB_DOWN, color=ft.colors.BLUE_600,
                        bgcolor=ft.colors.WHITE, elevation=10),
                ],
                actions_alignment=ft.MainAxisAlignment.SPACE_AROUND,
                on_dismiss=lambda: print("Dialog dismissed!")
            )

            # SHOW THE ALERT DIALOGUE
            page.dialog = alrtDialogue
            alrtDialogue.open = True
            page.update()

            # FUNCTIONS FOR BUTTON
            def hasConsentedToWrite(e):
                # ASSIGN A NEW ID TO THE CURRENT STUDENT
                addOrEditDbObj = DarulQuranDb(connection = sqlite3.connect(dataBaseName, isolation_level=None))
                if editMode == False:
                    addOrEditDbObj.addStudentToDB(
                        student_first_nameVal=student_first_name_value,
                        student_middle_nameVal=student_middle_name_value,
                        student_last_nameVal=student_last_name_value,
                        students_genderVal=students_gender,
                        d_o_bVal=f"{dob_day_value}-{monthsToNumbersDicts[dob_month_value]}-{dob_year_drp_year_value}",
                        students_classVal=students_class_value,
                        fathers_nameVal=fathers_name_value,
                        mothers_nameVal=mothers_name_value,
                        fathers_telephoneVal=fathers_telephone_value,
                        mothers_telephoneVal=mothers_telephone_value,
                        studens_tribeVal=studens_tribe_value,
                        students_locationVal=students_location_value                    
                    )
                else:
                    addOrEditDbObj.editStudentData(
                        idVal=idOfStudentToEdit,
                        student_first_nameVal=student_first_name_value,
                        student_middle_nameVal=student_middle_name_value,
                        student_last_nameVal=student_last_name_value,
                        students_genderVal=students_gender,
                        d_o_bVal=f"{dob_day_value}-{monthsToNumbersDicts[dob_month_value]}-{dob_year_drp_year_value}",
                        students_classVal=students_class_value,
                        fathers_nameVal=fathers_name_value,
                        mothers_nameVal=mothers_name_value,
                        fathers_telephoneVal=fathers_telephone_value,
                        mothers_telephoneVal=mothers_telephone_value,
                        studens_tribeVal=studens_tribe_value,
                        students_locationVal=students_location_value                    
                    )

                # CLOSE CONFIRM WRITE DIALOGUE
                alrtDialogue.open = False
                page.update()
                # CLEAR THE FILEDS
                if not editMode:
                    clearFields(e)

            def hasNotConsented(e):
                ft.AlertDialog(title=ft.Text("Ok,  Cancelling..."))
                # CLOSE CONFIRM WRITE DIALOGUE
                alrtDialogue.open = False
                page.update()

            # ELSE DO NOT WRITE DATA

    addStudentPageView: ft.View = ft.View(
        route=addStudentPageRoute,
        controls=[
            ft.Column(
                controls=[
                    ft.Row(controls=[
                        backButton,
                    ],),
                    ft.Container(
                        border=ft.border.all(
                            width=containerBorderWidth, color=containerBorderColor),
                        margin=ft.Margin(
                            left=10, right=10,
                            top=30, bottom=10,
                        ),
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            stops=[0.3, 1.0],
                            colors=[ft.colors.BLUE_100,
                                                ft.colors.CYAN],
                        ),
                        content=ft.Column(
                            controls=[
                                ft.ResponsiveRow(controls=[
                                    ft.Container(students_first_name, col={
                                                 "sm": 6, "md": 4, "xl": 4}, margin=10),
                                    ft.Container(students_middle_name, col={
                                                 "sm": 6, "md": 4, "xl": 4}, margin=10),
                                    ft.Container(students_last_name, col={
                                                 "sm": 6, "md": 4, "xl": 4}, margin=10),
                                ],
                                ),
                                ft.ResponsiveRow(
                                    controls=[
                                        ft.Container(dob_intro_text, col={
                                                     "sm": 3, "md": 3, "xl": 3}, margin=10),
                                        ft.Container(dob_day_drp_dwn_field, col={
                                                     "sm": 2, "md": 2, "xl": 2}, margin=10),
                                        ft.Container(dob_month_drp_dwn_field, col={
                                                     "sm": 4, "md": 3, "xl": 3}, margin=10),
                                        ft.Container(dob_year_drp_dwn_field, col={
                                                     "sm": 4, "md": 3, "xl": 3}, margin=10),
                                    ],
                                ),
                                ft.ResponsiveRow(
                                    [
                                        ft.Container(class_drop_down_field, col={
                                                     "sm": 3.8, "md": 3.8, "xl": 3.8}, margin=10),
                                        ft.Container(gender_dropdown_field, col={
                                                     "sm": 3, "md": 3, "xl": 3}, margin=10),
                                    ]
                                ),
                                ft.Column(controls=[
                                    ft.Container(fathers_name, col={
                                                 "sm": 3, "md": 3, "xl": 3}, margin=10),
                                    ft.Container(mothers_name, col={
                                                 "sm": 3, "md": 3, "xl": 3}, margin=10),
                                    ft.ResponsiveRow(
                                        [
                                            ft.Container(fathers_telephone, col={
                                                         "sm": 4, "md": 4, "xl": 4}, margin=10),
                                            ft.Container(mothers_telephone, col={
                                                         "sm": 4, "md": 4, "xl": 4}, margin=10),
                                        ]
                                    ),
                                    ft.Container(student_location, col={
                                                 "sm": 3, "md": 3, "xl": 3}, margin=10),
                                    ft.Container(students_tribe, col={
                                                 "sm": 3, "md": 3, "xl": 3}, margin=10),
                                ],),
                            ],
                        ),
                        width=800,
                        bgcolor=ft.colors.WHITE30,
                        border_radius=20,
                        padding=20,
                        alignment=ft.alignment.center,
                    ),
                    ft.Column(controls=[
                        ft.Container(
                            margin=15,
                            content=ft.ElevatedButton(
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(
                                            name=ft.icons.DONE_OUTLINE_OUTLINED, color="pink"),
                                        ft.Text(
                                            value="  Done", size=20),
                                    ],
                                    vertical_alignment="center"),
                                width=175, height=50,
                                icon_color="green400",
                                on_click=onBttonClicked),
                        ),
                    ],
                        width=800,
                        horizontal_alignment="center",)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ]
    )
    addStudentPageView.bgcolor = ft.colors.WHITE
    addStudentPageView.scroll = ft.ScrollMode.ADAPTIVE
    return addStudentPageView


def landingPage(page=ft.Page) -> ft.View:
    page.title = APP_NAME
    
    page.theme_mode = ft.ThemeMode.LIGHT

    ft.AnimatedSwitcher(
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
        )
    def onTileHover(e:ft.HoverEvent):
        if e.data == "true":
            e.control.width = containerWidth + 15
            e.control.height = containerHeight + 15
            e.control.bgcolor = ft.colors.WHITE
            e.control.update()
        else:
            addStudentsCard.width = containerWidth
            addStudentsCard.height = containerHeight
            e.control.width = containerWidth
            e.control.height = containerHeight
            e.control.bgcolor = ft.colors.WHITE
            e.control.update()

    containerWidth, containerHeight = 150, 150
    theBarHeight = 22
    theBarWidth = 1400
    containerShadowSpread = 30
    cardMargin = 20
    tileAnimationDuration = 1000

    theBar: ft.Container = ft.Container(content=ft.Text(
        value="Student database operations", size=15, weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK, font_family="Mafia"
    ),
        margin=ft.Margin(
        top=0, left=0,
        right=0, bottom=0
    ),
        padding=ft.Padding(
        top=0, left=10,
        right=0, bottom=0
    ),
        border_radius=ft.BorderRadius(bottomLeft=10,
                                      bottomRight=10,
                                      topLeft=0,
                                      topRight=0
                                      ),
        bgcolor=ft.colors.WHITE,
        width=theBarWidth,
        height=theBarHeight,
    )

    addStudentTile: ft.Container = ft.Container(
        animate = ft.animation.Animation(tileAnimationDuration, "bounceOut"),
        on_hover=lambda hoverEvent: onTileHover(e=hoverEvent),
        on_click=lambda _: page.go(addStudentPageRoute),
        width=containerWidth, height=containerHeight,
        ink=True,
        padding=15,
        border_radius=14,
        content=ft.Image(src=addUserTileIcon),
        bgcolor=ft.colors.WHITE,
        margin=ft.Margin(
            top=0, left=0,
            right=0, bottom=0
        ),

    )

    removeStudentTile: ft.Container = ft.Container(
        on_hover=lambda hoverEvent: onTileHover(e=hoverEvent),
        animate=ft.animation.Animation(tileAnimationDuration, "bounceOut"),
        on_click=lambda _: page.go(f"{selectStudentClassRoute}/{delAction}"),
        width=containerWidth, height=containerHeight,
        ink=True,
        padding=15,
        border_radius=14,
        content=ft.Image(src=removeUserTileIcon),
        bgcolor=ft.colors.WHITE,
        margin=ft.Margin(
            top=0, left=0,
            right=0, bottom=0
        ),
    )

    editStudentTile: ft.Container = ft.Container(
        animate=ft.animation.Animation(tileAnimationDuration, "bounceOut"),
        on_hover=lambda hoverEvent: onTileHover(e=hoverEvent),
        on_click=lambda _: page.go(f"{selectStudentClassRoute}/{editAction}"),
        width=containerWidth, height=containerHeight,
        ink=True,
        padding=15,
        border_radius=14,
        content=ft.Image(src=editStudentTileIcon),
        bgcolor=ft.colors.WHITE,
        margin=ft.Margin(
            top=0, left=0,
            right=0, bottom=0
        ),
    )

    showStudentProfileTile: ft.Container = ft.Container(
        on_hover=lambda hoverEvent: onTileHover(e=hoverEvent),
        animate=ft.animation.Animation(tileAnimationDuration, "bounceOut"),
        on_click=lambda _: page.go(f"{selectStudentClassRoute}/{showProfileAction}"),
        width=containerWidth, height=containerHeight,
        ink=True,
        padding=15,
        border_radius=14,
        content=ft.Image(src=showStudentProfileTileIcon),
        bgcolor=ft.colors.WHITE,
        margin=ft.Margin(
            top=0, left=0,
            right=0, bottom=0
        ),
    )

    listStudentsTile: ft.Container = ft.Container(
        on_hover=lambda hoverEvent: onTileHover(e=hoverEvent),
        animate=ft.animation.Animation(tileAnimationDuration, "bounceOut"),
        on_click=lambda _: page.go(f"{selectStudentClassRoute}/{listStudentsAction}"),
        width=containerWidth, height=containerHeight,
        ink=True,
        padding=15,
        border_radius=14,
        content=ft.Image(src=listUsersTileIcon),
        bgcolor=ft.colors.WHITE,
        margin=ft.Margin(
            top=0, left=0,
            right=0, bottom=0
        ),
    )

    addStudentsCard = ft.Card(content=addStudentTile,
                              elevation=containerShadowSpread,
                              margin=cardMargin
                              )
    removeStudentCard = ft.Card(content=removeStudentTile,
                                elevation=containerShadowSpread,
                                margin=cardMargin
                                )
    editStudentCard = ft.Card(content=editStudentTile,
                                elevation=containerShadowSpread,
                                margin=cardMargin
                                )
    showStudentProfileCard = ft.Card(content=showStudentProfileTile,
                                elevation=containerShadowSpread,
                                margin=cardMargin
                                )
    listStudentsProfileCard = ft.Card(content=listStudentsTile,
                                elevation=containerShadowSpread,
                                margin=cardMargin
                                )

    landingPageView: ft.View = ft.View(
        route=landingPageRoute,
        controls=[
            # page.add(
            ft.Column(
                # width=theBarWidth,
                #   height=containerHeight + 50,
                controls=[
                    ft.Card(content=theBar, elevation=20,
                                    height=theBarHeight + 15, ),
                    ft.ResponsiveRow(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                col={"sm": 6, "md": 4, "xl": 2},
                                margin=ft.Margin(
                                    top=20, bottom=0, left=0, right=0),
                                content=ft.Column(
                                    controls=[
                                        addStudentsCard,
                                        ft.Container(
                                            content=ft.Text(
                                                value="Add Student Data", text_align=ft.TextAlign.CENTER,),
                                            width=containerWidth, margin=ft.Margin(
                                                top=10, bottom=10, left=20, right=10)
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                )
                            ),
                            ft.Container(
                                col={"sm": 6, "md": 4, "xl": 2},
                                margin=ft.Margin(
                                    top=20, bottom=0, left=0, right=0),
                                content=ft.Column(
                                    controls=[
                                        removeStudentCard,
                                        ft.Container(
                                            content=ft.Text(
                                                value="Remove Student Data", text_align=ft.TextAlign.CENTER,),
                                            width=containerWidth, margin=ft.Margin(
                                                top=10, bottom=10, left=20, right=10)
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                )
                            ),
                            ft.Container(
                                col={"sm": 6, "md": 4, "xl": 2},
                                margin=ft.Margin(
                                    top=20, bottom=0, left=0, right=0),
                                content=ft.Column(
                                    controls=[
                                        editStudentCard,
                                        ft.Container(
                                            content=ft.Text(
                                                value="Edit Student Data", text_align=ft.TextAlign.CENTER,),
                                            width=containerWidth, margin=ft.Margin(
                                                top=10, bottom=10, left=20, right=10)
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                )
                            ),
                            ft.Container(
                                col={"sm": 6, "md": 4, "xl": 2},
                                margin=ft.Margin(
                                    top=20, bottom=0, left=0, right=0),
                                content=ft.Column(
                                    controls=[
                                        showStudentProfileCard,
                                        ft.Container(
                                            content=ft.Text(
                                                value="Show Student's Profile", text_align=ft.TextAlign.CENTER,),
                                            width=containerWidth, margin=ft.Margin(
                                                top=10, bottom=10, left=20, right=10)
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                )
                            ),
                            ft.Container(
                                col={"sm": 6, "md": 4, "xl": 2},
                                margin=ft.Margin(
                                    top=20, bottom=0, left=0, right=0),
                                content=ft.Column(
                                    controls=[
                                        listStudentsProfileCard,
                                        ft.Container(
                                            content=ft.Text(
                                                value="List Students", text_align=ft.TextAlign.CENTER,),
                                            width=containerWidth, margin=ft.Margin(
                                                top=10, bottom=10, left=20, right=10)
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                )
                            )
                        ]
                    )
                ]
            )
        ]
    )
    landingPageView.scroll =  ft.ScrollMode.ALWAYS

    landingPageView.padding = 0
    page.padding = 0
    page.update()
    return landingPageView


def selectClassPage(page: ft.Page, action:str) -> ft.View:
    page.title = f"Select class - {APP_NAME}"

    parentContainerBackgroundColor: ft.colors = containerBgColor
    parentContainerWidth = 1000
    containerBackgrounColor: ft.colors = ft.colors.WHITE
    containerWidth = parentContainerWidth-200
    # containerBorderWidth = containerBorderWidth
    containerChildernPadding = 10
    # containerBorderColor: ft.colors = containerBorderColor
    # borderRadiusForEverything = borderRadiusForEverything
    marginForContainer = 20
    containerHeight = 90
    marginBetweenNameAndIcon = 20
    fontsColor: ft.colors = ft.colors.BLACK
    fontsSize = 24
    iconsSize = 35
    iconsColor: ft.colors = ft.colors.BLACK
    haadisTileData = mallam_Haadi
    umarTileData = mallam_Umar
    sSahnunTileData = mallam_Sahnun
    awalTileData = mallam_Awal
    musahTileData = mallam_Musah
    rabiTileData = mallama_Rabi
    azuminTileData = mallama_Azumi
    tileAnimationDuration = 500

    def onContainerClick(e: ft.ControlEvent, className: str):
        page.go(f"{studentsListViewPageRoute}/{className}-{action}")

    def onContainerHover(e: ft.ControlEvent):
        if e.data == "true":
            control: ft.Control = e.control
            control.width = containerWidth + 50
            control.height = containerHeight + 20
            control.bgcolor = "lightgreen200" if control.bgcolor == "white" else "lightgreen200"
            control.update()
        else:
            control: ft.Control = e.control
            control.width = containerWidth
            control.height = containerHeight
            control.bgcolor = "white" if control.bgcolor == "lightgreen200" else "white"
            page.update()
            pass

    backButton: ft.Control = ft.ElevatedButton(
        on_click=lambda _: page.go(landingPageRoute),
        color=ft.colors.BLUE_300,
        text="back",
        icon=ft.icons.ARROW_BACK_SHARP
    )

    listTileHadi: ft.Container = ft.Container(
        col={"sm": 12, "md": 12, "xl": 12},
        animate=ft.animation.Animation(tileAnimationDuration, "bounceOut"),
        margin=marginForContainer,
        data=haadisTileData,
        on_hover=lambda e: onContainerHover(e=e),
        on_click=lambda e: onContainerClick(e=e, className=e.control.data),
        bgcolor=containerBackgrounColor, border_radius=borderRadiusForEverything,
        border=ft.border.all(width=containerBorderWidth,
                             color=containerBorderColor),
        padding=containerChildernPadding, width=containerWidth, height=containerHeight,
        content=ft.Row(
            controls=[ft.Row(
                controls=[
                    ft.Container(content=ft.Icon(
                        ft.icons.PERSON, color=iconsColor, size=iconsSize), margin=marginBetweenNameAndIcon),
                    ft.Text(mallam_Haadi,
                            color=fontsColor, size=fontsSize),
                ],
            ),
                ft.Row(
                        controls=[ft.Icon(name=ft.icons.ARROW_CIRCLE_RIGHT, 
                       color=iconsColor, size=iconsSize)],
                       alignment=ft.MainAxisAlignment.END),

            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    umarListTile: ft.Container = ft.Container(
        animate=ft.animation.Animation(tileAnimationDuration, "bounceOut"),
        data=umarTileData,
        margin=marginForContainer,
        on_hover=lambda e: onContainerHover(e=e),
        on_click=lambda e: onContainerClick(e=e, className=e.control.data),
        bgcolor=containerBackgrounColor, border_radius=borderRadiusForEverything,
        border=ft.border.all(width=containerBorderWidth,
                             color=containerBorderColor),
        padding=containerChildernPadding, width=containerWidth, height=containerHeight,
        content=ft.Row(
            controls=[ft.Row(
                controls=[
                    ft.Container(content=ft.Icon(
                        ft.icons.PERSON, color=iconsColor, size=iconsSize), margin=marginBetweenNameAndIcon),
                    ft.Text(mallam_Umar,
                            color=fontsColor, size=fontsSize),
                ],
            ),
                ft.Row(controls=[ft.Icon(name=ft.icons.ARROW_CIRCLE_RIGHT,
                       color=iconsColor, size=iconsSize)], alignment=ft.MainAxisAlignment.END),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    sSahnunListTile: ft.Container = ft.Container(
        animate=ft.animation.Animation(tileAnimationDuration, "bounceOut"),
        data=sSahnunTileData,
        margin=marginForContainer,
        on_hover=lambda e: onContainerHover(e=e),
        on_click=lambda e: onContainerClick(e=e, className=e.control.data),
        bgcolor=containerBackgrounColor, border_radius=borderRadiusForEverything,
        border=ft.border.all(width=containerBorderWidth,
                             color=containerBorderColor),
        padding=containerChildernPadding, width=containerWidth, height=containerHeight,
        content=ft.Row(
            controls=[ft.Row(
                controls=[
                    ft.Container(content=ft.Icon(
                        ft.icons.PERSON, color=iconsColor, size=iconsSize), margin=marginBetweenNameAndIcon),
                    ft.Text(mallam_Sahnun,
                            color=fontsColor, size=fontsSize),
                ],
            ),
                ft.Row(controls=[ft.Icon(name=ft.icons.ARROW_CIRCLE_RIGHT,
                       color=iconsColor, size=iconsSize)], alignment=ft.MainAxisAlignment.END),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )
    awalListTile: ft.Container = ft.Container(
        animate=ft.animation.Animation(tileAnimationDuration, "bounceOut"),
        data=awalTileData,
        margin=marginForContainer,
        on_hover=lambda e: onContainerHover(e=e),
        on_click=lambda e: onContainerClick(e=e, className=e.control.data),
        bgcolor=containerBackgrounColor, border_radius=borderRadiusForEverything,
        border=ft.border.all(width=containerBorderWidth,
                             color=containerBorderColor),
        padding=containerChildernPadding, width=containerWidth, height=containerHeight,
        content=ft.Row(
            controls=[ft.Row(
                controls=[
                    ft.Container(content=ft.Icon(
                        ft.icons.PERSON, color=iconsColor, size=iconsSize), margin=marginBetweenNameAndIcon),
                    ft.Text(mallam_Awal,
                            color=fontsColor, size=fontsSize),
                ],
            ),
                ft.Row(controls=[ft.Icon(name=ft.icons.ARROW_CIRCLE_RIGHT,
                       color=iconsColor, size=iconsSize)], alignment=ft.MainAxisAlignment.END),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )
    musahListTile: ft.Container = ft.Container(
        animate=ft.animation.Animation(tileAnimationDuration, "bounceOut"),
        data=musahTileData,
        margin=marginForContainer,
        on_hover=lambda e: onContainerHover(e=e),
        on_click=lambda e: onContainerClick(e=e, className=e.control.data),
        bgcolor=containerBackgrounColor, border_radius=borderRadiusForEverything,
        border=ft.border.all(width=containerBorderWidth,
                             color=containerBorderColor),
        padding=containerChildernPadding, width=containerWidth, height=containerHeight,
        content=ft.Row(
            controls=[ft.Row(
                controls=[
                    ft.Container(content=ft.Icon(
                        ft.icons.PERSON, color=iconsColor, size=iconsSize), margin=marginBetweenNameAndIcon),
                    ft.Text(mallam_Musah,
                            color=fontsColor, size=fontsSize),
                ],
            ),
                ft.Row(controls=[ft.Icon(name=ft.icons.ARROW_CIRCLE_RIGHT,
                       color=iconsColor, size=iconsSize)], alignment=ft.MainAxisAlignment.END),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )
    rabiListTile: ft.Container = ft.Container(
        animate=ft.animation.Animation(tileAnimationDuration, "bounceOut"),
        data=rabiTileData,
        margin=marginForContainer,
        on_hover=lambda e: onContainerHover(e=e),
        on_click=lambda e: onContainerClick(e=e, className=e.control.data),
        bgcolor=containerBackgrounColor, border_radius=borderRadiusForEverything,
        border=ft.border.all(width=containerBorderWidth,
                             color=containerBorderColor),
        padding=containerChildernPadding, width=containerWidth, height=containerHeight,
        content=ft.Row(
            controls=[ft.Row(
                controls=[
                    ft.Container(content=ft.Icon(
                        ft.icons.PERSON, color=iconsColor, size=iconsSize), margin=marginBetweenNameAndIcon),
                    ft.Text(mallama_Rabi,
                            color=fontsColor, size=fontsSize),
                ],
            ),
                ft.Row(controls=[ft.Icon(name=ft.icons.ARROW_CIRCLE_RIGHT,
                       color=iconsColor, size=iconsSize)], alignment=ft.MainAxisAlignment.END),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )
    azuminListTile: ft.Container = ft.Container(
        animate=ft.animation.Animation(tileAnimationDuration, "bounceOut"),
        data=azuminTileData,
        margin=marginForContainer,
        on_hover=lambda e: onContainerHover(e=e),
        on_click=lambda e: onContainerClick(e=e, className=e.control.data),
        bgcolor=containerBackgrounColor, border_radius=borderRadiusForEverything,
        border=ft.border.all(width=containerBorderWidth,
                             color=containerBorderColor),
        padding=containerChildernPadding, width=containerWidth, height=containerHeight,
        content=ft.Row(
            controls=[ft.Row(
                controls=[
                    ft.Container(content=ft.Icon(
                        ft.icons.PERSON, color=iconsColor, size=iconsSize), margin=marginBetweenNameAndIcon),
                    ft.Text(mallama_Azumi,
                            color=fontsColor, size=fontsSize),
                ],
            ),
                ft.Row(controls=[ft.Icon(name=ft.icons.ARROW_CIRCLE_RIGHT,
                       color=iconsColor, size=iconsSize)], alignment=ft.MainAxisAlignment.END),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    selectClassViewObj = ft.View(
        route=selectStudentClassRoute,
        controls=[
            ft.Row(
                [
                    backButton
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.ResponsiveRow(
                controls=[
                    ft.Container(
                        col={"sm": 12, "md": 8, "xl": 8},
                        alignment=ft.alignment.center,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            stops=[0.5, 1.0],
                            colors=[ft.colors.BLUE_50, ft.colors.CYAN_400],
                        ),
                        width=parentContainerWidth,
                        bgcolor=parentContainerBackgroundColor, border_radius=borderRadiusForEverything,
                        border=ft.border.all(
                            width=containerBorderWidth, color=containerBorderColor),
                        padding=containerChildernPadding,
                        content=ft.Column(
                            controls=[
                                ft.Text(value="Select a class to perform operation.", color=fontsColor,
                                        style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                                ft.ResponsiveRow(controls=[listTileHadi],),
                                ft.ResponsiveRow(controls=[umarListTile],),
                                ft.ResponsiveRow(controls=[sSahnunListTile]),
                                ft.ResponsiveRow(controls=[awalListTile]),
                                ft.ResponsiveRow(controls=[musahListTile]),
                                ft.ResponsiveRow(controls=[rabiListTile]),
                                ft.ResponsiveRow(controls=[azuminListTile]),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]
    )

    selectClassViewObj.scroll = ft.ScrollMode.ADAPTIVE
    return selectClassViewObj



def studentsListView(page: ft.Page, params: str) -> ft.View:
    pageView: ft.View = ft.View(route=studentsListViewPageRoute,)
    pageView.scroll = ft.ScrollMode.ADAPTIVE
    className, selectedAction = params.split("-")[0], params.split("-")[1]
    sqliteObj = DarulQuranDb(connection=sqlite3.connect(dataBaseName, isolation_level=None))
    listOfStudentIdAndNames = sqliteObj.getAllStudentsIdsAndFullNamesInClass(className=className)
    page.title = f"{selectedAction} - {className}'s class - {APP_NAME}"


    foregroundColorForContainer = ft.colors.BLACK
    backgroundColorForContainer = ft.colors.WHITE
    confirmDeleteAlertDialouge = ft.AlertDialog()

    backButton: ft.Control = ft.ElevatedButton(
        on_click=lambda _: page.go(f"{selectStudentClassRoute}/{selectedAction}"),
        color=ft.colors.BLUE_300,
        text="back",
        icon=ft.icons.ARROW_BACK_SHARP
    )

    userIcon = ft.Container(content=ft.Icon(name=ft.icons.PERSON,
                                            color=foregroundColorForContainer, size=25),
                            border=ft.border.all(width=2, color=foregroundColorForContainer),
                            border_radius=100)
    
    def getCustomContainerWithNamesAndIds(id, firstName, middleName, lastName, rowObj)-> ft.Container:
            tileContainer=ft.Container(
            on_click=lambda e: containerOnclick(id= id, obj = rowObj),
            border=ft.border.all(
                width=5, color=foregroundColorForContainer),
            bgcolor=backgroundColorForContainer,
            border_radius=borderRadiusForEverything - 15,
            col={"sm": 12, "md": 12, "xl": 12},
            padding=10,
            ink=True,
            content=ft.ResponsiveRow(
                columns=12,
                controls=[
                    ft.Row(
                        col={"xs": 6, "sm": 9, "md": 10,"lg": 10, "xl": 10, "xxl": 10},
                        controls=[
                            userIcon,
                            ft.Container(ft.Text(f"{id}- {firstName} {middleName} {lastName}",
                                                 style=ft.TextStyle(color=foregroundColorForContainer, size=ft.TextThemeStyle.DISPLAY_MEDIUM),
                                                 color=foregroundColorForContainer),
                                         margin=ft.Margin(
                                             left=10, right=0, top=0, bottom=0),
                                         ),
                        ]
                    ),
                    ft.Row(
                        col={"xs": 4, "sm": 3, "md": 2, "lg": 2, "xl": 1, "xxl": 1},
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.EDIT,
                                icon_color=foregroundColorForContainer,
                                icon_size=25,
                                bgcolor=backgroundColorForContainer,
                                on_click=lambda _: goToEditData(id=id)
                            ),
                            ft.IconButton(
                                icon=ft.icons.DELETE,
                                icon_color=foregroundColorForContainer,
                                icon_size=25,
                                bgcolor=backgroundColorForContainer,
                                on_click=lambda _:deleteConfirmationDialogue(control=rowObj)
                            )
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
            )
            return tileContainer

    def deleteConfirmationDialogue(control:ft.Control):
        idValue = control.data["id"]
        listTileFromTileObj = control.data["controlObj"]
        saidStudentData = []
        for element in listOfStudentIdAndNames:
            if element[0] == idValue:
                saidStudentData = element

        confirmDeleteAlertDialouge.title = ft.Text(value="Do really wanna delete all data pertaining to this student.")
        confirmDeleteAlertDialouge.content = ft.Text(value=f"""
                            id:{saidStudentData[0]}
                            Name:{saidStudentData[1]} {saidStudentData[2]} {saidStudentData[3]} 
                            """)
        confirmDeleteAlertDialouge.actions = [ft.Row(controls=[
            ft.ElevatedButton(
                text="Yes",
                on_click=lambda _:hasConsentedDelete(control),
                icon=ft.icons.THUMB_UP, color=ft.colors.BLUE_600,
                bgcolor=ft.colors.WHITE, elevation=10),
            ft.ElevatedButton(text="No", on_click=lambda _:closeAlertDialogue(),
                              icon=ft.icons.THUMB_DOWN, color=ft.colors.BLUE_600,
                              bgcolor=ft.colors.WHITE, elevation=10),], alignment=ft.MainAxisAlignment.SPACE_AROUND,
        ), ]

        page.dialog = confirmDeleteAlertDialouge
        confirmDeleteAlertDialouge.open = True
        page.update()

    def closeAlertDialogue():
        confirmDeleteAlertDialouge.open = False
        page.update()

    def hasConsentedDelete(containerObj:ft.Control):
        id = containerObj.data["id"]
        sqliteObjForDel = DarulQuranDb(connection=sqlite3.connect(dataBaseName, isolation_level=None))
        sqliteObjForDel.deleteStudentsData(studentId=id)
        pageView.controls.remove(containerObj)
        confirmDeleteAlertDialouge.open = False
        pageView.update()
        page.update()

    def containerOnclick(id, obj:ft.Control):
        if selectedAction == delAction:
            deleteConfirmationDialogue(control=obj)
        elif selectedAction == editAction:
            goToEditData(id=id)
        elif selectedAction == showProfileAction or selectedAction == listStudentsAction:
            goToProfile(id=id)

    def goToEditData(id ):
        page.go(f"{editStudentPageViewRoute}/{id}-{listStudentsAction}-{selectedAction}")

    def goToProfile(id):
        page.go(f"{studentProfileViewPageRoute}/{className}-{id}")


    pageView.controls.append(backButton)
    for nameAndId in listOfStudentIdAndNames:
        id, firstName, middleName, lastName = nameAndId[0], nameAndId[1], nameAndId[2], nameAndId[3],
        responsiveStudentTile: ft.ResponsiveRow = ft.ResponsiveRow()

        theTile:list[ft.Control] = [
                getCustomContainerWithNamesAndIds(
                    id=id, 
                    firstName=firstName, 
                    middleName=middleName, 
                    lastName=lastName,
                    rowObj=responsiveStudentTile
                        ),
                    ]
        responsiveStudentTile.controls= theTile
        responsiveStudentTile.data= {"id": id, "controlObj": responsiveStudentTile}
        pageView.controls.append(responsiveStudentTile)


    return pageView



def ProfilePage(paramsFromPrevPage:str, page=ft.Page) -> ft.View:
    className, id = paramsFromPrevPage.split("-")[0], paramsFromPrevPage.split("-")[1]
    dbObj = DarulQuranDb(connection = sqlite3.connect(dataBaseName, isolation_level=None))
    "[0]Student Id"	
    "[1]Student first name"	
    "[2]Student middle name"	
    "[3]Student last name"	
    "[4]Student gender"	
    "[5]Student day of birth"	
    "[6]Student month of birth"	
    "[7]Student year of birth"	
    "[8]class"	
    "[9]fathers name"	
    "[10]mothers name"	
    "[11]fathers telephone"	
    "[12]mothers telephone"	
    "[13]students tribe"	
    "[14]students location" 
    # for sql
    "[0]Student Id"	
    "[1]Student first name"	
    "[2]Student middle name"	
    "[3]Student last name"	
    "[4]Student gender"	
    "[5]Student day of birth [0] Student month of birth [1] Student year of birth[2]"	
    "[6]class"	
    "[7]fathers name"	
    "[8]mothers name"	
    "[9]fathers telephone"	
    "[10]mothers telephone"	
    "[11]students tribe"	
    "[12]students location" 
    
    # listOfStudentsData = readSpecificStudentDataFromExcel(id=int(id), className=className)
    listOfStudentsData = dbObj.getSpecificStudentsFullData(id=int(id))[0]

    userId = id
    userFirstName, userMiddleName, LastName = listOfStudentsData[1], listOfStudentsData[2], listOfStudentsData[3]
    userGender = listOfStudentsData[4]
    userClass = className
    dob = listOfStudentsData[5].split("-")
    dob_day_drp_dwn_field = dob[0]
    dob_month_drp_dwn_field = [key for key,value in monthsToNumbersDicts.items() if value==int(dob[1])][0]
    dob_year_drp_dwn_field = dob[2] 
    userBirthDay = f"{dob_day_drp_dwn_field} {dob_month_drp_dwn_field}, {dob_year_drp_dwn_field}"
    userFathersName = listOfStudentsData[7]
    userMothersName = listOfStudentsData[8]
    usersFathersPhoneNo = listOfStudentsData[9]
    usersMothersPhoneNo = listOfStudentsData[10]
    userTribe = listOfStudentsData[11]
    userLocation = listOfStudentsData[12]
    page.title = f"{userFirstName} {userMiddleName}'s Profile - {APP_NAME}"

    stackWidth = 700
    stackHeight = 1290
    parentContainerHeight = 800
    parentContainerWidth = 620
    parentContainerBorderRadius = 40
    parentContainerAbsolute_bottom = 390
    parentContainerAbsolute_left = 40
    imageWidth = 150
    imageHeight = 150
    imageAbsolute_right = 280
    dataCardMargins = 10
    dataCardsWidth = parentContainerWidth-50
    dataFieldsContainerWidths = (dataCardsWidth-20)/2
    dataFieldsContainerHeight = 30
    dataFieldsContainerMargins = ft.Margin(
        left=10, right=10, bottom=10, top=10)

    def showAlertDialougForDeleteConformation(e: ft.TapEvent): 
        confirmDeleteAlertDialouge = ft.AlertDialog(
            title=ft.Text(
                value="Do really wanna delete all data pertaining to this student."),
            content=ft.Text(value=f"""
                                id:{listOfStudentsData[0]}
                                Name:{listOfStudentsData[1]} {listOfStudentsData[2]} {listOfStudentsData[3]} 
                                """),
            actions=[ft.Row(controls=[
                            ft.ElevatedButton(
                                text="Yes",
                                on_click=lambda e:hasConsentedDelete(e),
                                icon=ft.icons.THUMB_UP, color=ft.colors.BLUE_600,
                                bgcolor=ft.colors.WHITE, elevation=10),
                            ft.ElevatedButton(text="No", on_click=lambda e:hasNotConsentedDelete(e),
                                              icon=ft.icons.THUMB_DOWN, color=ft.colors.BLUE_600,
                                              bgcolor=ft.colors.WHITE, elevation=10),], alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            ), ],
        )
        page.dialog = confirmDeleteAlertDialouge
        confirmDeleteAlertDialouge.open = True
        page.update()

        def hasConsentedDelete(e):
            sqliteObjForDel = DarulQuranDb(connection=sqlite3.connect(dataBaseName, isolation_level=None))
            sqliteObjForDel.deleteStudentsData(studentId=id)
            confirmDeleteAlertDialouge.open = False
            page.update()
            page.go(f"{studentsListViewPageRoute}/{className}-{showProfileAction}")
            # print(f"Here is the route {studentsListViewPageRoute}/{className} and the Id is:{id}/className {className}")
            

        def hasNotConsentedDelete(e):
            confirmDeleteAlertDialouge.open = False
            page.update()

        

    backButton: ft.Control = ft.ElevatedButton(
        on_click=lambda _:page.go(f"{studentsListViewPageRoute}/{className}-{showProfileAction}"),
        color=ft.colors.BLUE_300,
        text="back",
        icon=ft.icons.ARROW_BACK_SHARP
    )
    
    editButton: ft.Control = ft.ElevatedButton(
        width=140,
        color=ft.colors.BLUE_300,
        text="Edit User",
        icon=ft.icons.EDIT,
        on_click = lambda _:page.go(f"{editStudentPageViewRoute}/{id}-{showProfileAction}-{editAction}")
    )

    deleteUserButton: ft.Control = ft.ElevatedButton(
        width=140,
        color=ft.colors.BLUE_300,
        text="Delete User",
        icon=ft.icons.PERSON_REMOVE,
        on_click=lambda e: showAlertDialougForDeleteConformation(e)
    )

    # page.add(
    studentProfileViewObj:ft.View = ft.View(route=studentProfileViewPageRoute,
            controls=[
                ft.Row(
                    controls=[backButton,
                              ft.Container(
                                  margin=ft.Margin(
                                      left=0, right=20, top=0, bottom=0),
                                  content=ft.Row(
                                      controls=[
                                          editButton,
                                          deleteUserButton
                                      ]
                                  ),
                              )
                              ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    controls=[
                        ft.Stack(
                            width=stackWidth,
                            height=stackHeight,
                            controls=[
                                ft.Container(
                                    border=ft.border.all(width=containerBorderWidth, color=containerBorderColor),
                                    height=parentContainerHeight, width=parentContainerWidth,
                                    border_radius=parentContainerBorderRadius,
                                    bottom=parentContainerAbsolute_bottom,
                                    left=parentContainerAbsolute_left,
                                    gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.alignment.bottom_center,
                                        stops=[],
                                        colors=[ft.colors.BLUE_100,
                                                ft.colors.CYAN],
                                    ),
                                    content=ft.Column(
                                        controls=[
                                            ft.Container(
                                                margin=ft.Margin(
                                                    top=55, bottom=10, left=10, right=10),
                                                alignment=ft.alignment.center,
                                                content=ft.Text(selectable=True,
                                                                value=f"{userFirstName} {LastName}",
                                                                style=ft.TextThemeStyle.HEADLINE_LARGE,
                                                                color=ft.colors.PURPLE,
                                                                ),  
                                            ),
                                            ft.Container(
                                                border_radius=parentContainerBorderRadius - 10,
                                                width=parentContainerWidth,
                                                bgcolor=ft.colors.BLUE_100,
                                                height=300,
                                                padding=15,
                                                margin=dataCardMargins,
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Text(selectable=True,
                                                                value="Student's data",
                                                                style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                                                color=ft.colors.BLACK,
                                                                ),
                                                        ft.Row(
                                                            [
                                                                # studentsDataContainer
                                                                ft.Container(
                                                                    width=dataCardsWidth,
                                                                    content=ft.Column(
                                                                        controls=[
                                                                            # 1- fullNameContainer take one Row
                                                                            ft.Container(
                                                                                margin=dataFieldsContainerMargins,
                                                                                height=dataFieldsContainerHeight,
                                                                                content=ft.Row(
                                                                                    controls=[
                                                                                        ft.Icon(
                                                                                            name=ft.icons.PERSON_OUTLINE_ROUNDED,
                                                                                            color=ft.colors.BLACK
                                                                                        ),
                                                                                        ft.Text(selectable=True,
                                                                                                value=f"User full name: {userFirstName} {userMiddleName} {LastName}.",
                                                                                                color=ft.colors.BLACK,
                                                                                                style=ft.TextThemeStyle.TITLE_MEDIUM,
                                                                                                )
                                                                                    ]
                                                                                ),
                                                                            ),
                                                                            # 2- gender and id container takes one row
                                                                            ft.Container(
                                                                                # bgcolor=ft.colors.GREEN,
                                                                                height=dataFieldsContainerHeight,
                                                                                margin=dataFieldsContainerMargins,
                                                                                width=dataCardsWidth,
                                                                                content=ft.Row(
                                                                                    controls=[
                                                                                        # 2-a Gender container
                                                                                        ft.Container(
                                                                                            width=dataFieldsContainerWidths,
                                                                                            height=dataFieldsContainerHeight,
                                                                                            content=ft.Row(
                                                                                                controls=[
                                                                                                    ft.Image(
                                                                                                        src=userGenderIconLocation,
                                                                                                    ),
                                                                                                    ft.Text(selectable=True,
                                                                                                            value=f"User Gender: {userGender}",
                                                                                                            color=ft.colors.BLACK,
                                                                                                            style=ft.TextThemeStyle.TITLE_MEDIUM,
                                                                                                            ),
                                                                                                ]
                                                                                            ),),
                                                                                        # 2-b User ID container
                                                                                        ft.Container(
                                                                                            width=dataFieldsContainerWidths,
                                                                                            height=dataFieldsContainerHeight,
                                                                                            margin=ft.Margin(
                                                                                                left=0, right=10, bottom=0, top=0),
                                                                                            content=ft.Row(
                                                                                                controls=[
                                                                                                    ft.Image(
                                                                                                        src=userIdImageLocation, ),
                                                                                                    ft.Text(selectable=True,
                                                                                                            value=f"User Id No. : {userId}.",
                                                                                                            color=ft.colors.BLACK,
                                                                                                            style=ft.TextThemeStyle.TITLE_MEDIUM,
                                                                                                            ),

                                                                                                ]
                                                                                            ),
                                                                                        ),
                                                                                    ]
                                                                                ),
                                                                            ),
                                                                            # 3 User class and birthday take one row
                                                                            ft.Container(
                                                                                height=dataFieldsContainerHeight,
                                                                                margin=dataFieldsContainerMargins,
                                                                                width=dataCardsWidth,
                                                                                content=ft.Row(
                                                                                    controls=[
                                                                                        # 3-a Container for user class
                                                                                        ft.Container(
                                                                                            width=dataFieldsContainerWidths,
                                                                                            height=dataFieldsContainerHeight,
                                                                                            content=ft.Row(
                                                                                                controls=[
                                                                                                    ft.Image(
                                                                                                        src=userClassIconLoaction, ),
                                                                                                    ft.Text(selectable=True,
                                                                                                            value=f"User class: {userClass}.",
                                                                                                            color=ft.colors.BLACK,
                                                                                                            style=ft.TextThemeStyle.TITLE_MEDIUM,
                                                                                                            ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                        # 3-b Container for user birth date
                                                                                        ft.Container(
                                                                                            width=dataFieldsContainerWidths,
                                                                                            height=dataFieldsContainerHeight,
                                                                                            content=ft.Row(
                                                                                                controls=[
                                                                                                    ft.Image(
                                                                                                        src=userBirthDayIconLocation, ),
                                                                                                    ft.Text(selectable=True,
                                                                                                            value=f"Birthday: {userBirthDay}.",
                                                                                                            color=ft.colors.BLACK,
                                                                                                            style=ft.TextThemeStyle.TITLE_MEDIUM,
                                                                                                            ),
                                                                                                ]
                                                                                            ),
                                                                                        ),
                                                                                    ]
                                                                                ),
                                                                            ),
                                                                            # 4- User location and tribe take one row
                                                                            ft.Container(
                                                                                height=dataFieldsContainerHeight,
                                                                                margin=dataFieldsContainerMargins,
                                                                                width=dataCardsWidth,
                                                                                content=ft.Row(
                                                                                    controls=[
                                                                                        # 4-a user location field
                                                                                        ft.Container(
                                                                                            width=dataFieldsContainerWidths,
                                                                                            height=dataFieldsContainerHeight,
                                                                                            content=ft.Row(
                                                                                                controls=[ft.Image(
                                                                                                    src=userLocationIconLocation, ),
                                                                                                    ft.Text(selectable=True,
                                                                                                            value=f"Location:{userLocation}.",
                                                                                                            color=ft.colors.BLACK,
                                                                                                            style=ft.TextThemeStyle.TITLE_MEDIUM,
                                                                                                            ),
                                                                                                ],
                                                                                            ),
                                                                                        ),
                                                                                        # 4-b User Tribe field
                                                                                        ft.Container(
                                                                                            width=dataFieldsContainerWidths,
                                                                                            height=dataFieldsContainerHeight,
                                                                                            content=ft.Row(
                                                                                                controls=[
                                                                                                    ft.Image(
                                                                                                        src=userTribeIconLocation, ),
                                                                                                    ft.Text(selectable=True,
                                                                                                            value=f"Tribe: {userTribe}.",
                                                                                                            color=ft.colors.BLACK,
                                                                                                            style=ft.TextThemeStyle.TITLE_MEDIUM,
                                                                                                            ),

                                                                                                ]
                                                                                            ),
                                                                                        ),
                                                                                    ]
                                                                                ),
                                                                            ),
                                                                        ]
                                                                    )
                                                                )
                                                            ],
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            # Student's Parents cards
                                            ft.Container(
                                                border_radius=parentContainerBorderRadius - 10,
                                                width=parentContainerWidth,
                                                bgcolor=ft.colors.BLUE_200,
                                                height=300,
                                                padding=15,
                                                margin=dataCardMargins,
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Text(selectable=True,
                                                                value="Parent's data",
                                                                style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                                                color=ft.colors.BLACK,
                                                                ),
                                                        ft.Row(
                                                            [
                                                                # studentsDataContainer
                                                                ft.Container(
                                                                    width=dataCardsWidth,
                                                                    content=ft.Column(
                                                                        controls=[
                                                                            # 1- Father's Name take one Row
                                                                            ft.Container(
                                                                                margin=dataFieldsContainerMargins,
                                                                                height=dataFieldsContainerHeight,
                                                                                content=ft.Row(
                                                                                    controls=[
                                                                                        ft.Image(
                                                                                            src=usersFathersIcon
                                                                                        ),
                                                                                        ft.Text(selectable=True,
                                                                                                value=f"User's Father Name: {userFathersName}",
                                                                                                color=ft.colors.BLACK,
                                                                                                style=ft.TextThemeStyle.TITLE_MEDIUM,
                                                                                                )
                                                                                    ]
                                                                                ),
                                                                            ),
                                                                            # 2- Father's Telephone take one Row
                                                                            ft.Container(
                                                                                margin=dataFieldsContainerMargins,
                                                                                height=dataFieldsContainerHeight,
                                                                                content=ft.Row(
                                                                                    controls=[
                                                                                        ft.Icon(
                                                                                            name=ft.icons.PHONE,
                                                                                            color=ft.colors.BLACK
                                                                                        ),
                                                                                        ft.Text(selectable=True,
                                                                                                value=f"User's Father Phone Number: {usersFathersPhoneNo}.",
                                                                                                color=ft.colors.BLACK,
                                                                                                style=ft.TextThemeStyle.TITLE_MEDIUM,
                                                                                                )
                                                                                    ]
                                                                                ),
                                                                            ),
                                                                            # 3- Mother's Name Container
                                                                            ft.Container(
                                                                                margin=dataFieldsContainerMargins,
                                                                                height=dataFieldsContainerHeight,
                                                                                content=ft.Row(
                                                                                    controls=[
                                                                                        ft.Image(
                                                                                            src=usersMotherIcon,
                                                                                        ),
                                                                                        ft.Text(selectable=True,
                                                                                                value=f"User's Mother Name: {userMothersName}.",
                                                                                                color=ft.colors.BLACK,
                                                                                                style=ft.TextThemeStyle.TITLE_MEDIUM,
                                                                                                )
                                                                                    ]
                                                                                ),
                                                                            ),
                                                                            # 4- Mother's Telephone take one Row
                                                                            ft.Container(
                                                                                margin=dataFieldsContainerMargins,
                                                                                height=dataFieldsContainerHeight,
                                                                                content=ft.Row(
                                                                                    controls=[
                                                                                        ft.Icon(
                                                                                            name=ft.icons.PHONE,
                                                                                            color=ft.colors.BLACK
                                                                                        ),
                                                                                        ft.Text(selectable=True,
                                                                                                value=f"User's Mother Phone Number: {usersMothersPhoneNo}.",
                                                                                                color=ft.colors.BLACK,
                                                                                                style=ft.TextThemeStyle.TITLE_MEDIUM,
                                                                                                )
                                                                                    ]
                                                                                ),
                                                                            ),

                                                                        ]
                                                                    )
                                                                )
                                                            ],
                                                        ),
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),

                                ),
                                ft.Image(
                                    src=boyAvatar,
                                    width=imageWidth,
                                    height=imageHeight,
                                    right=imageAbsolute_right,
                                    fit=ft.ImageFit.CONTAIN,
                                    repeat=ft.ImageRepeat.NO_REPEAT,
                                    border_radius=ft.border_radius.all(
                                        100
                                    ),
                                ) if userGender == "Male" else
                                ft.Image(
                                    src=girAvatar,
                                    width=imageWidth,
                                    height=imageHeight,
                                    right=imageAbsolute_right,
                                    fit=ft.ImageFit.CONTAIN,
                                    repeat=ft.ImageRepeat.NO_REPEAT,
                                    border_radius=ft.border_radius.all(
                                        100
                                    ),
                                ),
                            ],
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ]
            )
    
    
    studentProfileViewObj.scroll = ft.ScrollMode.ADAPTIVE
    return studentProfileViewObj




class DarulQuranDb:
    def __init__(self, connection: sqlite3.Connection, connection_pool=None):
        self.connection = connection
        # Create a connection pool
        self.connection_pool = queue.Queue(maxsize=5)
        # Create users table
        self.execute_query(query=f'''CREATE TABLE IF NOT EXISTS {tableName}
                   (id INTEGER PRIMARY KEY, 
                    student_first_name STRING NOT NULL,
                    student_middle_name STRING,
                    student_last_name STRING NOT NULL,
                    students_gender STRING NOT NULL,
                    d_o_b DATETIME NOT NULL,
                    students_class STRING NOT NULL,
                    fathers_name STRING NOT NULL,
                    mothers_name STRING NOT NULL,
                    fathers_telephone STRING,
                    mothers_telephone STRING,
                    studens_tribe STRING NOT NULL,
                    students_location STRING NOT NULL
                 )'''
                           )

  
    # Define a function to get a connection from the pool
    def get_connection(self):
        # Check if a connection is available in the pool
        if not self.connection_pool.empty():
            return self.connection_pool.get()
        # If the pool is empty, create a new connection
        conn = self.connection
        return conn

    # Define a function to release a connection back to the pool
    def release_connection(self):
        self.connection_pool.put(self.connection)
        # self.connection.close()

    # Define a function to execute a query using a connection from the pool
    def execute_query(self, query, params: tuple = (), commitData: bool = False, shouldReturnData: bool = False)->list:
        result = None
        connection = self.get_connection()
        # self.connection_pool.put(connection)
        cursor = connection.cursor()
        cursor.execute(query, params)
        
        if commitData:
            connection.commit()

        if shouldReturnData:
            result = cursor.fetchall()

        self.release_connection()
        cursor.close()
        # print(f"Type of the result is >>{type(result)} and result is {result}")
        return result

    # Function to add a new user

    def addStudentToDB(self,
                       student_first_nameVal: str,
                       student_middle_nameVal: str,
                       student_last_nameVal: str,
                       students_genderVal: str,
                       d_o_bVal: str,
                       students_classVal: str,
                       fathers_nameVal: str,
                       mothers_nameVal: str,
                       fathers_telephoneVal: str,
                       mothers_telephoneVal: str,
                       studens_tribeVal: str,
                       students_locationVal: str
                       ):

        self.execute_query(f"""INSERT INTO {tableName} (
                student_first_name,
                student_middle_name,
                student_last_name,
                students_gender,
                d_o_b,
                students_class,
                fathers_name,
                mothers_name,
                fathers_telephone,
                mothers_telephone,
                studens_tribe,
                students_location
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                           params=(
                               # idVal,
                               student_first_nameVal,
                               student_middle_nameVal,
                               student_last_nameVal,
                               students_genderVal,
                               d_o_bVal,
                               students_classVal,
                               fathers_nameVal,
                               mothers_nameVal,
                               fathers_telephoneVal,
                               mothers_telephoneVal,
                               studens_tribeVal,
                               students_locationVal
                           ),
                           commitData=True
                        )
    # Function to existing  user

    def editStudentData(self,
                       student_first_nameVal: str,
                       student_middle_nameVal: str,
                       student_last_nameVal: str,
                       students_genderVal: str,
                       d_o_bVal: str,
                       students_classVal: str,
                       fathers_nameVal: str,
                       mothers_nameVal: str,
                       fathers_telephoneVal: str,
                       mothers_telephoneVal: str,
                       studens_tribeVal: str,
                       students_locationVal: str,
                       idVal:int
                       ):

        self.execute_query(f"""UPDATE {tableName} 
            SET student_first_name=?,
                student_middle_name=?,
                student_last_name=?,
                students_gender=?,
                d_o_b=?,
                students_class=?,
                fathers_name=?,
                mothers_name=?,
                fathers_telephone=?,
                mothers_telephone=?,
                studens_tribe=?,
                students_location=?
                WHERE id=?""",
                params=(
                   student_first_nameVal,
                   student_middle_nameVal,
                   student_last_nameVal,
                   students_genderVal,
                   d_o_bVal,
                   students_classVal,
                   fathers_nameVal,
                   mothers_nameVal,
                   fathers_telephoneVal,
                   mothers_telephoneVal,
                   studens_tribeVal,
                   students_locationVal,
                   idVal,
                ),
                commitData=True
                )
        
    def deleteStudentsData(self, studentId:int):
        self.execute_query(f"DELETE FROM {tableName} WHERE id=?", (studentId,), commitData=True)

    # get a specific student's full data
    def getSpecificStudentsFullData(self, id):
        data = self.execute_query(
            f"SELECT * FROM {tableName} WHERE id = ?", params=(id,), shouldReturnData=True
        )
        return data

    # get all users id and full names
    def getAllStudentsIdsAndFullNamesInClass(self, className):
        students = self.execute_query(f"SELECT id, student_first_name, student_middle_name, student_last_name FROM {tableName} WHERE students_class='{className}' ", shouldReturnData=True)
        return students
    
    def getStudentClassNameUsingId(self, id)->str:
        className = self.execute_query(f"SELECT students_class FROM {tableName} WHERE id={id} ", shouldReturnData=True)[0]
        return className[0]
    





def main(page: ft.Page):
    
    def route_change(route):
        page.views.clear()
        page.views.append(landingPage(page))
        page.title = APP_NAME
        
        parameter = urlparse(page.route).path.split("/")[-1]
        # print(f"Here is the route {page.route} and here is the parameter {parameter}")
        #print(f"here is the params {parameter} and here is the acatual route {page.route} this will go to")
        if page.route == f"{selectStudentClassRoute}/{parameter}":
            #print(selectStudentClassRoute)
            page.views.append(selectClassPage(page, action=parameter))
        elif page.route == addStudentPageRoute:
            #print(addStudentPageRoute)
            page.views.append(addStudentPage(page))
        elif page.route == f"{studentsListViewPageRoute}/{parameter}" and parameter != page.route:
            # print(f"Here is the full route {route} and here is the parameters {parameter}")
            page.views.append(studentsListView(page=page, params=parameter))
        elif page.route == f"{studentProfileViewPageRoute}/{parameter}" and page.route != parameter:
            #print(studentProfileViewPageRoute)
            page.views.append(ProfilePage(page=page, paramsFromPrevPage=parameter))
        elif page.route == f"{editStudentPageViewRoute}/{parameter}" and page.route != parameter:
            page.views.append(addStudentPage(page=page, editMode=True, paramsFrmPrevPage=parameter))


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
