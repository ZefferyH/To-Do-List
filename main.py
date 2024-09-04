import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import calendar_
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *
# This import is for the missing file in tkcalendar
import time_clock
import graphics_and_save
HEIGHT = "800"
WIDTH = "600"
class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.task = {} # Temporary task storer
        self.tasks = []
        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, width=160, height=16, selectmode=tk.SINGLE,font = ("Arial",20))
        self.task_listbox.pack(side = "top")
        # Double click
        self.task_listbox.bind('<Double-1>',self.open_task)
        # Add button
        self.add_button = tk.Button(self.root, text="Add Task", command=self.new_task, height=1,font = ("Arial", 26))
        self.add_button.place(relx=1.0, rely=1.0, anchor='se')
        # Load tasks from file
        self.load_tasks()
    def open_task(self,event):
        def save_edit():
            summary = summary_entry.get()
            description = description_box.get("1.0", tk.END).strip()
            priority = dropdown_box.get()
            hour = hour_entry.get()
            if len(hour) == 1:
                hour = "0" + hour
            minute = minute_entry.get()
            if len(minute) == 1:
                minute = "0" + minute
            time = hour + ':' + minute
            date = str(date_entry.get_date())
            if summary == "":
                messagebox.showwarning("Warning", "Summary cannot be blank.")
            elif priority == "":
                messagebox.showwarning("Warning", "Please choose a priority.")
            elif date == "":
                messagebox.showwarning("Warning", "Please choose a date.")
            elif not time_clock.is_valid_time(time):
                messagebox.showwarning("Warning", "Please enter a valid time.")
            else:
                self.task = {"summary": summary, "description": description, "priority": priority, "time": time,
                             "date": date}
                if self.task:
                    self.tasks[index] = self.task
                    self.update_listbox()
                    self.task = ""
                    edit_window.destroy()
        def delete_task():
            response = messagebox.askyesno("Warning", "Are you sure you want to delete?")
            if response:
                del self.tasks[index]
                self.update_listbox()
                edit_window.destroy()
        index = self.task_listbox.curselection()[0]
        edit_window = tk.Toplevel(root)
        edit_window.transient(root)
        edit_window.title("Edit Task")
        edit_window.geometry("400x350")
        graphics_and_save.center_window(edit_window,400,350)
        selected_task = self.tasks[index]
        #Summary
        summary_label = tk.Label(edit_window, text="Task Summary:", font=("Arial", 12))
        summary_label.grid(row = 0, column = 0,padx=10, pady=10, sticky = "e")
        summary_entry = tk.Entry(edit_window,font = ("Arial",12), width = 25)
        summary_entry.insert(0,selected_task["summary"])
        summary_entry.grid(row = 0, column = 1,padx=10, pady=10,sticky = "e")
        #Description
        description_label = tk.Label(edit_window, text="Description:", font=("Arial", 12))
        description_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        description_box = tk.Text(edit_window, height=5, width=20, font=("Arial", 12))
        description_box.insert(1.0,selected_task["description"])
        description_box.grid(row=1, column=1, padx=10, pady=10)
        #Priority Box
        dropdown_label = tk.Label(edit_window, text="Priority:", font=("Arial", 12))
        dropdown_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        priority = ["Urgent", "Medium", "Low"]
        priority_selection = {"Urgent": 0, "Medium": 1, "Low": 2}
        dropdown_box = ttk.Combobox(edit_window, values=priority, state="readonly", font=("Arial", 12))
        dropdown_box.current(priority_selection[selected_task["priority"]])
        dropdown_box.grid(row=2, column=1, padx=10, pady=10)
        # Time
        hour_label = tk.Label(edit_window, text="Time(24h):", font=("Arial", 12))
        hour_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        time_frame = tk.Frame(edit_window)
        time_frame.grid(row=3, column=1)
        hour_entry = tk.Entry(time_frame, width=4, font=("Arial", 12))
        hour_entry.grid(row=3, column=1, padx=10, pady=10)
        hour_entry.insert(0,selected_task["time"][0:2])
        mid_label = tk.Label(time_frame, text=":", font=("Arial", 12))
        mid_label.grid(row=3, column=2, padx=10, pady=10)
        minute_entry = tk.Entry(time_frame, width=4, font=("Arial", 12))
        minute_entry.insert(0, selected_task["time"][3:])
        minute_entry.grid(row=3, column=3, padx=10, pady=10)
        # Date
        date_label = tk.Label(edit_window, text="Date:", font=("Arial", 12))
        date_label.grid(row=4, column=0, padx=10, pady=10, sticky = "e")
        date_entry = DateEntry(edit_window, date_pattern='yyyy/mm/dd')
        date_entry.set_date(selected_task["date"])
        date_entry.grid(row=4, column=1, padx=10, pady=10)
        # Save change button:
        add_task_button = tk.Button(edit_window, command=save_edit, text="Save Change(s)", font=("Arial", 12))
        add_task_button.grid(row=5, column=1, sticky="e", padx=10, pady=10)
        # Delete button:
        delete_button = tk.Button(edit_window, command = delete_task, text="Delete", font=("Arial", 12))
        delete_button.grid(row=5,column= 0, sticky = "e", padx=10, pady=10)
    def new_task(self):
        def add_task():
            summary = summary_box.get()
            description = description_box.get("1.0", tk.END).strip()
            priority = dropdown_box.get()
            hour = hour_entry.get()
            if len(hour) == 1:
                hour = "0" + hour
            minute = minute_entry.get()
            if len(minute) == 1:
                minute = "0" + minute
            time = hour + ':' + minute
            date = str(calendar.get_date())
            if summary == "":
                messagebox.showwarning("Warning", "Summary cannot be blank.")
            elif priority == "":
                messagebox.showwarning("Warning", "Please choose a priority.")
            elif date == "":
                messagebox.showwarning("Warning", "Please choose a date.")
            elif not time_clock.is_valid_time(time):
                messagebox.showwarning("Warning", "Please enter a valid time.")
            else:
                self.task = {"summary" : summary, "description": description, "priority": priority, "time": time, "date": date}
                if self.task:
                    self.tasks.append(self.task)
                    self.update_listbox()
                    self.task = ""
                    add_task_window.destroy()
        add_task_window = tk.Toplevel(root)
        add_task_window.transient(root)
        add_task_window.title("Add Task")
        add_task_window.geometry("400x350")
        graphics_and_save.center_window(add_task_window, 400, 350)
        # Task Summary
        summary_label = tk.Label(add_task_window, text="Task Summary:",font = ("Arial",12))
        summary_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        summary_box = tk.Entry(add_task_window,font = ("Arial",12), width = 25)
        summary_box.grid(row=0, column=1, padx=10, pady=10)
        # Task Description
        description_label = tk.Label(add_task_window, text="Description:",font = ("Arial",12))
        description_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        description_box = tk.Text(add_task_window, height=5, width=20,font = ("Arial",12))
        description_box.grid(row=1, column=1, padx=10, pady=10)
        # Priority
        dropdown_label = tk.Label(add_task_window, text="Priority:",font = ("Arial",12))
        dropdown_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        priority = ["Urgent", "Medium", "Low"]
        dropdown_box = ttk.Combobox(add_task_window, values=priority, state = "readonly",font = ("Arial",12))
        dropdown_box.grid(row=2, column=1, padx=10, pady=10)

        # Time
        hour_label = tk.Label(add_task_window, text="Time(24h):",font = ("Arial",12))
        hour_label.grid(row=3, column=0, padx=10, pady=10,sticky = "e")
        time_frame = tk.Frame(add_task_window)
        time_frame.grid(row=3, column=1)
        hour_entry = tk.Entry(time_frame,width = 4,font = ("Arial",12))
        hour_entry.grid(row=3, column=1, padx=10, pady=10)
        mid_label = tk.Label(time_frame, text=":",font = ("Arial",12))
        mid_label.grid(row=3, column=2, padx=10, pady=10)
        minute_entry = tk.Entry(time_frame, width=4,font = ("Arial",12))
        minute_entry.grid(row=3, column=3, padx=10, pady=10)
        # Date
        date_label = tk.Label(add_task_window, text = "Date:", font = ("Arial",12))
        date_label.grid(row = 4, column = 0,padx = 10, pady = 10,sticky = "e")
        calendar = DateEntry(add_task_window, date_pattern='yyyy/mm/dd')
        calendar.grid(row = 4, column = 1,padx = 10,pady = 10)
        # Submit button:
        add_task_button = tk.Button(add_task_window, command = add_task, text = "Add Task", font = ("Arial",12))
        add_task_button.grid(row = 5, column = 1, sticky = "e")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks.sort(key = time_clock.task_to_mktime)
        for task in self.tasks:
            time_left = time_clock.time_difference(f"{task["date"]} {task["time"]}")
            formatted_time = f"{time_left["days"]}D {time_left["hours"]}h {time_left["minutes"]}min"
            self.task_listbox.insert(tk.END, f"{task["summary"]} | Due in: {formatted_time}")
        self.priority_color()
        root.after(60000,self.update_listbox)
        self.save_tasks()
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    self.tasks.append(graphics_and_save.string_to_dict(line.strip()))
            self.update_listbox()
        except FileNotFoundError:
            pass

    def priority_color(self):
        for i in range(len(self.tasks)):
            priority_chart = {"Urgent": "red", "Medium": "#FFA200", "Low": "green"}
            task_priority = self.tasks[i]["priority"]
            self.task_listbox.itemconfig(i, {'fg': priority_chart[task_priority]})

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do-List")
    root.geometry(f"{HEIGHT}x{WIDTH}")
    graphics_and_save.center_window(root, int(HEIGHT), int(WIDTH))
    root.resizable(False, False)
    WINDOW = TodoList(root)


    root.mainloop()
