import tkinter as tk
from tkinter import ttk

task = []

# ---------------- FUNCTIONS ----------------

def add_task():
    text = entry.get().strip()
    if text:
        task.append(text)
        listbox.insert(tk.END, f"✔ {text}")
        entry.delete(0, tk.END)

def remove_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        task.pop(index)

def clear_all():
    task.clear()
    listbox.delete(0, tk.END)

# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("🔥 TASK MASTER")
root.geometry("420x550")
root.configure(bg="#0f172a")  # dark modern background

# ---------------- STYLE (ttk) ----------------

style = ttk.Style()
style.theme_use("clam")

style.configure("TButton",
    font=("Arial", 11, "bold"),
    padding=10
)

style.configure("Add.TButton", background="#22c55e", foreground="white")
style.configure("Del.TButton", background="#ef4444", foreground="white")
style.configure("Clear.TButton", background="#f59e0b", foreground="white")

# ---------------- TITLE ----------------

title = tk.Label(
    root,
    text="🧠 TASK MASTER",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#0f172a"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Organize your life like a pro",
    font=("Arial", 10),
    fg="#94a3b8",
    bg="#0f172a"
)
subtitle.pack()

# ---------------- ENTRY ----------------

entry = tk.Entry(
    root,
    font=("Arial", 13),
    bg="#1e293b",
    fg="white",
    insertbackground="white",
    relief="flat",
    width=28
)
entry.pack(pady=20, ipady=8)

# ---------------- BUTTONS ----------------

btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=10)

add_btn = ttk.Button(btn_frame, text="➕ Add", style="Add.TButton", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

del_btn = ttk.Button(btn_frame, text="❌ Delete", style="Del.TButton", command=remove_task)
del_btn.grid(row=0, column=1, padx=5)

clear_btn = ttk.Button(btn_frame, text="🧹 Clear", style="Clear.TButton", command=clear_all)
clear_btn.grid(row=0, column=2, padx=5)

# ---------------- LISTBOX ----------------

listbox_frame = tk.Frame(root, bg="#0f172a")
listbox_frame.pack(pady=20)

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(
    listbox_frame,
    width=40,
    height=15,
    font=("Arial", 11),
    bg="#1e293b",
    fg="white",
    selectbackground="#334155",
    selectforeground="white",
    relief="flat",
    yscrollcommand=scrollbar.set
)

listbox.pack()
scrollbar.config(command=listbox.yview)

# ---------------- RUN ----------------

root.mainloop()