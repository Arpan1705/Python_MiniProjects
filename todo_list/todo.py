import tkinter as tk
from tkinter import messagebox
from database import create_table, add_task, get_tasks, delete_task

#Function to refresh the task list
def refresh_tasks():
    tasks_listbox.delete(0, tk.END)
    for task in get_tasks():
        task_text = task[1]
        if task[2] is not None:
            task_text += f" (Duration: {task[2]} min)" #insert the task duration from 3rd position of tuple with task text
        tasks_listbox.insert(tk.END, task_text) #insert the task text with duration

#Function to add a task
def add_task_command():
    task = task_entry.get()
    duration = duration_entry.get()
    if task:
        if duration:    
            try:
                duration = int(duration)
            except ValueError:
                messagebox.showwarning("Warning", "Duration must be a number.")
                return
        else:
            duration = None

        add_task(task, duration)
        task_entry.delete(0, tk.END)
        duration_entry.delete(0, tk.END)
        refresh_tasks()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

#Function to delete a task
def delete_task_command():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        selected_task_text = tasks_listbox.get(selected_task_index)
        tasks = get_tasks()
        for task in tasks:
            task_text = task[1]
            if task[2] is not None:
                task_text += f" (Duration: {task[2]} min)"
            if task_text == selected_task_text:
                    delete_task(task[0])
                    break
        refresh_tasks()
    else:
        messagebox.showwarning("Warning", "You must select a task.")

    
#Create the tasks table if it doesn't exist
create_table()

#Initialize the main window
root = tk.Tk()
root.title("TO-DO List")

#Create the task entry widget
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

#Create the duration entry widget
duration_lable = tk.Label(root, text="Duration (minutes, optional):")
duration_lable.pack(pady=5)
duration_entry = tk.Entry(root, width=50)
duration_entry.pack(pady=5)

#Create the tasks listbox
tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.pack(pady=10)

#Create the add task button
add_task_button = tk.Button(root, text="Add Task", command=add_task_command)
add_task_button.pack(pady=5)

#Create the delete task button
delete_task_button = tk.Button(root, text="Delete Task", command=delete_task_command)
delete_task_button.pack(pady=5)

#Refresh the tasks listbox to display tasks from the database
refresh_tasks()

#Run the main event loop
root.mainloop()