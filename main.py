import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Time")
root.geometry("300x300")

def vaqt():
    hozir = datetime.now().strftime("%H:%M:%S")
    label.config(text=hozir)
    root.after(1000, vaqt)

label = tk.Label(root,
    text="Vaqt",
    font=("Calibri", 15, "underline", "bold", "italic"),
    fg="blue",
    bg="white"
)
label.pack(pady=20)

btn = tk.Button(root,
    text="Bos!",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="blue",
    command=vaqt
)
btn.pack(pady=15)

root.mainloop()
