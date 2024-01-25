import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Reminder App")

        self.tasks = []

        # The listbox
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Entry widget
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT, padx=5)
        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_tasks)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Bind double-click event on listbox to mark task as completed
        self.task_listbox.bind("<Double-1>", self.mark_completed)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.update_listbox()

    def clear_tasks(self):
        self.tasks = []
        self.update_listbox()

    def mark_completed(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            completed_task = self.tasks.pop(selected_index[0])
            messagebox.showinfo("Task Completed", f"Task completed: {completed_task}")
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
