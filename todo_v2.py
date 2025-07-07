import tkinter as tk
from tkinter import messagebox

tasks = []

def load_tasks(): #loads tasks from saved file
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

def save_tasks(): #saves task to saved file
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(): #adds task to list
    task = entry.get().strip()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def delete_task(): #deletes task to list
    try:
        selected_index = listbox.curselection()[0]
        task_to_delete = tasks[selected_index]
        confirm = messagebox.askyesno("Delete Task", f"Delete '{task_to_delete}'?")
        if confirm:
            tasks.pop(selected_index)
            listbox.delete(selected_index)
            save_tasks()
    except IndexError:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

def clear_all():#clear all tasks
    confirm = messagebox.askyesno("Clear all Tasks","Are you sure you want to clear all tasks?")
    if confirm:
        tasks.clear()
        save_tasks()
        listbox.delete(0, tk.END)

# GUI Setup
window = tk.Tk()
window.title("To-Do App")
window.geometry("400x400")

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10)

delete_button = tk.Button(window, text="Delete Selected Task", command=delete_task)
delete_button.pack()

clear_button = tk.Button(window, text = "Clear All", command = clear_all)
clear_button.pack()

load_tasks()
for task in tasks:
    listbox.insert(tk.END, task)

window.mainloop()
