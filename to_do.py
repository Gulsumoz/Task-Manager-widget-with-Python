import os
import random
import tkinter
from tkinter import messagebox
import task
import widgets as wd

# root window
root1 = wd.root



def add_to_do():

    add_task_tx = text_input.widget.get()
    if not add_task_tx == "":
        to_do_list.add_new_task(add_task_tx)
        text_input.widget.delete(0, 'end')
        clear_to_do_list()
        show_to_do_list()
    else:
        alert_text_input.alert('No Task Entered', '''Please enter a task and priority value\n 
         1-for high, 2-for medium, 3-for low''')


def sort_asc():
    clear_to_do_list()
    to_do_list.tasks.sort()
    show_to_do_list()
    print("Your to do list has been sorted in ascending order.")


def sort_desc():
    clear_to_do_list()
    to_do_list.tasks.sort()
    to_do_list.tasks.reverse()
    show_to_do_list()
    print("Your to do list has been sorted in descending order.")


def random_choice():
    task = (random.choice(to_do_list.tasks))
    label_display.widget['text'] = task
    print(task)


def reset_tasks():

    confirm = tkinter.messagebox.askyesno("Delete All To Dos", "Are you sure you wish to delete all to dos in the list?")
    to_do_list.reset_tasks(confirm)
    show_to_do_list()


def remove_by_name():

    delete_task = list_box.widget.get('active')
    if delete_task in to_do_list.tasks:
        clear_to_do_list()
        to_do_list.delete_task_name(delete_task)
        show_to_do_list()


def remove_by_index():
    index = int(input("What task number do you want to remove?"))
    to_do_list.delete_task_number(index)


def search_to_dos():
    search_task = input("What task would you like to search for?")
    to_do_list.search_tasks(search_task)


def to_do_list_length():
    number_of_to_dos = len(to_do_list.tasks)
    msg = "Number of to dos to complete: {}".format(number_of_to_dos)
    task_number_display.widget['text'] = msg


def show_to_do_list():
    clear_to_do_list()
    for to_do in to_do_list.tasks:
        list_box.widget.insert("end", to_do)


def clear_to_do_list():
    list_box.widget.delete(0, "end")


# class instances
to_do_list = task.Tasks()
label_title = wd.Widgets(root1)
label_display = wd.Widgets(root1)
task_number_display = wd.Widgets(root1)
text_input = wd.Widgets(root1)
btn_add_task = wd.Widgets(root1)
btn_shows_tasks = wd.Widgets(root1)
btn_delete_all = wd.Widgets(root1)
btn_delete_one = wd.Widgets(root1)
btn_sort_asc = wd.Widgets(root1)
btn_sort_desc = wd.Widgets(root1)
btn_choose_random = wd.Widgets(root1)
btn_number_of_to_dos = wd.Widgets(root1)
btn_reset_tasks = wd.Widgets(root1)
btn_exit = wd.Widgets(root1)
list_box = wd.Widgets(root1)
alert_text_input = wd.Widgets(root1)
delete_confirmation_message = wd.Widgets(root1)

# widgets
label_title.set_name('To do List', 1, 0)
task_number_display.set_name('', 2, 1)
text_input.input_text()
btn_shows_tasks.display_button("Show all to dos", show_to_do_list, 2, 0)
btn_add_task.display_button("Add new to do", add_to_do, 4, 0)
# btn_delete_all.display_button('Delete all to dos', to_do_list.delete_all_tasks)
btn_delete_one.display_button('Delete to do', remove_by_name, 5, 0)
btn_sort_asc.display_button('Sort tasks (asc)', sort_asc, 6, 0)
btn_sort_desc.display_button('Sort tasks (desc', sort_desc, 7, 0)
btn_choose_random.display_button('Choose random to do', random_choice, 8, 0)
btn_number_of_to_dos.display_button('Number of to dos', to_do_list_length, 9, 0)
btn_reset_tasks.display_button('Delete All Todos', reset_tasks, 11, 0)
btn_exit.display_button('Exit', exit, 12, 0)
label_display.set_name('', 3, 1)
list_box.to_do_box()


# main loop
# functions to run on start up
show_to_do_list()
root1.mainloop()
print_list_to_console = False


# main loop
