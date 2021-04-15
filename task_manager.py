import os
import random
import tkinter
from tkinter import messagebox
import task
import widgets as wd
from PIL import Image, ImageTk
import csv

# root window
root1 = wd.root


def add_task():

    add_task_tx = text_input.widget.get()
    if not add_task_tx == "":
        to_do_list.add_new_task(add_task_tx)
        text_input.widget.delete(0, 'end')
        clear_to_do_list()
        show_to_do_list()
        msg = "{} is added to your list".format(add_task_tx)
        task_number_display.widget['text'] = msg
    else:
        alert_text_input.alert('No Task Entered', "Please enter a task ")


def give_priority():
    prior_task = text_input.widget.get()
    if prior_task in to_do_list.tasks:
        a = to_do_list.tasks.index(prior_task)
        b = a-1
        to_do_list.tasks[b], to_do_list.tasks[a] = to_do_list.tasks[a], to_do_list.tasks[b]
        clear_to_do_list()
        show_to_do_list()




def sort_asc():
    clear_to_do_list()
    to_do_list.tasks.sort()
    show_to_do_list()



def sort_desc():
    clear_to_do_list()
    to_do_list.tasks.sort()
    to_do_list.tasks.reverse()
    show_to_do_list()



def random_choice():
    task = (random.choice(to_do_list.tasks))
    msg = "{} is your random task".format(task)
    task_number_display.widget['text'] = msg



def empty_tasks():

    confirm = tkinter.messagebox.askyesno("Delete All To Dos", "Are you sure you wish to delete all to dos in the list?")
    to_do_list.reset_tasks(confirm)
    show_to_do_list()


def remove_by_name():

    delete_task = text_input.widget.get()
    text_input.widget.delete(0, 'end')
    if delete_task in to_do_list.tasks:
        clear_to_do_list()
        to_do_list.delete_task_name(delete_task)

        show_to_do_list()
        msg = "{} is deleted from your list".format(delete_task)
        task_number_display.widget['text'] = msg
    elif len(to_do_list.tasks)==0:
        msg = "Task list is already empty"
        task_number_display.widget['text'] = msg
    elif delete_task and not (delete_task in to_do_list.tasks):
        msg = "Task list is not in the list"
        task_number_display.widget['text'] = msg
    elif not delete_task:
        delete_task = list_box.widget.get('active')
        clear_to_do_list()
        to_do_list.delete_task_name(delete_task)
        show_to_do_list()
        msg = "{} is deleted from your list".format(delete_task)
        task_number_display.widget['text'] = msg




def search_task():
    search_task = text_input.widget.get()
    text_input.widget.delete(0, 'end')
    if search_task in to_do_list.tasks:
        msg = "{} exist your list".format(search_task)
        task_number_display.widget['text'] = msg
    else:
        msg = "{} does not exist your list".format(search_task)
        task_number_display.widget['text'] = msg


def to_do_list_length():
    number_of_to_dos = len(to_do_list.tasks)
    msg = "Total Number of Tasks: {}".format(number_of_to_dos)
    task_number_display.widget['text'] = msg


def show_to_do_list():
    clear_to_do_list()
    for task in to_do_list.tasks:
        list_box.widget.insert("end", task)


def clear_to_do_list():
    list_box.widget.delete(0, "end")


def save_task_to_file():
    list = to_do_list.tasks
    csv_file = open("output.csv", 'w')
    for r in list:
        csv_file.write(r + "\n")
    csv_file.close()
    msg = "Tasks are  saved to output.csv file"
    task_number_display.widget['text'] = msg


def load_task():
    with open('test.csv', newline='') as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')
        temp_list = list(map(tuple, reader))
    for item in temp_list:
        to_do_list.tasks.append(item)

    clear_to_do_list()
    show_to_do_list()
    msg = "Tasks are  loaded from  file"
    task_number_display.widget['text'] = msg
    if not file:
        msg = "error happened during load"
        task_number_display.widget['text'] = msg


to_do_list = task.Tasks()
label_title = wd.Widgets(root1)
label_display = wd.Widgets(root1)
task_number_display = wd.Widgets(root1)
text_input = wd.Widgets(root1)
btn_add_task = wd.Widgets(root1)
btn_shows_tasks = wd.Widgets(root1)
btn_search_tasks = wd.Widgets(root1)
btn_delete_all = wd.Widgets(root1)
btn_delete_one = wd.Widgets(root1)
btn_sort_asc = wd.Widgets(root1)
btn_sort_desc = wd.Widgets(root1)
btn_choose_random = wd.Widgets(root1)
btn_number_of_to_dos = wd.Widgets(root1)
btn_empty_tasks = wd.Widgets(root1)
btn_exit = wd.Widgets(root1)
btn_save_csv = wd.Widgets(root1)
btn_load_csv = wd.Widgets(root1)
list_box = wd.Widgets(root1)
btn_priority=wd.Widgets(root1)
alert_text_input = wd.Widgets(root1)
inform_text_input = wd.Widgets(root1)
delete_confirmation_message = wd.Widgets(root1)

# widgets
label_title.set_name('Welcome To Task Manager Program ', 0, 0)
label_title.set_name('Enter Task Here', 3, 1)
task_number_display.set_name('Please select an action', 1, 3)
text_input.input_text()

btn_add_task.display_button("Add new task", add_task, 2, 2)
btn_shows_tasks.display_button("Show all tasks", show_to_do_list, 7, 2)
btn_search_tasks.display_button("Search a tasks", search_task, 3, 2)
btn_delete_one.display_button('Delete task', remove_by_name, 6, 2)
btn_sort_asc.display_button('Sort tasks (asc)', sort_asc, 4, 2)
btn_sort_desc.display_button('Sort tasks (dsc)', sort_desc, 5, 2)
btn_choose_random.display_button('Choose random task', random_choice, 2, 3)
btn_number_of_to_dos.display_button('Number of tasks', to_do_list_length, 3, 3)
btn_empty_tasks.display_button('Delete all tasks', empty_tasks, 4, 3)
btn_exit.display_button('Exit', exit, 7, 3)
btn_save_csv.display_button('Save Tasks', save_task_to_file, 5, 3)
btn_load_csv.display_button("Load Task ", load_task, 6, 3)
btn_priority.display_button("Give Priority", give_priority, 7, 3)

list_box.task_box()

img = Image.open("pr.jpg")  # PIL solution
img = img.resize((250, 160), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img) #
l = tkinter.Label(image=img)
l.grid(row=1, column=0)

# main loop
# functions to run on start up
show_to_do_list()
root1.mainloop()




