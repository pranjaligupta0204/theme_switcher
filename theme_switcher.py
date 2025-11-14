import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Theme Switcher")
root.geometry("350x300")


light_bg = "#ffffff"
light_fg = "#000000"
dark_bg = "#1a1a1a"
dark_fg = "#ffffff"

def set_light():
    apply_theme(light_bg, light_fg, "Light Theme Active")

def set_dark():
    apply_theme(dark_bg, dark_fg, "Dark Theme Active")

def set_auto():
    hour = datetime.now().hour
    if 6 <= hour < 18:
        apply_theme(light_bg, light_fg, "Auto Mode: Light Theme")
    else:
        apply_theme(dark_bg, dark_fg, "Auto Mode: Dark Theme")

def apply_theme(bg, fg, message):
    root.config(bg=bg)
    label.config(bg=bg, fg=fg)
    status_label.config(text=message, bg=bg, fg=fg)
    preview_box.config(bg=bg)

label = tk.Label(root, text="Theme Switcher", font=("Arial", 18))
label.pack(pady=15)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_light = tk.Button(btn_frame, text="Light", width=10, command=set_light)
btn_light.grid(row=0, column=0, padx=5)

btn_dark = tk.Button(btn_frame, text="Dark", width=10, command=set_dark)
btn_dark.grid(row=0, column=1, padx=5)

btn_auto = tk.Button(btn_frame, text="Auto", width=10, command=set_auto)
btn_auto.grid(row=0, column=2, padx=5)

preview_box = tk.Label(root, text="Preview Area", width=25, height=5, relief="ridge")
preview_box.pack(pady=15)

status_label = tk.Label(root, text="Choose a theme", font=("Arial", 10))
status_label.pack(pady=10)

set_light()

root.mainloop()
