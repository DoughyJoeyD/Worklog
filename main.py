import time
import sys

from task import Task, clearscreen

#allows the user to create multiple task entries each time they run the program
tasks = []


def get_task():
    """This function gets the users task and stores it as an instance that
        can be used to search for specific parts of each task"""
    #This calls the Class Task to get a user input
    #also temorary assigns it to instance before adding it to tasks list
    instance = Task()
    #Grabs the name of task
    instance.get_task_name()
    #Grabs the date
    instance.get_date()
    #grabs the time
    instance.get_time()
    #Grabs extra notes the user name want to include
    instance.get_remarks()
    #clears the screen
    clearscreen()
    #prints the task in a neat way
    instance.taskprinter()
    #ask the user if everything the entered is correct
    save = False
    clearscreen()
    while save is False:
        choices = ['Y', 'N']
        yes = ['Y']
        no = ['N']
        instance.taskprinter()
        correct = input('Does Everything Look Correct? (Y/N): ')
        #....if it is correct
        if correct.upper() in yes:
            clearscreen()
            print('Task has been Added')
            time.sleep(1)
            save = True

        #...if its not correct
        if correct.upper() in no:
            clearscreen()
            time3 = instance.time
            name = instance.name
            date = instance.date.strftime('%m/%d/%Y')
            extra = instance.extra
            #asks the user whats wrong
            print("1:Name:{}".format(name), "2:Date:{}".format(date), "3:Time:{}".format(time3), "4:Extra:{}".format(extra))
            options = [1, 2, 3, 4]
            fixed = False
            while fixed == False:
                wrong = input('Whats Wrong?: ')
                #if the dont enter what were looking for send them an error
                #run it again
                if wrong not in options:
                    print("Not an Option- Enter 1-4")
                #if the name is selected
                if wrong == '1':
                    #calls the name part of the instance to edit it
                    instance.get_task_name()
                    fixed = True
                    clearscreen()
                #if date is selected
                if wrong == '2':
                    #calls the date part of the instance to edit it
                    instance.get_date()
                    fixed = True
                    clearscreen()
                #if time is selected
                if wrong == '3':
                    #calls the time part of the instance to edit it
                    instance.get_time()
                    fixed = True
                    clearscreen()
                #if notes or extra is selected
                if wrong == '4':
                    #calls the notes part of the task entry to edit it
                    instance.get_remarks()
                    fixed = True
                    clearscreen()
        #if the user doesnt give a Y or N this message shows
        if correct.upper() not in choices:
            clearscreen()
            print('Not an option Buddy')


    #adds the fully finished task instance to the tasks list
    tasks.append(instance)


def by_date():
    """The by_date function prints out a list of dates and allows the user
        to search within the dates for specific tasks. If no tasks are in the system
        the function will return a message saying, "Sorry No Entries....", and will
        bring you back to the main menu"""
    clearscreen()
    list_of_dates = {}
    count = 1
    #Displays the dates of the task instances saved in the tasks list
    for task in tasks:
        if task.date not in list_of_dates:
            varb = task.date.strftime('%m/%d/%Y')
            print(str(count)+" : "+str(varb))
            list_of_dates[count] = task.date.strftime('%m/%d/%Y')
            count += 1
    #After the script checks for tasks, if there are 0.., returns the message bellow
    if count == 1:
        clearscreen()
        print('Sorry Entries in DataBase(Tasks List)')
        time.sleep(2)
        print('Taking you back to the main page!')
        time.sleep(2)
        #calls the main menu to bring the user back to the menu
        menu()
    #If tasks list has tasks in it then the script will prompt the user to
    #choose a date the tasks were completed on
    if count >= 2:
        try:
            dates = int(input("Please Choose Date: "))
            try:
                choice = list_of_dates[dates]
                clearscreen()
                for task in tasks:
                    if task.date.strftime('%m/%d/%Y') == choice:
                        task.taskprinter()
                disgard = input("Press Enter To Continue ")
            #if they dont enter a number itll kick back this message
            except KeyError:
                clearscreen()
                print('Hey man, that isnt a option...')
                time.sleep(1)
                #asks the user to enter a date again
                by_date()
        #if the user doesnt give a number this error is raised and the message displayed
        except ValueError:
            clearscreen()
            print('Hey man, that isnt a number...')
            time.sleep(1)
            #brings them back to the date menu
            by_date()


def by_time():
    """By time is identical to by_date, except for the fact that it is searching by
        the time atribute of the instance created when the task was entered into the
        system. This function prompts the user for a number of min the task was, returns matching Tasks
        or returns tasks from a range surronding the original ask, if the user wants"""
    clearscreen()
    how_long = input("How many Min was the task?(numbers only): ")
    count = 0
    clearscreen()
    #if the user response matches the task min, taskprinter is called which
    #displays the tasks that match, then waits for the user to continue
    for task in tasks:
        if int(task.time) == int(how_long):
            task.taskprinter()
            count += 1
    if count >= 1:
        disgard = input('Press Enter To Continue')
    #if the user response doesnt match any tasks in task list, and asks the user if
    #they want to search within 20% above or belove the user response
    if count == 0:
        clearscreen()
        print('Sorry no tasks {} Min long...'.format(how_long))
        time.sleep(2)
        varb1 = int(how_long) * .8
        varb2 = int(how_long) * 1.2
        print('Would you like to search from tasks between {}-{} Min long?'.format(int(varb1), int(varb2)))
        time.sleep(2)
        yes = 'Y'
        no = 'N'
        yesno = ['Y', 'N']
        runner = True
        while runner == True:
            again = input('Y or N: ')
            if again.upper() == yes:
                clearscreen()
                for task in tasks:
                    if int(varb1) <= int(task.time) <= int(varb2):
                        task.taskprinter()
                disgard = input('Press Enter To Continue')
                runner = False
            if again.upper() == no:
                runner = False
                clearscreen()
            #catches the errors in user input and makes them enter again
            if again.upper() not in yesno:
                clearscreen()
                print('Hmm, Looking for a Y or N here... Thanks!')

def by_name():
    """Searches the tasks list by name to find tasks matching the users input"""
    clearscreen()
    print('You Selected - By Name')
    name = input("Task Name: ")
    count = 0
    clearscreen()
    for task in tasks:
        if task.name == name.upper():
            count += 1
    #if the user response matches a task name it will call the .taskprinter of the instance
    if count >= 1:
        for task in tasks:
            if task.name == name.upper():
                task.taskprinter()
        #then waits for the user to continue
        disgard = input('Press Enter To Continue')
        clearscreen()
    #if no matching names, this message is displayed
    if count == 0:
        clearscreen()
        print('Sorry no tasks by the name "{}"!'.format(name.upper()))
        time.sleep(1)
        clearscreen()
    #Asks the user if they want to go again
    try:
        print("Again Old Friend?")
        choice = int(input('1:Search Again, 2:Back or 3:Quit: '))
        #if the user is getting clever, still wont error
        if choice >= 4:
            clearscreen()
            print('Hey! I asked for 1-3 not {}'.format(choice))
            time.sleep(2)
            by_name()
        #runs the name search again
        if choice == 1:
            by_name()
        #runs search menu
        if choice == 2:
            search()
        #quits the script
        if choice == 3:
            quit()
    #catches most of the errors from the user response
    except ValueError:
        print('Oops Please enter a Number!')
        time.sleep(1)
        #runs the name search function again
        by_name()


def by_pattern():
    """Give the user the option to search by the extra or notes part of the task
        also searches again all of the names in the task printing those as well"""
    count = 0
    clearscreen()
    keyword = input("Pattern to Match: ")
    #prints the matching tasks from the user response
    for task in tasks:
        if keyword.upper() == task.name:
            task.taskprinter()
            count += 1

        if keyword.upper() == task.extra:
            task.taskprinter()
            count += 1
    #if no tasks prints message below
    if count == 0:
        print('Sorry not in list')
        time.sleep(1)
        runner = True
        yes = 'Y'
        no = 'N'
        yesno = ['Y', 'N']
        while runner == True:
            clearscreen()
            #asks the user if they want to search more
            print('Would You like to Search Again?')
            again = input('Y or N: ')
            if again.upper() == yes:
                runner = False
                by_pattern()
                exit()
            if again.upper() == no:
                runner = False
                clearscreen()
            if again.upper() not in yesno:
                clearscreen()
                print('Hmm, Looking for a Y or N here... Thanks!')
                time.sleep(1)
    disgard = input('Press Enter to Continue ')

def search():
    """The main menu for the search part of the script"""
    clearscreen()
    #Give the user 5 options to choose from
    options = {1:'By Name', 2:'By Time Spent', 3:'By Date', 4:'In Notes/Name', 5:'Back'}
    print('You selected Search!')
    runner = True

    while runner == True:
        #asks the user to choose a method to search from or go back
        try:
            print(options)
            choice = int(input('Choose a Search Parameter!: '))
        #catches all the errors with the user entry
        except ValueError:
            print('Oops Please Enter a Number!')
            time.sleep(1)
            search()
            quit()
        #directs the user response to a function call or search method
        if choice == 1:
            by_name()
            runner = False
        if choice == 2:
            by_time()
            runner = False
        if choice == 3:
            by_date()
            runner = False
        if choice == 4:
            by_pattern()
            runner= False
        if choice == 5:
            menu()
            runner = False



def menu():
    """The main menu for the script, asks the user to either enter a task, search or quit"""

    clearscreen()
    options = ['NEW TASK', 'SEARCH', 'Quit']
    print('Welcome To WorkLog Manager')
    runner = True
    while runner == True:
        choice = input('New Task or Search?: ')
        if choice.upper() == 'NEW TASK':
            clearscreen()
            get_task()
            runner = False
        if choice.upper() == 'SEARCH':
            clearscreen()
            search()
            runner = False
        if choice.upper() == 'Quit':
            print('Thanks')
        if choice.upper() not in options:
            clearscreen()
            print('Oops, Not an option... Try again')
            time.sleep(1)

    clearscreen()

def again():
    """Asks the user if they want to preform another task, only bypassed when quit is called"""
    clearscreen()
    #asks for a user response
    print("Would you like to prefrom another task? ")
    response = input("Yes-1 - No-2 ")
    #if they give a vaild response
    try:
        if int(response) < 3:
            if int(response) == 1:
                menu()
            if int(response) == 2:
                quit()
        if int(response) >= 3:
            print("1 or 2... not another number")
            time.sleep(1)
            again()
    #if they give us trouble
    except ValueError:
        print("Ooops Select 1 or 2...")
        time.sleep(1)
        again()
    again()


def __init__():
    """calls the menu and again script to effectivly start the program, but not when imported"""
    menu()
    again()

__init__()
